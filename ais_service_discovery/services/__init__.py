from .helpers import default_namespace, extract_service_parts
from .cloudmap import CloudmapAdapter


class Services:
    def __init__(self, adapter):
        self.adapter = adapter

    def discover(self, *args, **kwargs):
        return self.adapter.discover(*args, **kwargs)

    def register(self, *args, **kwargs):
        return self.adapter.register(*args, **kwargs)

    def create_namespace(self, *args, **kwargs):
        return self.adapter.create_namespace(*args, **kwargs)

    def create_service(self, *args, **kwargs):
        return self.adapter.create_service(*args, **kwargs)

    def update_instance(self, *args, **kwargs):
        return self.adapter.update_instance(*args, **kwargs)
