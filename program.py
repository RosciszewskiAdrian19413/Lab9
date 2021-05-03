# -*- coding: utf-8 -*-
"""
Created on Mon May 03 20:31:19 2021

@author: Rosciszewski
"""

import mojeklasy

def testy():
    pass

print("Zad 1")
pkt1 = mojeklasy.Punkt2D(16,24)
pkt1.drukuj()
pkt1.zeruj()
pkt1.drukuj()
print()

print("Zad 2")
pkt2 = mojeklasy.Punkt3D(16,24,32)
pkt2.drukuj()
pkt2.zeruj()
pkt2.drukuj()
print()

print("Zad 3")
dluOdc = mojeklasy.Odcinek(16,24,24,40)
dluOdc.drukuj()
print()

if __name__ == "__main__":
    testy()