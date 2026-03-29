# Lab 01 - Network Recon

29.03.2026
Target: tryhackme.com
Difficulty: easy
Tools used: ping, tracert, nslookup, whois

## About

Perform passive and active reconnaissance on tryhackme.com using only built-in Windows tools and public WHOIS data. Goal: understand what information is publicly visible about a target before any real attack begins. This is what a hacker does first — before touching anything.

## Commands & Output

### Checking if target is alive

#### ping tryhackme.com

Reply from 2606:4700:10::6814:1d42: time=21ms
Reply from 2606:4700:10::6814:1d42: time=20ms
Reply from 2606:4700:10::6814:1d42: time=19ms
Reply from 2606:4700:10::6814:1d42: time=16ms

#### ping -4 tryhackme.com (ip4)

Reply from 172.66.164.239: bytes=32 time=21ms TTL=54
Reply from 172.66.164.239: bytes=32 time=20ms TTL=54
Reply from 172.66.164.239: bytes=32 time=18ms TTL=54
Reply from 172.66.164.239: bytes=32 time=20ms TTL=54

### Trace the route 

#### tracert tryhackme.com

  1     3 ms     3 ms     3 ms  2a02:a31a:a1c8:5900::1
  2    16 ms    15 ms    13 ms  2a02:a304:0:a55::1
  3    26 ms    51 ms    11 ms  2a02:a300:e60:6:0:1502:0:1
  4     *        *        *     
  5    20 ms    21 ms    17 ms  2001:730:2c00::5474:8024
  6    17 ms    16 ms    18 ms  2001:4c08:200f::68e
  7     *        *        *     
  8    40 ms    22 ms    19 ms  2001:978:2:4b::49
  9    16 ms    16 ms    16 ms  2400:cb00:923:3::
 10    14 ms    18 ms    20 ms  2606:4700:10::ac42:a4ef

### DNS lookup

#### nslookup tryhackme.com

Name:     tryhackme.com
Addresses:  2606:4700:10::6814:1d42
          2606:4700:10::ac42:a4ef
          104.20.29.66
          172.66.164.239

## Findings

Packet travels through 10 hops to reach the server. Most hops are inside ISP infrastructure. Interesting: some hops returned * * * — those routers are configured to drop ICMP packets (stealth mode)

## ?

How does Cloudflare decide which IP to return for a DNS query? Is it based on my location? I got two different IPs — are they in different data centers?






