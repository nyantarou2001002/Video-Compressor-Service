import socket
import os
from ._header import *
from .json_tool import *

class TCP_Client:
    def __init__(self, server_address, server_port):
        self.server_address = server_address
        self.server_port = server_port
        self.sock, self.addr, self.port = self.startup_tcp_client(self.server_address, self.server_port)

    def __enter__(self):
        return self
    
    def __exit__(self, *args):
        """
            python終了時にsocketをcloseする
        """
        self.sock.close()

    def startup_tcp_client(self, server_address:str, server_port: int) -> tuple:
        """
            TCPクライエントを起動する関数
            connect用のsocketと、(IP_address, PORT)のタプルを返す
        """
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
            sock.connect((server_address, server_port))
            return (sock, server_address, server_port)
        except (socket.timeout, ConnectionRefusedError):
            return
        except socket.error as e:
            print(e)
            return 

class Client():
    # configファイルのパス
    config_path = "config.json"

    def __init__(self):
        self.load_config()

    def load_config(self):
        """
            configファイルから必要な情報を読み込む
        """
        config_dict = load_json(self.config_path)
        self.server_address = config_dict["webserver"]["address"]
        self.server_port = config_dict["webserver"]["port"]

    def save_config(self, address:str, port:int):
        """
            configファイルに書き込む
        """
        config_dict = {}
        config_dict["webserver"] = {}
        config_dict["webserver"]["address"] = address
        config_dict["webserver"]["port"] = port
        save_json(config_dict, self.config_path)

    def recieve_file_client(self,directory_path):
        """
            file受け取り用のクライアント
        """
        with TCP_Client(self.server_address, self.server_port) as c:
            try:
                header = c.sock.recv(HEADER_SIZE)

                # header のパース
                filename_length, json_length, data_length = json_header_parsing(header)
                stream_rate = 4096

                filename = c.sock.recv(filename_length).decode(CHARA_CODE)

                if json_length != 0:
                    raise Exception("This data is not currently supported.")
                if data_length == 0:
                    raise Exception("No data to read from client.")

                with open(os.path.join(directory_path, filename), "wb+") as f:

                    print("recieved...", end="")
                    while data_length > 0:
                        data = c.sock.recv(data_length if data_length <= stream_rate else stream_rate)
                        f.write(data)
                        data_length -= len(data)

                print()
                print("Finished download!")
            except Exception as e:
                print("Error: " + str(e))
        return

    def send_file_client(self,filepath):
        """
            ファイル送信用のクライアント
        """
        with TCP_Client(self.server_address, self.server_port) as c:

            with open(filepath, "rb") as f:
                f.seek(0, os.SEEK_END)
                filesize = f.tell()
                f.seek(0,0)

                if filesize > pow(2, 32):
                    raise Exception("File must be below 2GB.")

                filename = os.path.basename(f.name)

                filename_bits = filename.encode(CHARA_CODE)

                header = create_send_json_header(len(filename_bits), 0, filesize)

                c.sock.send(header)
                c.sock.send(filename_bits)

                data = f.read(4096)
                while data:
                    # print("Sending...")
                    c.sock.send(data)
                    data = f.read(4096)

def send_tcp_header(sock, header_message:str) -> None:
    """
        TCPクライアントからheaderを送信する
    """
    header = request_header(header_message, 0, 0)
    sock.send(header)

def send_tcp_message(sock, message: str) -> None:
    """
        TCPクライアントからメッセージを送信する
    """
    message = encode_message(message)
    sock.send(message)

def encode_message(message: str) -> bytes:
    """
        utf-8 の 
        str -> byte へのエンコード
    """
    return message.encode("utf-8")