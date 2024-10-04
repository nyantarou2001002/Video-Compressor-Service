# 文字コード
CHARA_CODE = "UTF-8"

# header size
HEADER_SIZE = 8

# type
TYPE_AUDIO_CONVERSION = "audio conversion"
TYPE_GIF_CONVERSION = "gif conversion"

# initial_menu
COMPRESSION = 1
RESOLUTION = 2
AUDIO_CONVERSION = 3
GIF_CONVERSION = 4

# directory
INPUT_DIRECTORY = "input"
OUTPUT_DIRECTORY = "output"
JSON_DIRECTORY = "json"

#-----------------header mehod------------------------

def request_header(client_request, message_length,data_length):
    """
        送信用のheaderを作成する関数
    """
    return client_request.to_bytes(1, "big") + message_length.to_bytes(3,"big") + data_length.to_bytes(4, "big")


def create_send_json_header(filename_length, json_length, data_length):
    """
        送信用ヘッダーを作成する
    """
    return filename_length.to_bytes(1, "big") + json_length.to_bytes(3,"big") + data_length.to_bytes(4,"big")


def json_header_parsing(header):
    """
        json受け渡し時のヘッダーをパースする
    """
    filename_length = int.from_bytes(header[:1], "big")
    json_length = int.from_bytes(header[1:3], "big")
    data_length = int.from_bytes(header[4:8], "big")
    return (filename_length, json_length, data_length)