from urllib.request import urlopen
import warnings
import os
import json

URL  = 'http://www.oreilly.com/pub/sc/osconfeed'
# JSON = 'data/osconfeed.json'
JSON = 'data/schedule1_db'

def load():
    if not os.path.exists(JSON):
        msg = 'downloading {} to {}'.format(URL, JSON)
        warnings.warn(msg)
        with urlopen(URL) as remote, open(JSON, 'wb') as local:
            local.write(remote.read())
    with open(JSON, encoding='utf8') as f:
        return json.load(f)

if __name__ == "__main__":
    dataframe = load()
    print(dataframe)