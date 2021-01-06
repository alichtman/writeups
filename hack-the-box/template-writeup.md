# HOSTNAME (`10.10.10.IP`)

## Summary

## `/etc/hosts`

I begin by adding an entry in `/etc/hosts` to resolve `HOSTNAME.htb` to `10.10.10.IP`. I use this later in my report.

## Enumeration

I start a portscan of all ports (`-p-`), running OS, service version, and vulnerability scripts (`-A`), skipping host discovery (`-Pn`), with verbose logging (`-v`) and output to a file (`-oN`).

```bash
$ nmap -A -v -p- -Pn -oN allports HOSTNAME.htb

```

The current attack surface is:

-

## Reverse Shell

## Upgrading Shell

## Privilege Escalation

## Root
