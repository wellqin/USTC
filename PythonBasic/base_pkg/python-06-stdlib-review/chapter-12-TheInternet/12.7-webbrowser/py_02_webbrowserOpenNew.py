import webbrowser

"""
The URL is opened in a browser window, 
and that window is raised to the top of the window stack. 

The documentation says that an existing window will be reused, if possible,
but the actual behavior may depend on your browser’s settings. 

If you use Firefox on Mac OS X, a new window is always created.

open(), open_new() and open_new_tab() share same behavior on my office PC(winos)
"""

webbrowser.open_new(
    'https://docs.python.org/3/library/webbrowser.html',
)

webbrowser.open_new_tab(
    'https://docs.python.org/3/library/webbrowser.html',
)
