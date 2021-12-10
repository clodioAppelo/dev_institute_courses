# Instructions :
# Using the requests and time modules, create a function which returns the amount of time it
# takes a webpage to load (how long it takes for a complete response to a request).
# Test your code with multiple sites such as google, ynet, imdb.

import requests

def web_loading_time(web):
    time_response = requests.get(web)
    return time_response.elapsed

print(web_loading_time('http://www.google.com/'))
print(web_loading_time('http://www.ynet.co.il/'))
print(web_loading_time('http://www.imdb.com/'))
