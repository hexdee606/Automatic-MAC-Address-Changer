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

Names|Twitter|Github|Mail
---|---|---|---
hexdee606|<a href="https://twitter.com/hexdee606" target="blank"><img align="center" src="https://camo.githubusercontent.com/35b0b8bfbd8840f35607fb56ad0a139047fd5d6e09ceb060c5c6f0a5abd1044c/68747470733a2f2f6564656e742e6769746875622e696f2f537570657254696e7949636f6e732f696d616765732f7376672f747769747465722e737667" alt="hexdee606" width="40" /></a>|[<img align="center" src="https://camo.githubusercontent.com/4133dc1cd4511d4a292b84ce10e52e4ed92569fb2a8165381c9c47be5edc2796/68747470733a2f2f6564656e742e6769746875622e696f2f537570657254696e7949636f6e732f696d616765732f706e672f6769746875622e706e67" width="40"/>](https://github.com/hexdee606)|<a href="mailto:hexdee606@gmail.com" target="blank"><img align="center" src="https://camo.githubusercontent.com/4a3dd8d10a27c272fd04b2ce8ed1a130606f95ea6a76b5e19ce8b642faa18c27/68747470733a2f2f6564656e742e6769746875622e696f2f537570657254696e7949636f6e732f696d616765732f7376672f676d61696c2e737667" alt="hexdee606" width="40" /></a>
Paradox44|<a href="https://twitter.com/paradox_044" target="blank"><img align="center" src="https://camo.githubusercontent.com/35b0b8bfbd8840f35607fb56ad0a139047fd5d6e09ceb060c5c6f0a5abd1044c/68747470733a2f2f6564656e742e6769746875622e696f2f537570657254696e7949636f6e732f696d616765732f7376672f747769747465722e737667" alt="paradox_044" width="40" /></a>| [<img align="center" src="https://camo.githubusercontent.com/4133dc1cd4511d4a292b84ce10e52e4ed92569fb2a8165381c9c47be5edc2796/68747470733a2f2f6564656e742e6769746875622e696f2f537570657254696e7949636f6e732f696d616765732f706e672f6769746875622e706e67" width="40"/>](https://github.com/Paradox44)|<a href="mailto:paradoxhex44@gmail.com" target="blank"><img align="center" src="https://camo.githubusercontent.com/4a3dd8d10a27c272fd04b2ce8ed1a130606f95ea6a76b5e19ce8b642faa18c27/68747470733a2f2f6564656e742e6769746875622e696f2f537570657254696e7949636f6e732f696d616765732f7376672f676d61696c2e737667" alt=" paradoxhex44" width="40" /></a>
Itachi|<a href="https://twitter.com/itachi_9197" target="blank"><img align="center" src="https://camo.githubusercontent.com/35b0b8bfbd8840f35607fb56ad0a139047fd5d6e09ceb060c5c6f0a5abd1044c/68747470733a2f2f6564656e742e6769746875622e696f2f537570657254696e7949636f6e732f696d616765732f7376672f747769747465722e737667" alt="itachi_9197" width="40" /></a>|[<img align="center" src="https://camo.githubusercontent.com/4133dc1cd4511d4a292b84ce10e52e4ed92569fb2a8165381c9c47be5edc2796/68747470733a2f2f6564656e742e6769746875622e696f2f537570657254696e7949636f6e732f696d616765732f706e672f6769746875622e706e67" width="40"/>](https://github.com/Itachi-91)|<a href="mailto:itachiuchiha9197@gmail.com" target="blank"><img align="center" src="https://camo.githubusercontent.com/4a3dd8d10a27c272fd04b2ce8ed1a130606f95ea6a76b5e19ce8b642faa18c27/68747470733a2f2f6564656e742e6769746875622e696f2f537570657254696e7949636f6e732f696d616765732f7376672f676d61696c2e737667" alt="itachi_9197" width="40" /></a>
---
