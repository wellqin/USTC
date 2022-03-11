"""
! what?
hmac: cryptographic message signing and verification
the basic idea is to generate a cryptographic hash of the actual data combined with a shared secret key.

the resulting hash can then be used to check the transmitted or store message to determine a level of trust,
w/o transimitting the secret key.

! why?
HMAC algorithm can be used to verify the integrity of information
passed between applications or stored in a potentially vulnerable locations.

! how?

hmac
|-- sign messages
|-- alternative digest types
|-- binary digests
|-- applications of message signatures

"""