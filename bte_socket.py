import socket

# need to know mac address to begin with

class Network():
    def __init__(self):
        self.hostMACAddress = 'ac:74:b1:54:51:4a'
        self.server = self.hostMACAddress
        self.port = 4
        self.backlog = 1
        self.size = 1024

        self.isServer = True
        self.clients = []
        self.running = True

        self.startup()
        self.main()
    
    def startup(self):
        if self.isServer:
            self.socket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
            self.socket.bind((self.hostMACAddress, self.port))
            self.socket.listen(self.backlog)
            print('Running server...')
            return
        
        if not self.isServer:
            self.socket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
            self.socket.connect((self.hostMACAddress, self.port))

    def accept_client(self):
        try:
            client, address = self.s.accept()
            self.clients.append(self.client)
        except Exception as e:
            print('accept_client', e)

    def read_from_clients(self):
        while True:
            for client in self.clients:
                data = client.recv(self.size)
                if data:
                    self.send_to_clients(data)

    def send_to_clients(self, data):
        print(data)
        for client in self.clients:
            client.send(data)
        
    def send_to_server(self, data):
        self.socket.send(bytes(data, 'UTF-8'))

    def accept_message(self):
        while True:
            msg = input()
            if msg:
                self.send_to_clients(msg)

    def clean_exit(self):
        print('exiting')
        for client in self.clients:
            try:
                client.close()
            except:
                pass
        # can probably check server status
        try:
            self.s.close()
        except:
            pass

    def swap_server(self):
        pass
    
    def main(self):
        while self.running:
            # three threads
            self.accept_client()
            self.read_from_clients()
            self.accept_message()
        
        self.clean_exit()

