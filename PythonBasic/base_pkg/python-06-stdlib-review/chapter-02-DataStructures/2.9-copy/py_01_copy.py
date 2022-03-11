"""
P130-P133, copy: Duplicate Objects

! What is it?

https://docs.python.org/3/library/copy.html

# A: the copy module includes two functions, copy() and deepcopy() 
# for duplicating existing objects

The difference between shallow and deep copying is only relevant for **compound objects** 
(objects that contain other objects, like lists or class instances):
- A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.
- A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.

! Why?

# A: Python refers everything as 'ByRef' in VB or '*pointer' in C/C++ by default
# in some situation, it's convenient to duplicate a copy of objects rather than referencing it directly

Two problems often exist with deep copy operations that don’t exist with shallow copy operations:
- Recursive objects (compound objects that, directly or indirectly, contain a reference to themselves) may cause a recursive loop.
- Because deep copy copies everything it may copy too much, such as data which is intended to be shared between copies.

! how to use?

copy
|-- shallow copy
|-- deep copy
|-- custome copy behavior
|-- recursion in deep copy

"""