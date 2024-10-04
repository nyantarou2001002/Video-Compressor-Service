from ._header import *
from .print_tool import *

def input_loop_initial_menu() -> int:
    """
        initial_menuの項目をループして問い合わせる
    """
    
    menu = ["1.動画を圧縮",
            "2.解像度を変更",
            "3.音声ファイルに変換",
            "4.GIFへの変換",
            ]

    while True:
        print_menu(menu)
        ipt = input("> ")

        # 数字でない
        if not ipt.isdigit(): continue

        # 数字に変換
        ipt = int(ipt)

        # モードを選択
        if ipt == COMPRESSION: return COMPRESSION
        elif ipt == RESOLUTION: return RESOLUTION
        elif ipt == AUDIO_CONVERSION: return AUDIO_CONVERSION
        elif ipt == GIF_CONVERSION: return GIF_CONVERSION