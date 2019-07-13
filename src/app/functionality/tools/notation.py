"""Вспомогательные инструменты для работы с числами в разных системах счисления."""


def transform(x, n, digits='0123456789abcdefghijklmnopqrstuvwxyz', based=False, width=0):
	"""Возвращает строковое представление числа x в системе счисления n.

	Необязательный параметр digits задаёт цифры, используемые для представления числа, по умолчанию используются арабские
	цифры и маленькие буквы латинского алфавита. Если необязательный параметр based равен True, то основание выходной
	системы счисления добавляется к результирующей строке через нижние подчёркивание, значение по умолчанию False.
	Если width больше, чем количество цифр, то выходная строка будет расширена до ширины width."""
	result = ''
	while x:
		result = digits[x % n] + result
		x //= n
	if not result:
		result += digits[0]
	if width and width > len(result):
		result = digits[0] * (width - len(result)) + result
	if based:
		#result += '_{' + str(n) + '}'
		result = f"{result}<sub>{str(n)}</sub>"
	return result.upper()


def minLimitedNumberStr(base, target, width, limit, digit, repeat):
	"""Функция возвращает строковое представление минимального числа,
	которое в системе счисления с основанием base**target имеет ровно width цифр
	и в системе счисления с основанием base**limit имеет ровно repeat цифр digit."""
	digit_source = transform(digit, base)
	digit_width = len(digit_source)
	if digit:
		assert width * target >= (repeat - 1) * limit + digit_width, "Insufficient width number: " + ' '.join(map(str, (base, target, width, limit, digit, repeat)))
		if (width - 1) * target < (repeat - 1) * limit + digit_width:
			return ('0' * (limit - digit_width) + digit_source) * repeat
		else:
			if base ** (target * (width - 1) % limit) == digit:
				repeat -= 1
			return '1' + ('0' * ((width - 1) * target - limit * repeat)) + ('0' * (limit - digit_width) + digit_source) * repeat
	else:
		assert width * target >= repeat * limit + 1, "Insufficient width number: " + ' '.join(map(str, (base, target, width, limit, digit, repeat)))
		if (width - 1) * target < repeat * limit:
			return '1' + '0' * limit * repeat
		else:
			return '1' + '0' * ((width - 1) * target % limit + limit * repeat) + ('0' * (limit - 1) + '1') * ((width - 1) * target // limit - repeat)


def maxLimitedNumberStr(base, target, width, limit, digit, repeat):
	"""Функция возвращает строковое представление максимального числа,
	которое в системе счисления с основанием base**target имеет ровно width цифр
	и в системе счисления с основанием base**limit имеет ровно repeat цифр digit."""
	digit_source = transform(digit, base)
	digit_width = len(digit_source)
	big_digit = base ** limit - 1
	big_digit_source = transform(big_digit, base)
	big_base_digit_source = transform(base - 1, base)
	tail = width * target % limit
	if digit and digit != big_digit:
		assert width * target >= (repeat - 1) * limit + digit_width, "Insufficient width number: " + ' '.join(map(str, (base, target, width, limit, digit, repeat)))
		if width * target // limit < repeat:
			return ('0' * (limit - digit_width) + digit_source) * repeat
		else:
			if base ** tail - 1 == digit:
				repeat -= 1
			return big_base_digit_source * (tail + (width * target // limit - repeat) * limit) + ('0' * (limit - digit_width) + digit_source) * repeat
	elif digit == big_digit:
		prev_source = transform(big_digit - 1, base)
		prev_width = len(prev_source)
		assert width * target >= (repeat - 1) * limit + digit_width, "Insufficient width number: " + ' '.join(map(str, (base, target, width, limit, digit, repeat)))
		if width * target // limit < repeat:
			return ('0' * (limit - digit_width) + digit_source) * repeat
		else:
			if base ** tail - 1 == digit:
				repeat -= 1
			return big_base_digit_source * tail + ('0' * (limit - digit_width) + digit_source) * repeat + ('0' * (limit - prev_width) + prev_source) * (width * target // limit - repeat)
	else:
		assert width * target >= repeat * limit + 1, "Insufficient width number: " + ' '.join(map(str, (base, target, width, limit, digit, repeat)))
		return big_base_digit_source * (width * target - repeat * limit) + '0' * repeat * limit


def minLimitedNumber(base, target, width, limit, digit, repeat):
	"""Функция возвращает минимальное число,
	которое в системе счисления с основанием base**target имеет ровно width цифр
	и в системе счисления с основанием base**limit имеет ровно repeat цифр digit."""
	return int(minLimitedNumberStr(base, target, width, limit, digit, repeat), base)


def maxLimitedNumber(base, target, width, limit, digit, repeat):
	"""Функция возвращает максимальное число,
	которое в системе счисления с основанием base**target имеет ровно width цифр
	и в системе счисления с основанием base**limit имеет ровно repeat цифр digit."""
	return int(maxLimitedNumberStr(base, target, width, limit, digit, repeat), base)

