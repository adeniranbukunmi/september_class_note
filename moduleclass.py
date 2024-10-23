""" module is a file that contain python code. A module should contain similar function and class. we have python library that provides us with numerous module and all we need to do is to import and nt install or download."""

import random
import folder1.myfirst_moduleclass as myfirst_moduleclass
from folder1.myfirst_moduleclass import register as Rg

list_itm=["Temi","Taiwo","Excel", "Tikristi"]
leader=random.choice(list_itm)
print(leader)

print(myfirst_moduleclass.home())
# print(Rg())
