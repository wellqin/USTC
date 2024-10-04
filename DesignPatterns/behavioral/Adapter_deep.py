# 适配器模式
from abc import ABCMeta, abstractmethod


class HTTPRequest(object):
    def __init__(self, url, body):
        self.url = url
        self.body = body

    def get(self):
        print(f"http get->{self.url}-{self.body}")

    def post(self):
        print(f"http post->{self.url}-{self.body}")


class WebSocket(object):
    def __init__(self, url, msg):
        self.url = url
        self.msg = msg

    def request(self):
        print(f"websocket-{self.url}-{self.msg}")


class Request(object):
    def __init__(self, method, url, body, proto):
        self.method = method
        self.url = url
        self.body = body
        self.proto = proto


class RequestAdapter(metaclass=ABCMeta):
    @abstractmethod
    def send(self, request: Request):
        pass


class WebSocketAdapter(RequestAdapter):
    def send(self, request: Request):
        websocket = WebSocket(url=request.url, msg=request.body)
        websocket.request()


class HttpAdapter(RequestAdapter):
    def send(self, request: Request):
        http = HTTPRequest(url=request.url, body=request.body)
        if request.method == "get":
            http.get()
        elif request.method == "post":
            http.post()


class ApiRequest(object):
    adapter: RequestAdapter

    def __init__(self, method="", url="", body="", proto="http"):
        self.request = Request(
            method,
            url,
            body,
            proto
        )

    def send(self):
        if self.request.proto == "websocket":
            adapter = WebSocketAdapter()
        elif self.request.proto == "http":
            adapter = HttpAdapter()
        else:
            raise ValueError(self.request.proto)
        adapter.send(self.request)


if __name__ == '__main__':
    # http和websocket两套适配器 同一套接口测试不同协议的接口服务
    ApiRequest(proto="websocket").send()
    ApiRequest(proto="http", method="get").send()
