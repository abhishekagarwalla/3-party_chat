#!/usr/bin/python

import getopt
import os
from socket import *
from threading import *
from datetime import datetime
from sys import *
from random import randint

#Command-Line Argument Usage function
def f_Usage():
        print 'asn1.py  -n <name of chatter>  -a <port number on which this program will receive chat msgs from others>   -p <port_no of program>    -d <ipv6 address of 2nd party>,<ipv6 address of 3rd party>    -r <port number of 2nd party>,<port number of 3rd party>'

#Text Decoration
def color(text, color_code):
        if platform == "win32" and os.getenv("TERM") != 'xterm':
                return text
        return '\x1b[%dm%s\x1b[0m' % (color_code, text)

def red(text):
        return color(text, 31)

def green(text):
        return color(text, 32)

def bold(text):
        return color(text, 1)


name="Guest-"+str(randint(1,99))        #Default name

#Command-Line Handler
try:
        opts, args = getopt.getopt(argv[1:],"n:p:a:d:r:")
except getopt.GetoptError:
        f_Usage()
        exit(1)
for opt, arg in opts:
        if opt == '-h':         #help
                f_Usage()
                exit()
        elif(opt in ("-n")):    #<name of chatter>
                name = arg
        elif(opt in ("-p")):    #<port number on which this program will receive chat msgs from others>
                try:
                        myPort = int(arg)
                        if myPort not in range(1024,65536): #handles Port if overflow range:1024-65535
                                print'INVALID PORT NUMBER!Port must be range of 1024-65535\n'
                                f_Usage()
                                exit(1)
                except ValueError as e:
                        print "Could'nt find  port:",e
                        f_Usage()
                        exit(1)
        elif(opt in ("-a")):    #<port_no of program>
                myName = arg
        elif(opt in ("-d")):    #<ipv6 address of 2nd party>,<ipv6 address of 3rd party>
                server_name = arg.split(',')
                name_2 = server_name[0]
                try:
                        name_3 = server_name[1]
                except IndexError:
                        pass

        elif(opt in ("-r")):    #<port number of 2nd party>,<port number of 3rd party>
                port_number = arg.split(',',1)
                port_2 = int(port_number[0])
                try:
                        if port_number[1] != '':
                                port_3 = int(port_number[1])
                except IndexError:
                        pass
#IPV6 socket creation
try:
        mySocket = socket(AF_INET6, SOCK_DGRAM)
        print name,myName,myPort,name_2,name_3,port_2,port_3
        mySocket.bind(('', myPort))
except ValueError as e:
        print "ValueError Occured:",e
        f_Usage()
        exit(1)
except NameError as e:
        print "NameError Occured:",e
        f_Usage()
        exit(1)
except gaierror as e:
        print "Address-related error:",e
        f_Usage()
        exit(1)
except error as e:
        print e
        f_Usage()
        exit(1)
print "--------------CHAT BOX---------------"
print "TO EXIT:Type \"quit\" and press Enter"

def sender():

        try:
                mySocket.sendto(bold(green(name+" is online! ")), (name_2,port_2))
                mySocket.sendto(bold(green(name+" is online! ")), (name_3,port_3))
        except gaierror as e:
                print "Address-related error:",e
                f_Usage()
                exit(1)
        while 1:
                message = raw_input()
                if message !='':

                        if message =="quit":    #when message typed is "quit" program exit  
                                mySocket.sendto(bold(red(name+" is offline! ")), (name_2,port_2))
                                mySocket.sendto(bold(red(name+" is offline! ")), (name_3,port_3))
                                mySocket.close()
                                os._exit(1)

                        #To Display the time message is send
			print "sent at "+datetime.now().strftime("%I:%M%p")+"\n"

                        mySocket.sendto(bold(name)+":"+message , (name_2,port_2))
                        mySocket.sendto(bold(name)+":"+message , (name_3,port_3))

def receiver():

        while 1:
                recdmessage , addr = mySocket.recvfrom(2048)
                print '\n'+recdmessage

                print "Received at "+datetime.now().strftime("%I:%M%p")+"\n"

t1 = Thread(target=sender,args=())
t2 = Thread(target=receiver,args=())
t1.start()
t2.start()
                        
