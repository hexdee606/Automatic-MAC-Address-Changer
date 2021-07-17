# AMC- Automatic Media Access Control (MAC) Address Changer 

### **About**

**AMC script helps you to change your network interface address (MAC) as per given interval time without interupting your network(Internet).**



### Tested On 

 Kali Linux:
 - 2021.2 (VBox      NAT Network) 
 - 2021.1 (VBox      NAT Network) 
 - 2020.4 (VM & VBox NAT Network)
 - 2019.4 (VBox      NAT Network)
 - 2018.4 (VBox      NAT Network)
 



### **Features** 

1. Change MAC address without interputing internet.
2. Command Line Based Script
3. Lightweight and easily handleable 





**Requirements**

1. macchanger 
2. Python 3 
3. pyinstaller (Optional)




### Steps to set up **automatic Mac changer**

#### Required Package
```console
root@kali:~$ sudo apt-get update -y

root@kali:~$ sudo apt-get install -y macchanger
```


#### Installation of automatic Mac changer

**First, we create an Amc folder/directory:**
```console
root@kali:~$ mkdir Amc 

root@kali:~$ cd Amc
```

**Now we have to clone the automatic Mac changer from Github**
```console
root@kali:~$ git clone " https://github.com/hexdee606/Automatic-MAC-Address-Changer.git   "
```
**Whenever you want to run you have to come to the Amc folder**

**Method 1 : By using chmod**

#### **To Run automatic Mac changer**
```console

root@kali:~$ cd Automatic-MAC-Address-Changer

root@kali:~$ cd dist/amc

root@kali:~$ sudo chmod +x amc  

root@kali:~$ ./amc
```


**Method 2 : BY creating your own excutable file**
```console 

root@kali:~$ cd Amc

root@kali:~$ cd Automatic-MAC-Address-Changer

root@kali:~$ pyinstaller amc.py

root@kali:~$ cd dist/amc

root@kali:~$ ./amc -h

```

    -h      Help menu
    
    -i      network interface
    
    -t      Time to change the mac address 



**Example**
```console
root@kali:~$ ./amc  -i eth0 -t 30
```


#### Troubleshoot method if internet doesn't work.
```console
root@kali:~$ /etc/NetworkManager/ 

root@kali:~$ nano NetworkManager.conf 

**change: managed=true default: managed=false**

```

 
