#!/bin/python3 
import random, os
proxy_ip=[]
tor_ip=[]
col=int(input("Колличество фековых ip\n"))
net=str(input("t - использовать сеть тор\np использовать список proxy (По умолчанию)\n"))
string="-D "
if net == "t" or net == "T" or net == "Tor" or net == "TOR" or net == "tor":
	os.system("toriptables2.py -l; curl suip.biz/ip/ > doc.txt")
	my_file = open("doc.txt")
	my_string = my_file.read()
	my_file.close()
	tor_ip.append(my_string)
	for i in range(col-1):
		os.system("sudo kill -HUP $(pidof tor) ; curl suip.biz/ip/ > doc.txt")
		my_file = open("doc.txt")
		my_string = my_file.read()
		my_file.close()
		tor_ip.append(my_string)
	for i in range(len(tor_ip)):
		if i!=0:
			string+=","+str(tor_ip[i])
		else:
			string+=str(tor_ip[i])
	print ("\n\n"+"-"*50+"\n\n")
	print(string)	
	print ("\n\n"+"-"*50+"\n\n")

else:
	with open ("proxy-list.txt",'r') as f:
		strings = f.read().splitlines()
	i=0
	while i<col:
		rand = random.randint(0, len(strings)-1)
		if strings[rand] in proxy_ip:
			if len(proxy_ip)==len(strings):
				print("Создано максимальное колличество")
				break
		else:
			proxy_ip.append(strings[rand])
			i+=1
	for i in range(len(proxy_ip)):
		if i!=0:
			string+=","+str(proxy_ip[i])
		else:
			string+=str(proxy_ip[i])
	print ("\n\n"+"-"*50+"\n\n")
	print(string)
	print ("\n\n"+"-"*50+"\n\n")
