from pandas.core.common import flatten
from decorator import logger_with_path

NESTED_LIST = [
	['a', 'b', 'c', [1, 2, 3, [3, 4]]],
	['d', 'e', 'f', 'h', False],
	[1, 2, None]
]

@logger_with_path(r'E:\\')
def flat_generator(lis):
	flatted = list(flatten(lis))
	k = 0
	while k < len(flatted):
		yield flatted[k]
		k += 1


if __name__ == '__main__':
	flat_generator(NESTED_LIST)