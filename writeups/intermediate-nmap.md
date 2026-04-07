# Intermediate Nmap — Write-up

In this room, the goal was to combine Nmap scanning and basic protocol knowledge to gain access to the target machine and retrieve the flag.

## Step 1

nmap -p- -A MACHINE_IP

We can see: 

In case I forget - user:pass
ubuntu:Dafdas!!/str0ng

## Step 2

root@ip-10-113-125-24:~# ssh ubuntu@10.113.134.123 -p 22

And we are in!

## Step 3

$ pwd
/home/ubuntu
$ cd ..
$ ls
ubuntu	user
$ cd user
$ ls
flag.txt
$ cat flag.txt
** flag{251f309497a18888dde5222761ea88e4} **

Key Takeaways
1. Always scan all ports, not just the default ones
2. High ports can expose useful hints or hidden services
3. Pay attention to service responses - they often guide the next step