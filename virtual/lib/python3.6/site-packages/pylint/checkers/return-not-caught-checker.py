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
        last = node.body[-1] # I think this is the return statement? last line of a function? is there a better way to find the return statement?
        if isinstance(last, astroid.Return): # if last thing is a return statement
            self._function_def_stack.append(node.body.name) # keep track of function name
            if node.body.name in self._function_calls_stack: # check if function has been called
                self.add_message(
                    'return-not-caught', node=node,
                )

    def visit_call(self, node): # so here: not sure if we can figure out if this is assigned? this represents "func()" but could also I think be a child of "foo = func()" :/
        self._function_calls_stack.append(node.body.func.as_string())# keep track of func name
        if node.body.func.as_string() in self._function_def_stack: # same as above, check if its in the other list
                self.add_message(
                    'return-not-caught', node=node,
                )

def register(linter):
    """required method to auto register this checker"""
    linter.register_checker(ReturnNotCaught(linter))
