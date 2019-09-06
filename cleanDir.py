import os

#removes all text files from directory

try:
    os.remove("sec.txt")
finally:
    for i in range(1, 100000, 1):
        name = "to" + str(i) + ".html"
        try:
            print(name)
            f = open(name, 'r')
            f.close()
            os.remove(name)
        except FileNotFoundError:
            print("done")
            break
print("donezo")

