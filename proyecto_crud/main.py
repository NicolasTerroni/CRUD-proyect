clients = "Pablo,Ricardo,"

def create_client(client_name):
    global clients
    
    clients+=client_name
    _add_comma()


def list_clients():
    global clients

    print(clients)


def _add_comma():
    global clients
    
    clients+=","


def _print_welcome():
    print("PLATZI-VENTAS")
    print("*" * 50)
    print("Choose an option:")
    print("1) CREATE CLIENT")
    print("2) DELETE CLIENT")
    print("3) SHOW CLIENTS")
    print("4) EXIT")


if __name__ == "__main__":
    while True:
        _print_welcome()
        
        command = input("Input command ----> ")

        if command == "1":
            client_name = input("Input client name: ")
            create_client(client_name)
        elif command == "2":
            pass
        elif command == "3":
            print("*" * 50)
            list_clients()
            print("*" * 50)
        elif command == "4":
            print("")
            print("Thank you for choosing us.")
            print("")
            break
        else:
            print("")
            print("Unknown command. Try again.")
            print("")