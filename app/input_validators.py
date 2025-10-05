def parse_two_floats(tokens):
    # Expect: [cmd, a, b]
    if len(tokens) < 3:
        raise ValueError("Need two numbers")
    try:
        a = float(tokens[1]); b = float(tokens[2])
    except ValueError as e:
        raise ValueError("Inputs must be numbers") from e
    return a, b
