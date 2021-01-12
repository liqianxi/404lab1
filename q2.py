import requests as req
print(req.__version__)
request = req.get('http://www.google.com/',auth=('user','pass'))
print(request.status_code)

