from itertools import izip, chain, repeat

from grid.models import Grid


def grouper(n, iterable, padvalue=None):
    "grouper(3, 'abcdefg', 'x') --> ('a','b','c'), ('d','e','f'), ('g','x','x')"
    return izip(*[chain(iterable, repeat(padvalue, n-1))]*n)


def grid_headers(request):
    grid_headers = list(Grid.objects.filter(header=True))[:30]
    grid_headers = grouper(8, grid_headers)
    return {'grid_headers': grid_headers}
