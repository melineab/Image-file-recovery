import os


class RecoverImage:
    def __init__(self, filename):
        self.chunk_size = 1024
        self.filename = filename

    def recover(self):
        with open(self.filename, 'r+b') as file:
            file.seek(3 * self.chunk_size)

            while True:
                chunk = file.read(self.chunk_size)
                if len(chunk) < self.chunk_size:
                    break
                file.seek(file.tell() - self.chunk_size)
                file.write(chunk[::-1])
                file.seek(file.tell() + 2 * self.chunk_size)

    def recover_as(self, recovered_file_name):

        with open(self.filename, 'rb') as file:
            file_size = os.stat(self.filename).st_size
            read_info = file.read(3 * self.chunk_size)
            with open(recovered_file_name, "ab") as new_file:
                while True:
                    reversed_chunk = file.read(self.chunk_size)[::-1]
                    new_file.write(read_info)
                    new_file.write(reversed_chunk)
                    read_info = file.read(2 * self.chunk_size)

                    file_size = file_size - self.chunk_size
                    if file_size < self.chunk_size:
                        break


if __name__ == '__main__':
    # RecoverImage('damaged.jpg').recover()
    RecoverImage('damaged.jpg').recover_as('recovered.jpg')
