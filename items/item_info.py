class item_info(object):
	def __init__(self, group, name, context=None, count=1):
		self.group = group
		self.name = name
		self.context = context
		self.count = count

	@property
	def count(self):
		return self._count

	@count.setter
	def count(self, value):
		if value <= 0:
			logger.warn('{}.count <= 0 ({})'.format(repr(self), value))
		if not self.is_simple() and value != 1:
			logger.warn('{}.count != 0 ({}) and item is not simple'.format(repr(self), value))
		self._count = value

	def is_simple(self):
		return self.context is None or len(self.context) == 0

	def __repr__(self):
		return "<item {g}/{n} x {cnt}{ctx}".format(
			g=self.group,
			n=self.name,
			cnt=self.count,
			ctx='' if self.is_simple() else ' ' + repr(self.context)
		)

