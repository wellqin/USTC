"""
! what?
`sched` implements a generic event scheduler 
for running tasks at specific times.

the scheduler class uses a `time` function to learn the current time,
uses a `delay` function to wait for a specific period of time.

the actual units of time are not important,
so the interface is flexible enough to be used for many purposes.

- `time` function
is called w/o any arguments, and should return a number representing the current time.

- `delay` function
is called with a single integer argument, using the same scale as the time function,
and should wait that many time until before returning.

by default,
monotonic() and sleep() from the `time` module are used,
but the examples in this section use time.time(), which also meets the requirements,
because it makes the output easier to understand.

NOTE:
to support multithreaded applications,
the delay functino is called with argument 0 after each event is generated,
to ensure that other threads also have a chance to run.


! why?
why not

! how?

sched: Timed Event Scheduler
|-- running events with a Delay
|-- overlapping events
|-- event priorities
|-- canceling events

"""