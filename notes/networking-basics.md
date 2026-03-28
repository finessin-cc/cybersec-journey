# Networking Basics

# 28.03.2026

## Creature №1 — Anatomy of the Internet

Dossier: How data travels across the network

Imagine the internet as a Jurassic-era ecosystem. Vast, complex, with its own survival rules.
Every computer in this ecosystem is an island. To send a message from one island to another, you need a system. That system is called TCP/IP.

# Act 1 — IP Address: Island Coordinates

Every island has coordinates — an IP address. For example: 192.168.1.1.
It’s like GPS coordinates in the jungle. Without them, no one can find your island.

There are two types:

Local IP — your address inside your home network. Only nearby devices can see it.
Public IP — your address on the global internet. The whole world can see it.

# Act 2 — Ports: Doors on the Island

Imagine your computer is a giant Diplodocus. It has 65,535 doors (ports) all over its body.
Each door is for a specific visitor:

Door 80 — regular web traffic (HTTP)
Door 443 — secure web traffic (HTTPS)
Door 22 — SSH (remote control)
Door 21 — FTP (file transfer)

A hacker’s first move is to knock on all the doors — checking which ones are open. This is called port scanning. That’s exactly what Nmap does — the primary reconnaissance tool.

# Act 3 — Protocols: Language of Creatures

Different creatures speak different languages. In networking, these are called protocols.

TCP — slow but reliable. Like a Triceratops: strong and methodical. It establishes a connection first, then sends data. If a packet is lost — it resends it.
UDP — fast but with no guarantees. Like a Pterodactyl: swift and agile. It just throws data and moves on. Used in games and video calls — where speed matters most

# Act 4 — DNS: Name Translator

You type “google.com” — but the computer doesn’t understand words, only numbers (IP addresses).

DNS is the translator. Like a creature that knows every language in the ecosystem.

You say:
“google.com” → DNS replies: “that’s 142.250.185.46” → the browser goes there.

# Act 5 — OSI Model: The Food Chain

When you send a message to a friend — it passes through 7 layers. Like a food chain: each level consumes the previous one and passes it on.

## All People Seem To Need Data Processing

Application, Presentation, Session, Transport, Network, Data Link, Physical

# Application — Application Layer

HTTP, DNS, FTP, SSH
The alpha predator — what the user actually sees

This is what you interact with directly — browser, email, messenger. Protocols include: HTTP (websites), DNS (addresses), FTP (file transfer), SMTP (email).

Attacks: XSS, SQL injection, phishing

# Presentation — Presentation Layer

Encryption, compression, encoding
The translator — transforms data formats

Converts data into a format the receiver can understand. This is where SSL/TLS encryption works — the very thing that makes HTTPS secure.

Attacks: SSL stripping, downgrade attacks

# Session — Session Layer

Session and connection management
The memory of the ecosystem — remembers who is talking to whom

Responsible for establishing, maintaining, and terminating sessions between applications. Cookies and authentication tokens operate at this level.

Attacks: session hijacking, cookie theft

# Transport — Transport Layer

TCP and UDP — ports 0–65535
Logistics — how to deliver and through which door

Determines HOW data is delivered. TCP — reliable with acknowledgment. UDP — fast with no guarantees. This is where ports live — the doors to your computer.

Attacks: port scanning, SYN flood, TCP hijacking

# Network — Network Layer

IP addresses, routing
The navigator — charts the path through the jungle

Responsible for addressing and routing — how a packet finds its way from your computer to a server through dozens of intermediate nodes. This is where IP addresses live.

Attacks: IP spoofing, MITM, routing attacks

# Data Link — Data Link Layer

MAC addresses, Ethernet, Wi-Fi
A local resident — knows all neighbors on the network

Handles data transfer between devices within the same local network. Each device has a unique MAC address — like a hardware fingerprint.

Attacks: ARP spoofing, MAC flooding

# Physical — Physical Layer

Cables, radio waves, bits
The ground — the foundation everything stands on































