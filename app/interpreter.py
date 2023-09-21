from memory_profiler import profile

from app.callstack.call_stack import CallStack
from app.callstack.activation_record import ActivationRecord, ARType
from app.binary.binaryops import proc_binary
from app.function_optimizer.memoizer import try_memoize, try_recover_memoization


class Interpreter:
    def __init__(self):
        self.call_stack = CallStack()

    def eval_let(self, term):
        result = self.eval_term(term['value'])
        if result is not None:
            ar = self.call_stack.peek()
            ar[term['name']['text']] = result

    def eval_print(self, term):
        result = self.eval_term(term['value'])
        print(result)
        return result

    def eval_var(self, term):
        ar = self.call_stack.peek()
        return ar[term['text']]

    def eval_str(self, term):
        return term['value']

    def eval_int(self, term):
        return term['value']

    def eval_bool(self, term):
        return term['value']

    def eval_binary(self, term):
        lhs = self.eval_term(term['lhs'])
        rhs = self.eval_term(term['rhs'])
        op = term['op']

        return proc_binary(op, lhs, rhs)

    def eval_function(self, term):
        return term

    def eval_if(self, term):
        if self.eval_term(term['condition']):
            return self.eval_term(term['then'])
        else:
            return self.eval_term(term['otherwise'])

    def eval_call(self, term):
        callee = term['callee']['text']
        function_params = self.call_stack.peek()[callee]['parameters']
        arguments = term['arguments']

        # Create a new ActivationRecord for the function call
        ar = ActivationRecord(
            name=callee,
            type=ARType.FUNCTION_SCOPE,
            nesting_level=self.call_stack.peek().nesting_level + 1,
            members=self.call_stack.peek().get_members().copy(),
        )

        # Bind function parameters to arguments in the new ActivationRecord
        for param, arg in zip(function_params, arguments):
            ar[param['text']] = self.eval_term(arg)

        # Push the new ActivationRecord onto the call stack
        self.call_stack.push(ar)

        # Perform the function call and capture the result
        result = self.function_call(callee, self.call_stack.peek())

        # Pop the ActivationRecord from the call stack after the function call
        self.call_stack.pop()

        return result

    def function_call(self, callee, stack_frame):
        result = try_recover_memoization(self, callee, stack_frame)
        if result is not None:
            return result
        else:
            result = self.eval_term(stack_frame[callee]['value'])
            try_memoize(self, callee, stack_frame, result)
            return result

    # @profile
    def eval_term(self, term):
        evaluators = {
            "Let": self.eval_let,
            "Print": self.eval_print,
            "Str": self.eval_str,
            "Int": self.eval_int,
            "Var": self.eval_var,
            "Binary": self.eval_binary,
            "Function": self.eval_function,
            "Call": self.eval_call,
            "If": self.eval_if,
            "Bool": self.eval_bool
        }

        evaluator = evaluators.get(term['kind'])
        if evaluator:
            ret = evaluator(term)
            if ret is not None:
                return ret
            else:
                if 'next' in term:
                    return self.eval_term(term['next'])
        else:
            raise ValueError(f"Unsupported term kind: {term['kind']}")

    def interpret(self, ast):
        ar = ActivationRecord(
            name="main",
            type=ARType.GLOBAL_SCOPE,
            nesting_level=1
        )

        self.call_stack.push(ar)

        self.eval_term(ast['expression'])

        self.call_stack.pop()

    def dump_symbol_table(self):
        print("##################SYMBOL TABLE##################")
