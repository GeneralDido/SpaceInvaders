class TextInput:
    def __init__(self, filename):
        with open(filename, "r") as txt_file:
            self.signal = txt_file.read().replace('\n', '')
