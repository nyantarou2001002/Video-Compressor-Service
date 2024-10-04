import subprocess
import os
from ._header import *
from .json_tool import *
from .print_tool import *
from .file_select_tool import *


def gif_conversion_main() -> tuple:
    """
        4.GIFへの変換
        jsonのファイルパス と 変換ファイルのパスを返す
    """
    dic = {}
    # inputファイル
    contents = ls_input_directory()
    input_file = input_target_file(contents)
    dic["input"] = input_file
    input_file_path = create_file_path(input_file)

    # 固定比
    # 横幅に合わせて調整するオプション
    video_size = input_width_size()
    dic["video_size"] = str(video_size)
    
    # フレームレート
    fps = input_fps()
    dic["fps"] = str(fps)

    # 切り取る秒数
    video_length = get_video_length(input_file_path)
    start_time = input_start_time(video_length)
    end_time = input_end_time(start_time, video_length)
    dic["start_time"] = seconds_to_hms(start_time)
    dic["end_time"] = str(end_time)

    # outputファイル名
    output_file_name = input_output_file_name("gif")
    dic["output"] = output_file_name

    # jsonファイル作成
    json_dic = create_gif_conversion_json(dic)
    json_file_path = JSON_DIRECTORY + "/" + add_json_extension("gif_convert")
    save_json(json_dic, json_file_path)

    return (json_file_path, input_file_path)

def create_gif_conversion_json(dic) -> dict:
    """
        gif変換用のjsonファイルを作成
    """
    input_file_path = create_file_path(dic["input"])
    dic["filesize"] = os.stat(input_file_path).st_size
    dic["type"] = "gif conversion"
    return dic

def input_end_time(start_time, video_length) -> int:
    """
        動画を切り取るエンドタイムを指定してもらう
    """
    while True:
        print(f"動画を切り取る終了時間を指定してください({start_time} ~ {video_length})")
        end_time = int(input("> "))
        if end_time < 0 :
            print_error_messege("マイナスは指定できません")
            continue
        elif video_length <= end_time: 
            print_error_messege("動画時間を超えています")
            continue
        elif end_time <= start_time:
            print_error_messege("開始時間より手前を指定しています")
            continue
        # 切り出し開始時間より長く動画時間より短ければOK
        elif start_time < end_time and end_time < video_length: return end_time


def input_start_time(video_length) -> int:
    """
        動画を切り取るスタートタイムを指定してもらう
    """
    while True:
        print(f"動画を切り取る開始時間を指定してください(0 ~ {video_length})")
        start_time = int(input("> "))
        # 0以下ならやり直し
        if start_time < 0 :
            print_error_messege("マイナスは指定できません")
            continue
        elif video_length <= start_time: 
            print_error_messege("動画時間を超えています")
            continue
        # 動画時間より短ければOK
        elif start_time < video_length: return start_time

def print_error_messege(message):
    """
        エラーメッセージを表示する
    """
    print("-" * 50)
    print(message)
    print("-" * 50)

def seconds_to_hms(seconds: int) -> str:
    """
        秒数を00:00:00形式に変換する
    """
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return "{:02}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds))

def input_width_size() -> int:
    """
        固定したい横幅を指定してもらう
    """
    while True:
        print("固定したい横幅を指定してください")
        width = int(input("> "))
        if width <= 0 : continue
        else: return width

def input_fps() -> int:
    """
        変換したいフレームレートを入力してもらう(1~60)
    """
    while True:
        print("変換したいフレームレートを入力してください(1~60)")
        fps = int(input("> "))
        if fps < 1 or 60 < fps: continue
        else: return fps

def create_file_path(file_name:str) -> str:
    """
        file保存パスを作成する
    """
    return INPUT_DIRECTORY + "/" + file_name

def get_video_length(video_path):
    """
        動画時間を取得する
        小数以下は切り捨て
    """
    command = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", video_path]
    output = subprocess.check_output(command)
    # 小数以下は切り捨て
    video_length = int(float(output))
    return video_length

