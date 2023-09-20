# from symbol_table import SymbolTable


class CallStack:
    def __init__(self):
        self._records = []
        self._current_activation_record = None

    def push(self, ar):
        self._current_activation_record = ar
        self._records.append(ar)

    def pop(self):
        popped = self._records.pop()

        if self._records.__len__() > 0:
            self._current_activation_record = self._records[-1]
        else:
            None

        return popped

    def peek(self):
        return self._current_activation_record

    def __str__(self):
        s = '\n'.join(repr(ar) for ar in reversed(self._records))
        s = f'CALL STACK\n{s}\n'
        return s

    def __repr__(self):
        return self.__str__()
