import shutil

f_obj1 = open("example")
f_obj2 = open("file_to_write", "w")

# # копирование
# shutil.copyfileobj(f_obj1, f_obj2)

# shutil.copyfile("example", "file_to_write")

# shutil.copy(source, destination)

# shutil.rmtree("path")
# shutil.move("source", "destination")

f_obj1.close()
f_obj2.close()
