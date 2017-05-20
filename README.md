# SABSides2017
Programs and slides from my talk at San Antonio BSides 2017


## Layout
bad_encryption_template.py - An example of improperly handling IVs for AES-CBC in python


encrypted_client_server.py - A better example of handling IV and AES-CBC in python (stil not completely secure) A better implementation would involve some sort of key exchange protocol, like diffie hellman, to exchange IVs.


tcp_echo_client.py - TCP client example


tcp_echo_server.py - TCP server example


udp_echo_client.py - UDP client example


udp_echo_server.py - UDP server example
