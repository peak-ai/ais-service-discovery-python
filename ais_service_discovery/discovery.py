from boto3 import client
from .services import CloudmapAdapter, Services

service_discovery = client('servicediscovery')


class DiscoveryFactory:
    @staticmethod
    def instance(namespace, service):
        cloudmap_adaptor = CloudmapAdapter(service_discovery)
        adapter = Services(cloudmap_adaptor)
        return Discovery(adapter, namespace, service)


class Discovery:
    def __init__(self, adapter: Services, namespace, service):
        self.adapter = adapter
        self.namespace = namespace
        self.service = service

    def register(self, instance, kind, attributes):
        if self.namespace and self.service:
            attrs = {**attributes, 'type': kind}
            return self.adapter.register(self.namespace, self.service, instance, attrs)
        else:
            raise Exception('you must defined a namespace and service')

    def discover(self, instance):
        result = self.adapter.discover(self.namespace, self.service, instance)
        return list(result['Instances'])

    def create_namespace(self, namespace):
        return self.adapter.create_namespace(namespace)

    def create_service(self, service):
        return self.adapter.create_service(self.namespace, service)

    def update_instance(self, instance, kind, attributes):
        attrs = {**attributes, 'type': kind}
        return self.adapter.update_instance(self.namespace, self.service, instance, attrs)
