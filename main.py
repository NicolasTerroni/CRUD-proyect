import sys
import csv
import os

CLIENT_TABLE = ".clients.csv"
CLIENT_SCHEMA = ["name", "company", "email", "position"]
clients = []


def _initialize_clients_from_storage():
    with open(CLIENT_TABLE, mode="r") as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)

        for row in reader:
            clients.append(row)


def _save_clients_to_storage():
    tmp_table_name = f"{CLIENT_TABLE}.tmp"
    with open(tmp_table_name, mode="w") as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)

    os.remove(CLIENT_TABLE)
    os.rename(tmp_table_name, CLIENT_TABLE)


def create_client(client):
    global clients
    
    if client not in clients:
        clients.append(client)
        print("*" * 50)
        print("Client added")
        print("*" * 50)
    else:
        print("Client already in client´s list")

def list_clients():
    global clients

    for idx, client in enumerate(clients):
        print(f"""[{idx}] - {client["name"]} - {client["company"]} - {client["email"]} - {client["position"]}""")
        print("-" * 50)


def update_client(client_id):
    global clients

    for idx, client in enumerate(clients):
        if idx == client_id:
            print(f"""Updating ID: {idx} Client:´{client["name"]}´""")
            clients.pop(idx)
            client = {
                "name": _get_client_field("name"),
                "company":_get_client_field("company"),
                "email":_get_client_field("email"),
                "position":_get_client_field("position")          
                }
            create_client(client)
            break
    else:
        print("There´s no such client ID.")

def delete_client(client_id):
    global clients

    for idx, client in enumerate(clients):
        if idx == client_id:
            ask_again = input(f"""Are you sure? ID: {idx} Client:´{client["name"]}´ will be erased. (Y/N): """)
            if ask_again.upper() == "Y": 
                clients.pop(idx)
                print("*" * 50)
                print("Client removed.")
                print("*" * 50)
                break
            elif ask_again.upper() == "N":
                print("*" * 50)
                print("Canceling.")
                print("*" * 50)
                break
            else:
                print("*" * 50)
                print("Unknown command.")
                print("*" * 50)
                break
    else:
        print("*" * 50)
        print(f"Client ID: {idx} does not exist.")
        print("*" * 50)


def search_client(client_name):
    global clients

    for idx, client in enumerate(clients):
        if idx != client_id:
            continue
        else:
            print("-" * 50)
            print(f"""[{idx}] - {client["name"]} - {client["company"]} - {client["email"]} - {client["position"]}""")
            print("-" * 50)
            break
    else:
        print(f"Client ID: {idx} does not exist.")


def _get_client_field(field_name):
    field = None
    while not field or field == "":
        field =  input(f"Input new client´s {field_name} or ´exit´ to cancel and close: ")
        if field == "exit":
            _save_clients_to_storage()
            break
    if field == "exit":
        sys.exit()
    
    return field


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
    _initialize_clients_from_storage()
    while True:
        _print_welcome()
        
        command = input("Input command ----> ")

        if command == "1":
            client = {
                "name": _get_client_field("name"),
                "company":_get_client_field("company"),
                "email":_get_client_field("email"),
                "position":_get_client_field("position")          
                }
            create_client(client)

        elif command == "2":
            print("*" * 50)
            list_clients()
            print("*" * 50)
        elif command == "3":
            client_id = int(input("Input client ID to update: "))
            update_client(client_id)
        elif command == "4":
            client_id = int(input("Input client ID to delete: "))
            delete_client(client_id)
        elif command == "5":
            client_id = int(input("Input client ID to search: "))
            search_client(client_id)
            
        elif command == "6":
            print("")
            print("Thank you for choosing us.")
            print("")
            _save_clients_to_storage()
            break
        else:
            print("")
            print("Unknown command. Try again.")
            print("")