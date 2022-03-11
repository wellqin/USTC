from urllib import parse
from urllib import request

def urllib_request_post():
    query_args = {'q': 'query string', 'foo': 'bar'}
    encoded_args = parse.urlencode(query_args).encode('utf-8')
    url = 'http://localhost:8080/'
    print(request.urlopen(url, encoded_args).read().decode('utf-8'))


if __name__ == "__main__":
    urllib_request_post()