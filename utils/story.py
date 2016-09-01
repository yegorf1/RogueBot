
story = {}


def create_story(name, value=0):
	story = { name : value }
	return story


def get_story(name):
	value = story.get(name)
	return value


def update_story(name, value):
	if get_story(name) is None:
		create_story(name)
		story.update({name : value})
	else:
		story.update({name : value})


def reset_story(name):
	story.update({name : 0})


def clear_story():
	return story.clear()