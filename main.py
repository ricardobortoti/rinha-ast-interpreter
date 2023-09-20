import json
import logging
import time

from app.interpreter import Interpreter

if __name__ == '__main__':
    # logging.basicConfig(level=logging.ERROR)
    interpreter = Interpreter()
    with open('test_files/scratch.ast.json', 'r') as file:
        ast = json.load(file)
        start_time = time.time()

        interpreter.interpret(ast)

        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Function took {elapsed_time} seconds to execute.")
        # interpreter.dump_symbol_table()
