# AMC- Automatic Media Access Control (MAC) Address Changer

[![info](https://badgen.net/badge/Project/Info/blue?icon=information)](https://github.com/hexdee606/Automatic-MAC-Address-Changer#readme)
![Open source](https://badgen.net/badge/Open%20Source%3F/Yes%20%21/blue)
[![CC-0 license](https://img.shields.io/badge/License-CC--0-blue.svg)](https://github.com/hexdee606/Automatic-MAC-Address-Changer/blob/main/LICENSE)
[![Python](https://badgen.net/badge/Made%20with/Python3/blue)](https://github.com/hexdee606/Automatic-MAC-Address-Changer#readme)
![status](https://badgen.net/badge/Status/Beta/yellow)

## **About**

**AMC script helps you to change your network interface address (MAC) as per given interval time without interrupting your network(Internet).**

## Tested On 

 Sr. | Operating System | Version | Virtual Box | VM Ware |
--- | --- | --- | --- | --- |
1 | <img align="center" src="https://img.icons8.com/color/25/000000/kali-linux.png"> Kali Linux</img > | 2021.2 | ![status](https://badgen.net/github/status/micromatch/micromatch/4.0.1)| ![status](https://badgen.net/github/status/micromatch/micromatch/4.0.1) |
2 | <img align="center" src="https://img.icons8.com/color/25/000000/kali-linux.png"> Kali Linux</img > | 2021.1 | ![status](https://badgen.net/github/status/micromatch/micromatch/4.0.1)| ![status](https://badgen.net/github/status/micromatch/micromatch/4.0.1) |
3 | <img align="center" src="https://img.icons8.com/color/25/000000/kali-linux.png"> Kali Linux</img > | 2020.4 | ![status](https://badgen.net/github/status/micromatch/micromatch/4.0.1)| ![status](https://badgen.net/github/status/micromatch/micromatch/4.0.1) |
4 | <img align="center" src="https://img.icons8.com/color/25/000000/kali-linux.png"> Kali Linux</img > | 2019.4 | ![status](https://badgen.net/github/status/micromatch/micromatch/4.0.1)| ![status](https://badgen.net/github/status/micromatch/micromatch/4.0.1) |
5 | <img align="center" src="https://img.icons8.com/color/25/000000/kali-linux.png"> Kali Linux</img > | 2018.4 | ![status](https://badgen.net/github/status/micromatch/micromatch/4.0.1)| ![status](https://badgen.net/github/status/micromatch/micromatch/4.0.1) |
6 | <img align="center" src="https://img.icons8.com/ios/25/000000/ubuntu.png">  Ubuntu</img > | 21.04 | ![status](https://badgen.net/github/status/micromatch/micromatch/gh-pages)| ![status](https://badgen.net/github/status/micromatch/micromatch/gh-pages) |
7 | <img align="center" src="https://img.icons8.com/ios-glyphs/25/000000/debian.png">  Debian</img > | 10.0 | ![status](https://badgen.net/github/status/micromatch/micromatch/gh-pages)| ![status](https://badgen.net/github/status/micromatch/micromatch/gh-pages) |
8 | <img align="center" src="https://img.icons8.com/ios/25/000000/raspberry-pi.png">  Raspbian OS</img > | 5.10.17 | ![status](https://badgen.net/github/status/micromatch/micromatch/gh-pages)| ![status](https://badgen.net/github/status/micromatch/micromatch/gh-pages) |
 
## **Features** 

1. Change MAC address without interrupting the internet.
2. Command Line Based Script.
3. Lightweight and easily handleable.


## **Required packages**
- macchanger `required` 
- Python3 `required`
- pip3 `optional`
- pyinstaller `Optional`


## Install required packages
```console
root@kali:~$ sudo apt-get update -y

root@kali:~$ sudo apt-get install -y macchanger
```

## Install optional packages
```console
root@kali:~$ sudo apt-get update -y

root@kali:~$ sudo apt install python3-pip -y

root@kali:~$ pip install pyinstaller -y
```

## How to setup Automatic MAC Changer

>**Create new directory**
```console
root@kali:~$ mkdir amc 

root@kali:~$ cd amc
```

>**Clone AMC from github**
```console
root@kali:~$ git clone "https://github.com/hexdee606/Automatic-MAC-Address-Changer.git"
```

>**Method 1 : By using `chmod`**
```console

root@kali:~$ cd Automatic-MAC-Address-Changer

root@kali:~$ cd dist

root@kali:~$ sudo chmod +x amc  

root@kali:~$ ./amc
```

>**Method 2 : By creating your own `excutable` file**
```console 

root@kali:~$ cd Amc

root@kali:~$ cd Automatic-MAC-Address-Changer

root@kali:~$ pyinstaller amc.py

root@kali:~$ cd dist

root@kali:~$ ./amc -h

```

>**Available options**
 
    -h      Help menu (Optional)
    
    -i      network interface
    
    -t      Time to change the mac address 


>**Whenever you want use Automatic MAC changer follow this steps:**
```console
root@kali:~$ cd Amc

root@kali:~$ cd Automatic-MAC-Address-Changer

root@kali:~$ cd dist

root@kali:~$ ./amc

```

>**Example**
```console
root@kali:~$ ./amc  -i eth0 -t 30
```


## Troubleshoot method if internet doesn't work.

>If unable to connect to internet Change Mac address to original
```console
root@kali:~$ macchanger -p eth0 (Your Network interface)
```

>If amc is not working (after changing mac if the internet is not worked ) then do the following process:
```console
root@kali:~$ /etc/NetworkManager/ 
root@kali:~$ nano NetworkManager.conf

default: managed=false
To change: managed=true
```

## Connect Us

[![twitter](https://badgen.net/badge/icon/hexdee606?icon=twitter&label)](https://twitter.com/hexdee606)
[![github](https://badgen.net/badge/icon/hexdee606?icon=github&label)](https://github.com/hexdee606)
[![email](https://badgen.net/badge/email/hexdee606/blue)](mailto:hexdee606@gmail.com)
[![twitter](https://badgen.net/badge/icon/paradox_044?icon=twitter&label)](https://twitter.com/paradox_044)
[![github](https://badgen.net/badge/icon/Paradox44?icon=github&label)](https://github.com/Paradox44)
[![email](https://badgen.net/badge/email/paradox_044/blue)](mailto:hexdee606@gmail.com)
[![twitter](https://badgen.net/badge/icon/itachi_9197?icon=twitter&label)](https://twitter.com/itachi_9197)
[![github](https://badgen.net/badge/icon/Itachi-91?icon=github&label)](https://github.com/Itachi-91)
[![email](https://badgen.net/badge/email/Itachi-91/blue)](mailto:hexdee606@gmail.com)


>We hope you like our project. If 'Yes' click on the star icon at top right corner otherwise leave comment so we can improve this script.

:heart: from Alchemists.

---
