"""
! what?
`logging` defines a standard API for reporting errors and status
information from applications and libraries.

the key benefit of having a standard library module provide the logging API
is that all Python modules can participate in logging,
so an application's log can include message from third-party modules.

logging components
|-- Logger    :  Logger creates LogRecord, may have a number of Handler obj configured to receive and process log records
|-- LogRecord :  holds informatino in memory until it is processed
|-- Handler   :  receive and process log records
|-- Formatter :  Handler uses Formatter to turn the log records into output messages

! why?
stfu


! how?

logging: report status, error, and informational messages
|-- logging components
|-- logging in application vs libraries
|-- logging to a file
|-- rotating log files
|-- verbosity levels
|-- naming logger instances
|-- integration with the warning module


"""