"""
! what?
the Internent is a pervasive aspect of modern computing.
even small, single-use scripts frequently interact with remote services to send or receive data.

Python's rich set of tools for working with web prototcols 
makes it well suited for programming web-based applications,
either as a client or as a server.

HTTP POST requests are usually "form encoded" with `urlib`.
Binary data sent through a POST should be encoded with `base64` first,
to comply with the message format standard.


details
the `base64` module contains functions for translating binary data into a subset of ASCII suitable for transmission using plaintext protocol.
- Base64
- Base32
- Base16
- Base85
encodings convert 8-bit bytes to represent the data for compatibility
with systems that support only ASCII data, such as SMTP.

the base values correspond to the length of the alphabet used in each encoding.

URL-safe variations of the original encodings use slightly different alphabets.

! why?
why not

! how?

? difference btwn binascii and base64?
Table: binascii vs base64 vs uu
+--------+--------------------------------------+---------------+---------------+
| item   | binascii                             | uu            | base64        |
+========+======================================+===============+===============+
| what   | binary <-> various                   | high-level    | high-level    |
|        | ASCII-encoded binary representations |
+--------+--------------------------------------+---------------+---------------+
| why    | socket, encryptography etc.,         | high-level    | high-level    |
+--------+--------------------------------------+---------------+---------------+
| how    | contains low-level functions written | high-level    | high-level    |
|        | in C for greater speed that are used |               |               |
|        | by the higher-level modules          |               |               |
+--------+--------------------------------------+---------------+---------------+

base64: Encode Binary Data with ASCII
|-- Base 64 Encoding
|-- Base64 Decoding
|-- URL-Safe Variations
|-- Other Encodings

"""