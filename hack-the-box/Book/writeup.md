# Book

## IP: 10.10.10.176

## OS: Linux

```bash
$ nmap -vvv -sCV -oN book.nmap 10.10.10.176
# Nmap 7.80 scan initiated Thu Apr  9 11:52:19 2020 as: nmap -vvv -sCV -oN book.nmap 10.10.10.176
Nmap scan report for 10.10.10.176
Host is up, received syn-ack (0.055s latency).
Scanned at 2020-04-09 11:52:19 CDT for 10s
Not shown: 998 closed ports
Reason: 998 conn-refused
PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 f7:fc:57:99:f6:82:e0:03:d6:03:bc:09:43:01:55:b7 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDMrLSBfMJGYbweKg7qPaY0uw9OBPR3dlM6GiVPDVca05vEsQKJ47YXEIZoMCIg/QvJdP6RsmeQfcFbszP/stxoVfWPLBS6csfdl4rz8MjNuRAcUQjcYhPEejogNjRZKf695ggwUybHATBXNLBpCMNrrrCqtKVvgzljdEK9rnAlOVztI8bEaLbQV87lmQJvt38bHdt+UsO+HIJwrwrUkRzXeja1k/DJ4BfWgmTNUJyUWo8XiTQrpBe7JkeQ4DwJ7HZMtpnhHDv/BIwi6Tk994tDpbTGvmbnLivvT+j22KruHE6ZvEhbts+2907haztuZdgiNG5dFPH7jKapIrZWtxTB
|   256 a3:e5:d1:74:c4:8a:e8:c8:52:c7:17:83:4a:54:31:bd (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBNKAm6pa94qHHk0DuSIarpsJaCk2vUfZkgWkrXPeIorMjT/DyTCfsM2ViRnU9YSnrVj/c3OQ1vyW8eMxiRDoOB8=
|   256 e3:62:68:72:e2:c0:ae:46:67:3d:cb:46:bf:69:b9:6a (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICk6vCR5eZZvVb6fwpX7k054lgERxpbaEC8jyGKxJ4Xm
80/tcp open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: LIBRARY - Read | Learn | Have Fun
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Apr  9 11:52:29 2020 -- 1 IP address (1 host up) scanned in 10.32 seconds
```


```bash
$ gobuster dir -u http://10.10.10.176 -w ~/tools/wordlists/directory-list-2.3-medium.txt -o gobuster.log --wildcard -t 20
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.10.176
[+] Threads:        20
[+] Wordlist:       /home/alichtman/tools/wordlists/directory-list-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/04/09 11:55:00 Starting gobuster
===============================================================
/images (Status: 301)
/docs (Status: 301)
/admin (Status: 301)
/server-status (Status: 403)
===============================================================
2020/04/09 12:05:44 Finished
===============================================================
```

Go to `http://10.10.10.176` and click sign up, create a test account and then sign in.

Target XSS on `/collections.php`.


wfuzz -c -z file,/home/alichtman/tools/enum/xss-vectors.txt -d "title=FUZZ&author=FUZZ" http://10.10.10.176/collections.php

