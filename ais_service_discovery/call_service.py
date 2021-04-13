from boto3 import client
from .services import default_namespace, extract_service_parts, Services, \
    CloudmapAdapter
from .functions import LambdaAdaptor, Func
from .sns import SnsAdaptor, Publish
from .sqs import SqsAdaptor, Send
from json import dumps

function = client('lambda')
sns = client('sns')
sqs = client('sqs')
service_discovery = client('servicediscovery')

cloudmap_adaptor = CloudmapAdapter(service_discovery)
services = Services(cloudmap_adaptor)

lambda_adaptor = LambdaAdaptor(function)
func = Func(lambda_adaptor)

sns_adaptor = SnsAdaptor(sns)
publish = Publish(sns_adaptor)

sqs_adaptor = SqsAdaptor(sqs)
send = Send(sqs_adaptor)

def run_service(service, body, opts={}):
    type = service['Attributes']['type']
    if type in ['cloud-function', 'function', 'lambda']:
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


def call_service(namespace, service, handler, body, opts={}):
    instances = services.discover(
        namespace or default_namespace(), service, handler)['Instances']
    if not instances:
        raise Exception('Service {}.{}.{} not found'.format(
            namespace or default_namespace(), service, handler))
    [service_to_run] = instances
    payload = run_service(service_to_run, body, opts)
    if (payload and type(payload) is dict and
            ('errorMessage' in payload) and ('errorMessage' in payload)):
        raise Exception(payload)
    return dumps(payload)
