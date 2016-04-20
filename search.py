import webbrowser
search_term = 'h'
num = 0
def function(search_term):
    url = "https://www.bing.com/search?q={}".format(search_term)    
    webbrowser.open(url)
'''
calling function 10 times with new strings
'''
while num < 10:
    search_term += 'l'
    function(search_term)
    num += 1
