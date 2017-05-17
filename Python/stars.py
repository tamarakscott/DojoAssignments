x = [4, 6, 1, 3, 5, 7, 25]

def draw_stars():
    for element in x:
        if isinstance(x, int):
            print "*" * x
        elif isinstance(x, str):
            length = len(x)
            letter = x[0].lower()
            print letter * length
