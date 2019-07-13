from random import randint
from .notation import transform


class Address:
	"""IPv4 addresses"""
	bits = 32

	def __init__(self, data):
		"""Создание интернет адреса."""
		assert(type(data) == int)
		self.data = data

	def __lt__(self, other):
		"""Сравнение двух адресов на меньше."""
		return int(self) < int(other)

	def __eq__(self, other):
		"""Сравнение двух адресов на равенство."""
		return int(self) == int(other)

	def __iter__(self):
		"""Перебор байтов интернет адреса."""
		for rank in [24, 16, 8, 0]:
			yield self.data >> rank & 0xff

	def __getitem__(self, key):
		"""Доступ к отдельному байту адреса по индексу.

		Индексы соответствуют разрядам адреса в 256-тиричной системе счисления."""
		assert(type(key) == int and 0 <= key <= 3)
		return self.data >> (8 * key) & 0xff

	def __int__(self):
		"""Представление интернет адреса в виде целого числа"""
		return self.data

	def __str__(self):
		"""Представление интернет адреса в виде строки"""
		return ".".join(map(str, self))

	def ones(self):
		"""Возвращает количество единиц в адресе."""
		return transform(self.data, 2).count('1')

	def zeros(self):
		"""Возвращает количество нулей в адресе."""
		return self.bits - self.ones()

	@property
	def randhost(self):
		"""Случайный адрес"""
		return randint(2**24, 2**32 - 2**24)


class HostAddress(Address):
	"""Адресс компьютера."""
	def __init__(self, address=None):
		"""Создание адреса компьютера."""
		if address is None:
			address = Address(self.randhost)
			while str(address).split(".").count('0') != 0:
				address = Address(self.randhost)
		super().__init__(int(address))

	def __and__(self, other):
		"""Побитовая коньюкнция."""
		assert(isinstance(other, Mask))
		if type(other) == NetworkMask:
			return NetworkAddress(int(self) & int(other))
		elif type(other) == HostMask:
			return Address(int(self) & int(other))

	def __rand__(self, other):
		"""Побитовая коньюкнция."""
		return self & other


class Mask(Address):
	"""Маска для интернет адреса."""
	def __init__(self, address):
		"""Создание маски."""
		super().__init__(address)


class NetworkMask(Mask):
	"""Маска подсети."""
	def __init__(self, ones=None):
		"""Создание маски подсети.

		В качестве необязательного параметра принимает количество единиц в маске.
		Если количество единиц не задаётся, оно выбирается случайно от 3 до 29 включительно."""
		if ones is None:
			ones = randint(3, 29)
		super().__init__(int('1' * ones + '0' * (self.bits - ones), 2))


class HostMask(Mask):
	"""Маска хоста в подсети."""
	def __init__(self, netmask):
		"""Создание маски хоста."""
		assert(type(netmask) == NetworkMask)
		super().__init__(int(netmask) ^ int('1' * Address.bits, 2))


class NetworkAddress(Address):
	"""Адрес подсети."""
	def __init__(self, address):
		"""Создание адреса подсети."""
		super().__init__(address)

	def __or__(self, other):
		"""Побитовая дизьюнкция."""
		assert(isinstance(other, Address))
		assert(int(self) & int(other) == 0)
		return HostAddress(int(self) | int(other))

	def __ror__(self, other):
		"""Побитовая дизьюнкция."""
		return self | other


class MaskedHostAddress(HostAddress):
	"""Адрес компьютера с маской подсети."""
	def __init__(self, address=None, mask=None):
		"""Создание адреса компьютера с маской подсети."""
		super().__init__(address)
		self.network_mask = NetworkMask(mask)

	def host(self):
		"""Возвращает адрес компьютера."""
		return self

	def hostmask(self):
		"""Возвращает маску компьютера в подсети."""
		return HostMask(self.network_mask)

	def netmask(self):
		"""Возвращает маску подсети."""
		return self.network_mask

	def network(self):
		"""Возвращает адрес подсети."""
		return self & self.network_mask

	def hostnumber(self):
		"""Возвращает номер по порядку компьютера в подсети."""
		return int(self & self.hostmask())

	def neighbor(self, number):
		"""Возвращает адрес соседнего компьютера в нашей подсети с номером по порядку number."""
		return self.network() | Address(number)

	def suitable(self):
		"""Возвращает список масок, которые подходят для данной пары хоста и подсети."""
		return [NetworkMask(m) for m in range(self.bits + 1) if self & NetworkMask(m) == self.network()]


class MaskedHostAddressDeterminate(MaskedHostAddress):
	"""Адрес компьютера с маской подсети, которую можно однозначно восстановить по адресу подсети."""
	def __init__(self):
		"""Создание адреса компьютера с определённой маской подсети."""
		super().__init__()
		self.data |= 3 << (self.network_mask.zeros() - 1)


class LimitMaskedHostAddressDeterminate(MaskedHostAddress):
	"""Адрес компьютера с маской подсети, которую можно однозначно восстановать по адресу подсети, и с ограничениями.

	Количество компьютеров в подсети данного хоста не может превышать 2**16."""
	def __init__(self, n_ones=None):
		"""Создание адреса компьютера с определённой и ограниченной маской подсети."""
		super().__init__()
		if n_ones is None:
			n_ones = randint(21, 29)
		self.network_mask = NetworkMask(n_ones)
		self.data |= 3 << (self.network_mask.zeros() - 1)
		

class LimitMaskedHostAddress(MaskedHostAddress):
	"""Адрес компьютера с маской подсети и с ограничениями.

	Количество компьютеров в подсети данного хоста не может превышать 2**16."""
	def __init__(self, n_ones=None):
		"""Создание адреса компьютера c ограниченной маской подсети."""
		super().__init__()
		if n_ones is None:
			n_ones = randint(21, 29)
		self.network_mask = NetworkMask(n_ones)
