from urllib import request

def urllib_request_header():
    r = request.Request('http://localhost:8080/')
    r.add_header(
        'User-agent',
        'PyMOTW (https://pymotw.com/)',
    )
    response = request.urlopen(r)
    data = response.read().decode('utf-8')
    print(data)