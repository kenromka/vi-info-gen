from functools import reduce
from random import randint, choice, shuffle


def positive(x, count, limit):
	"""Возможные количества положительных слагаемых при разложении числа x ровно на count ненулевых слагаемых,
	каждое из которых по модулю не больше limit."""
	assert(count > 0)
	assert(limit > 0)
	return set((k for k in range(1, count) if (k*limit + k - count - x) * (k - count*limit + k*limit - x) <= 0))


def minimum_count_pos_terms(s, limit):
	"""Возвращает минимальное количество слагаемых, на которые можно разбить каждое число из списка s так,
	чтобы количество положительных слагаемых у всех чисел было одинаковым."""
	count = 1
	assert limit > 1 or sum(x % 2 for x in s) in [0, len(s)], "Такие числа невозможно выровнять по слагаемым"
	while not reduce(lambda x, y: x & y, [positive(x, count, limit) for x in s]):
		count += 1
	return count


def positive_edge(x, pos, neg, limit):
	"""Определяет минимальную и максимальную сумму pos положительных слагаемых,
	которая вместе с neg отрицительными слагаемыми даёт x."""
	min_x = max(x + neg, pos)
	max_x = min(x + neg*limit, limit*pos)
	return min_x, max_x


def single_decompose(x, k, limit):
	"""Разбивает число x на k положительных слагаемых, каждое из которых не больше limit по модулю."""
	r = [x // k + 1 for _ in range(x % k)] + [x // k for _ in range(x % k, k)]
	shuffle(r)
	for _ in range(randint(2*k, 10*k)):
		i = randint(0, k - 1)
		j = randint(0, k - 1)
		if i != j and r[i] < limit - 1 and r[j] > 1:
			r[i] += 1
			r[j] -= 1
	return r


def binary_decompose(x, pos, neg, limit):
	"""Разбивает число x на pos положительных и neg отрицательных слагаемых, каждое из них не больше limit по модулю."""
	x_pos = randint(*positive_edge(x, pos, neg, limit))
	x_neg = x_pos - x
	return single_decompose(x_pos, pos, limit), single_decompose(x_neg, neg, limit)


def decompose(s, limit):
	"""Разбивает каждое число из списка чисел s на минимальное одинаковое количество слагаемые разных знаков так,
	чтобы количество слагаемых одинаковых знаков было равным для каждого числа из s."""
	count = minimum_count_pos_terms(s, limit)
	pos_count = choice(list(reduce(lambda x, y: x & y, [positive(x, count, limit) for x in s])))
	return [binary_decompose(x, pos_count, count - pos_count, limit) for x in s]


def signed_decompose(s, limit):
	"""Разбивает каждое число из списка чисел s на минимальное одинаковое количество слагаемые разных знаков так,
	чтобы количество слагаемых одинаковых знаков было равным для каждого числа из s."""
	left, right = [x for x in s if x >= 0], [-x for x in s if x < 0]
	count = max(minimum_count_pos_terms(left, limit), minimum_count_pos_terms(right, limit))
	pos_left = reduce(lambda x, y: x & y, [positive(x, count, limit) for x in left])
	pos_right = reduce(lambda x, y: x & y, [positive(x, count, limit) for x in right])
	while count < min(pos_left) + min(pos_right):
		count += 1
		pos_left = reduce(lambda x, y: x & y, [positive(x, count, limit) for x in left])
		pos_right = reduce(lambda x, y: x & y, [positive(x, count, limit) for x in right])
	res = []
	pos_left = min(pos_left)
	pos_right = count - pos_left
	for x in s:
		a = pos_left if x >= 0 else pos_right
		b = count - a
		y = binary_decompose(abs(x), a, b, limit)
		res.append(y[::1 if x >=0 else -1])
	return res
