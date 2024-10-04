"""
! what?
the Internent is a pervasive aspect of modern computing.
even small, single-use scripts frequently interact with remote services to send or receive data.

Python's rich set of tools for working with web prototcols 
makes it well suited for programming web-based applications,
either as a client or as a server.

Well-behaved clients that access many sites as a spider or crawler
should use `urlib.robotparser` to ensure they have permission before placing a heavy load on the remote server.

robotparser implements a parser for the robot.txt file format,
including a function that checks whether a given user agent can access a resource.
It is intended for use in well-behaved spiders, or other crawler applications that need to be throttled or otherwise restricted.

? what is `robots.txt`?
the robots.txt file format is a simple text-based access control system
for computer programs that automatically access web resources("spiders", "crawlers", and the like).

The file is made up of records that specify the user agent identifier for the program,
followed by a list of URLs (or URL prefixes) that the agent may not access. 

further reference
link: www.robotstxt.org/orig.html

! why?
why not

! how?

"""