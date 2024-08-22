


def status_bar(current_value: int, max_value: int, bar_width: int=20, config=None):
    if config is None:
        config = {
            "l": "[",
            "r": "]",
            "fill": "@",
            "space": " ",
        }
    ratio = current_value/max_value
    fill_length = int(ratio * bar_width)
    space = bar_width - fill_length

    l = config.get("l", "[")
    r = config.get("r", "[")
    fill = config.get("fill", "=")
    empty = config.get("space", " ")

    return f"{l}{fill_length * fill}{space * empty}{r}"


if __name__ == "__main__":
    for _ in range(40):
        print(status_bar(_+ 1, 40))