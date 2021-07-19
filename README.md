
# AMC- Automatic Media Access Control (MAC) Address Changer

[![info](https://badgen.net/badge/Project/Info/blue?icon=information)](https://github.com/hexdee606/Automatic-MAC-Address-Changer#readme)
[![Open source](https://badgen.net/badge/Open%20Source%3F/Yes%20%21/blue)](#)
[![CC-0 license](https://img.shields.io/badge/License-CC--0-blue.svg)](https://github.com/hexdee606/Automatic-MAC-Address-Changer/blob/main/LICENSE)
[![Python](https://badgen.net/badge/Made%20with/Python3/blue)](https://github.com/hexdee606/Automatic-MAC-Address-Changer#readme)
[![status](https://badgen.net/badge/Status/Beta/yellow)](#)

## **About**

**AMC script helps you change your network interface address (MAC) as per the given interval time without interrupting your network(Internet).**

## Tested On 

 Sr. | Operating System | Version | Virtual Box | VM Ware | Network Type |
--- | --- | --- | --- | --- | --- |
1 | <img align="center" src="https://img.icons8.com/color/25/000000/kali-linux.png"> Kali Linux</img > | 2021.2 | [![status](https://badgen.net/github/status/micromatch/micromatch/4.0.1)](#)| [![status](https://badgen.net/github/status/micromatch/micromatch/4.0.1)](#)| [![network](https://badgen.net/badge/Network/NAT/brown)](#) |
2 | <img align="center" src="https://img.icons8.com/color/25/000000/kali-linux.png"> Kali Linux</img > | 2021.1 | [![status](https://badgen.net/github/status/micromatch/micromatch/4.0.1)](#)| [![status](https://badgen.net/github/status/micromatch/micromatch/4.0.1)](#)| [![network](https://badgen.net/badge/Network/NAT/brown)](#) |
3 | <img align="center" src="https://img.icons8.com/color/25/000000/kali-linux.png"> Kali Linux</img > | 2020.4 | [![status](https://badgen.net/github/status/micromatch/micromatch/4.0.1)](#)| [![status](https://badgen.net/github/status/micromatch/micromatch/4.0.1)](#)| [![network](https://badgen.net/badge/Network/NAT/brown)](#) |
4 | <img align="center" src="https://img.icons8.com/color/25/000000/kali-linux.png"> Kali Linux</img > | 2019.4 | [![status](https://badgen.net/github/status/micromatch/micromatch/4.0.1)](#)| [![status](https://badgen.net/github/status/micromatch/micromatch/4.0.1)](#)| [![network](https://badgen.net/badge/Network/NAT/brown)](#) |
5 | <img align="center" src="https://img.icons8.com/color/25/000000/kali-linux.png"> Kali Linux</img > | 2018.4 |[![status](https://badgen.net/github/status/micromatch/micromatch/4.0.1)](#)| [![status](https://badgen.net/github/status/micromatch/micromatch/4.0.1)](#)| [![network](https://badgen.net/badge/Network/NAT/brown)](#) |
6 | <img align="center" src="https://img.icons8.com/ios/25/000000/ubuntu.png">  Ubuntu</img > | 20.04 | [![status](https://badgen.net/github/status/micromatch/micromatch/4.0.1)](#)| [![status](https://badgen.net/github/status/micromatch/micromatch/4.0.1)](#)| [![network](https://badgen.net/badge/Network/NAT/brown)](#) |
7 | <img align="center" src="https://img.icons8.com/ios-glyphs/25/000000/debian.png">  Debian</img > | 10.0 | [![status](https://badgen.net/github/status/micromatch/micromatch/f4809eb6df80b)](#)| [![status](https://badgen.net/github/status/micromatch/micromatch/f4809eb6df80b)](#) | [![network](https://badgen.net/badge/Network/NAT/red)](#) |
8 | <img align="center" src="https://img.icons8.com/ios/25/000000/raspberry-pi.png">  Raspbian OS</img > | 5.10.17 | ![status](https://badgen.net/github/status/micromatch/micromatch/gh-pages)| ![status](https://badgen.net/github/status/micromatch/micromatch/gh-pages) | [![network](https://badgen.net/badge/Network/Unknown/brown)](#) |

 
## **Features** 

1. Change MAC address without interrupting the internet.
2. Command Line Based Script.
3. Lightweight and easily handleable.


## **Required packages**
- git `required`
- net-tools `required`
- macchanger `required`
- Python3 `required`
- pip3 `optional`
- pyinstaller `Optional`


## Install required packages
```console
root@kali:~$ sudo apt update -y

root@kali:~$ sudo apt install git-all -y

root@kali:~$ sudo apt install net-tools -y

root@kali:~$ sudo apt install -y macchanger
```

## Install optional packages
```console
root@kali:~$ sudo apt update -y

root@kali:~$ sudo apt install python3-pip -y

root@kali:~$ pip install pyinstaller -y
```

## How to setup Automatic MAC Changer

>**Create new directory**
```console
root@kali:~$ mkdir AMC

root@kali:~$ cd AMC
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

>**Method 2 : By creating an `executable` file**
```console 

root@kali:~$ cd AMC

root@kali:~$ cd Automatic-MAC-Address-Changer

root@kali:~$ pyinstaller --onefile amc.py

root@kali:~$ cd dist

root@kali:~$ ./amc -h

```

>**Available options**
 
    [-h]    Help menu 
    
    -i      Network interface
    
    -t      Time to change the mac address 


>**Whenever you want to use Automatic MAC Changer AMC follow these steps.**
```console
root@kali:~$ cd AMC

root@kali:~$ cd Automatic-MAC-Address-Changer

root@kali:~$ cd dist

root@kali:~$ ./amc

```

>**Example**
```console
root@kali:~$ ./amc  -i eth0 -t 30
```


## Troubleshooting methods if the internet is not working.

>If unable to access internet/ connection not established then do the following step (`after using AMC`): 
```console
root@kali:~$ macchanger -p eth0 (Your Network interface)
```

>If AMC is not working then do the following process:
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
[![twitter](https://badgen.net/badge/icon/Paradox_044?icon=twitter&label)](https://twitter.com/Paradox_044)
[![github](https://badgen.net/badge/icon/Paradox44?icon=github&label)](https://github.com/Paradox44)
[![email](https://badgen.net/badge/email/paradoxhex44/blue)](mailto:paradoxhex44@gmail.com)
[![twitter](https://badgen.net/badge/icon/itachi_9197?icon=twitter&label)](https://twitter.com/itachi_9197)
[![github](https://badgen.net/badge/icon/Itachi-91?icon=github&label)](https://github.com/Itachi-91)
[![email](https://badgen.net/badge/email/itachiuchiha9197/blue)](mailto:itachiuchiha9197@gmail.com)


>We hope you like our project. If 'Yes' click on the star icon at the top right corner or leave a comment so we can improve this script.

:heart: from Alchemists.
