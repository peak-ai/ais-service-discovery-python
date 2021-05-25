from ais_service_discovery import call

try:
    res = call(
        'my-namespace',
        'my-service',
        'my-instance', {
            'arg': 'hello-word',
    })
    print(res)
except Exception as e:
    print(e)

