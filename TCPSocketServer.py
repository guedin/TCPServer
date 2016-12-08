import socketserver
import sqlite3
import time
import random
import struct

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
		# self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip().decode()
        self.request = self.data.split('Request')[1]
        print("{x} request : {y}".format(x=self.client_address[0], y=self.request))

        if self.request == "GetServerList":
            print("Send the server list")
        elif self.request == "AddSession":
            print("Add a new session")
        else:
            print("Error : Unexpected request")

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS sessionList(id INTEGER, name TEXT, current INTEGER, max INTEGER)")

def data_entry():
    sessionName = 'Guedin'
    currentPlayer = 1
    c.execute("INSERT INTO sessionList (name, current) VALUES (?, ?)", (sessionName, currentPlayer))
    conn.commit()
    print("Data inserted")

if __name__ == "__main__":
    HOST, PORT = "127.0.0.1", 8081

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C


    conn = sqlite3.connect('Session.db')
    c = conn.cursor()

    create_table()

    data_entry()

    server.serve_forever()
