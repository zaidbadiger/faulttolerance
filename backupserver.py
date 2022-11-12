import socket            
import time

def backupserver():
    backupserver = socket.socket()    
    host = socket.gethostname()  
    ack = "ack"  
    
    # Define the port on which you want to connect
    port = 12345         
    
    # connect to the server on local computer
    backupserver.connect((host, port))
    
    
    backupserver.send("Backup".encode())
    
    # receive data from the server and decoding to get the string.
    ack = (backupserver.recv(1024).decode())
    while True:
        backupserver.send("heartbeat".encode())
        ack = (backupserver.recv(1024).decode())
        if(ack=="ack"):
            print("Heartbeat received")
        time.sleep(1)


    backupserver.close()

    # close the connection
    
if __name__ == '__main__':
    backupserver()