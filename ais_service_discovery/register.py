from boto3 import client
from .services import default_namespace, extract_service_parts, Services, \
    CloudmapAdapter

service_discovery = client('servicediscovery')

cloudmap_adaptor = CloudmapAdapter(service_discovery)
services = Services(cloudmap_adaptor)


def register(namespace: str, service: str, instance: str, kind: str, attributes: dict):
    attrs = {**attributes, 'type': kind}
    return services.register(namespace, service, instance, attrs)
