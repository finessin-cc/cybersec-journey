# Nmap — The Echolocator

**Date:** 30.03.2026
**Target:** scanme.nmap.org
**Tools:** Nmap

## Objective

Map the target using three progressive scans.
Each scan reveals more than the previous one.
Goal: understand what information each Nmap
flag unlocks — and why attackers use all three.

## Scan 1 — Basic Port Discovery

nmap scanme.nmap.org

PORT      STATE    SERVICE
22/tcp    open     ssh
25/tcp    filtered smtp
80/tcp    open     http
9929/tcp  open     nping-echo
31337/tcp open     Elite

Result: 5 ports found. Know what's open.
Don't know what's running on them yet.

## Scan 2 — Service Version Detection (-sV)

nmap -sV scanme.nmap.org

PORT      STATE    SERVICE    VERSION
22/tcp    open     ssh        OpenSSH 6.6.1p1 Ubuntu
25/tcp    filtered smtp
80/tcp    open     http       Apache httpd 2.4.7 (Ubuntu)
9929/tcp  open     nping-echo Nping echo
31337/tcp open     tcpwrapped

New information: exact software versions exposed.
Apache 2.4.7 = released 2014.
Search cve.mitre.org for "Apache 2.4.7" →
known vulnerabilities with public exploits available.
Old software = open door.

## Scan 3 — Default Scripts (-sC)

nmap -sC scanme.nmap.org

New information: SSH host keys exposed.
DSA, RSA, ECDSA, ED25519 fingerprints visible.

If the key changes on next scan →
possible MITM attack between me and server.
SSH keys are a fingerprint of server identity.

## Analysis

### Port 22 — SSH (Secure Shell)
Remote server management. Encrypted.
Attack vector: brute force password attacks.
Defense: key-based auth + change default port.

### Port 25 — SMTP (filtered)
Mail server. Firewall blocking probes.
Filtered ≠ closed. Something is there.
High security or deliberate concealment.

### Port 80 — Apache 2.4.7
Web server. Version from 2014.
CVE hunting target — search exploit-db.com
for known vulnerabilities on this exact version.

### Port 9929 — Nping Echo
Nmap's own test tool. Expected on scanme.nmap.org.

### Port 31337 — Elite
Named after hacker leet speak: 31337 = ELEET.
Historical: used by Back Orifice RAT (1998).
First major Remote Access Trojan in history.
On this server: intentional easter egg.
In the wild: red flag. Investigate immediately.

## Three Scans — Three Layers of Intelligence

nmap target          → doors (what's open)
nmap -sV target      → tenants (what's running)
nmap -sC target      → secrets (keys, configs, details)

Always run all three. Each layer matters.

## What Surprised Me

Port 31337 being named "Elite" — I didn't expect
cultural history inside a port number.
Hacker culture embedded in a network scan.

Apache 2.4.7 from 2014 still running on a public server.
Real targets run outdated software all the time.
Version detection isn't just information —
it's a direct path to known exploits.

## Open Questions

- How do I search CVE databases efficiently?
- What does tcpwrapped mean on port 31337?
- Can Nmap detect if a service is honeypot?
- What other Nmap flags exist beyond -sV and -sC?

## Tags
nmap, port-scanning, reconnaissance, ssh, http,
apache, cve, version-detection, network,
leet, back-orifice, fingerprinting