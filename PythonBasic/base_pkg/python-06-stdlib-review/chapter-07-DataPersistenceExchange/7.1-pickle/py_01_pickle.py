"""
! what?
pickle: object serialization

Serialization in Java is the process of converting the Java code Object into a Byte Stream,
to transfer the Object Code from one Java Virtual machine to another
and recreate it using the process of Deserialization.

! why?
Communication: Serialization involves the procedure of object serialization and transmission. 
               This enables multiple computer systems to design, share and execute objects simultaneously.
Caching: The time consumed in building an object is more compared to the time required for de-serializing it. 
         Serialization minimizes time consumption by caching the giant objects.

Deep Copy: Cloning process is made simple by using Serialization. 
           An exact replica of an object is obtained by serializing the object to a byte array, and then de-serializing it.

Cross JVM Synchronization: The major advantage of Serialization is that it works across different JVMs
                            that might be running on different architectures or Operating Systems

! how?

pickle
|-- encode and decode data in strings
|-- work with streams
|-- problems reconstructing objects
|-- unpicklable objects
|-- circular reference

? what is file handle?
`A number` that the operating system assigns temporarily to a file when it is opened.
The operating system uses the file handle internally when accessing the file.
`A special area of main memory` is reserved for file handles, 
and the size of this area determines how many files can be open at once.

In DOS and Windows, you can set the maximum number of open files with the FILES= statement in CONFIG.SYS.

"""