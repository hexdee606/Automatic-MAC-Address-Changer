# Automatic-MAC-Address-Changer
### **About**

**An automatic Mac changer** is a script to change the mac address of your Linux machine without **losing the internet**.



### Capability

 Tested on Kali Linux version till 2021.2



### **Features** 

Command-line argument

Checks the network interfaces

Manual time setting (Between 25 to 60)



**Requirements**

macchanger 

Python 3



### Steps to set up **automatic Mac changer**

#### Required Package

$ sudo apt-get update -y

$ sudo apt-get install -y macchanger



#### Installation of automatic Mac changer

**First, we create an Amc folder/directory:**

$ mkdir Amc 

$ cd Amc

**Now we have to clone the automatic Mac changer from Github**

$ git clone "    "

**Whenever you want to run you have to come to the Amc folder**



#### **To Run automatic Mac changer**

$ cd Amc*

$ ./amc



    -h      Help menu
    
    -i      network interface
    
    -t      Time to change the mac address 



**Example**

$ ./amc  -i eth0 -t 30



#### Troubleshoot method If internet doesn't work.

$ cd /etc/NetworkManager/ 

$ nano NetworkManager.conf 

**change: managed=true default: managed=false**

