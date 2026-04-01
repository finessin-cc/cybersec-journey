# Questions & Answers
**1. What is the difference between Stored XSS and Reflected XSS?**

Stored XSS occurs when a malicious script is permanently stored on the server (e.g., in a database) and executed when users load the affected page.
Reflected XSS occurs when the malicious script is included in a request (such as a URL) and immediately reflected in the server’s response without being stored.

**2. Why doesn’t <script>alert('xss')</script> always work?**

Most modern applications use input filtering, output encoding, and Web Application Firewalls (WAFs) that block or sanitize basic XSS payloads, preventing them from executing.

**3. What is document.cookie and why do attackers want to steal it?**

document.cookie provides access to cookies stored in the browser. Attackers target it because cookies often contain session identifiers, which can be used to hijack a user’s session and impersonate them.

**4. Why is btoa() used in XSS payloads?**

btoa() encodes data into Base64, allowing it to be safely transmitted in URLs or requests without breaking due to special characters. It is not inherently a filter bypass technique but can help obfuscate payloads.

**5. What does HTTP status code 302 mean?**

HTTP 302 indicates a temporary redirect, meaning the requested resource is temporarily located at a different URL.

**6. How is traceroute different from ping?**

ping checks whether a host is alive and measures response time.
traceroute shows the path packets take through the network, including each intermediate hop.

**7. What is a supply chain attack? Explain using GitHub as an example.**

A supply chain attack targets trusted third-party services or dependencies. In the context of GitHub, an attacker might compromise a dependency, integration, or external service used by a project, thereby affecting all users of that project.

**8. Why is try/except used in Python?**

try/except is used for error handling. It allows a program to catch and handle exceptions without crashing, ensuring more stable execution.

**9. What does sock.settimeout(1) do in a port scanner?**

It sets the maximum time (1 second) the program will wait for a response from a port. If no response is received within that time, the port is treated as closed or unresponsive.

**10. Which NS servers does GitHub use?**

GitHub uses AWS-managed DNS servers (e.g., awsdns), despite being owned by Microsoft.
