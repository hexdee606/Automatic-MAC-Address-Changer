#!/bin/bash

echo "Please enter your network interface name:\t"
read ntwrk_inter

echo "Please enter interval time:\t"
read intrvl_tm

sudo python3 amc.py -i $ntwrk_inter -t $intrvl_tm

echo "Press Enter to Exit code."
read wt