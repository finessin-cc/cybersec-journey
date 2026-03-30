# Burp Suite Recon — OWASP Juice Shop

**Date:** 30.03.2026
**Target:** juice-shop.herokuapp.com
**Difficulty:** Easy
**Tools:** Burp Suite Community Edition, Browser

## Objective

Perform passive reconnaissance on OWASP Juice Shop
using Burp Suite. Goal: intercept real requests,
identify information leaks, and understand what
an attacker sees before any real exploitation begins.

## Target Overview

OWASP Juice Shop — intentionally vulnerable web application.
Designed for security training. Hosted on Heroku.
Safe and legal to attack.

## Findings

### 1. Login Form — Credentials in Plain Sight

Intercepted POST request during login attempt:

POST /rest/user/login HTTP/1.1
Host: juice-shop.herokuapp.com
Content-Type: application/json

{"email":"admin","password":"12345"}

The password travels in plaintext inside the request body.
A Man-in-the-Middle attacker positioned between the user
and the server receives credentials without any effort.
No brute force needed. No server access needed.
Just intercept and read.

Attack vector: MITM → credential theft → admin takeover
→ full access to customer data → privilege escalation.

### 2. Open Redirect — The Server Betrays Its Users

Found in HTTP History:

GET /redirect?to=https://github.com/juice-shop/juice-shop

The application redirects users to an external URL
passed as a parameter. This parameter is not validated.

An attacker can replace the destination:
/redirect?to=https://evil-fake-login.com

The victim sees a trusted domain in the URL.
The site redirects them to a phishing page.
The company's own infrastructure becomes the attack weapon.
This is called an Open Redirect vulnerability.

### 3. Server Header — Technology Fingerprint

Found in HTTP Response headers:

Server: Heroku

One header reveals the entire hosting infrastructure.
Now an attacker knows:
→ Platform: Heroku (cloud hosting)
→ Can search Shodan for exposed Heroku instances
→ Can research Heroku-specific vulnerabilities
→ Knows what misconfigurations to look for

Information the company didn't intend to share.
Leaked automatically with every single response.

## What Surprised Me

I expected hacking to be complicated.
The first real finding was just... reading.
The password was right there in the intercepted request.
No special technique. No exploit. Just being in the middle.

The Open Redirect was even more surprising.
The site itself becomes a phishing tool.
The attacker doesn't need to build infrastructure —
they use the victim's trusted domain against them.

The most dangerous attacks aren't loud.
They're quiet. They use what's already there.

## Attack Chain (what this could lead to)

Recon → Intercept login → steal admin credentials
→ login as admin → access all customer data
→ modify redirect → phish other users
→ full compromise

## Open Questions

- Can I intercept HTTPS traffic the same way?
  (Burp has SSL certificates for this — research next)
- What other headers leak technology information?
- How do sites protect against Open Redirect?
  What does proper validation look like?
- If the password is hashed before sending,
  can it still be intercepted and reused? (pass-the-hash)

## Tags

burp-suite, proxy, http, intercept, mitm,
open-redirect, information-disclosure, credentials,
heroku, owasp, juice-shop, reconnaissance