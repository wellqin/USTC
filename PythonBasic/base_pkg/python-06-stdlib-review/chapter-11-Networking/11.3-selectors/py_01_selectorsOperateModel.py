"""
the `selectors` module provides a platform-independent abstraction layer
on top of the platform-specific I/O monitoring function in `select`


the APIs in selectors are event based,
similar to poll() from select or socket?

several implementations exist,
and the module automatically sets the alias `DefaultSelector` 
to refer to the most efficient one for the current system configuration.

a selector object provides methods for specifying which events to look for on a socket,
and then lets the caller wait for events in a platform-independent way.

registering interest in an event creates a SelectorKey,
which holds the socket, information about the events of interest,
and optional application data.

the ownwer of the selector calls its `select()` method to learn about events.
the return value is a sequence of key objects and a bitmask indicating
which events have occurred. 

a program using a selector should repeatedly call `select()`,
and then handle the events appropriately.

"""