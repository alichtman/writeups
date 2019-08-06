# Mirai Writeup

1. `nmap -vvv -sCV -oA nmap/mirai 10.10.10.48` showed that ports 22, 53 and 80 were open.
2. Opened `10.10.10.48` in Firefox and saw a blank page. Ran `gobuster dir -u 10.10.10.48 --wordlist /usr/share/wordlist/dirb/common.txt`

```bash
gobuster dir -u http://10.10.10.48/ -w /usr/share/wordlists/dirb/common.txt 
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.10.48/
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2019/08/05 20:39:47 Starting gobuster
===============================================================
/admin (Status: 301)
/swfobject.js (Status: 200) 
===============================================================
2019/08/05 20:41:13 Finished
===============================================================
```

3. Went to the admin page, saw it was a RPi running PiHole and tried to log in to the admin panel with the default password (`raspberry`). That did not work.
4. Tried to ssh in with `ssh 10.10.10.48` with the default password, and failed.
5. `ssh pi@10.10.10.48` with the default password worked because people don't follow instructions to disable default accounts.
6. Found the `user.txt` file at `/home/pi/Desktop/user.txt`
7. `cat ~/.bash_history` showed someone ran `sudo su`. Tried that and got root.
8. `cat /root/root.txt` and found a hint that someone lost the original `root.txt` file but had a backup on their USB stick.
9. Located file on `/media/usbstick` saying that the backup had been deleted.
10. Looked at `/media/usbstick/lost+found/`, and found nothing. So, I ran `dd if=/dev/sdb of=usbstick.bin`, then ran `strings` on the `dd` image to see what was inside it. A string that used the right charset and was the correct length for a hash popped out. That was the root proof!
