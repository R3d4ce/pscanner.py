#!/usr/bin/python3

#Basic port scanner 

#usage: ./pscanner, follow prompt


import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

host = input("Enter IP: ")
port = int(input("Port to scan: "))


def portscanner(port):
        if s.connect_ex((host, port)):
                print("Port closed")
        else:
                print("OPEN")

portscanner(port)
