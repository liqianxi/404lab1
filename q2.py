import requests as req
print(req.__version__)
request = req.get('https://raw.github.com/liqianxi/404lab1/main/q2.py')
print(request.text)


