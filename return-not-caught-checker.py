import astroid

from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker

class ReturnNotCaught(BaseChecker):
    __implements__ = IAstroidChecker

    name = 'return-not-caught'
    priority = -1
    msgs = {
        'W0001': (
            'Return not caught.',
            'return-not-caught',
            'A function returns something but when the function is called, the return value is not saved.'
        ),
    }
    
    def __init__(self, linter=None):
        super(ReturnNotCaught, self).__init__(linter)
        self._function_def_stack = [] # functions w/ return calls
        self._function_calls_stack = [] # functions called w/o variable assignments

    def visit_functiondef(self, node):
        last = node.body[-1]
        if isinstance(last, astroid.Return):
            self._function_def_stack.append(node.name)
            if node.name in self._function_calls_stack:
                self.add_message(
                    'return-not-caught', node=node,
                )

    def visit_call(self, node):
        self._function_calls_stack.append(node.func.as_string())
        if node.func.as_string() in self._function_def_stack:
                self.add_message(
                    'return-not-caught', node=node,
                )

def register(linter):
    """required method to auto register this checker"""
    linter.register_checker(ReturnNotCaught(linter))
