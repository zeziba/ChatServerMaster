[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/zeziba/ChatServerMaster/graphs/commit-activity)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/zeziba/ChatServerMaster/blob/master/LICENSE)
[![Build Status](https://travis-ci.org/zeziba/ChatServerMaster.svg?branch=master)](https://travis-ci.org/zeziba/ChatServerMaster)
[![codecov](https://codecov.io/gh/zeziba/ChatServerMaster/branch/master/graph/badge.svg)](https://codecov.io/gh/zeziba/ChatServerMaster)



[![ForTheBadge powered-by-electricity](http://ForTheBadge.com/images/badges/powered-by-electricity.svg)](http://ForTheBadge.com)
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

### Mission Statement

The is an open source version of a chat server and client, the chat server will save all input from the users with the option
to disable this feature.

There will be a web interface that can be loaded by any client to attach itself to the server with the
only required information being the ip address and the port number to connect to.


Features to be implemented:
*Users and passwords
*Encrypted data streams
*Database to store chats

### Installation

To install the server follow these steps
 
 1. `git clone -b ChatServerMaster https://github.com/zeziba/ChatServerMaster.git`
 2. `cd ./ChatServerMaster`
 3. `python3 -m pip install setup.py`
 
 
### Using the Chat Server
 
 Once the program is installed then the server can be launched with
 `python server.py <IP> <PORT>`
 
 After the server is launched a client can connect to the specified
 IP address and port number. The server uses the websocket protocol
 so any client using that protocol is fine to use for communications.
 


