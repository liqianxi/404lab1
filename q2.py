import requests as req
print(req.__version__)
request = req.get('https://github.com/liqianxi/404lab1/blob/main/q2.py',auth=('user','pass'))
print(request.status_code)

