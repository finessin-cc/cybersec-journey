# Introductory Networking

## Task 2.The OSI Model: An Overview

Anxious Pale Shakespeare Treated Nervous Drunks Patiently

### Which layer would choose to send data over TCP or UDP? Answer with the number of the layer: e.g. if the answer would be "the application layer", then you would enter "7".

Layer 4 -- Transport

### Which layer checks received information to make sure that it hasn't been corrupted?

Layer 2 -- Data Link

### In which layer would data be formatted in preparation for transmission?

Layer 2 -- Data Link

### Which layer transmits and receives data?

Layer 1 -- Physical

### Which layer encrypts, compresses, or otherwise transforms the initial data to give it a standardised format?

Layer 6 -- Presentation

### Which layer tracks communications between the host and receiving computers?

Layer 5 -- Session

### Which layer accepts communication requests from applications?

Layer 7 -- Application

### Which layer handles logical addressing?

Layer 3 -- Network

### When sending data over TCP, what would you call the "bite-sized" pieces of data? 

With a protocol selected, the transport layer then divides the transmission up into bite-sized pieces (over TCP these are called segments, over UDP they're called datagrams), which makes it easier to transmit the message successfully. 

segments

### Which layer would the FTP protocol communicate with?

Layer 7 -- Application

### Which transport layer protocol would be best suited to transmit a live video?

UDP

## Task 3.Encapsulation

### How would you refer to data at layer 2 of the encapsulation process (with the OSI model)?

Frames

### How would you refer to data at layer 4 of the encapsulation process (with the OSI model), if the UDP protocol has been selected?

Datagrams

### What process would a computer perform on a received message?

de-encapsulation

### Which is the only layer of the OSI model to add a trailer during encapsulation?

Data Link

### Does encapsulation provide an extra layer of security (Aye/Nay)?

Aye

## Task 4. The TCP/IP Model

The TCP/IP model is, in many ways, very similar to the OSI model. It's a few years older, and serves as the basis for real-world networking. The TCP/IP model consists of four layers: Application, Transport, Internet and Network Interface.

The processes of encapsulation and de-encapsulation work in exactly the same way with the TCP/IP model as they do with the OSI model. At each layer of the TCP/IP model a header is added during encapsulation, and removed during de-encapsulation.

"Frank SYN-ACKtra"

When you attempt to make a connection, your computer first sends a special request to the remote server indicating that it wants to initialise a connection. This request contains something called a SYN (short for synchronise) bit, which essentially makes first contact in starting the connection process. The server will then respond with a packet containing the SYN bit, as well as another "acknowledgement" bit, called ACK

### Which model was introduced first, OSI or TCP/IP?

TCP/IP

### Which layer of the TCP/IP model covers the functionality of the Transport layer of the OSI model (Full Name)?

Transport

### Which layer of the TCP/IP model covers the functionality of the Session layer of the OSI model (Full Name)?

Application

### The Network Interface layer of the TCP/IP model covers the functionality of two layers in the OSI model. These layers are Data Link, and?.. (Full Name)?

Physical

### Which layer of the TCP/IP model handles the functionality of the OSI network layer?

Internet

### What kind of protocol is TCP?

connection-based

### What is SYN short for?

synchronise

### What is the second step of the three way handshake?

SYN/ACK

### What is the short name for the "Acknowledgement" segment in the three-way handshake?

ACK

## Task 5. Ping

The ping command is used when we want to test whether a connection to a remote resource is possible

The basic syntax for ping is ping <target>

### What command would you use to ping the bbc.co.uk website?

ping bbc.co.uk

### Ping muirlandoracle.co.uk What is the IPv4 address?

217.160.0.152

### What switch lets you change the interval of sent ping requests?

Step 1: man ping (on Linux)

-i

### What switch would allow you to restrict requests to IPv4?

-4

### What switch would give you a more verbose output?

-v

## Task 6. Traceroute

The logical follow-up to the ping command is traceroute. Traceroute can be used to map the path your request takes as it heads to the target machine.

The basic syntax for traceroute on Linux is this: traceroute <destination>

man traceroute (on Linux)

### What switch would you use to specify an interface when using Traceroute?

-i

### What switch would you use if you wanted to use TCP SYN requests when tracing the route?

-T or --tcp

### Which layer of the TCP/IP model will traceroute run on by default (Windows)?

Internet

## Task 7. WHOIS

Whois lookups are very easy to perform. Just use whois <domain> to get a list of available information about the domain registration

Step 1: whois facebook.com

### What is the registrant postal code for facebook.com?

94025

### When was the facebook.com domain first registered (Format: DD/MM/YYYY)?

29/03/1997

Step 2: whois microsoft.com

### Which city is the registrant based in?

Redmond

### [OSINT] What is the name of the golf course that is near the registrant address for microsoft.com?

Bellevue Golf Course

### What is the registered Tech Email for microsoft.com?

msnhst@microsoft.com

## Task 8. Dig

Dig allows us to manually query recursive DNS servers of our choice for information about domains:
dig <domain> @<dns-server-ip>

### What is DNS short for?

Domain Name System

### What is the first type of DNS server your computer would query when you search for a domain?

recursive

### What type of DNS server contains records specific to domain extensions (i.e. .com, .co.uk*, etc)*? Use the long version of the name.

Top-Level Domain

### Where is the very first place your computer would look to find the IP address of a domain?

Hosts File

### Google runs two public DNS servers. One of them can be queried with the IP 8.8.8.8, what is the IP address of the other one?

8.8.4.4

### If a DNS query has a TTL of 24 hours, what number would the dig query show?

86400 : 3600*24 hours
