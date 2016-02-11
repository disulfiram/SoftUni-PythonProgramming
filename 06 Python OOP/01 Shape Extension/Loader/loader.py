import os


class Loader:
    def __init__(self,filename):
        if os.access(filename, os.R_OK) and os.path.isfile(filename):
            self.filename=filename
        else:
            raise ValueError("Inaccessible file'{}".format(filename))

    def load(self):
        raise NotImplementedError()