import webbrowser
'''
Chnage the serach_term for your own use later it will be appended by the append operation in the while loop
'''
search_term = 'h'
num = 0
def function(search_term):
    url = "https://www.bing.com/search?q={}".format(search_term)    
    webbrowser.open(url)
'''
calling function 10 times with new strings change the limit to request more from the search engine
'''
while num < 10:
    search_term += 'l'
    function(search_term)
    num += 1
