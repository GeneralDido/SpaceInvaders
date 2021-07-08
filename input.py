class TextInput:
    """ Gets row input and possible rows/cols from text file. """

    def __init__(self, filename):
        with open(filename, "r") as txt_file:
            lines = txt_file.readlines()
            if len(lines) != 0:
                self.rows = len(lines)
                self.cols = len(lines[0]) - 1
            else:
                raise ValueError("File is empty.")
        with open(filename, "r") as txt_file:
            self.row_signal = txt_file.read().replace('\n', '')
