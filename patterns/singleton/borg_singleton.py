class Borg:
	_shared_state = {}

	def __init__(self):
		self.__dict__ = self._shared_state


class Singleton(Borg):

	def __init__(self):
		Borg.__init__(self)

	def __init__(self, **kwargs):
		Borg.__init__(self)
		self.update(**kwargs)

	def update(self, **kwargs):
		self._shared_state.update(kwargs)

	def flush(self):
		self._shared_state = {}

	def __str__(self):
		return str(self._shared_state)


print("init monostate s1,s2: `s1 = Singleton()`, `s2 = Singleton()`")
s1 = Singleton()
s2 = Singleton()

print(f"s1 is s2: {s1 is s2}")
print(f"type(s1): {type(s1)}")
print(f"type(s2): {type(s2)}")
print()

print(f"s1._shared_state: {s1}")
print(f"s2._shared_state: {s2}")
print()

s1.update(key=1)
print("updated s1: `s1.update(key=1)`")
print(f"s1._shared_state: {s1}")
print(f"s2._shared_state: {s2}")
print()

print("flushing monostate: `s1.flush()`")
s1.flush()
print()

s3 = Singleton(key1=1)
print("init monostate s3: `s3 = Singleton(key1=1)`")
print(f"s3._shared_state: {s3}")
print()

s4 = Singleton(key2=2)
print("init monostate s4: `s4 = Singleton(key2=2)`")
print(f"s3._shared_state: {s3}")
print(f"s4._shared_state: {s4}")
print()
