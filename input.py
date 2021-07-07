class TextInput:
    def __init__(self, filename):
        with open(filename, "r") as txt_file:
            lines = txt_file.readlines()
            self.rows = len(lines)
            self.cols = len(lines[0]) - 1
        with open(filename, "r") as txt_file:
            self.row_signal = txt_file.read().replace('\n', '')
