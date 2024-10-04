"""
! what?
shelve: persistence storage of objects

the shelf is accessed by keys, just as with a dictionary.
the values are pickled and written to a database taht is created and managed by `dbm`

! why?
`shelve` module can be used as a simple presistent storage option
for Python objects when a relational database is not required.


! how?

shelve
|-- create a new shelf
|-- writeback
|-- specific shelf types

"""