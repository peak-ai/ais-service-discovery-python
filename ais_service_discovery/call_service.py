"""
call_service

Calls services via the service discovery library
"""
from os import environ as env
from json import dumps

from boto3 import client
from botocore.config import Config

from .services import default_namespace, Services, \
    CloudmapAdapter
from .functions import LambdaAdaptor, Func
from .sns import SnsAdaptor, Publish
from .sqs import SqsAdaptor, Send


BOTO_MAX_ATTEMPTS = int(env.get('BOTO_MAX_ATTEMPTS', 1))
BOTO_READ_TIMEOUT = float(env.get('BOTO_READ_TIMEOUT', 5))
BOTO_CONNECTION_TIMEOUT = float(env.get('BOTO_CONNECTION_TIMEOUT', 60))

config = Config(
    read_timeout=BOTO_READ_TIMEOUT,
    retries={'total_max_attempts': BOTO_MAX_ATTEMPTS},
    connect_timeout=BOTO_CONNECTION_TIMEOUT
)

function = client('lambda', config=config)
sns = client('sns', config=config)
sqs = client('sqs', config=config)
service_discovery = client('servicediscovery', config=config)

cloudmap_adaptor = CloudmapAdapter(service_discovery)
services = Services(cloudmap_adaptor)

lambda_adaptor = LambdaAdaptor(function)
func = Func(lambda_adaptor)

sns_adaptor = SnsAdaptor(sns)
publish = Publish(sns_adaptor)

sqs_adaptor = SqsAdaptor(sqs)
send = Send(sqs_adaptor)


def run_service(service, body, opts):
    """ run_service """
    service_type = service['Attributes']['type']
    if service_type in ['cloud-function', 'function', 'lambda']:
        return func.call(**{
            'FunctionName': service['Attributes']['arn'],
            'Payload': dumps(body),
            **opts
        })
    if type in ['event']:
        return publish.call(**{
            'TopicArn': service['Attributes']['arn'],
            'Message': dumps(body),
            **opts
        })
    if type in ['queue', 'sqs']:
        return send.call(**{
            'QueueUrl': service['Attributes']['url'],
            'MessageBody': dumps(body),
            **opts
        })
    return None


def call_service(namespace, service, handler, body, opts):
    """ call_service """
    instances = services.discover(
        namespace or default_namespace(), service, handler)['Instances']
    if not instances:
        raise Exception('Service {}.{}.{} not found'.format(
            namespace or default_namespace(), service, handler))
    [service_to_run] = instances
    payload = run_service(service_to_run, body, opts)
    if (payload and isinstance(payload) is dict and
            ('errorMessage' in payload) and ('errorMessage' in payload)):
        raise Exception(payload)
    return dumps(payload)
