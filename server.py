import socket
from threading import Thread

class Server():
    def __init__(self):
        self.running = True
        self.socket = socket.socket()
        self.host = socket.gethostname()
        self.port = 50000
        self.size = 1024

        self.clients = []
        
    def startup(self):
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)
        print('server running')

    def on_new_client(self, clientsocket, addr):
        self.clients.append(clientsocket)
        while self.running:
            msg = clientsocket.recv(self.size)
            if msg != '':
                self.send_to_clients(msg)
        clientsocket.close()
    
    def send_to_clients(self, msg):
        for client in self.clients:
            try:
                client.sendall(msg)
            except Exception as e:
                # getting broken pipe but ignore for now
                pass

    def main(self):
        self.startup()
        while self.running:
            c, addr = self.socket.accept()
            Thread(target=self.on_new_client, args=(c, addr)).start()
        
        self.socket.close()
    
server = Server()
server.main()
