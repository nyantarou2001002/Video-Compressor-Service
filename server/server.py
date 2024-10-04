import shutil

from lib._header import *
from lib.ffmpeg_tool import * 
from lib.json_tool import *
from lib.file_server import *
from lib.tcp_server import *

def main() -> None:
    server = Server()

    with TCP_Server(server.address, server.port) as s:
        # socket
        sock = s.sock
        while True:
            print("Ctrl + C キーで終了します。")
            try:
                # jsonの受け取り
                json_file_name = server.recieve_file_server(sock)

                # fileの受け取り
                recieved_file_name = server.recieve_file_server(sock)

                # jsonのfileパスを作成する
                json_filepath = "tmp/" + json_file_name

                # jsonのパース
                command = json_parser(json_filepath)
                output_file_name = "tmp/" + get_output_file_name(json_filepath)
                
                # 処理を行う
                run_ffmpeg(command)

                # 仕切りを表示
                print("-"*50)

                # fileの送信処理
                server.send_file_server(output_file_name, sock)

            except KeyboardInterrupt:
                # 終了処理 (Ctrl+C)
                break
            finally:
                # 最後に、受け取ったファイルとJSONファイルを削除する
                remove_tmp_directory()
    return

def remove_tmp_directory() -> None:
    """
        tmpディレクトリの中身を削除する処理
    """
    target_dir = "tmp"
    shutil.rmtree(target_dir)

def get_output_file_name(filepath: str) -> str:
    """
        outputファイル名を取得する
    """
    json_dict = load_json(filepath)
    return json_dict["output"]

def json_parser(filepath:str) -> list:
    """
        parseしたJSONからコマンドを作成する
    """
    # json load
    json_dict = load_json(filepath)

    # 変換タイプの指定
    convert_type = json_dict["type"]
    # ffmpegで使うコマンドに直す
    # 動画圧縮
    if convert_type == TYPE_COMPRESSION:
        command = command_generation_compression(json_dict)
    # 動画の解像度の変更
    elif convert_type == TYPE_RESOLUTION:
        command = command_generation_resolution(json_dict)
    # 音声ファイルに変更する
    elif convert_type == TYPE_AUDIO_CONVERSION:
        command = command_generation_audio_conversion(json_dict)
    # gif動画に変更する
    elif convert_type == TYPE_GIF_CONVERSION:
        command = command_generation_gif_conversion(json_dict)
    return command

if __name__ == "__main__":
    main()