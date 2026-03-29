# Burp Suite — The Predator's Infrared Vision

**Date:** 29.03.2026
**Source:** Self-directed lab + exploration

## What is Burp Suite

A proxy tool that sits between your browser and the internet.
You become invisible. You see everything. You control everything.
```
Normal:    Browser ————————————→ Server
With Burp: Browser → Burp → Server
                      ↑
             you see and control everything here
```

The browser thinks it's talking to the server.
The server thinks it's talking to the browser.
Burp is the silent hunter in between.

## Core Concepts

### HTTP Request anatomy
```
GET /page HTTP/1.1       ← method + path + protocol version
Host: tryhackme.com      ← where the request goes
User-Agent: Mozilla/5.0  ← who is asking (can be faked)
Accept: text/html        ← what format we want back
Cookie: session=xyz      ← your identity token
```

### HTTP Response codes — the server's language
```
200 — OK, everything fine
301 — moved here permanently
302 — moved here temporarily  
403 — you are not allowed here
404 — doesn't exist
500 — server broke itself
```

### The four tools I used today

**Proxy → Intercept**
Stops every request before it reaches the server.
You decide: forward it, drop it, or modify it first.
This is where change User-Agent, parameters, cookies — anything.

**Proxy → HTTP History**
Every request that passed through Burp, logged automatically.
One page load = ~15 requests. Most sites = 100-200.
The internet is loud

**Repeater**
Send the same request infinite times with modifications.
Change one thing, observe what breaks.
This is how you test for vulnerabilities — methodically, like a scientist.

**Intruder** (discovered, not used yet)
Automated attack tool. Fuzzing, brute force, parameter testing.
Saving this for later. 

## What I Actually Did

### Modified User-Agent mid-flight
Intercepted a request to tryhackme.com.
Changed User-Agent to:
```
User-Agent: Predator/1.0 (HunterOS; x64)
```
The server received exactly that. It believed me.
Servers cannot verify who is really asking.
This is the foundation of identity spoofing.

### Sent a request to a path that doesn't exist
In Repeater: changed GET / to GET /doesnotexist
Server returned 404 — not found.
Interesting: the response still contained server headers.

## What Surprised Me

One page = 15+ requests. I thought clicking a link
was one action. It's actually dozens of parallel conversations
happening in milliseconds, completely invisible.

Also: I can lie to any server about who I am.
User-Agent, headers, cookies — all of it is just text I send.
The server has no way to verify any of it.
The entire web is built on trust. That trust can be abused.

The moment Intercept caught the first request and the browser
froze waiting — that was the moment I understood what a 
man-in-the-middle attack actually feels like. You are the middle.

## Open Questions

- What happens if I modify a Cookie header mid-request?
  Can I steal someone else's session this way?
- What is the Intruder tab actually capable of?
- How do sites detect that someone is using Burp?
- Can servers see that traffic is coming through a proxy?

## Tags
burp-suite, proxy, http, request-manipulation, 
intercept, repeater, web-security, mitm, headers