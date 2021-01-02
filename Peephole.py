#!/usr/bin/python3
import socket

# SHitty PortScanner


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

# host = target! (137.74.187.100 = web adresa za website koji je za vjezbu).
host = input("Please enter IP address of the target")
port = int(input("Enter a Port number you wan to scan"))

def portScanner(port):
    if s.connect_ex((host, port)):
        print("Port is closed")
    else: print("Port is OPEN")

portScanner(port)
