def addBreaker(func):
    def inner(*args, **kwargs):
        Breaker = '\n{:-^50}'
        print(Breaker.format(''))
        func(*args, **kwargs)

    return inner


def get_root_path(path: str, n: int) -> str:
    """return path of root directory of a given *path*
    Args:
        path (str): path of a file
        n (int): layers inside of root path. 0 means in same layer, n means n-depth in root directory

    Raises:
        ValueError: n must be positive or 0

    Returns:
        str: path of root directory

    note: if using this function as pkg, u would get fucked. if not using this function directly, then it's silly as hell
    """
    import os
    if n < 0:
        raise ValueError('n must be >= 0')
    if n == 0:
        return os.path.dirname(path)
    else:
        return get_root_path(os.path.dirname(path), n - 1)
