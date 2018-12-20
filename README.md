# Remote-Log-Monitoring

This project is a desktop project remotely log user browser activity using [python3](https://www.python.org/download/releases/3.0/) and 
standard gui interface [Tkinter](https://docs.python.org/3/library/tk.html).

## Pre conditions 

Before using the application you should install python better if the vesrsion is python 3.6.* 

	$ pip install tkinter

	$ pip install watchdog

	$ pip install apache_log_parser

	$ pip install logging 

## How to use the application
Assume you are at the logger side start py running : 

	$ python login_waf.py

![screenshot from 2018-12-20 02-50-28](https://user-images.githubusercontent.com/45997793/50274248-c141a680-040a-11e9-880d-f88e59968a30.png)
![screenshot from 2018-12-20 02-49-27](https://user-images.githubusercontent.com/45997793/50274294-e0403880-040a-11e9-9f1a-46266fe5a367.png)
![screenshot from 2018-12-20 02-50-00](https://user-images.githubusercontent.com/45997793/50274303-e7674680-040a-11e9-8aa6-d397e786996d.png)



# Documentation of Project 

## INTRODUCTION
It is often the case that web applications face suspicious activities due to various reasons, 
such as a kid scanning a website using an automated vulnerability scanneror a person trying to fuzz a parameter for SQL Injection, etc.
In many such cases, logs on the web server have to be analyzed to figure out what is going on. 
If it is a serious case, it may require a forensic investigation.In the current scenario where time is money, the internet due to its versatile nature and time-saving features has influenced every age group and made them dependent on it, which has increased the internet usage exponentially. Due to a vast number of users, the internet has become more vulnerable to threats and attacks. This tool that monitors the web server for possible malicious activities and file modification (defacement) it also detects a malicious web shell and malicious files in a web server.


## Project features 
                                          
    • should detect file modification
    • should detect all types of files extensions      
    • should have Remote log access capability
    • should have an alert for any suspicious modifications and activity
    • should have a remote view dashboard

## Web applications attacks
Web based attacks are considered by security experts to be the greatest and oftentimes the least understood of all risks related to confidentiality, availability, and integrity.
Detecting file modification 
Any unusual modification inside contents might be harmful for the server.
    • Modify - the last time the file was modified (content has been modified).
    • Change - the last time metadata of the file was changed.
Conditions to meet in order to detect file modification would be.
    1. If the system gives an alert that the file modified at some unexpected time. Here the flowchart of this module
    2. If the system gives an alert that there has been a change in file size either increase or decrease.
		

Detect all types of files extensions:A file extension sometimes called a file suffix or a filename extension is the character or group of characters after the period that makes up an entire filename.our web application firewall alert if there has been a change for file extension in the system.


### Shell upload (New Activities )
Test Upload Of Malicious Files OTG-BUSLOGIC-009 
Many application’s business processes allow for the upload of data/information. We regularly check the validity and security of text but accepting files can introduce even more risk. To reduce the risk we may only accept certain file extensions, but attackers are able to encapsulate malicious code into inert file types. Testing for malicious files verifies that the application/system is able to correctly protect against attackers uploading malicious files.

Vulnerabilities related to the uploading of malicious files is unique in that these “malicious” files can easily be rejected through including business logic that will scan files during the upload process and reject those perceived as malicious. Additionally, this is different from uploading unexpected files in that while the file type may be accepted the file may still be malicious to the system.

Finally, "malicious" means different things to different systems, for example Malicious files that may exploit SQL server vulnerabilities may not be considered a "malicious" to a mainframe flat file environment.

Web server log files
A Web log file records activity information when a Web user submits a request to a Web Server. The main source of raw data is the web access log which we shall refer to as log file. As log files are originally meant for debugging purposes. 
A log file can be located in three different places:
 i) Web Servers, 
             ii)Web proxy Servers, and
iii)Client browsers.




i)Server side logs:These logs generally supply the most complete and accurate usage data.
A log file is an extremely valuable piece of information which is provided by a server. Almost all servers, services and applications provide some sort of logging. log file records events and actions that take place during the runtime of a service or application.
 Log files provide us with a precise view of the behavior of a server as well as critical information like when, how and “by whom” a server is being accessed. This kind of information can help us monitor the performance, troubleshoot and debug applications, as well as help forensic investigators unfold the chain of events that may have led to a malicious activity.
Let’s take as an example a web-server. Most commonly, Apache HTTP Server will provide two main log files – access.log and the error.log. The access.log records all requests for files. If a visitor requests www.example.com/main.php, the following entry will be added in the log file.
88.54.124.17 - - [16/Apr/2016:07:44:08 +0100] "GET /main.php 
HTTP/1.1" 200 203 "-" "Mozilla/5.0 (Windows NT 6.0; WOW64; rv:45.0) 
Gecko/20100101 Firefox/45.0"
The above log describes that a visitor with an IP address of 88.54.124.178 requested main.php file on April 16th 2016 07:44 and the request was successful.
Having established that a log file is a critical asset, let’s look at an everyday example of how a log file would help identify when, how and “by whom” a website was hacked.


### Regular Expressions (Regex)
Regular expressions enable a powerful, flexible, and efficient text processing. Regular expressions allow you, with a general pattern notation almost like a mini programming language, to describe and parse text. This powerful pattern language and the patterns themselves are called regular expressions.Regular expressions are available in many types of tools, but their power is most fully exposed when available as part of a programming language. The goal of a regular expression is to match a certain expression within a lump of text.

### Detecting Attacks
Web applications are running on the OSI layer 7 ­ the application layer. To detect attacks against web applications, the detection mechanisms have to be application layer aware and see the relevant traffic. Attacks can be detected at different zones and devices in the network infrastructure. Each place has a different view of the traffic and has its advantages and disadvantages. 


## System overview



 ![screenshot from 2018-12-20 03-12-06](https://user-images.githubusercontent.com/45997793/50274343-06fe6f00-040b-11e9-995a-f8398fedf1ec.png)


## References 

http://resources.infosecinstitute.com/log-analysis-web-attacks-beginners-guide/#gref

https://link.springer.com/article/10.1007/s11950-008-1008-y

