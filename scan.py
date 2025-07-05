def scan(ReturnType: type, prompt: object='', error: object=''):
    """Read a string from a standard input and validate a specified return type.
       Print error message if input and return type are incompatible."""
    if not isinstance(ReturnType, type | None):
        raise TypeError(f"invalid ReturnType argument for scan(): '{ReturnType}'")
    while True:
        user = input(prompt).strip()
        if ReturnType is None:
            return None
        try:
            return ReturnType(user)
        except (ValueError, TypeError, SyntaxError) as e:
            print(error if error else e)
            continue
