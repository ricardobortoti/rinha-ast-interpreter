import sys
from io import StringIO


class StdoutCapture:
    def __enter__(self):
        self.stdout_capture = StringIO()
        self.original_stdout = sys.stdout
        sys.stdout = self.stdout_capture
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout = self.original_stdout
        self.captured_output = self.stdout_capture.getvalue()
        self.stdout_capture.close()

    def get_output(self):
        return self.captured_output
