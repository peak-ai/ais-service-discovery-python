class SnsAdaptor:
    def __init__(self, client):
        self.client = client

    def call(self, **kwargs):
        res = self.client.publish(**kwargs)
        return res['MessageId']

class Publish:
    def __init__(self, adapter):
        self.adapter = adapter

    def call(self, **kwargs):
        return self.adapter.call(**kwargs)
