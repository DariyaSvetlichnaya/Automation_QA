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
        self.last_written_value = None

    def write_to_file(self, data):
        if data != self.last_written_value:
            with open(self.__file_path, 'a') as f:
                f.write(data + '\n')
                self.last_written_value = data


class ProxyReaderWriter:
    def __init__(self, file_path):
        self.file_path = file_path
        self.reader = Reader(file_path)
        self.writer = Writer(file_path)
        self.data = None

    def read(self):
        self.reader.read_file()
        self.data = self.reader.data

    def write(self, row):
        last_value = self.reader.data.strip().split('\n')[-1] if self.reader.data else None
        if row != last_value:
            self.writer.write_to_file(row)
            self.read()


proxy_rw = ProxyReaderWriter(file_path='team_salary.txt')

proxy_rw.read()
proxy_rw.read()
proxy_rw.write('aa')
proxy_rw.read()
proxy_rw.write('aa')
proxy_rw.write('ab')
proxy_rw.read()
proxy_rw.write('aa')

print(proxy_rw.data)
