# импорты
# стандартная библиотека
import time
import random

print(time.time())
print(random.random())

# все импорты должны быть в первых строках - сверху!
from time import time
from random import random

print(time())
print(random())

import custom_module
custom_module.print_message("Hello!")

from custom_module import simple_calc
print(simple_calc())

# rename module
import random as rd
print(rd.random())
