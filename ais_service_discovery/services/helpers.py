from os import getenv


def default_namespace():
    ENV = getenv('ENV')
    if ENV:
        return 'default-{}'.format(ENV)
    return 'default'


NAMESPACE_NOTATION = '.'
HANDLER_NOTATION = '->'


def get_handler(service_id):
    if HANDLER_NOTATION in service_id:
        return service_id.split(HANDLER_NOTATION)
    return False


def extract_service_parts(service_id):
    '''
    This takes a service_id in the user-facing form and
    reconsitutes it into parts an in our internal form.
    For example, `namespace.service->handler`, becomes
    `namespace.service.handler`.
    And `service->handler` becomes: `service.handler`.
    This is because we have to differentiate between the three segments as
    there's no way of assuring which is a namespace and which is a service,
    as a namespace is optional.
    '''
    # If service ID contains a NAMESPACE_NOTATION - which denotes that
    # the ID contains both a namespace and a service.
    # Split the two, check for a handler
    if NAMESPACE_NOTATION in service_id:
        [namespace, service] = service_id.split(NAMESPACE_NOTATION)
        # Check if the service contains a handler, denoted
        # by a HANDLER_NOTATION.
        has_handler = get_handler(service)
        if has_handler:
            [service_name, handler] = has_handler
            return {
             'namespace': namespace,
             'service': service_name,
             'handler': handler
             }
        return {
         'namespace': namespace,
         'service': service
         }
    # If service has a function handler
    # return service with handler in base format.
    has_handler = get_handler(service)
    if has_handler:
        [service_name, handler] = has_handler
        return {
         'namespace': default_namespace(),
         'service': service_name,
         'handler': handler
        }
    # Default behavior, returns serviceId given, with the default namespace.
    return {
     'namespace': default_namespace(),
     'service': service_id,
    }
