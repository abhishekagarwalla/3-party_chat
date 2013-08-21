Abhhishek Agarwalla
1pi10is135

-------------------------------------------------
  Assignment : 1
  Project    : B1 ( 3 party chat using IPv6)
-------------------------------------------------

Group Members :
Akshay R Bastawad       1PI10IS010
Kushwant singh Saluja   1PI10IS127
Abhishek Agarwalla      1PI10IS135
-------------------------------------------------


Files :
Program file : asn1.py
Output file  : output.txt (sample output)
Readme files :
                1.  Readme_1pi10is010.txt - 1PI10IS010
                2.  Readme_1pi10is127.txt - 1PI10IS127
                3.  Readme_1pi10is135.txt - 1PI10IS135

Contribution:
-------------
1.1PI10IS010 : Core programming , command-line script , testing
2.1PI10IS127 : Core Programming , Exception-handling  , testing
3.1PI10IS135 : Core Programming , Text-Decoration     , testing

STEPS:
-----
step1: Program names: 1)asn1.py
--------------------

step2:Execution
---------------
a)python asn1.py -n <name of chatter> -a <ipv6 address to be used by this program> -p <port number on which this program will receive chat msgs from others> -d <ipv6 address of 2nd party>,<ipv6 address of 3rd party> -r <port number of 2nd party>,<port number of 3rd party>

example:
a)On same System:
abhishek@ubuntu:~/Desktop$python asn1.py -n abhishek -a ::1 -p 12345  -d ::1,::1 -r 12347,12346

b)On different System:

//myip:fe80::4eeb:42ff:fe0f:d142
//myport:12345
//sender ip:fe80::be77:37ff:fe26:d7cf

abhishek@ubuntu:~/Desktop$python asn1.py -n abhishek -a fe80::4eeb:42ff:fe0f:d142 -p 12345  -d fe80::be77:37ff:fe26:d7cf,fe80::4eeb:42ff:fe0f:d142 -r 12347,12346

Testing
--------
1)Done on local system,i.e. same system
        Example:abhishek@ubuntu:~/Desktop$python asn1.py -n abhishek -a ::1 -p 12345  -d ::1,::1 -r 12347,12346
2)Done on 2 system,2-terminal on 1-system and 1-terminal on other-system.

        Example:command as shown in Execution.
        output file has been uploaded for same.

3)Checked for errors and exception and then handled.

Modules used:
---------------
1 socket : To handle creation and operation of sockets and respective functions.
2 threading : For implentation of MultiThreading
3 getopt : To take values from Commandline.
4 datetime : To access current time.
5 sys : For successful or unsuccessful termination of program using sys.exit([status]).
6 random : To generate random number.used when -n(name) is not provided.example:Guest-25.

Understanding
-------------
1)to create a 3-party chat that sends and receives message in syncronized manner(user can send any number of message without waiting for reply for each message.
2)Input to be passed from cmd-line.
3)ipv6 supporting socket creation.
4)Display sends ONLINE message if the user runs the program correctly.
5)to display the message send on console with the sendes id(name)
6)Display OFFLINE message if user "quit" from console


Working
--------
1)Create socket to create client-server environment.
2)has two function sender and receiver
3)sender()-sends the message type,online,offline message.
4)receiver()-receives the message send.
5)when user runs program it displays ONLINE message to other users if they are available.
6)when user wants to exit from program type "quit" and a OFFLINE message will be send to available users.
7)send and receive time is displays after message is send or received.




Challenges faced:
----------------
1.To syncronise sending message.
2.handling exception handling.

Things not done
----------------
1)keyboard Interrupt not handled.Instead type "quit" to exit(Problem may be due to multithreading)
2)validation of IPV6 address using Regex.Contribution:


NOTE:Program has been tested on ubuntu and not on other OS(windows,MAC 0S)
NOTE:output.txt has been uploaded.
NOTE: Regarding Readme file :Only Understanding , program execution, challenges faced and testing parts in Readme have been written individually  and others (like Modules used , Commandline-usage etc) parts in readme have been commonly written and are same in all 3 Readme files.
