"""
P121-P127 weakref: impermanent references to objects

! what is weakref?
# A: weakref supports weak references to objects.

! why weakref?
# A: A normal reference increments the reference count on the object and prevents it from being garbage collected.
# this outcome is not always desirable, 
# especially when a circular reference might be present or when a cache of objects should deleted when memory is needed.
# A weak reference is a handle to an object that does not keep it from being cleaned up automatically. 
# aha, somehow it resembles maganet..

! how?

weakref
|-- references
|-- reference Callbacks
|-- finalizing Objects
|-- Proxies
|-- Caching objects

"""