import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(sys.argv[0], '..', '..')))
print(sys.path)
import usermanager
import config
from items import item_info

for i in os.listdir(config.USERS_PATH):
    if not i.endswith('.usr'):
        continue
    u = usermanager.get_user(i.rstrip('.usr'))
    items = u.items[:]
    u.items = []
    for item in items:
        if len(item) > 2:
            ctx = item[2]
        else:
            ctx = None
        u.add_item(item[0], item[1], context=ctx)
    usermanager.save_user(u)
    print(i, len(items), len(u.items))

