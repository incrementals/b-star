import src.interpreter.globals as globals
from src.interpreter.expression import Expression


def while_func(condition, body):
    result = []
    while Expression(condition, globals.codebase):
        res = Expression(body, globals.codebase)
        if res is not None:
            result.append(res)
    return result
