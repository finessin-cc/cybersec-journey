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

Target tryhackme.com resolves to two address types:
IPv4: 172.66.164.239 and IPv6: 2606:4700:10::6814:1d42
Multiple IPs returned — the site uses Cloudflare CDN.

Proof: nslookup -type=NS tryhackme.com returned:
nameserver = uma.ns.cloudflare.com
nameserver = kip.ns.cloudflare.com

This means the real server IP is hidden behind Cloudflare.
What we see is Cloudflare's IP, not the actual server.
This is important — you cannot attack the real server directly
without first finding its true IP address.

Packet travelled through 10 hops to reach the target.
Hops 4 and 7 returned * * * — these routers are configured
to drop ICMP packets and are invisible to traceroute.
Average latency: ~20ms — server is geographically close.

## ?

I didn't expect a domain to hide behind a CDN like this.
I thought nslookup would give me the real server IP,
but it actually gives Cloudflare's IP instead.
The real server is completely invisible from the outside.
This changes everything — reconnaissance is not just
"find the IP", it's "find the real IP behind the shield".

Also surprised by the * * * hops in traceroute.
I thought it meant the connection failed,
but those routers are deliberately silent.
Someone configured them to be invisible. That's intentional stealth.

## Tags

networking, reconnaissance, dns, ping, traceroute, 
whois, osint, cloudflare, ipv4, ipv6, windows




