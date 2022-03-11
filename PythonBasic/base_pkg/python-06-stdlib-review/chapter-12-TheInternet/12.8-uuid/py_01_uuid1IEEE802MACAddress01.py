import uuid

"""
! UUID version 1 values are computed using the host’s MAC address.

If a system has more than one network card, 
and so more than one MAC address, 
any one of the values may be returned.

"""
print(hex(uuid.getnode()))