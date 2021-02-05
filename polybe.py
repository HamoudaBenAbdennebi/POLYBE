

def saisiecle():
    x = input('donner le mot clee :').upper()
    while not (3 <= len(x) <= 10) or (not x.isalpha()):
        x = input('donner le mot clee :').upper()
    return(x)


def verif(c):
    v = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    for i in range(len(c)):
        if not(c[i] in v):
            return True
    return False


def remp(x):
    alph = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
    for i in range(len(alph)):
        if not(alph[i] in x):
            x += alph[i]
    m = [[x[i] for i in range(j*5, j*5+5)]for j in range(5)]
    for i in m:
        print(i)
    return(m)


def saisiemsg():
    c = input('donner le messgae a crypter: ').upper()
    while (len(c) < 0) or verif(c):
        c = input('donner le messgae a crypter: ').upper()
    return c


def lookfor(m, c):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if (m[i][j] == c):
                return (str(i+1)+str(j+1))


def cryptage():
    cv = ""
    for i in range(len(msg)):
        if (msg[i] == " "):
            cv += "_"
        elif (msg[i] == "W"):
            cv += lookfor(m, "V")
        else:
            cv += lookfor(m, msg[i])
    print(cv)


# pp
cle = saisiecle()
m = remp(cle)
msg = saisiemsg()
cryptage()
