from boto3 import client
from .services import default_namespace, extract_service_parts, Services, \
    CloudmapAdapter
from .functions import LambdaAdaptor, Func
from json import dumps

function = client('lambda')
service_discovery = client('servicediscovery')

cloudmap_adaptor = CloudmapAdapter(service_discovery)
services = Services(cloudmap_adaptor)

lambda_adaptor = LambdaAdaptor(function)
func = Func(lambda_adaptor)


def run_service(service, body, opts={}):
    type = service['Attributes']['type']
    if type in ['cloud-function', 'function', 'lambda']:
        return func.call(**{
            'FunctionName': service['Attributes']['arn'],
            'Payload': dumps(body),
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
