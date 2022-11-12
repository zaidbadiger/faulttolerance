import socket
import time
import _thread

def on_new_connection(conn, addr):
    connectionMessage = conn.recv(1024).decode()
    if(connectionMessage == "Client 1"):
        main_client_communication(conn, addr)
    else:
        backup_communication(conn, addr)

def main_client_communication(conn, addr):
    clientReply="ack"
    value=0
    
    while clientReply=="ack":
        with open('number.txt', 'r') as reader:
            value = int(reader.readline())
        
        # send value to client
        conn.send(str(value).encode())
                
        clientReply = conn.recv(1024).decode()

        time.sleep(0.3)
    conn.close()
    
def backup_communication(conn, addr):
    while True:
        conn.send("ack".encode())
        heartbeat = conn.recv(1024).decode()

        
    clientReply = conn.recv(1024).decode()
    conn.close()
    
def server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 12345   
    
    
    with open('number.txt', 'w') as writer:
        writer.write("0")
        
    server.bind((host, port)) #bind host and port together
    print ("server binded to port %s" %(port))
    
    
    # put the socket into listening mode
    server.listen()    
    print(f"Listening on {(host, port)}")

 
    # Establish connection with client.
    try:
        conn, addr = server.accept()  
        print ('Got connection from', addr )
        _thread.start_new_thread(on_new_connection,(conn,addr))    
        conn, addr = server.accept()  
        print ('Got connection from', addr )
        _thread.start_new_thread(on_new_connection,(conn,addr))   
        startTime = time.time()
        while time.time()-startTime<5:
            continue
        print ('server died')
        server.close()
    except KeyboardInterrupt:
        print ('server stopped')
        server.close()


    
    

    

if __name__ == '__main__':
    server()