from urllib import request

URL = 'file:///C:/Users/5106001995/AppData/Roaming/Microsoft/Google/_01_chromohome_Django-Scheme.html'

def urllib_request_urlopen():
    response = request.urlopen(URL)
    print('RESPONSE :', response)
    print('URL      :', response.geturl())
    headers = response.info()
    print('DATE     :', headers['date'])
    print('HEADERS  :')
    print('---------')
    print(headers)
    data = response.read().decode('utf-8')
    print('LENGTH   :', len(data))
    print('DATA     :')
    print('---------')
    print(data)

def urllib_request_urlopen_iterator():
    response = request.urlopen(URL)
    for line in response:
        print(line.decode('utf8').rstrip())
    ...
if __name__ == "__main__":
    urllib_request_urlopen()