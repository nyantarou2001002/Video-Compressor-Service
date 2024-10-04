import os
import sys
import socket
from ._header import *
from .json_tool import *


class TCP_Server:
    def __init__(self, address,port):
        self.sock, self.addr, self.port = self.startup_tcp_server(address, port)

    def __enter__(self):
        return self
    
    def __exit__(self, *args):
        self.sock.close()

    def startup_tcp_server(self, server_address:str, server_port:int, listen=5) -> tuple:
        """
            TCPサーバーを立てる関数
            connect用のsocketと、(IP_address, PORT)のタプルを返す
        """
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
            sock.bind((server_address, server_port))
            sock.listen(listen)
            return (sock, server_address, server_port)
        except (socket.timeout, ConnectionRefusedError):
            return

class Server():
    # configファイルのパス
    config_path = "config.json"
    FILE_DIRECTORY = "tmp"
    JSON_DIRECTORY = "tmp"

    def __init__(self):
        self.load_config()

    def load_config(self):
        """
            configファイルから必要な情報を読み込む
        """
        config_dict = load_json(self.config_path)
        self.address = config_dict["webserver"]["address"]
        self.port = config_dict["webserver"]["port"]

    def save_config(self, address:str, port:int):
        """
            configファイルに書き込む
        """
        config_dict = {}
        config_dict["webserver"] = {}
        config_dict["webserver"]["address"] = address
        config_dict["webserver"]["port"] = port
        save_json(config_dict, self.config_path)

    def send_file_server(self, filepath:str, sock) -> None:
        """
            filepathのjsonファイルを送信する
        """
        connection, client_address = sock.accept()

        with open(filepath, "rb") as f:
            f.seek(0, os.SEEK_END)
            filesize = f.tell()
            f.seek(0,0)

            if filesize > pow(2, 32):
                raise Exception("File must be below 2GB.")

            filename = os.path.basename(f.name)

            filename_bits = filename.encode(CHARA_CODE)

            header = create_send_json_header(len(filename_bits), 0, filesize)

            connection.send(header)
            connection.send(filename_bits)

            data = f.read(4096)
            print("Sending...", end="")
            while data:
                connection.send(data)
                data = f.read(4096)
            print()
            print("complete!")
            return 

    def recieve_file_server(self, sock) -> str:
        """
            ファイル受け渡し用のサーバ
        """

        # 受け渡し用のディレクトリを作成
        self.create_file_directory()

        connection, client_address = sock.accept()
        try:
            print("connection from", client_address)
            header = connection.recv(HEADER_SIZE)

            filename_length, json_length, data_length = json_header_parsing(header)

            stream_rate = 4096

            filename = connection.recv(filename_length).decode(CHARA_CODE)

            if json_length != 0:
                raise Exception("This data is not currently supported.")
            if data_length == 0:
                raise Exception("No data to read from client.")

            with open(os.path.join(FILE_DIRECTORY, filename), "wb+") as f:
                while data_length > 0:
                    data = connection.recv(data_length if data_length <= stream_rate else stream_rate)
                    f.write(data)
                    data_length -= len(data)
                    print(data_length)

            print("Finished downloading the file from client.")
        except Exception as e:
            print("Error: " + str(e))
        return filename

    def create_file_directory(self) -> None:
        """
            file受け渡しをする fileフォルダを作成する
        """
        if not os.path.exists(FILE_DIRECTORY):
            os.makedirs(FILE_DIRECTORY)
            
    def create_json_directory(self) -> None:
        """
            json受け渡しをするjsonフォルダを作成する
        """
        if not os.path.exists(JSON_DIRECTORY):
            os.makedirs(JSON_DIRECTORY)


def send_server_message(connection, message):
    """
        connectionに、messageをutf-8にencodeして送る関数
    """
    connection.send(message.encode(CHARA_CODE))

def server_exit(sock):
    """
        serverのソケット終了処理
    """
    sock.close()
    sys.exit(0)
