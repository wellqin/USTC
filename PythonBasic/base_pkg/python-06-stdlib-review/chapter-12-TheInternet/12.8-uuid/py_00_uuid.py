"""
! what?
the Internent is a pervasive aspect of modern computing.
even small, single-use scripts frequently interact with remote services to send or receive data.

Python's rich set of tools for working with web prototcols 
makes it well suited for programming web-based applications,
either as a client or as a server.

`uuid` is used for generating identifiers for resources
that need unique values.

UUIDs are good choices for automatically generating URN(Uinform Resource Name) values,
where the name of the resource needs to be unique but does NOT need to convery any meaning.

! why?
why not

! how?
`uuid` implements Universally Unique Identifiers as described in RFC 4122;
this RFC defines a system for creating unique identifiers for resources in a way that does not
require a central registrar.

UUID values are 128 bits long and, as the reference guide says,
“can guarantee uniqueness across space and time.” They are useful for generating identifiers

for documents, hosts, and application clients, and in other situations where a unique value
is necessary. The RFC specifically focuses on the creation of a Uniform Resource Name
namespace and covers three main algorithms:
- Using IEEE 802 MAC addresses as a source of uniqueness
- Using pseudorandom numbers
- Using well-known strings combined with cryptographic hashing

In all cases, the seed value is combined with the system clock and a clock sequence value
used to maintain uniqueness in case the clock is set backward.

! aha, system clock is from CPU  clock, it's monotonic ..
! clever

uuid: Universally Unique Identifiers
|-- UUID1: IEEE 802 MAC Address
|-- UUID3 and 5: Name-Based Values
|-- UUID4: Random Values
|-- Working with UUID Obj

"""