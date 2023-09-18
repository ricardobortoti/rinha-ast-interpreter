from unittest import TestCase

from app.callstack.activation_record import ActivationRecord, ARType


class TestActivationRecord(TestCase):
    def test_get(self):
        activation_record = ActivationRecord("test", ARType.GLOBAL_SCOPE, 1)
        expected = 2
        expected2 = 6
        activation_record['variable'] = expected
        activation_record['variable2'] = expected2
        variable = activation_record.get('variable')
        variable2 = activation_record['variable2']
        self.assertEqual(variable, expected)
        self.assertEqual(variable2, expected2)
