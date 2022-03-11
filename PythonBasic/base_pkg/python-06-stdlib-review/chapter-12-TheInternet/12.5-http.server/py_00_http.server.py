"""
! what?
the Internent is a pervasive aspect of modern computing.
even small, single-use scripts frequently interact with remote services to send or receive data.

Python's rich set of tools for working with web prototcols 
makes it well suited for programming web-based applications,
either as a client or as a server.

HTTP POST requests are usually "form encoded" with `urlib`.
Binary data sent through a POST should be encoded with `base64` first,
to comply with the message format standard.

! why?
why not

! how?

`http.server` uses classes from `socketserver` to create base classes for making HTTP servers.
HTTPServer can be used directly, but `BaseHTTPRequestHandler` is intended to be extended to handle each protocol method.

http.server: Base Classes for Implementing Web Servers
|-- HTTP GET
|-- HTTP POST
|-- Threading and Forking
|-- Handling Errors
|-- Setting Headers
|-- Command-Line Use

"""