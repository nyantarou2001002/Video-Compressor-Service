import json

def save_json(dic: dict, filepath: str) -> None:
    """
        dicをjsonとして保存する
    """
    with open(filepath, "w") as f:
        json.dump(dic, f)

def load_json(filepath: str) -> None:
    """
        filepathのjsonをロードする
    """
    with open(filepath, "r") as f:
        d = json.load(f)
    return d

def save_arr_json(arr: list, filepath: str) -> None:
    """
        配列をjsonとして保存する
    """
    with open(filepath, "w") as f:
        json.dump(arr, f)

def add_json_extension(file:str) -> str:
    """
        jsonの拡張子を付け加える
    """
    return file + ".json"

