"""
! what?
temporrary file system objects

! why?
Creating temporary files with `unique names` `securely`,
so they cannot be guessed by someone wanting to break the application or steal the data, is challenging


! how?
Applications that need temporary files to store data,
w/o needing to share that file with other programs,
should use tempfile


tempfile
|-- temporary files
|-- named files
|-- spooled files
|-- temporary directories
|-- predicting names
|-- temporary file location

"""