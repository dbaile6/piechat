clients = {}
addresses = {}

HOST = ''
port = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        client.send(bytes("Howdy!"+
                          "Pick a username and press the enter button", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()