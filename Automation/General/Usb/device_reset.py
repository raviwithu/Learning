#!/usr/bin/python3

from usb.core import find as finddev

#for hackrf
dev = finddev(idVendor=0x1d50, idProduct=0x6089)

dev.reset()
