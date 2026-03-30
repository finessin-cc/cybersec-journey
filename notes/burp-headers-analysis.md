# HTTP Headers — What Servers Accidentally Confess

**Date:** 30.03.2026
**Target:** juice-shop.herokuapp.com
**Tools:** Burp Suite

## Objective

Analyze HTTP response headers to extract technology
information without touching the server.
Headers are public. Servers can't hide them.
Every response is a confession.

## Findings

### Headers that leaked infrastructure

Server: Heroku
→ hosting platform identified

Via: 1.1 heroku-router
→ internal routing system exposed
→ confirms Heroku infrastructure

Feature-Policy: payment 'self'
→ site processes payments
→ payment flows exist = high value target

### The unexpected find

X-Recruiting: /#/jobs
→ Juice Shop recruits developers via HTTP header
→ In real applications: custom headers sometimes
  reveal internal paths, test endpoints, employee names
→ Always read ALL headers. Nothing is too small.

### Security headers present (good practices)

X-Content-Type-Options: nosniff
→ prevents MIME type sniffing attacks

X-Frame-Options: SAMEORIGIN
→ prevents clickjacking

### X-Powered-By — absent
→ deliberately hidden by Juice Shop
→ good security practice
→ but other headers compensated —
  infrastructure still fingerprinted

## IDOR Attempt — /rest/products/1/reviews

Changed product ID from 1 → 2 → 3 in Repeater.
Response did not change.
Either all products have the same reviews,
or the endpoint is not vulnerable to IDOR here.

Note: IDOR exists when changing an ID gives you
access to someone else's data.
This endpoint didn't expose it — but the pattern
is worth remembering. Real IDOR targets:
/api/users/1 → /api/users/2
/orders/1001 → /orders/1002

## What Surprised Me

X-Recruiting header — a company hiding its tech stack
but advertising jobs through HTTP headers.
Security and marketing living in the same response.

Also: X-Powered-By was absent but the infrastructure
was still fully fingerprinted through other headers.
You can't hide everything. Something always leaks.

## Key Takeaway

Headers are not decoration.
They are an unintended autobiography of the server.
Read every single one.

## Tags
burp-suite, http-headers, fingerprinting,
information-disclosure, idor, heroku, recon


