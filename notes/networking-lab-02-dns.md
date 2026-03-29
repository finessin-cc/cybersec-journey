# Lab 02 - DNS lookup

29.03.2026
Target: tryhackme.com
Difficulty: easy
Tools used: nslookup

## About

DNS Under the Microscope

## Commands & Output

#### nslookup -type=MX tryhackme.com

Address:  2a02:a302:0:1::10

#### nslookup -type=TXT tryhackme.com

Address:  2a02:a302:0:1::10

tryhackme.com   text =

        "zapier-domain-verification-challenge=267a6fd6-7041-48fe-ba4b-02d72fe60413"
tryhackme.com   text =

        "v=spf1 include:_spf.google.com include:email.chargebee.com include:7168674.spf05.hubspotemail.net ~all"
tryhackme.com   text =

        "6ca7e8e9845fa51969caa46c95cf230d"
tryhackme.com   text =

        "anthropic-domain-verification-azydkj=zpI52q9Mi6RXuR8EflRqMe6q1"
tryhackme.com   text =

        "google-site-verification=AlFrMBXuBQ-zDeey1Qo8m0dRJRUrrNBMnFa4r4aX4gI"
tryhackme.com   text =

        "google-site-verification=GCyTff0OB7u9Z0DvK942SCYTy1hLYcwWvalZWlRFbCs"
tryhackme.com   text =

        "google-site-verification=umR4x8HuzWMF5g3656JY1b-61NuryD0-GqGnYN13ONo"

#### nslookup -type=NS tryhackme.com

Address:  2a02:a302:0:1::10

tryhackme.com   nameserver = uma.ns.cloudflare.com
tryhackme.com   nameserver = kip.ns.cloudflare.com

## Findings

MX (Mail Exchange) — identifies the mail servers responsible for receiving email on behalf of the domain.
NS (Name Server) — specifies the authoritative name servers for the domain.
TXT (Text Records) — contains arbitrary text data; often used for verification, security (e.g., SPF, DKIM), or sometimes hidden interesting information

What I actually found — OSINT in action:

TXT records revealed the entire tech stack of TryHackMe:

1. Anthropic (Claude AI)
   anthropic-domain-verification-azydkj=zpI52q9Mi6RXuR8EflRqMe6q1
   → TryHackMe uses Claude. Found in DNS. No hacking needed.

2. Google
   include:_spf.google.com
   → Google handles their email infrastructure.

3. Chargebee
   include:email.chargebee.com
   → This is their payment system. The one that charges
     your Premium subscription.

4. HubSpot
   include:7168674.spf05.hubspotemail.net
   → Marketing emails and user analytics.

This technique is called tech stack fingerprinting.
From one SPF record, we mapped what services a company
runs — without touching their servers.
This is real OSINT. Public data, zero noise.

## What Surprised Me

I expected DNS to just return IP addresses.
Instead it revealed the entire infrastructure of a company.
One TXT record = their payment provider, email system,
AI tools, and marketing platform.

The most unexpected find: TryHackMe uses Anthropic (Claude).
I discovered this not from their website — from their DNS.
That's the point. Companies can't hide what's in their DNS.
It's public by design. And that's exactly why attackers look here first.
