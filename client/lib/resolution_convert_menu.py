import os
from .print_tool import *
from .file_select_tool import *
from .json_tool import *

# mode
RATIO_4_3 = 1
RATIO_16_9 = 2

def resolution_main() -> tuple:
    """
        2.解像度を変換
        解像度変更用のメイン対話シェル

    """
    dic = {}

    # inputファイル
    contents = ls_input_directory()
    input_file = input_target_file(contents)
    dic["input"] = input_file
    input_file_path = create_file_path(input_file)

    # outputファイル名
    output_file_name = input_output_file_name("mp4")
    dic["output"] = output_file_name

    # 解像度を選択してもらう
    width, height = select_resolution()
    dic["width"] = str(width)
    dic["height"] = str(height)

    # jsonファイル作成
    json_dic = create_resolution_json(dic)
    json_file_path = JSON_DIRECTORY + "/" + add_json_extension("resolution_convert")
    save_json(json_dic, json_file_path)

    return (json_file_path, input_file_path)

def create_resolution_json(dic: dict) -> dict:
    """
        解像度変換用のjsonファイルを作成
    """
    input_file_path = create_file_path(dic["input"])
    dic["filesize"] = os.stat(input_file_path).st_size
    dic["type"] = "resolution"
    return dic

def select_resolution() -> tuple:
    """
        解像度を選択してもらう
        width, heightのタプルを返す
    """
    # select ratio
    ratio = select_ratio()

    # 4:3
    if ratio == RATIO_4_3:
        width, height = select_4_3()

    # 16:9
    elif ratio == RATIO_16_9:
        width, height = select_16_9()

    return (width, height)

def select_4_3() -> tuple:
    """
        4:3の画面解像度を選択してもらう
    """
    menu = [
        "1. 3200 x 2400(QUXGA)",
        "2. 2048 x 1536(QXGA)",
        "3. 1600 x 1200(UXGA)", 
        "4. 1280 x 960(QVGA)",
        "5. 1024 x 768(XGA)",
        "6. 800 x 600(SVGA)",
        "7. 640 x 480(VGA)",
        "8. 320 x 240(QVGA)",
        "9. 160 x 120(QQVGA)"
    ]
    while True:
        print_menu(menu)
        print("解像度を数字で選択してください")
        select = input("> ")
        # 空白ならもう一度聞く
        if select == "": continue

        # 文字列ならもう一度聞く
        if not select.isdigit(): continue

        # 各解像度を返す
        if int(select) == 1: return (3200, 2400)
        if int(select) == 2: return (2048, 1536)
        if int(select) == 3: return (1600, 1200)
        if int(select) == 4: return (1280, 960)
        if int(select) == 5: return (1024, 768)
        if int(select) == 6: return (800, 600)
        if int(select) == 7: return (640, 480)
        if int(select) == 8: return (320, 240)
        if int(select) == 9: return (160, 120)


def select_16_9() -> tuple:
    """
        16:9の画面解像度を選択してもらう
    """
    menu = [
        "1. 7680 x 4320(8K)",
        "2. 3840 x 2160(4K)",
        "3. 2560 x 1440(WQHD)",
        "4. 1920 x 1080(FHD)",
        "5. 1600 x 900(WXGA++)",
        "6. 1280 x 720(HD)",
        "7. 1024 x 576",
        "8. 768 x 432",
        "9. 640 x 360",
        "10. 480 x 270",
        "11. 160 x 90"
    ]
    while True:
        print_menu(menu)
        print("解像度を数字で選択してください")
        select = input("> ")
        # 空白ならもう一度聞く
        if select == "": continue

        # 文字列ならもう一度聞く
        if not select.isdigit(): continue

        # 各解像度を返す
        if int(select) == 1: return (7680, 4320)
        if int(select) == 2: return (3840, 2160)
        if int(select) == 3: return (2560, 1440)
        if int(select) == 4: return (1920, 1080)
        if int(select) == 5: return (1600, 900)
        if int(select) == 6: return (1280, 720)
        if int(select) == 7: return (1024, 576)
        if int(select) == 8: return (768, 432)
        if int(select) == 9: return (640, 360)
        if int(select) == 10: return (480, 270)
        if int(select) == 11: return (160, 90)


def select_ratio() -> int:
    """
        画面の比率を選択する
    """
    menu = [
        "1. 4:3",
        "2. 16:9"
    ]
    
    while True:
        print_menu(menu)
        print("解像度の縦横比を数字で選択してください")
        select = input("> ")
        # 空白ならもう一度聞く
        if select == "": continue

        # 文字列ならもう一度聞く
        if not select.isdigit(): continue

        if int(select) == 1: return RATIO_4_3
        elif int(select) == 2: return RATIO_16_9

def create_file_path(file_name: str) -> str:
    """
        file保存パスを作成する
    """
    return INPUT_DIRECTORY + "/" + file_name

