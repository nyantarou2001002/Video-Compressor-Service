import subprocess

def command_generation_compression(json_dict: dict) -> list:
    """
        mp4を圧縮するコマンドを生成
    """
    # dictをパースする
    input_file_path = "tmp/" + json_dict["input"]
    output_file_path = "tmp/" + json_dict["output"]
    video_codec = json_dict["video codec"]
    audio_codec = json_dict["audio codec"]
    tune = json_dict["tune"]
    preset = json_dict["preset"]
    crf = json_dict["crf"]
    bit_rate = json_dict["bit rate"]

    # commandを作成
    # 以下、一例
    # ffmpeg -i input.mp4 -c:v libx264 -tune zerolatency -preset ultrafast -crf 40 -c:aac -b:a 32k output.mp4
    command = [
        "ffmpeg",
        "-i",
        input_file_path,
        # ビデオのコーデックを指定
        "-c:v",
        video_codec,
        # 最適化
        "-tune",
        tune,
        # プリセット
        "-preset",
        preset,
        # CRF(Constant Rate Factor)
        "-crf",
        crf,
        # オーディオのコーデック
        "-c:a",
        audio_codec,
        # オーディオのビットレート
        "-b:a",
        bit_rate,
        output_file_path
    ]
    return command

def command_generation_resolution(json_dict: dict) -> list:
    """
        mp4の解像度を変更するコマンドを生成
    """
    # dictをパースする
    input_file_path = "tmp/" + json_dict["input"]
    output_file_path = "tmp/" + json_dict["output"]
    scale = json_dict["width"] + ":" + json_dict["height"]

    # commandを作成
    # ffmpeg -i input.mp4 -filter:v scale=1280:720 -c:a copy output.mp4
    command = [
        "ffmpeg",
        "-i",
        input_file_path,
        "-vf" ,
        "scale=" + scale,       # 変換するvideoの解像度
        "-c:a",
        "copy",        # オーディオの変換は行わず、そのままオーディオを新しいファイルで使う
        output_file_path
    ]
    return command

def command_generation_audio_conversion(json_dict: dict) -> list:
    """
        mp4をmp3に変換するffmpegコマンドを作成する
    """
    # dictをパースする
    input_file_path = "tmp/" + json_dict["input"]
    output_file_path = "tmp/" + json_dict["output"]

    # commandを作成
    # ffmpeg -i input_file_name -vn output_file_name
    command = [
        "ffmpeg",
        "-y",
        "-i",
        input_file_path,
        "-vn",
        output_file_path
    ]
    return command

def command_generation_gif_conversion(json_dict:dict) -> list:
    """
        mp4をgifに変換するffmpegコマンドを作成する
    """

    # dictをパースする
    input_file_path = "tmp/" + json_dict["input"]
    output_file_path = "tmp/" + json_dict["output"]
    start_time = json_dict["start_time"]
    end_time = json_dict["end_time"]
    fps = json_dict["end_time"]
    scale = "scale="+json_dict["video_size"]+":-1"

    # commandを作成
    # ffmpeg -ss 00:00:20 -i input.mp4 -to 10 -r 10 -vf scale=300:-1 output.gif
    command = [
        "ffmpeg",
        "-y",
        "-ss",
        start_time,
        "-i",
        input_file_path,
        "-to",
        end_time,
        "-r",
        fps,
        "-vf",
        scale,
        output_file_path
    ]
    return command

def run_ffmpeg(command):
    """
        コマンドを受け取り、ffmpegを実行する
    """
    # コマンドの実行
    subprocess.run(command)

