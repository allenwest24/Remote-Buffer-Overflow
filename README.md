# Remote-Buffer-Overflow
Extension from the project Buffer Overflow to now work on a remote vulnerable server. 

### Introduction

An exploit (from the same word in the French language, meaning "achievement", or "accomplishment") is a piece of software, a chunk of data, or sequence of commands that take advantage of a bug, glitch or vulnerability in order to cause unintended or unanticipated behavior to occur on computer software, hardware, or something electronic (usually computerized). This frequently includes such things as violently gaining control of a computer system or allowing privilege escalation or a denial of service attack. There are several methods of classifying exploits. The most common is by how the exploit contacts the vulnerable software. A 'remote exploit' works over a network and exploits the security vulnerability without any prior access to the vulnerable system. This challenge aims to give students some hands-on experience with remote exploits by allowing them to attack a remote service that has a vulnerability.

### Detailed Description

The task was to exploit a remote vulnerability on a server that is running on the machine 'gangsta' on port ****. The objective was to 
create and inject an appropriate shellcode into the application and to take over control of its execution. The vulnerable server has its
set-guid (i.e. set group identification) bit enabled. The server has a simple buffer overflow vulnerability. The main difference to 
standard [buffer overflow](https://github.com/allenwest24/Buffer-Overflow), however, is that the server is remote and you do not get
much feedback from it once you send packets to it. 

### Contents
- buffscript.py - The exploit script.
- server.c - The vulnerable server source code.
- solution.txt - My strategy for approaching this challenge.
- terminal1.bash - The terminal session that used netcat to observe the port I specified in buffscript.py
- terminal2.bash - The terminal session where I executed buffscript.py
