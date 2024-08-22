from utils.text_block import TextBlock

class Screen:
    def __init__(self, width: int=40, height: int=20, debug: bool=True):
        self.width = width
        self.height = height

        self.data = self.build_data("█")
        self.border = True

        if debug:
            self.add_string(f'w:{self.width} h:{self.height}')
        

    def __str__(self):
        base_string = "\n".join("".join(row) for row in self.data)
        if self.border:
            nb = TextBlock(base_string, border=True)
            return f"{nb}"
        return base_string
    
    def build_data(self, starting_value: str=" "):
        return [[starting_value for i in range(self.width)] for j in range(self.height)]
    
    def replace(self, x, y, data):
        self.data[y][x] = data

    def replace_row(self, x, y, data):
        for _, ch in enumerate(data):
            current_position = x + _
            if current_position > self.width:
                continue
            self.replace(current_position, y, f"{ch}")

    def replace_section(self, x, y, data):
        for j, row in enumerate(data):
            for i, entry in enumerate(row):
                current_x = x + i
                current_y = y + j

                if current_x > self.width:
                    continue
                if current_y > self.height:
                    continue

                self.replace(current_x, current_y, f"{entry}")

    def add_string(self, string: str, x: int=0, y: int=0):
        # Completely disregard invalid input
        # if len(string) + x > self.width:
        #     return
        for _, ch in enumerate(string):
            current_x = x + _
            if current_x > self.width:
                continue
            self.replace(current_x, y, ch)

    def add_string_block(self, data, x: int=0, y: int=0):
        for j, row in enumerate(data.split("\n")):
            for i, entry in enumerate(row):
                current_x = x + i
                current_y = y + j

                if current_x > self.width:
                    continue
                if current_y > self.height:
                    continue

                self.replace(current_x, current_y, f"{entry}")

