import webbrowser

"""
The URL is opened in a browser window, 
and that window is raised to the top of the window stack. 

The documentation says that an existing window will be reused, if possible,
but the actual behavior may depend on your browser’s settings. 

If you use Firefox on Mac OS X, a new window is always created.
"""

webbrowser.open(
    'https://docs.python.org/3/library/webbrowser.html',
)