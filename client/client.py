import sys
import os
import shutil
from lib._header import *
from lib.initial_menu import *
from lib.audio_convert_menu import *
from lib.gif_convert_menu import *
from lib.resolution_convert_menu import *
from lib.compression_convert_menu import *
from lib.file_select_tool import *
from lib.tcp_client import *

def setup_directory() -> None:
    """
        最初に、必要なファイルを生成する
    """
    # input
    if not os.path.isdir(INPUT_DIRECTORY):
        os.mkdir(INPUT_DIRECTORY)

    # json
    if not os.path.isdir(JSON_DIRECTORY):
        os.mkdir(JSON_DIRECTORY)

    # output
    if not os.path.isdir(OUTPUT_DIRECTORY):
        os.mkdir(OUTPUT_DIRECTORY)

def remove_json_directory() -> None:
    """
        tmpディレクトリの中身を削除する処理
    """
    target_dir = "json"
    shutil.rmtree(target_dir)

def main() -> None:
    """
        対話的にメニューを表示して、動画の変換を行う
    """
    # client classを生成する
    client = Client()

    # 必要なディレクトリを作成する
    setup_directory()

    # inputディレクトリが空だった場合終了する
    if is_input_directory_empty():
        print("inputディレクトリが空です。inputディレクトリに変換したいファイルを設置してください。")
        sys.exit(1)

    # メニューを表示する
    select = input_loop_initial_menu()

    # 分岐して、変換対象のファイルパスと、jsonのパスを作成
    if select == COMPRESSION: 
        json_file_path, input_file_path = compression_main()
    elif select == RESOLUTION: 
        json_file_path, input_file_path = resolution_main()
    elif select == AUDIO_CONVERSION:
        json_file_path, input_file_path = audio_conversion_main()
    elif select == GIF_CONVERSION:
        json_file_path, input_file_path = gif_conversion_main()

    # jsonファイルを送信
    client.send_file_client(json_file_path)

    # 変換ファイルを送信
    client.send_file_client(input_file_path)

    # 仕切りを表示
    print("-"*50)

    # 変換後のファイルを受け取る
    client.recieve_file_client(OUTPUT_DIRECTORY)

    # jsonディレクトリを削除する
    remove_json_directory()

if __name__ == "__main__":
    main()
    

