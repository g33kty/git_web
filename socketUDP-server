import socket
import os
import json
from datetime import datetime

UDP_IP = '127.0.0.1'
UDP_PORT = 5000


def run_server(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server = ip, port
    sock.bind(server)
    try:
        while True:
            data, address = sock.recvfrom(1024)
            message = data.decode()
            print(f'Received data: {message} from: {address}')
            
            save_message(message)

    except KeyboardInterrupt:
        print(f'Destroy server')
    finally:
        sock.close()


def save_message(data_str, folder='storage', filename='data.json'):
    try:
        data_dict = eval(data_str)  # Обережно з eval, він виконує код. Для безпечності краще використовувати json.loads() для рядків JSON.
    except:
        print("Error in parsing string")
        return

    if not os.path.exists(folder):
        os.makedirs(folder)
    file_path = os.path.join(folder, filename)

    timestamp = str(datetime.now())
    messages = {}

    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            try:
                messages = json.load(file)
            except json.JSONDecodeError:
                print("Existing file is corrupted or empty. Overwriting.")

    messages[timestamp] = data_dict

    with open(file_path, 'w') as file:
        json.dump(messages, file, indent=2)

    print(f'Message saved successfully at {timestamp}')


if __name__ == '__main__':
    run_server(UDP_IP, UDP_PORT)
