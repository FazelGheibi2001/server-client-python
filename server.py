import socket
import pickle


def start_server():
    HOST = '127.0.0.1'
    PORT = 8885

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))

        s.listen()
        print("server listening on port ", PORT)

        while True:
            try:
                con, addr = s.accept()
                with con:
                    while True:
                        data = con.recv(1024)
                        signal = pickle.loads(data)
                        print('signal_type: ', signal.signal_type)
                        print('value: ', signal.value)
            except:
                print("client disconnected")


if __name__ == '__main__':
    start_server()
