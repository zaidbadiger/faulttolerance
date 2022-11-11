import socket            
 

def client():
    client = socket.socket()    
    host = socket.gethostname()  
    ack = "ack"  
    
    # Define the port on which you want to connect
    port = 12345         
    data=-1      
    
    # connect to the server on local computer
    client.connect((host, port))
    
    # receive data from the server and decoding to get the string.
    while True:
        data = (client.recv(1024).decode())
        print('Received from server: ' + data)
        if(data==""):
            break
        # once we receive value, write new value to file
        value = int(data)+10
        with open('number.txt', 'w') as writer:
            writer.write(str(value))
        client.send(ack.encode())
    client.close()

    # close the connection
    
if __name__ == '__main__':
    client()