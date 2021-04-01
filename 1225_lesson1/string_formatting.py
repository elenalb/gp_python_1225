# %
name = "Lena"
print("My name %s" % name)
print("%-10s %-10s %-10s" % ('param1', 'param2', 'param3'))
print("%.2f" % (20. / 8))
# %d, %f, %o, %x

# format()
print("My name {}".format(name))
print("{:>20} {:>20} {:>20}".format('param1', 'param2', 'param3'))
print("{:.2f}".format(9./7))

# f-string !!
print(f"My name {name}")
print(f"{1 + 2}")
print(f"{'param1':>10} {'param2':<10} {'param3':<10}")
