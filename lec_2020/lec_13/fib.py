def fib(n):
    """
    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(3)
    2
    >>> fib(5)
    5
    >>> fib(-5)
    'Error'
    """
    if n < 0:
        return 'Error'
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
