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
        self.inAssign = False # checks whether call node is within an assign node

    def visit_functiondef(self, node):
        last = node.body[-1] # should be return node if there is one?
        if isinstance(last, astroid.Return): # if it is
            self._function_def_stack.append(node.name) # add function name to stack
            if node.name in self._function_calls_stack: # if function has already been called w/o assignment
                self.add_message(
                    'return-not-caught', node=node,
                )

    def visit_assign(self, node): # when we enter an assign node, change flag to reflect that
        self.inAssign = True

    def leave_assign(self, node): # we have exited an assign node so no longer true
        self.inAssign = False
                
    def visit_call(self, node):
        if not self.inAssign: # if not in assign node
            self._function_calls_stack.append(node.func.as_string()) # add name to check if it's defined later
        if node.func.as_string() in self._function_def_stack and not self.inAssign: # if function returns something but the call is not within an assign node, return error
                self.add_message(
                    'return-not-caught', node=node,
                )

def register(linter):
    """required method to auto register this checker"""
    linter.register_checker(ReturnNotCaught(linter))
