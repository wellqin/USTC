"""
! what?
`dbm.ndbm` provides an interface 
to the `Unix` `ndbm` implementations of the dbm format, 
depending on how the module was configured during compilation


`dbm.dumb` module is a portable fallback implemenation of the DBM API
when no other implementations are available.

dbm
- dbm.gnu
- dbm.ndbm
- dbm.dumb

! why?
No external dependencies are required to use `dbm.dumb`.
but it works more slowly than most other implemenations.


! how?

dbm
|-- database types
|-- create a new database
|-- open an existing database
|-- error cases

# wait a second, do i really need `dbm`?


"""