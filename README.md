# AMC- Automatic Media Access Control (MAC) Address Changer 

### **About**

**AMC script helps you to change your network interface address (MAC) as per given interval time without interrupting your network(Internet).**



### Tested On 

 Kali Linux:
 - 2021.2 (VBox      NAT Network) 
 - 2021.1 (VBox      NAT Network) 
 - 2020.4 (VM & VBox NAT Network)
 - 2019.4 (VBox      NAT Network)
 - 2018.4 (VBox      NAT Network)
 



### **Features** 

1. Change MAC address without interputing internet.
2. Command Line Based Script.
3. Lightweight and easily handleable.





**Requirements**

1. macchanger 
2. Python 3 
3. pyinstaller (Optional)




#### Install Required Package
```console
root@kali:~$ sudo apt-get update -y

root@kali:~$ sudo apt-get install -y macchanger
```


#### How to Use Automatic MAC Changer

**First, we create an Amc folder/directory:**
```console
root@kali:~$ mkdir Amc 

root@kali:~$ cd Amc
```

**Now we have to clone the automatic Mac changer from Github**
```console
root@kali:~$ git clone "https://github.com/hexdee606/Automatic-MAC-Address-Changer.git"
```
**Setting up Amc**

**Method 1 : By using chmod**

#### **To Run automatic Mac changer**
```console

root@kali:~$ cd Automatic-MAC-Address-Changer

root@kali:~$ cd dist

root@kali:~$ sudo chmod +x amc  

root@kali:~$ ./amc
```


**Method 2 : BY creating your own excutable file**
```console 

root@kali:~$ cd Amc

root@kali:~$ cd Automatic-MAC-Address-Changer

root@kali:~$ pyinstaller amc.py

root@kali:~$ cd dist

root@kali:~$ ./amc -h

```
 ** Available options **
 
    -h      Help menu (Optional)
    
    -i      network interface
    
    -t      Time to change the mac address 


** Whenever you want use Automatic MAC changer follow this steps: **
```console
root@kali:~$ cd Amc

root@kali:~$ cd Automatic-MAC-Address-Changer

root@kali:~$ cd dist

root@kali:~$ ./amc

```

**Example**
```console
root@kali:~$ ./amc  -i eth0 -t 30
```


#### Troubleshoot method if internet doesn't work.
```console
If unable to connect to internet Change Mac address to original
root@kali:~$ macchanger -p eth0 (Your Network interface)


If amc is not working (after changing mac if the internet is not worked ) then do the following process:
root@kali:~$ /etc/NetworkManager/ 

root@kali:~$ nano NetworkManager.conf 

default: managed=false
To change: managed=true

```
We hope you like our project. If 'Yes' click on the star icon at top right corner otherwise leave comment so we can improve this script.
Love from Alchemists.

<h3 align="left">Connect Us:</h3>

Names|Twitter|Github|Gmail
---|---|---|---
hexdee606|<a href="https://twitter.com/hexdee606" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="hexdee606" height="30" width="40" /></a>|[<img src="https://s18955.pcdn.co/wp-content/uploads/2018/02/github.png" width="25"/>](https://github.com/hexdee606)|<a href="mailto:hexdee606@gmail.com" target="blank"><img align="center" src="https://fonts.gstatic.com/s/i/materialiconsoutlined/email/v16/24px.svg" alt="hexdee606" height="30" width="40" /></a>
Paradox44|<a href="https://twitter.com/paradox_044" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="paradox_044" height="30" width="40" /></a>| [<img src="https://s18955.pcdn.co/wp-content/uploads/2018/02/github.png" width="25"/>](https://github.com/Paradox44)|<a href="mailto:paradoxhex44@gmail.com" target="blank"><img align="center" src="https://fonts.gstatic.com/s/i/materialiconsoutlined/email/v16/24px.svg" alt=" paradoxhex44" height="30" width="40" /></a>
Itachi|<a href="https://twitter.com/itachi_9197" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="itachi_9197" height="30" width="40" /></a>|[<img src="https://s18955.pcdn.co/wp-content/uploads/2018/02/github.png" width="25"/>](https://github.com/Itachi-91)|<a href="mailto:itachiuchiha9197@gmail.com" target="blank"><img align="center" src="https://fonts.gstatic.com/s/i/materialiconsoutlined/email/v16/24px.svg" alt="itachi_9197" height="30" width="40" /></a>
---
