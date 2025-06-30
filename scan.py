def scan(prompt: object = '', ReturnType=None, error: object = ''):
    """Read a string from a standard input and validates a specified return type.
       Print error message if input and return type are incompatible."""
    if not isinstance(ReturnType, type | None):
        raise TypeError(f"invalid ReturnType argument for scan(): '{ReturnType}'")
    import ast
    while True:
        user = input(prompt).strip()
        if ReturnType:
            try:
                return ReturnType(user)
            except ValueError:
                print(error)
                continue
        else:
            try:
                if not isinstance((ast.literal_eval(user)), str):
                    return ast.literal_eval(user)
                return user
            except ValueError:
                print(error)
                return user
