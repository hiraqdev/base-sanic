def format_error(status=None, title=None, detail=None, code=None):
    '''Formatting JSON API Error Object

    Constructing an error object based on JSON API standard
    ref: http://jsonapi.org/format/#error-objects

    Args:
        status: Can be a http status codes
        title: A summary of error
        detail: A descriptive error message
        code: Application error codes (if any)

    Returns:
        A dictionary contains of status, title, detail and code
    '''
    error = {}
    error.update({ 'title': title })

    if status is not None:
        error.update({ 'status': status })

    if detail is not None:
        error.update({ 'detail': detail })

    if code is not None:
        error.update({ 'code': code })

    return error

def return_an_error(*args):
    '''List of errors

    Put all errors into a list of errors
    ref: http://jsonapi.org/format/#errors

    Args:
        *args: A tuple contain errors

    Returns:
        A dictionary contains a list of errors
    '''
    list_errors = []
    list_errors.extend(list(args))

    errors = { 'errors': list_errors }
    return errors
