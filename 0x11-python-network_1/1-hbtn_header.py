import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    headers = dict(response.getheaders())
    x_request_id = headers.get("X-Request-Id")
    print(x_request_id)
