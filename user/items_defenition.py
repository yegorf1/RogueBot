import items.itemloader as itemloader
from items.item_info import item_info

def _remove_item(item, ind, count=1):
	'''
	Removes count of item.
	If this item completely removed (count <= 0), returns ind. Otherwise returns -1
	'''
	if item.is_simple():
		new_count = item.count - count
		if new_count <= 0:
			return ind
		else:
			item.count = new_count
	else:
		return ind
	return -1

def _find_item_by_name(items, name):
	for i, item in enumerate(items):
		if item.name == name:
			return i, item

	return None

def _remove_item_by_name(info, items, name):
	'''
	Searches for item with given name (not code_name) and removes it.
	info -- source of item_infos
	items -- source of loaded items
	'''
	found = _find_item_by_name(items, name)
	if found is None:
		return False
	ind, item = found
	ind = _remove_item(info[ind], ind)
	if ind >= 0 and items[ind] and not items[ind].iscursed:
		del items[ind]
	return True

def remove_item(self, code_name, count=1):
	ind = -1
	for idx, i in enumerate(self.items):
		if i.name == code_name:
			ind = _remove_item(i, idx, count=count)
			break
	if ind >= 0:
		del self.items[ind]

def remove_items_with_tag(self, tag):
	items = self.get_items()
	active_items = self.get_active_items()

	new_items = [ item_info(i.buff, i.code_name) for i in items if tag not in i.tags ]
	new_active_items = [ item_info(i.buff, i.code_name) for i in active_items if tag not in i.tags ]

	self.items = new_items
	self.active_items = new_items

def deactivate_item_by_name(self, name):
	items = self.get_active_items()
	# return _remove_item_by_name(self.active_items, items, name)
	return _remove_item_by_name(self.items, items, name)

def remove_item_by_name(self, name):
	items = self.get_items()
	return _remove_item_by_name(self.items, items, name)

def get_item_by_name(self, name):
	items = self.get_items()
	found = _find_item_by_name(items, name)
	if found is not None:
		return found[1]
	return None

def get_active_item_by_name(self, name):
	items = self.get_active_items()
	found = _find_item_by_name(items, name)
	if found is not None:
		return found[1]
	return None

def get_items(self):
	def load_item(i):
		ctx = i.context if i.context is not None else {}
		return itemloader.load_item(i.name, i.group, ctx, self, count=i.count)

	return [ i for i in [ load_item(i) for i in self.items ] if i is not None ]

def iterate_over_items(self):
	for i in self.get_items():
		for j in range(i.count):
			yield i

def get_active_items(self):
	return self.get_items()

def get_counted_items(self):
	items = self.get_active_items()
	result = []
	for i in items:
		result.append((i, i.count))
	return result

def get_active_slots_len(self):
	return 10 + self.rooms_count // 15

def has_item(self, code_name):
	for i in self.items:
		if i.name == code_name:
			return True

	return False

def add_item(self, buff, name, context={}, count=1):
	if len(context) != 0:
		self.items.append(item_info(buff, name, context))
	for i in self.items:
		if i.name == name and i.group == buff and i.is_simple():
			i.count += count
			break
	else:
		self.items.append(item_info(buff, name, context))

