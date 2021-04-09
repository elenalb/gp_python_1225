# psutil

import psutil

# системные вызовы, контекстные переключатели
print(psutil.cpu_stats())

# инфо о диске
print(psutil.disk_usage("C:"))

# инфо о состоянии памяти
print(psutil.virtual_memory())
