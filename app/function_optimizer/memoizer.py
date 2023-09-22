def try_memoize(self, callee, stack_frame, result):
    params = ''.join([f"{item['text']}{stack_frame.members[item['text']]}"
                      for item in stack_frame.members[callee]['parameters']
                      if item['text'] in stack_frame.members])
    index = f'{callee}' + params
    self.call_stack.function_result_cache[index] = result


def try_recover_memoization(self, callee, stack_frame):
    params = ''.join([f"{item['text']}{stack_frame.members[item['text']]}"
                      for item in stack_frame.members[callee]['parameters']
                      if item['text'] in stack_frame.members])
    index = f'{callee}' + params
    if index in self.call_stack.function_result_cache:
        # print("memoization hit")
        return self.call_stack.function_result_cache[index]
    return None
