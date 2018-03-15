#!usr/bin/python

# -*- coding: ascii -*-

#	serial parser / logger / debugger
#
# ===================================================================
#
#	n.jOy[dream]	|	ver0.02 @ mar 14 2018AD
#		
#
#	"its not much of a cheese shop, is it?"
#
# ===================================================================

import socket
from serial import serial
import time
import sys
import thread
import getopt

z1baudrate = 9600
z1port = '/dev/ttyACM0'

sampling_t = []
sampling_data = []

# logger

def serial_logger():
	z1serial = serial.Serial(port=z1port, baudrate=z1baudrate)
	z1serial.timeout = 2

	print z1serial.is_open
	if z1serial.is_open:
		L = []
		thread.start_new_thread(input_thread, (L,))
		while True:
			size = z1serial.inWaiting()
			if size:
				new_data = str(z1serial.read(size)+" "+str(time.time()))
				sampling_data.append(new_data)
				print new_data
				time.sleep(.1)
			else:
				print ("no data")
			if L: 
				z1serial.close()
				logout(sampling_data)
				break
	return;


def internet_logger():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	addr_srv = ('42.42.42.42', 80)

	print >>sys.stderr, 'starting up on %s port %s' % addr_srv
	sock.bind(addr_srv)
	sock.listen(1)
	while True:
		print >>sys.stderr, 'waiting for conn'
		connection, client_address = sock.accept()
	try:
		print >> sys.stderr, ' connection from ', client_address
		data = connection.recv(1)
		if data:
			new_data = str(data)+" "+str(time.time())
			sampling_data.append(new_data)
	finally:
		if L:
			connection.close()
			logout(sampling_data)
	return;
#abre um thread pra esperar input do usuario
def input_thread(L):
	pudim = raw_input()
	L.append(pudim)

#loga os dados depois de fechar a conexao
def logout(sampling_data):
	print("parsing data into file out.csv")
	f = open('out.csv', 'w')
	sampling_n = len(sampling_data)

	for j in range(0, sampling_n):
		f.write(sampling_data[j])

	f.close()
#essa merda tem que funcionar
def main(argv):
	try:
		opts, args = getopt.getopt(argv,"wd", ["wireless","debug"])
	except getopt.GetoptError:
		print 'test.py -w --wireless or -d --debug'
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-w", "--wireless"):
			internet_logger()
			sys.exit()
		elif opt in ("-d", "--debug"):
			serial_logger()
			sys.exit()


#esse pedaco aqui n sei pqq serve 
if __name__ == "__main__":
	main(sys.argv[1:])
# ======================================================
#
#
#                       .ed"""" """$$$$be.                     
#                     -"           ^""**$$$e.                  
#                   ."                   '$$$c                 
#                  /                      "4$$b                
#                 d  3                     $$$$                
#                 $  *                   .$$$$$$               
#                .$  ^c           $$$$$e$$$$$$$$.              
#                d$L  4.         4$$$$$$$$$$$$$$b              
#                $$$$b ^ceeeee.  4$$ECL.F*$$$$$$$              
#    e$""=.      $$$$P d$$$$F $ $$$$$$$$$- $$$$$$              
#   z$$b. ^c     3$$$F "$$$$b   $"$$$$$$$  $$$$*"      .=""$c  
#  4$$$$L   \     $$P"  "$$b   .$ $$$$$...e$$        .=  e$$$. 
#  ^*$$$$$c  %..   *c    ..    $$ 3$$$$$$$$$$eF     zP  d$$$$$ 
#    "**$$$ec   "\   %ce""    $$$  $$$$$$$$$$*    .r" =$$$$P"" 
#          "*$b.  "c  *$e.    *** d$$$$$"L$$    .d"  e$$***"   
#           ^*$$c ^$c $$$      4J$$$$$% $$$ .e*".eeP"         
#               "$$$$$$"'$=e....$*$$**$cz$$" "..d$*"           
#                 "*$$$  *=%4.$ L L$ P3$$$F $$$P"              
#                    "$   "%*ebJLzb$e$$$$$b $P"                
#                      %..      4$$$$$$$$$$ "                  
#                      $$$e   z$$$$$$$$$$%                    
#                        "*$c  "$$$$$$$P"                      
#                         ."""*$$$$$$$$bc                      
#                      .-"    .$***$$$"""*e.                   
#                   .-"    .e$"     "*$c  ^*b.                 
#            .=*""""    .e$*"          "*bc  "*$e..            
#          .$"        .z*"               ^*$e.   "*****e.      
#          $$ee$c   .d"                     "*$.        3.     
#          ^*$E")$..$"                         *   .ee==d%     
#             $.d$$$*                           *  J$$$e*      
#              """""                             "$$$"   
#
#
#
# ===================================================================