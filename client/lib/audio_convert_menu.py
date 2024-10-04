import os
from ._header import *
from .json_tool import *
from .file_select_tool import *

def audio_conversion_main() -> tuple:
    """
        3.音声ファイルへの変換
        音声ファイル変換のメイン対話シェル
        jsonのファイルパスと変換ファイルのパスを返す
    """
    # inputディレクトリの内容を取得
    contents = ls_input_directory()

    # inputディレクトリから変換対象を選ばせる
    input_file = input_target_file(contents)

    # jsonファイル用辞書を作成
    d = create_audio_conversion_json(input_file)

    # jsonファイルを作成する
    json_file_path = JSON_DIRECTORY+ "/" + add_json_extension("audio_convert")
    save_json(d, json_file_path)

    # 変換対象のファイルパスを作成
    input_file_path = create_file_path(input_file)

    return (json_file_path, input_file_path)

def create_audio_conversion_json(input_file):
    """
        音声変換用のjsonファイルを作成
    """
    json_dict = {}
    json_dict["input"] = input_file 
    json_dict["filesize"] = os.stat(create_file_path(input_file)).st_size
    json_dict["output"] = "output_" + input_file.replace(".mp4", "") + ".mp3"
    json_dict["type"] = "audio conversion"
    return json_dict

def create_file_path(file_name):
    """
        file保存パスを作成する
    """
    return INPUT_DIRECTORY + "/" + file_name

def crate_json_path(json_name):
    """
        jsonの保存パスを作成する
    """
    return JSON_DIRECTORY + "/" + json_name