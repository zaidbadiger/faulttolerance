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
    try:
        while True:
            backupserver.send("heartbeat".encode())
            ack = (backupserver.recv(1024).decode())
            if(ack=="ack"):
                print("Heartbeat received")
            time.sleep(1)
    except ConnectionResetError:
        backupserver.close()
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        port = 12345   
        
        server.bind((host, port)) #bind host and port together
        print (" backup server binded to port %s" %(port))
        
        
        # put the socket into listening mode
        server.listen()    
        print(f"Listening on {(host, port)}")

    
        # Establish connection with client.
        conn, addr = server.accept()  
        print ('Got connection from', addr )
        clientReply="ack"

    
        while clientReply=="ack":
            with open('number.txt', 'r') as reader:
                value = int(reader.readline())
            
            # send value to client
            conn.send(str(value).encode())
                    
            clientReply = conn.recv(1024).decode()

            time.sleep(0.3)
        conn.close()



    

    # close the connection
    
if __name__ == '__main__':
    backupserver()