def wsgi_application(environ. start_response):
    status = '2001 OK'
    headers = [
        ('Content_type', 'text/plain')
        ]
    body = 'Hello, World!'
    start_response(status, headers)
    return [body]
