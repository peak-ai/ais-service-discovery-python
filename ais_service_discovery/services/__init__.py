from .helpers import default_namespace, extract_service_parts
from .cloudmap import CloudmapAdapter


class Services:
    def __init__(self, adapter):
        self.adapter = adapter

    def discover(self, *args, **kwargs):
        return self.adapter.discover(*args, **kwargs)
