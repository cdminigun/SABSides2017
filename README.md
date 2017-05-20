# SABSides2017
Programs and slides from my talk at San Antonio BSides 2017


## Layout
bad_encryption_template.py - An example of improperly handling IVs for AES-CBC in python

encrypted_client_server.py - A better example of handling IV and AES-CBC in python (stil not completely secure) A better implementation would involve some sort of key exchange protocol, like diffie hellman, to exchange IVs.
```
usage: encrypted_client_server.py [-h] [-t TYPE_OF_SOCKET] [-p PORT]
                                  [-e ECHO_STRING] [-r REMOTE_ADDRESS]

Client and Server template.

optional arguments:
  -h, --help            show this help message and exit
  -t TYPE_OF_SOCKET, --type_of_socket TYPE_OF_SOCKET
                        The input for type of socket you want. Options: Client
                        or Server
  -p PORT, --port PORT  port number that you want hosted. Anything <= 1024
                        requires sudo requirements.
  -e ECHO_STRING, --echo_string ECHO_STRING
                        prints this string
  -r REMOTE_ADDRESS, --remote_address REMOTE_ADDRESS
                        The remote server client.

Invocations:
Client:
python encrypted_client_server.py -t client -p 1337 -e "hello world" -r 127.0.0.1
Server:
python encrypted_client_server.py -t server -p 1337

```
tcp_echo_client.py - TCP client example


tcp_echo_server.py - TCP server example


udp_echo_client.py - UDP client example


udp_echo_server.py - UDP server example
