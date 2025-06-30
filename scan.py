def scan(prompt: object = '', ReturnType=None, error: object = ''):
    """Read a string from a standard input and validates a specified return type.
       Print error message if input and return type are incompatible."""
    if not isinstance(ReturnType, type | None):
        raise TypeError(f"invalid ReturnType argument for scan(): '{ReturnType}'")
    import ast
    while True:
        user = input(prompt).strip()
        if ReturnType is str:
            return user
        elif not ReturnType:
            try:
                if not isinstance((ast.literal_eval(user)), str):
                    return ast.literal_eval(user)
                return user
            except (SyntaxError, ValueError, TypeError):
                return user
        elif ReturnType not in (int, bool, float): ### aka a list, set, etc
            try:
                return ReturnType(ast.literal_eval(user)) #### return range(10); return list(1, 2); return dict({"language" : "english}"), for example
            except (SyntaxError, ValueError, TypeError):
                print(error)
                continue
        try:
            return ReturnType(ast.literal_eval(user)) #####
        except (SyntaxError, ValueError, TypeError) as e:
            print(error)
            continue
