import sys
import re
from lib.tcp_server import *

def main():
    s = Server()

    print("現在の設定は以下のようになっています")
    print("-"*50)
    print(f"address: {s.address}")
    print(f"port: {s.port}")
    print("-"*50)
    while True:
        ipt = input("設定を変更しますか？(y/n) > ")
        
        if ipt.lower() == "y":
            address = input_address()
            port = input_port()
            s.save_config(address, int(port))
            print("-"*50)
            print("設定を変更しました。")
            print(f"address: {s.address}")
            print(f"port: {s.port}")
            print("-"*50)
            sys.exit()
        elif ipt.lower() == "n":
            sys.exit()

def input_address():
    """
        IPアドレスを入力してもらう
    """
    while True:
        print("addressを入力してください。")
        address = input("> ")

        if is_valid_ipv4(address):
            return address
        else:
            print("Error: IPアドレスの形式ではありません")
        
def input_port():
    """
        port番号を入力してもらう
    """
    while True:
        print("port番号を入力してください。")
        port = input("> ")

        # 空白か数字かを判定してエラーを返す
        if not port.isdigit() or port.isspace():
            print("Error: 数字で入力してください。")
            continue

        # portとして正しい形式かを判定する
        if is_valid_port(port):
            return port

def is_valid_ipv4(ip):
    """
        IPv4アドレスかどうかを判定
    """
    # IPv4アドレスの正規表現パターン
    pattern = re.compile(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
    return bool(pattern.match(ip))  

def is_valid_port(port:str) -> bool:
    """
        ポート番号の形式にマッチするかを判定
    """
    # ポート番号の正規表現パターン
    pattern = re.compile(r'^(6553[0-5]|655[0-2][0-9]|65[0-4][0-9]{2}|6[0-4][0-9]{3}|[1-5][0-9]{4}|[1-9][0-9]{0,3}|0)$')
    return bool(pattern.match(port))

if __name__ == "__main__":
    main()

