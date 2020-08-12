import sys

clients = ["Pablo","Ricardo"]

def create_client(client_name):
    global clients
    
    if client_name not in clients:
        clients.append(client_name.capitalize())
        print("*" * 50)
        print("Client added")
        print("*" * 50)
    else:
        print("Client already in client´s list")

def list_clients():
    global clients

    print("*" * 50)
    for idx, client in enumerate(clients):
        print(f"{idx}: {client}")
    print("*" * 50)


def update_client(client_name, updated_client_name):
    global clients

    if client_name.capitalize() in clients:
        idx = clients.index(client_name.capitalize())
        clients[idx] = updated_client_name.capitalize()
        print("*" * 50)
        print("Client updated.")
        print("*" * 50)
    else:
        print("Client is not in clients list.")


def delete_client(client_name):
    global clients

    if client_name.capitalize() in clients:
        ask_again = input(f"Are you sure? ´{client_name.capitalize()}´ will be erased. (Y/N): ")
        if ask_again.upper() == "Y": 
            clients.remove(client_name.capitalize())
            print("*" * 50)
            print("Client removed.")
            print("*" * 50)
        elif ask_again.upper() == "N":
            print("*" * 50)
            print("Canceling.")
            print("*" * 50)
        else:
            print("*" * 50)
            print("Unknown command.")
            print("*" * 50)
    else:
        print("*" * 50)
        print("Client is not in clients list.")
        print("*" * 50)


def search_client(client_name):
    global clients

    for client in clients:
        if client != client_name.capitalize():
            continue
        else:
            return True


def _get_client_name():
    client_name = None
    while not client_name or client_name == "":
        client_name =  input("Input client´s name or ´exit´ to cancel: ")
        if client_name == "exit":
            break
    if client_name == "exit":
             sys.exit()

    return client_name


def _print_welcome():
    print("PLATZI-VENTAS")
    print("*" * 50)
    print("Choose an option:")
    print("1) CREATE CLIENT")
    print("2) LIST CLIENTS")
    print("3) UPDATE CLIENT")
    print("4) DELETE CLIENT")
    print("5) SEARCH CLIENT")
    print("*" * 50)
    print("6) EXIT")
    print("*" * 50)


if __name__ == "__main__":
    while True:
        _print_welcome()
        
        command = input("Input command ----> ")

        if command == "1":
            client_name = _get_client_name()
            create_client(client_name)
        elif command == "2":
            print("*" * 50)
            list_clients()
            print("*" * 50)
        elif command == "3":
            client_name = _get_client_name()
            updated_client_name = input("Input the updated client name: ")
            update_client(client_name,updated_client_name)
        elif command == "4":
            client_name = _get_client_name()
            delete_client(client_name)
        elif command == "5":
            client_name = _get_client_name()
            found = search_client(client_name)
            if found:
                print("-" *50)
                print(f"´{client_name.capitalize()}´ is in the client´s list.")
                print("-" *50)
            else:
                print("-" *50)
                print(f"´{client_name.capitalize()}´ is not in the client´s list.")
                print("-" *50)
        elif command == "6":
            print("")
            print("Thank you for choosing us.")
            print("")
            break
        else:
            print("")
            print("Unknown command. Try again.")
            print("")