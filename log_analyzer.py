file = open("app.log", "r")

content = file.readlines()

for line in content:
    if "ERROR" in line:
        print(line)

file.close()