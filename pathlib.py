import os

class Path:
    """Simple pathlib.Path shim for Python 2 compatibility used in tests.
    Supports only the methods required by the test suite: is_file() and read_text().
    """
    def __init__(self, path):
        self._path = path

    def is_file(self):
        return os.path.isfile(self._path)

    def read_text(self, encoding='utf-8'):
        with open(self._path, 'r', encoding=encoding) as f:
            return f.read()
