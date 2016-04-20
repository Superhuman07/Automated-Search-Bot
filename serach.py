import webbrowser
search_term = 'hello'
num = 0
while num < 10:
    
    url = "https://www.bing.com/search?q={}".format(search_term)    
    webbrowser.open(url)
    num = num + 1