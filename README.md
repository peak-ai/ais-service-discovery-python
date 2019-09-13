# ais-service-discovery-python

## Cloud Application Framework

![logo](https://raw.githubusercontent.com/peak-ai/ais-service-discovery-python/master/logo.png)


## Description

This repository interfaces Service Discovery, in this instance CloudMap, in order to locate and communicate with different services. As opposed to storing ARN's in environment variables, this library will interface CloudMap to find a service by a user-friendly naming convention and will understand what 'type' of service you've requested and use the correct code to communicate/call that service.

## Services supported
- Lambda (`call`).

## TODO
- Lambda (`request`)
- SNS (`publish`). // subscribe not supported by SNS.
- SQS (`queue`|`listen`),
- Http (`request`|`call`).
- Fargate/ECS Task (`run`).

## Note:
This library requires *Python 3.5 and above*.

## Examples:

### Lambda Call

```python
from ais_service_discovery import call
response=call('namespace', 'service', 'handler', {<Payload>})
print(response)
```

### Lambda Async Call

```python
from ais_service_discovery import call
response=call('namespace', 'service', 'handler', {<Payload>}, {'InvocationType': 'Event'})
print(response)
```
