"""
! what?

! why?
the frameworks in `socketserver` abstract out a significant portion of the repetitive
work necessary to create a new network server.

the classes can be combined to create servers that fork or use threads and support TCP or UDP.
only the actual message handling needs to be provided by the application.

! how?

socketserver: Creating Network Servers
|-- Server Types
|-- Server Objects
|-- Implementing a Server
|-- Request Handlers
|-- Echo Example
|-- Threading and Forking

"""