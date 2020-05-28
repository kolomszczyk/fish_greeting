# żeby działoło przy właczeni fish-shell
# zapisujemy ~/.config/fish/functions/
# plik o nazwie fish_greeting.fish
# w pliku:
# function fish_greeting
# 	# print funny ascii picture
# 	python3 `ten skrypt`
# end




import os
try:
    # folder z ascii zdjeciami
    sourse = "/home/klomszczyk/Aplication/fish_greeting/asci-picures/"

    # chose random picture

    from os import walk
    f = []
    len = 0
    for (dirpath, dirnames, filenames) in walk(sourse):
        f.extend(filenames)
        break
    for i in f:
        len = len + 1

    import random

    pictureLocalization = sourse + f[random.randint(0, len) -1]

    picture = open(pictureLocalization , 'r')

    # print this
    howManyLine = 0
    for i in picture:
        print(i, end="")
        howManyLine += 1

    strRows, strColumns = os.popen('stty size', 'r').read().split()

    rows = int(strRows)


    while(howManyLine + 1 < rows):
        print()
        howManyLine += 1




    #print(picture.read())



    input("Press any buton")
except Exception as e:
    print(e)


finally:
    os.system("clear")
