"""
hmm?

ModuleNotFoundError ...

ma-, iiya

"""
import resource
import time

RESOURCES = {
    ('ru_utime', 'User time'),
    ('ru_stime', 'System time'),
    ('ru_maxrss', 'Max. Resident Set Size'),
    ('ru_ixrss', 'Shared Memory Size'),
    # (,),
}

usage = resource.getrusage(resource.RUSAGE_SELF)

for name, desc in RESOURCES:
    print('{:<25} ({:<10}) = {}'.format(desc.name, getattr(usage, name)))