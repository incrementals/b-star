# TODO: (Rename argument) Not necessarily just numbers, but also strings, etc.
def add(number: any, *bys: tuple[any]):
    result = number

    for num in bys:
        result += num
    return result
