lines = 30

def line_wrap_print(mes: str) -> None:
    """
        行頭に|をつけてprintする
    """
    print("| ", end="")
    print(mes)

def print_menu(string_arr: list) -> None:
    """
        配列で渡した文字列を表示する
    """
    print("-" * lines)
    for i in range(len(string_arr)):
        line_wrap_print(string_arr[i])
    print("-" * lines)