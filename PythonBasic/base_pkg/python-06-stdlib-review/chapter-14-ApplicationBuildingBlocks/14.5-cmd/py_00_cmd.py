"""
! what?
`cmd` contains one public class, "Cmd",
which is designed to be used as a base class
for interactive shells and other command interpreters.

by default, `cmd` uses readline for interactive prompt handling,
command-line editing, and command completion.

! why?
why not

! how?

cmd: line-oriented command processor
|-- processing commands
|-- command arguments
|-- Live help
|-- auto-completion
|-- overriding base class method
|-- configureing Cmd throu attributes
|-- running shell commands
|-- alternative inputs
|-- commands from sys.argv

"""