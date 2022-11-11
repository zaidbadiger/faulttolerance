import socket
import time

def server():
    server = socket.socket()
    host = socket.gethostname()
    port = 12345
    clientReply="ack"
    value=0
    
    with open('number.txt', 'w') as writer:
        writer.write("0")
        
    server.bind((host, port)) #bind host and port together
    print ("server binded to port %s" %(port))
    
    # put the socket into listening mode
    server.listen(2)    
    print ("socket is listening")    
    # Establish connection with client.
    conn, addr = server.accept()    
    print ('Got connection from', addr )       
    
    # a forever loop until we interrupt it or
    # an error occurs
    while clientReply=="ack" and value<100:
        with open('number.txt', 'r') as reader:
            value = int(reader.readline())
        
        # send value to client
        conn.send(str(value).encode())
                
        clientReply = conn.recv(1024).decode()
        
        

        
        time.sleep(1)
        
    conn.close()

    

if __name__ == '__main__':
    server()