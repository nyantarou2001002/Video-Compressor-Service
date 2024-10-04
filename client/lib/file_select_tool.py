import sys
import os
from ._header import *
from .print_tool import *

def ls_input_directory() -> list:
    """
        inputフォルダの内容を配列にする
    """
    contents = os.listdir(INPUT_DIRECTORY)
    # dotファイルを除く
    contents = [content for content in contents if not content.startswith(".")]
    return contents

def input_target_file(contents: list) -> str:
    """
        変換対象のファイルを取得
    """
    while True:
        if len(contents) == 0:
            print("inputフォルダにファイルがありません")
            sys.exit(1)
        print_menu(contents)
        print("変換するfile名を指定してください")
        file = input("> ")
        # ファイルの存在を確認
        if has_input_directory(contents, file):
            # 拡張子がmp4ならOK
            if file[-4:] == ".mp4":
                return file
            print("拡張子が mp4 ではありません")

def has_input_directory(contents: list, name: str) -> bool:
    """
        指定のファイルがinputフォルダにあるか確認する
    """
    return name in contents

def is_input_directory_empty() -> bool:
    """
        inputディレクトが空かどうかを判定する
    """
    l = ls_input_directory()
    return not bool(l)

def input_output_file_name(extension:str) -> str:
    """
        outputファイル名を指定してもらう
    """
    while True:
        print("output時のファイル名を指定してください。(指定ない場合はqを入力)")
        filename = input("> ")
        if filename == "": continue
        if filename == "q": return "output" + "." + extension
        return filename
