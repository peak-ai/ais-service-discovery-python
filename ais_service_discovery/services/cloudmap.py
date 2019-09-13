class CloudmapAdapter:
    def __init__(self, client):
        self.client = client

    def discover(self, namespace, name, handler):
        return self.client.discover_instances(
            NamespaceName=namespace,
            ServiceName=name,
            QueryParameters={
                'handler': handler,
            }
        )
