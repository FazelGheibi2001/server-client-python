import random
import socket
import time

import model
import pickle


def start_client():
    HOST = '127.0.0.1'
    PORT = 8885

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            signal = prepare_signal()
            if signal:
                s.send(pickle.dumps(signal))
                time.sleep(.5)


def prepare_signal():
    if random.randint(1, 20) > 18:
        return model.Signal("BITCOIN", 1250)
    return None


if __name__ == '__main__':
    start_client()