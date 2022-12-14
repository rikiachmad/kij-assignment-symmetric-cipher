# kij-assignment-symmetric-cipher

# Table of contents
- [kij-assignment-symmetric-cipher](#kij-assignment-symmetric-cipher)
- [Table of contents](#table-of-contents)
  - [Description](#description)
  - [Requirements](#requirements)
  - [Usage](#usage)

## Description
![alt text](https://github.com/rikiachmad/kij-assignment-symmetric-cipher/blob/main/assets/Symmetric-Encryption.jpg?raw=true)

In this assignment we create a program written in python to send or receives files from different hosts with socket. This program also use various symmetric encryption/decryption method using the PyCrypto library. Available cipher used in this program are AES with CTR Mode of Operation, DES with CTR Mode of Operation, and RC4. Every keys and nonces used in this program is being hardcoded for educational purpose only. In real life scenarios we dont want to send the secret keys through the network with symmetric cipher.  

![alt text](https://github.com/rikiachmad/kij-assignment-symmetric-cipher/blob/main/assets/Workflow.jpg?raw=true)  
This program can be used as sender(client) or receiver(server) with specific command.
The workflow of this program goes like this:
1. Client encrypts file with hardcoded keys in the program.
2. Client creates new file named [original name + '.enc'].
3. Client write encrypted binary(encoded with b64) to the new file.
4. Client send the encrypted file to server with socket.
5. Server receives encrypted file.
6. Server decrypts the received file with the same keys hardcoded in the program.
7. Server creates new file named [original name] and write the decrypted file to the new file.

![alt text](https://github.com/rikiachmad/kij-assignment-symmetric-cipher/blob/main/assets/Class-Diagram.png?raw=true)  

And here is the Class Diagram of this program.


## Requirements
Requirements to run this program is defined in the requirements.txt. Run ``` pip install -r requirements.txt``` to install all the requirements.  


## Usage
Clone this repo to your local environment  
``` git clone https://github.com/rikiachmad/kij-assignment-symmetric-cipher.git ```  
<br />
This program can be run as client to send file or as server to receive the file. Use this command to run the program as client:  
<br />
``` python3 main.py send [FILE_PATH] [CIPHER] ```  
<br />
Available cipher options are AES, DES, and RC4. This will create new file named [original name + '.enc'] under your working directory which is the encrypted version of your original file. This way we can see the actual encryption text result for educational and analysis purpose. The file that is going to be send by the client is this encrypted file, not the original file.  
<br />
Before running the client side, you need to run as server to listen to any conneciton made. Use this command to start the server:  
<br />
``` python3 main.py receive```  
<br />
The file received by the server is the encrypted one. And then the program automatically decrypt the file with the hardcoded keys. So two files will appear to your current working directory, one is the received file from client(encrypted .enc file) and the other one is the decrypted file(original file).  

The cipher, original filename and size is also sent by the client separately, this way the server doesn't need to specify any cipher to decrypt the received file since the secret keys are hardcoded in the program. Again, this is for educational pupose only.