## All required functions
def newclient(n):
    fr = n + "1.txt"
    er = n + "2.txt"
    try:
        f = open(fr, "xt")
        f.close()
        f = open(er, "xt")
        f.close()
    except Exception as e:
        print("Name Already exists in Database")

def hmsdb_update(n, up):
    f = open(n, "a")
    f.write(up)
    f.close()

def hmsdb_print(n):
    f = open(n)
    con = f.read()
    print(con)
    f.close()

def getdate():
    import datetime
    return datetime.datetime.now()

def getclient():
    n = input("Enter client name:")
    return n

##global
cl = []

while(1):
    Menu = int(input("******Menu******\n 1.New Client\n 2.Client List\n 3.UpdateData\n 4.exit\nYour choice:"))

    if Menu == 1:
        name = input("Enter the client Name:")
        newclient(name)
        cl.append(name)
    elif Menu == 2:
        print(cl)
    elif Menu == 3:
        w = int(input("Select:\n 1. Lock\n 2. Retrieve\n Enter your choice:"))
        if w == 1:
            name = getclient()
            dt = getdate()
            update = ""
            l1 = int(input("Select:\n 1.Food\n 2.Exercise\n Enter your choice:"))
            if l1 == 1:
                name = name + "1.txt"
                up = input("enter the food eaten:")
            else:
                name = name + "2.txt"
                up = input("Enter the Exercise done:")
            update = str(dt) + " " + up + "\n"
            hmsdb_update(name, update)
        else:
            name = getclient()
            l1 = int(input("Select:\n 1.Food\n 2.Exercise\n Enter your choice:"))
            if l1 == 1:
                name = name + "1.txt"
            else:
                name = name + "2.txt"
            hmsdb_print(name)
    elif Menu == 4:
        break
