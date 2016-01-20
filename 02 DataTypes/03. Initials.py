userName = input("Input your name please.")
titles = ["Dr.", "Mr.", "Mrs.", "Eng.", "Др.", "Г-н", "Г-жа", "Инж."]

separateNames = userName.split(' ')
for name in separateNames:
    if name in titles:
        print(name + ' ', end='')
    else:
        print(name[0] + '.', end='')