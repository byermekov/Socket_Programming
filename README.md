# Socket Programming Implementation of Client-Server Bulletin Board System using TCP Connection (python socket)
**CS3201 Computer Networks** assignment for implementing client-server bulletin board system that allows clients to post, read, and retrieve text messages. The server runs on a specified port and supports three commands executed by the client: POST, READ, and QUIT.



## Features
<b>POST</b>: Allows clients to send text messages to the server. The client can enter the text line by line, with the first line containing the command "POST" and subsequent lines treated as the text. The end of the text input is signalled by entering a line consisting of only "#". The server acknowledges the receipt of the command with "OK".

<b>READ</b>: Upon receiving this command, the server sends all previously posted text messages by the client and other clients to the client as the standard output.

<b>QUIT</b>: Informs the server to close the socket connection to the client. The server acknowledges the receipt of the command with "OK".

## Usage

Clone the repository

```
git clone https://github.com/byermekov/Socket_Programming.git
```

Go to Folder /Socket_Programming/

```
cd Socket_Programming
```


For **`PC1 (Server)`** run server.py

```
python server.py
```

For **`PC2 (Client)`** run client.py

```
python client.py
```



- This will start the server on PC1. **PC1 and PC2 must be in the same WLAN**

- The client program will prompt you to enter the IP address and port number of the server
    - Take note of the IP address of PC1. You can find it by running the command ```ipconfig``` in the command line.

    - The server will be listening on port 16011.

 
 
 
 
## Options 
 

Once the connection is established, you can enter one of the following three commands: *POST*, *READ*, or *QUIT*. If an invalid command is entered, the server will return an "*ERROR*" message.

***`POST`***

- you can send multiple messages to the server. Enter each message as a separate line, and make sure to not include "*`#`*" in any of the lines. 

- To end the POST process and store the messages on the server, enter "#" in a new line.

- The server will respond with "OK" to acknowledge the receipt of the POST command.

***`READ`*** 

- the client will receive all the messages saved on the server and display them.

***`QUIT`*** 

- the client will terminate the connection with the server, and the client-server interaction will end. The server will send "OK" in response.

## Possible rundown

```
client> hello
``` 

```
server> ERROR - Command not understood
```
```
client> POST
client> Welcome socket programming
client> Text#!
client> more text.
client> #
```
```
server> OK
```

```
client> READ
```

```
server> Welcome socket programming
server> Text#!
server> more text.
server> #
```

```
client> QUIT
```
```
server> OK
```

Feel free to modify and extend the code to suit your specific requirements or add more functionality to it.