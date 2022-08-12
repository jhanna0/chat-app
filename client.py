import socket
from threading import Thread

# remove ignoring '' to see if junk is constantly being sent

class Client():
    def __init__(self):
        self.running = True
        self.host = socket.gethostname()
        self.port = 50000
        self.size = 1024

    def startup(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
    
    def listen(self):
        while self.running:
            data = self.socket.recv(1024)
            data = data.decode("utf-8")
            if data != '':
                print(data)
    
    def send(self):
        while self.running:
            data = input()
            self.socket.sendall(bytes(data, 'UTF-8'))

    def main(self):
        self.startup()
        Thread(target=self.listen).start()
        Thread(target=self.send).start()
        print('Chat:')

client = Client()
client.main()