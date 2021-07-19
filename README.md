# AMC- Automatic Media Access Control (MAC) Address Changer

[![info](https://badgen.net/badge/Project/Info/blue?icon=information)](https://github.com/hexdee606/Automatic-MAC-Address-Changer#readme)
![Open source](https://badgen.net/badge/Open%20Source%3F/Yes%20%21/blue)
[![CC-0 license](https://img.shields.io/badge/License-CC--0-blue.svg)](https://github.com/hexdee606/Automatic-MAC-Address-Changer/blob/main/LICENSE)
[![Python](https://badgen.net/badge/Made%20with/Python3/blue)](https://github.com/hexdee606/Automatic-MAC-Address-Changer#readme)
![status](https://badgen.net/badge/Status/Beta/yellow)

## **About**

**AMC script helps you to change your network interface address (MAC) as per given interval time without interrupting your network(Internet).**

## Tested On 

 Kali Linux:
 - 2021.2 (VBox      NAT Network) 
 - 2021.1 (VBox      NAT Network) 
 - 2020.4 (VM & VBox NAT Network)
 - 2019.4 (VBox      NAT Network)
 - 2018.4 (VBox      NAT Network)
 

## **Features** 

1. Change MAC address without interputing internet.
2. Command Line Based Script.
3. Lightweight and easily handleable.


## **Requirements**

1. macchanger 
2. Python 3 
3. pyinstaller (Optional)


## Install Required Packages
```console
root@kali:~$ sudo apt-get update -y

root@kali:~$ sudo apt-get install -y macchanger
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
[![twitter](https://badgen.net/badge/icon/paradox_044?icon=twitter&label)](https://twitter.com/paradox_044)
[![github](https://badgen.net/badge/icon/Paradox44?icon=github&label)](https://github.com/Paradox44)
[![twitter](https://badgen.net/badge/icon/itachi_9197?icon=twitter&label)](https://twitter.com/itachi_9197)
[![github](https://badgen.net/badge/icon/Itachi-91?icon=github&label)](https://github.com/Itachi-91)


>We hope you like our project. If 'Yes' click on the star icon at top right corner otherwise leave comment so we can improve this script.

:heart: from Alchemists.

---
