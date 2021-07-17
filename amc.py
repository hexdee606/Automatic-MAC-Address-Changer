#!/usr/bin/python3
"""
#############################################################################
#       Automatic Media Access Control [MAC] Address Changing Script.       #
#############################################################################
# Copyright 2021 Alchemists                                                 #
#############################################################################
# Automatic Media Access Control [MAC] Address Changing Script (c) 2021     #
# This work is marked with CC0 1.0 Universal.                               #
# To view a copy of this license, visit                                     #
#                                                                           #
# http://creativecommons.org/publicdomain/zero/1.0                          #
#                                                                           #
# Unless required by applicable law or agreed to in writing, software       #
# distributed under the License is distributed on an "AS IS" BASIS,         #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  #
# See the License for the specific language governing permissions and       #
# limitations under the License.                                            #
#############################################################################
#                               ABOUT Alchemists                            #
#############################################################################
#           |   Github      |   Twitter     |   GMail                       #
############|###############|###############|################################
# Developer |   hexdee606   |   hexdee606   |   hexdee606                   #
# Research  |   Itachi-91   |   Itachi_9197 |   itachiuchiha9197            #
# Tester    |   Paradox44   |   Paradox_044 |   paradoxhex44                #
# Guide     |               |   Metal_robo  |                               #
#############################################################################
# this script is written in Python3 using PyCharm Community Edition 2021    #
# for Linux operating system. We hope you enjoy our work.                   #
# This software program is written for educational purposes only if you     #
# received any legal notice from cyber cell/ police then we will not        #
# responsible for that. use this script for your own risk.                  #
#############################################################################
"""
# importing some needed libraries for script support.
import argparse
import socket
import subprocess
import sys

from os import system, name, popen
from time import sleep

# variables for development information
project_version = "1.0.9.9                                 "
project_build = "BETA-20210717P1159-Kali_Linux_2021.2    "


# to clear terminal/ command prompt
def clear():
    """
    This function help  to clear your terminal/ command prompt window.
    :return: clear terminal/ command prompt window.
    """
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


# to show error message
def error_output(fatal_error, error):
    """
    error_output() to display error of function/ session
    :param error: is exception to catch error message
    :param fatal_error: is boolean if is true then application will be closed.
    :return: nothing
    """
    try:
        clear()
        print("#######################################################################")
        print("# ERROR : 1 - Something wrong here please contact development team    #")
        print("#######################################################################")
        print(str(error))
        print("#######################################################################")
        if fatal_error:
            sys.exit()
    except Exception as e:
        clear()
        print("#######################################################################")
        print("# ERROR : 2 - Something wrong here please contact development team    #")
        print("#######################################################################")
        print(str(e))
        print("#######################################################################")
        sys.exit()


# welcome message
def welcome_note():
    """
    This function is only to display welcome message on script start.
    :return: if script run's successfully then return True else False
    """
    try:
        print("#######################################################################")
        print("# Project name              : Automatic MAC Address Changer           #")
        print("# Project version           : {}#".format(project_version))
        print("# Build                     : {}#".format(project_build))
        print("# License type              : CC0 1.0 Universal                       #")
        print("# Coded using               : PyCharm 2021.1.3 (Community Edition)    #")
        print("#######################################################################")
        print("# Team Name                 : Alchemists                              #")
        print("# Research & Development    : Github :   hexdee606                    #")
        print("# Research & Testing        : Github :   paradox44 & itachi-91        #")
        print("#######################################################################")
        return True
    except Exception as e:
        error_output(False, e)


def process_output(network_interface, time_left):
    """
    To display process of mac changer
    :param network_interface: network interface name entered by user
    :param time_left: time left for change mac address
    :return: Nothing
    """
    clear()
    welcome_note()
    if time_left < 10:
        print("# Your MAC address of {} will be change in next {} sec.              #".format(network_interface,
                                                                                              time_left))
    else:
        print("# Your MAC address of {} will be change in next {} sec.             #".format(network_interface,
                                                                                             time_left))
    print("#######################################################################")
    subprocess.call(["macchanger", "-s", network_interface], shell=False)
    print("#######################################################################")
    print("# To exit use Ctrl + C                                                #")
    print("#######################################################################")


# send request to mac changer to change mac address.
def mac_change_request(network_interface):
    """
    send request to mac changer to change mac address of network interface entered by user
    :param network_interface: network interface name entered by user
    :return: nothing
    """
    try:
        clear()
        welcome_note()
        print("# Please wait, flushing new MAC address . . .                         #")
        print("# Please don't close or cancel, else your network will stop working   #")
        print("#######################################################################")
        subprocess.call(["service", "NetworkManager", "stop"], shell=False)
        subprocess.call(["ifconfig", network_interface, "down"], shell=False)
        subprocess.call(["macchanger", "-a", network_interface], shell=False)
        subprocess.call(["ifconfig", network_interface, "up"], shell=False)
        subprocess.call(["service", "NetworkManager", "start"], shell=False)
        clear()
        welcome_note()
        print("# MAC address for {} successfully changed.                          #".format(network_interface))
        print("#######################################################################")
        print("# Please wait, reconnecting to network communication...               #")
        print("#######################################################################")
        sleep(5)
    except Exception as e:
        error_output(True, e)


# let's check is given network is available or not
def check_network_interface(network_interface):
    """
    This function help to verify network interface.
    :param network_interface: network interface name entered by user
    :return: True if network interface found.
    """
    try:
        for index, interface in socket.if_nameindex():
            if network_interface == interface:
                return True
    except Exception as e:
        error_output(True, e)


# let's display available network interfaces.
def show_network_interface():
    """
    this function helps to display available network interfaces.
    :return: list of available network inter faces.
    """
    clear()
    welcome_note()
    print("# Sr. Number |   Network Interface Name  |   MAC Address              #")
    print("#######################################################################")
    list_of_network_interface = socket.if_nameindex()
    read_mac_address = []
    for index, network_interface in list_of_network_interface:
        read_mac_address.append(popen("cat /sys/class/net/{}/address".format(network_interface)).read().split("\n"))
    list_of_mac_address = [i[0] for i in read_mac_address]

    for (index, network_interface), mac_address in zip(list_of_network_interface, list_of_mac_address):
        if network_interface == "lo":
            print("# {}          |   {}                      |   {}        #".format(index, network_interface,
                                                                                     mac_address))
        else:
            print("# {}          |   {}                    |   {}        #".format(index, network_interface,
                                                                                   mac_address))
    print("#######################################################################")
    sys.exit()


# set minimum and maximum time for mac address changer
def check_change_time(change_time):
    """
    to check interval time is in set limit Min: 25 sec to  Max: 60 sec
    :param change_time: network interface name entered by user
    :return: True if condition satisfy
    """
    try:
        if int(change_time) < 25:
            clear()
            welcome_note()
            print("# Oh..! sorry but you are requesting MAC changer to change your MAC   #")
            print("# Address very frequently, it will damage network manager service.    #")
            print("# Please try again. The time is between 25 to 60 Sec.                 #")
            print("#######################################################################")
            sleep(2.5)
            sys.exit()
        elif int(change_time) > 60:
            clear()
            welcome_note()
            print("# Oh..! sorry but you are requesting MAC changer to change your MAC   #")
            print("# Address less frequently, There is no use for this script.           #")
            print("# Please try again. The time is between 25 to 60 Sec.                 #")
            print("#######################################################################")
            sleep(2.5)
            sys.exit()
        else:
            return True
    except ValueError:
        error_output(True, ValueError)


# Let's write main function.
def mac_change(change_time, network_interface):
    """
    automation function to calculate interval time and send request to change mac address
    :param change_time: interval time entered by user
    :param network_interface: network interface name entered by user
    :return:
    """
    try:
        time_increment = 0
        while True:
            time_left = change_time - time_increment
            if time_left == 0:
                time_increment = 0
                mac_change_request(network_interface)
            else:
                time_increment += 1
                process_output(network_interface, time_left)
            sleep(1)
    except KeyboardInterrupt:
        display_goodbye(network_interface)


# let's say good bye.
def display_goodbye(network_interface):
    """
    display good bye message and set permanent mac address.
    :param network_interface: network interface name entered by user
    :return:
    """
    clear()
    welcome_note()
    print("# Flushing your permanent  MAC Address to your network interface      #")
    print("#######################################################################")
    subprocess.call(["service", "NetworkManager", "stop"], shell=False)
    subprocess.call(["ifconfig", network_interface, "down"], shell=False)
    subprocess.call(["macchanger", "-p", network_interface], shell=False)
    subprocess.call(["ifconfig", network_interface, "up"], shell=False)
    subprocess.call(["service", "NetworkManager", "start"], shell=False)
    sleep(2)
    clear()
    welcome_note()
    print("# WE HOPE YOU ENJOY OUR WORK. LEAVE YOUR COMMENT/ FEEDBACKS ON GITHUB #")
    print("#######################################################################")
    sleep(1)


"""
Let's create argument menu for automatic mac address changer
-h for help
-i for network interface
-t for time interval
"""
parser = argparse.ArgumentParser(description="Automatic Media Access Control [MAC] Address Changing Script",
                                 usage="./amc [-h] -i -t")
parser.add_argument("-i", "--interface", type=str, metavar="", required=True, help="Network Interface name. Ex. eth0")
parser.add_argument("-t", "--time", type=int, metavar="", required=True,
                    help="Interval time to change your MAC address.")
args = parser.parse_args()

if __name__ == '__main__':
    a_interval_time = args.time
    a_network_interface = args.interface
    if a_interval_time == "" or a_network_interface == "":
        clear()
        welcome_note()
        print("# No such command found, please use ./amc -h for help.                #")
        print("#######################################################################")
    else:
        if a_network_interface == "lo":
            clear()
            welcome_note()
            print("# Sorry but you are trying to change your Loop-back (Localhost)       #")
            print("# MAC Address, and it's not allowed.                                  #")
            print("#######################################################################")
            user_reply = input("\n Do you want to see available network interfaces? (Y/N):             ")
            if user_reply == "Yes" or user_reply == "Y" or user_reply == "y" or user_reply == "yes":
                show_network_interface()
            else:
                clear()
                welcome_note()
                print("# Sorry but you are trying to change your Loop-back (Localhost)       #")
                print("# MAC Address, and it's not allowed.                                  #")
                print("# Please use ifconfig command to identify your Network interface.     #")
                print("#######################################################################")

        elif check_network_interface(a_network_interface):
            if check_change_time(a_interval_time):
                mac_change(a_interval_time, a_network_interface)
            else:
                clear()
                welcome_note()
                print("# No such command found, please use ./amc -h for help.                #")
                print("#######################################################################")
        else:
            clear()
            welcome_note()
            print(
                "# Network interface {} not found.                                   #".format(a_network_interface))
            print("#######################################################################")
            user_reply = input("\n Do you want to see available network interfaces? (Y/N):             ")
            if user_reply == "Yes" or user_reply == "Y" or user_reply == "y" or user_reply == "yes":
                show_network_interface()
            else:
                clear()
                welcome_note()
                print(
                    "# Network interface {} not found.                                   #".format(a_network_interface))
                print("# Please use ifconfig command to identify your Network interface.     #")
                print("#######################################################################")
