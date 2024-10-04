import webbrowser
"""
If for some reason your application needs to use a specific browser, you can access the set of
registered browser controllers using the get() function.

"lynx" browser, oh, this is fucking new to me?
chrome
ie
firefox
opera

"""
b = webbrowser.get('lynx')
b.open('https://docs.python.org/3/library/webbrowser.html')