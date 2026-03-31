# OSINT Profile — GitHub.com

**Date:** 31.03.2026
**Target:** github.com
**Tools:** ping, traceroute, nslookup, nmap, Burp Suite
**Environment:** TryHackMe AttackBox (Linux)

## Objective

Build a complete intelligence profile of github.com
using only public tools and data.
No touching the target. No exploitation.
Pure reconnaissance — the way every real attack begins.

## Commands & Output

### DNS Reconnaissance

nslookup -type=NS github.com
→ ns-421.awsdns-52.com
→ ns-520.awsdns-01.net
→ dns1.p08.nsone.net (x4)
→ ns-1283.awsdns-32.org
→ ns-1707.awsdns-21.co.uk

nslookup -type=MX github.com
→ github-com.mail.protection.outlook.com

nslookup -type=TXT github.com
→ SPF, verification tokens from multiple services
→ Full list in Findings section

### Port Scan

nmap -sV github.com (140.82.121.3)
→ 22/tcp  open  ssh
→ 80/tcp  open  http
→ 443/tcp open  ssl/https
→ 997 ports filtered

### HTTP Headers (Burp Suite)

Server: Windows-Azure-Web/1.0
X-Served-By: cache-iad-kjyo7100165-IAD,
             cache-fra-etou8220163-FRA

## Findings

### 1. Tech Stack — Full Company Profile from DNS

TXT records revealed every service GitHub uses:

Infrastructure & DNS:
→ AWS Route53 (awsdns) — DNS management
→ Microsoft Azure — web hosting (Server header)
→ Tailscale — internal VPN

Communication & Support:
→ Outlook/Exchange — corporate email (MX record)
→ Zendesk — customer support
→ Mailchimp (mcsv.net) — marketing emails
→ SendGrid — transactional emails

Business Tools:
→ Atlassian — Jira/Confluence (issue tracking)
→ Salesforce — CRM
→ Docusign — document signing
→ Calendly — scheduling
→ Loom — video messaging
→ Miro — visual collaboration

Payments & Commerce:
→ Stripe — payment processing
→ Shopify — e-commerce

Analytics & Identity:
→ Adobe — analytics/identity
→ Facebook — domain verification
→ Google — site verification (x2)
→ Jamf — Apple device management
→ Krisp — audio/noise cancellation

This is called attack surface mapping.
Every service is a potential entry point.
You don't need to attack GitHub directly —
you attack their weakest vendor.

### 2. Microsoft Uses AWS for DNS

GitHub is owned by Microsoft. Hosted on Azure.
But DNS runs on AWS Route53 — a competitor's product.

This is normal in enterprise environments.
Companies mix cloud providers for reliability.
But it means: even Microsoft trusts AWS
with critical infrastructure.

NS records = AWS
Web server = Azure
Email = Microsoft Outlook

Three different providers for one company.
Each is an independent attack surface.

### 3. CDN Geolocation — Where the Servers Are

X-Served-By header revealed two CDN nodes:
IAD = Dulles International Airport = Washington DC
FRA = Frankfurt Airport = Frankfurt, Germany

Request from Poland → served by Frankfurt node.
Closest geographic server responds automatically.

This is how CDNs work — the real origin server
is hidden behind a global network of edge nodes.
GitHub's actual infrastructure is invisible.
What we see is Fastly/CDN — not the real servers.

### 4. Supply Chain Attack Surface

From one DNS lookup, we mapped 15+ vendors.
In 2020, SolarWinds was compromised not directly —
but through a software update from a trusted vendor.
Attackers accessed thousands of companies
without ever touching their main infrastructure.

GitHub's Stripe integration, Salesforce CRM,
Atlassian workspace — each is a door.
Not to GitHub. To GitHub's data.

### 5. Linux vs Windows Commands

Discovered during this lab:
Windows: tracert
Linux:   traceroute
Same function. Different name. Know both.

## What Surprised Me

Microsoft owns GitHub.
GitHub runs on Azure.
But GitHub's DNS runs on AWS — Microsoft's competitor.

Enterprise infrastructure is not clean and logical.
It's a patchwork of best-in-class services
accumulated over years of acquisitions and decisions.
Every patch is a potential gap.

15 vendors revealed from public DNS records.
Zero interaction with GitHub's servers needed.
The company's entire supply chain
is written in their TXT records.
They can't hide it. DNS is public by design.

## Attack Chain (theoretical)

Recon → map vendors via TXT records →
identify weakest vendor (smallest security team) →
find CVE for that vendor's software →
exploit vendor → pivot to GitHub data →
never touch github.com directly

This is how nation-state attacks work.

## Open Questions

- Which of these 15 vendors has had CVEs recently?
- How do I search for vendor-specific vulnerabilities
  efficiently? (next: exploit-db.com research)
- What is Tailscale and why does GitHub use it
  for internal networking?
- How does Fastly CDN hide the real origin IP?
  Can it be bypassed?

## Key Takeaway

Reconnaissance is not about the target.
It's about the target's ecosystem.
The weakest link is never the main door.

## Tags
osint, dns, recon, github, microsoft, aws, azure,
txt-records, supply-chain, cdn, attack-surface,
nmap, burp-suite, tech-fingerprinting, linux