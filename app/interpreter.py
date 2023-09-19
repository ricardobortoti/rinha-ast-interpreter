from app.callstack.call_stack import CallStack
from app.callstack.activation_record import ActivationRecord, ARType
from app.binary.binaryops import proc_binary


class Interpreter:
    def __init__(self):
        # logging.basicConfig(level=logging.ERROR)
        self.call_stack = CallStack()

    def eval_let(self, term):
        # logging.debug(f"Evaluating let variable name {term['name']['text']}")
        result = self.eval_term(term['value'])
        if result is not None:
            ar = self.call_stack.peek()
            ar[term['name']['text']] = result

    def eval_print(self, term):
        # logging.debug("Evaluating print")
        result = self.eval_term(term['value'])
        print(result)
        return result

    def eval_var(self, term):
        # logging.debug("Evaluating var")
        ar = self.call_stack.peek()
        return ar[term['text']]

    def eval_str(self, term):
        # logging.debug("Evaluating str")
        return term['value']

    def eval_int(self, term):
        # logging.debug("Evaluating int")
        return term['value']

    def eval_bool(self, term):
        # logging.debug("Evaluating bool")
        return term['value']

    def eval_binary(self, term):
        # logging.debug("Evaluating binary")
        lhs = self.eval_term(term['lhs'])
        rhs = self.eval_term(term['rhs'])
        op = term['op']

        return proc_binary(op, lhs, rhs)

    def eval_function(self, term):
        # logging.debug("Evaluating function : store symbolic rep")
        return term

    def eval_if(self, term):
        # logging.debug("Evaluating If")
        if self.eval_term(term['condition']):
            return self.eval_term(term['then'])
        else:
            return self.eval_term(term['otherwise'])

    def eval_call(self, term):
        # logging.debug("calling function")
        callee = term['callee']['text']
        function_params = self.call_stack.peek()[callee]['parameters']
        arguments = term['arguments']
        context = {param['text']: self.eval_term(arg) for param, arg in zip(function_params, arguments)}

        ar = ActivationRecord(
            name=callee,
            type=ARType.FUNCTION_SCOPE,
            nesting_level=self.call_stack.peek().nesting_level+1,
            members=self.call_stack.peek().get_members().copy(),
        )

        for key, value in context.items():
            ar[key] = value

        self.call_stack.push(ar)
        result = self.function_call(callee, self.call_stack.peek())
        self.call_stack.pop()

        return result

    def function_call(self, callee, stack_frame):
        return self.eval_term(stack_frame[callee]['value'])

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
