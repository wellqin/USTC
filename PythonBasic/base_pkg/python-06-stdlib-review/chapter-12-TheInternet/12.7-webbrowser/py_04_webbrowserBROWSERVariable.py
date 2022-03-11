"""

Users can control the webbrowser module from outside your application by setting the
environment variable BROWSER to the browser names or commands to try. 

The value used
should consist of a series of browser names separated by os.pathsep. 

If the name includes
%s, the name is interpreted as a literal command and executed directly, with the %s being
replaced by the URL. 

Otherwise, the name is passed to get() to obtain a controller object
from the registry.

"""