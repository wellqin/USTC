"""
! what?
memory-map files

using os virtual memory to access the data on the file system directly.

! why?
instead of accessing the data with the normal I/O functions,
mmap typically improves IO performance because it doest NOT requre either
making a separate system call for each access or copying data between buffers.

instead, the memory is accessed directly by both the kernel and the user application


! how?
Memory-mapped files can be treated as mutable strings or file-like objects,
depending on the need

? what do i read?
* quantum wave-partical duality, lol
a mapped file supports the expected file API methods,
such as `close()`, `flush()`, `read()`, `readline()`, `seek()`, `tell()` and `write()`

it also supports the string API, with features such `slicing` adn `find()`

NOTE:
mmap has different behaviors on winos and unix-like os

mmap
|-- reading
|-- writing
|-- regular expression

"""