class CloudmapAdapter:
    def __init__(self, client):
        self.client = client

    def filter_instances(self, response, id):
        filter_function = lambda instance : instance['InstanceId'] == id

        return {
            **response,
            'Instances': filter(filter_function, response['Instances'])
        }

    def discover(self, namespace, name, id):
        return self.filter_instances(self.client.discover_instances(
            NamespaceName=namespace,
            ServiceName=name
        ), id)
