
import os.path


os.mkdir('Hello')
directory = "Hello"
filename = "file.txt"
file_path = os.path.join(directory, filename)
if not os.path.isdir(directory):
    os.mkdir(directory)
file = open(file_path, "w")
file.write("html")
file.close()