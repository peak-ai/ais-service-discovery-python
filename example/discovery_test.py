from ais_service_discovery.discovery import DiscoveryFactory

discovery = DiscoveryFactory.instance("ais-latest", "test-service")

instance = discovery.register("test", "dataset", {
    "schema": "stage",
    "table": "tester",
})

print(instance)

result = discovery.update_instance("test", "dataset", {"testing": "123"})
print("result: ", result)

instance = discovery.discover("dataset")
print("instance: ", instance)
