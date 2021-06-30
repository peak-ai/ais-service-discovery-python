class CloudmapAdapter:
    def __init__(self, client):
        self.client = client

    def filter_instances(self, response, instance_id):
        filter_function = lambda instance : instance['InstanceId'] == instance_id
        return {
            **response,
            'Instances': filter(filter_function, response['Instances'])
        }

    def discover(self, namespace, service, instance):
        return self.filter_instances(self.client.discover_instances(
            NamespaceName=namespace,
            ServiceName=service,
        ), instance)

    def register(self, namespace, service, instance, attributes):
        namespace_id = self.get_namespace_id(namespace)
        srv = self.get_service(namespace_id, service)
        if srv is None:
            srv = self.create_service(namespace, service)
        existing = list(self.discover(namespace, service, instance)['Instances'])
        if existing:
            return existing
        self.client.register_instance(
            ServiceId=srv,
            InstanceId=instance,
            Attributes=attributes,
        )
        return list(self.discover(namespace, service, instance)['Instances'])

    def get_service(self, namespace, service):
        response = self.client.list_services(
            Filters=[
                {
                    'Name': 'NAMESPACE_ID',
                    'Values': [
                        namespace,
                    ],
                    'Condition': 'EQ',
                },
            ]
        )
        for item in response['Services']:
            if item['Name'] == service:
                return item['Id']
        return None

    def get_namespace_id(self, namespace):
        response = self.client.list_namespaces()
        result = response['Namespaces']
        for item in result:
            if item['Name'] == namespace:
                return item['Id']
        return None

    def create_namespace(self, namespace):
        response = self.client.create_http_namespace(
            Name=namespace,
        )
        return response['Namespace']

    def create_service(self, namespace, service):
        namespace_id = self.get_namespace_id(namespace)
        response = self.client.create_service(
            Name=service,
            NamespaceId=namespace_id,
            Type='HTTP'
        )
        return response['Service']['Id']

    def update_instance(self, namespace, service, instance, attributes):
        self.deregister_instance(namespace, service, instance)
        return self.register(namespace, service, instance, attributes)

    def deregister_instance(self, namespace, service, instance):
        namespace_id = self.get_namespace_id(namespace)
        service_id = self.get_service(namespace_id, service)
        instances = list(self.discover(namespace, service, instance)['Instances'])
        if len(instances) == 0:
            return None
        self.client.deregister_instance(
            ServiceId=service_id,
            InstanceId=instances[0]['InstanceId'],
        )
