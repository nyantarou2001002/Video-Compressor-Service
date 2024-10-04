import os
from ._header import *
from .print_tool import *
from .file_select_tool import *
from .json_tool import *

def compression_main():
    """
        1.動画を圧縮
        対話的に圧縮について聞き出す関数
    """
    dic = {}

    # inputファイルj
    contents = ls_input_directory()
    input_file = input_target_file(contents)
    dic["input"] = input_file
    input_file_path = create_file_path(input_file)

    # outputファイル名
    output_file_name = input_output_file_name("mp4")
    dic["output"] = output_file_name

    # 各種オプションの処理
    # video codec 
    dic["video codec"] = "libx264"
    # audio codec
    dic["audio codec"] = "aac"
    
    # 他のオプションは、圧縮レベルで変更
    dic = select_compression_menu(dic)

    # jsonファイル作成
    json_dic = create_compression_json(dic)
    json_file_path = JSON_DIRECTORY + "/" + add_json_extension("compression_convert")
    save_json(json_dic, json_file_path)

    return (json_file_path, input_file_path)

def create_compression_json(dic) -> dict:
    """
        動画圧縮用のjsonファイルを作成
    """
    input_file_path = create_file_path(dic["input"])
    dic["filesize"] = os.stat(input_file_path).st_size
    dic["type"] = "compression"
    return dic
    

def select_compression_menu(dic):
    """
        1.動画の圧縮メニュー
        H,M,L
    """
    menu = [
        "h. High",
        "m. Middle",
        "l. Low"
    ]

    while True:
        print_menu(menu)
        print('圧縮レベルを選択してください(ex."h" "High" "high")')
        select = input("> ")
        # 空白ならもう一度聞く
        if select == "": continue

        if select.lower() == "h" or select.lower() == "high": return compression_high(dic)
        elif select.lower() == "m" or select.lower() == "middle": return compression_middle(dic)
        elif select.lower() == "l" or select.lower() == "low": return compression_low(dic)

def compression_high(dic):
    """
        圧縮のHighテンプレート
    """
    dic["tune"] = "zerolatency"
    dic["preset"] = "veryslow"
    dic["crf"] = "18"
    dic["bit rate"] = "96k"
    return dic

def compression_middle(dic):
    """
        圧縮のmiddleテンプレート
    """
    dic["tune"] = "film"
    dic["preset"] = "faster"
    dic["crf"] = "23"
    dic["bit rate"] = "64k"
    return dic

def compression_low(dic):
    """
        圧縮のlowテンプレート
    """
    dic["tune"] = "fastdecode"
    dic["preset"] = "ultrafast"
    dic["crf"] = "28"
    dic["bit rate"] = "32k"
    return dic


def create_file_path(file_name):
    """
        file保存パスを作成する
    """
    return INPUT_DIRECTORY + "/" + file_name


