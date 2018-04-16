import requests
# icanhazdadjoke

res = 0
try:
    res = requests.get("http://www.google.com/", params={
        "location": "Indonesia",
        "isAlive": True
    }, headers={
        "Accept": "text/plain"      # text/html, application/json
    })
except SyntaxError as err:
    print('An exception has occurred', err)
finally:
    print(res)

# res.headers - response headers
# res.text - html for humans
# res.status_code() - response code
# res.json() - converts to json - dictionary format in python
