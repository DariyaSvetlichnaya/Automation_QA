class Reader:
    def __init__(self, file_path):
        self.__file_path = file_path
        self.data = None

    def read_file(self):
        with open(self.__file_path, 'r') as f:
            self.data = f.read()


class Writer:
    def __init__(self, file_path):
        self.__file_path = file_path

    def write_to_file(self, row):
        with open(self.__file_path, 'a') as f:
            f.write(row + '\n')


class ProxyReaderWriter:
    def __init__(self, file_path):
        self.file_path = file_path
        self.reader = Reader(file_path)
        self.writer = Writer(file_path)
        self.data = None
        self.last_read_data = None
        self.last_written_row = None

    def read(self):
        if self.data is not None and self.data == self.last_read_data:
            return

        self.reader.read_file()
        self.data = self.reader.data
        self.last_read_data = self.data
        return self.data

    def write(self, row):
        if row != self.last_written_row:
            self.writer.write_to_file(row)
            self.last_written_row = row


proxy_rw = ProxyReaderWriter(file_path='team_salary.txt')

# proxy_rw.read()
# proxy_rw.read()
# proxy_rw.write('aa')
# proxy_rw.write('aa')
# proxy_rw.read()
# proxy_rw.write('aa')
# proxy_rw.read()
# proxy_rw.write('ab')
# proxy_rw.read()
# proxy_rw.write('aa')
