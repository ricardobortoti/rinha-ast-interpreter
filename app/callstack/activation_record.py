from enum import Enum

from app.callstack.stack import Stack


class ARType(Enum):
    GLOBAL_SCOPE = 'GLOBAL_SCOPE'
    FUNCTION_SCOPE = 'FUNCTION_SCOPE'


class ActivationRecord:
    def __init__(self, name, type, nesting_level):
        self.name = name
        self.type = type
        self.nesting_level = nesting_level
        self.members = Stack()

    def __setitem__(self, key, value):
        self.members.peek()[key] = value

    def __getitem__(self, key):
        if None is self.members.peek().get(key):
            ar = self.prev
            return ar[key]
        return self.members.peek()[key]

    def get(self, key):
        return self.members.peek().get(key)

    def __str__(self):
        lines = [
            '{level}: {type} {name}'.format(
                level=self.nesting_level,
                type=self.type.value,
                name=self.name,
            )
        ]
        for name, val in self.members.items():
            lines.append(f'   {name:<20}: {val}')

        s = '\n'.join(lines)
        return s

    def __repr__(self):
        return self.__str__()
