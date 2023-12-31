from enum import Enum


class ARType(Enum):
    GLOBAL_SCOPE = 'GLOBAL_SCOPE'
    FUNCTION_SCOPE = 'FUNCTION_SCOPE'


class ActivationRecord:

    def __init__(self, name, type, nesting_level, members=None):
        self.name = name
        self.type = type
        self.nesting_level = nesting_level
        self.members = self.members = members if members is not None else {}

    def __setitem__(self, key, value):
        self.members[key] = value

    def __getitem__(self, key):
        return self.members[key]

    def get(self, key):
        return self.members.get(key)

    def get_members(self):
        return self.members

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
