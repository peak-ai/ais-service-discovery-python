# ais-service-discovery-python

![CodeQuality](https://github.com/peak-ai/ais-service-discovery-python/workflows/CodeQL/badge.svg) ![Publish](https://github.com/peak-ai/ais-service-discovery-python/workflows/Upload%20Python%20Package/badge.svg) ![stable](https://img.shields.io/github/v/release/peak-ai/ais-service-discovery-python) ![](https://img.shields.io/github/v/release/peak-ai/ais-service-discovery-python?include_prereleases) ![](https://img.shields.io/github/license/peak-ai/ais-service-discovery-python) ![](https://img.shields.io/github/languages/count/peak-ai/ais-service-discovery-python) ![](https://img.shields.io/github/languages/top/peak-ai/ais-service-discovery-python) ![](https://img.shields.io/github/issues-raw/peak-ai/ais-service-discovery-python) ![](https://img.shields.io/github/issues-pr-raw/peak-ai/ais-service-discovery-python) ![](https://img.shields.io/github/languages/code-size/peak-ai/ais-service-discovery-python) ![](https://img.shields.io/github/repo-size/peak-ai/ais-service-discovery-python)

## Cloud Application Framework

![logo](https://raw.githubusercontent.com/peak-ai/ais-service-discovery-python/master/logo.png)


## Description

This repository interfaces Service Discovery, in this instance CloudMap, in order to locate and communicate with different services. As opposed to storing ARN's in environment variables, this library will interface CloudMap to find a service by a user-friendly naming convention and will understand what 'type' of service you've requested and use the correct code to communicate/call that service.

## Services supported
- Lambda (`call`).
- SNS (`publish`).
- SQS (`queue`).


## TODO
- SQS (`listen`).
- Http (`request`|`call`).
- Fargate/ECS Task (`run`).
- Lambda (`request`).


## Note

This library requires *Python 3.5 and above*.


## Examples

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

## Configuration

This library can utilise the following environment variables:

```
BOTO_MAX_ATTEMPTS=10 // Boto3 exponential back-off attemps
BOTO_READ_TIMEOUT=300 // Boto3 timeout 
```

