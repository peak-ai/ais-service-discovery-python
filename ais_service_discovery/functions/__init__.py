from json import dumps, loads


class LambdaAdaptor:
    def __init__(self, client):
        self.client = client

    def call(self, **kwargs):
        res = self.client.invoke(**kwargs)
        if 'Payload' in res:
            payload = res['Payload'].read()
            if payload:
                return loads(payload.decode())
            return res['StatusCode']
        return res['StatusCode']


class Func:
    def __init__(self, adapter):
        self.adapter = adapter

    def call(self, **kwargs):
        return self.adapter.call(**kwargs)
