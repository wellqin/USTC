"""
! what?
subprocess: spawning additional processes
it provides an API for creating and communicating with secondary processes.
it is especially good for running programs that produce or consume text,
since the API supports passing data back and forth through the standard input and output channels of the new process.

! why?
`subprocess` is intended to replace functions 
such `os.system()`, `os.spawnv()`, the variations of popen() 
in the `os` and `popen2` modules and `commands` module

subprocess + CLI == win
why not?

! how?

subprocess
|-- run external command
|-- work with pipes directly
|-- connect segments of a pipe
|-- interact with another command
|-- signal between processes

"""