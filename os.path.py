import os.path
import datetime
n1 = input("Donne le nom d'un fichier : ")
state = os.stat(n1)
n1t = datetime.datetime.fromtimestamp(os.path.getatime(n1))

n2 = input("Donne le nom d'un fichier : ")
state = os.stat(n2)
n2t = datetime.datetime.fromtimestamp(os.path.getatime(n2))

if n2t > n1t :
    print(os.path.exists(n2), state.st_size, "octet")
    print(datetime.datetime.fromtimestamp(os.path.getatime(n2)))
    print(os.path.exists(n1), state.st_size, "octet")
    print(datetime.datetime.fromtimestamp(os.path.getatime(n1)))
else:
    print(os.path.exists(n1), state.st_size, "octet")
    print(datetime.datetime.fromtimestamp(os.path.getatime(n1)))
    print(os.path.exists(n2), state.st_size, "octet")
    print(datetime.datetime.fromtimestamp(os.path.getatime(n2)))