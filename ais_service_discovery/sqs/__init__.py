class SqsAdaptor:
  def __init__(self, client) :
    self.client = client

  def call(self, **kwargs) :
    res = self.client.send_message(**kwargs)
    return res

class Send:
  def __init__(self, adapter) :
    self.adapter = adapter

  def call(self, **kwargs) :
    return self.adapter.call(**kwargs)
