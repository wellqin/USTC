"""
Applications use the network to communicate with servers for domain name service (DNS)
operations such as converting between hostnames and IP addresses. 

asyncio event loops include convenience methods to take care of those operations 
in the background, so as to avoid blocking during the queries.
"""