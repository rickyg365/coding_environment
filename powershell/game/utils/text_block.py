
class TextBlock:
    def __init__(self, data: str, border: bool=False):
        self.data = data
        self.rows = self.data.split("\n")
        self.width = max([len(row) for row in self.rows])
        self.height = len(self.rows)
        self.border = border


    def __str__(self):
        if self.border:
            top_left = "╭"
            top_right = "╮"
            bot_left = "╰"
            bot_right = "╯"
            hor = "─"
            ver = "│"
        
            top = f"{top_left}{self.width * hor}{top_right}"
            middle = "\n".join("".join([ver, *row, ver]) for row in self.rows)
            bot = f"{bot_left}{self.width * hor}{bot_right}"

            return "\n".join([top, middle, bot])
        
        return self.data

    def update_data(self, new_data):
        self.data = new_data
        self.rows = new_data.split("\n")
