"""
! what?
`doctest` tests source code by running examples embeded in the documentation
and verifying that they produce the expected results.

it works by parsing the help text to find examples,
running them, and then comparing the output text with the expected value.

many developers find `doctest` easier to use than `unittest`
because, in its simplest form, there is no API to learn before using it.

however, as the examples become more complex,
the lack of fixture management can make writing `doctest` tests more
cumbersome than using `unittest`.

! why?
why not

! how?

doctest: testing throu documentation
|-- gettting started
|-- handling unpredictable output
|-- tracebacks
|-- work around whitespace
|-- test locations
|-- external documentation
|-- running tests
|-- test context


"""