#!/usr/bin/env python2

def write(companyName, formatValue, newname, filename):
    with open(filename, 'a') as f:
        f.write(newname+"\n")

def mangleOne(first_name, last_name, companyName, formatValue, domain, filename):
    newname=first_name + last_name
    if domain != '':
        newname = newname+"@"+domain
        write(companyName, formatValue, newname, filename)
    else:
        write(companyName, formatValue, newname, filename)
    return newname

def mangleTwo(first_name, last_name, companyName, formatValue, domain, filename):
    newname = last_name + first_name
    if domain != '':
        newname = newname+"@"+domain
        write(companyName, formatValue, newname, filename)
    else:
        write(companyName, formatValue, newname, filename)
    return newname

def mangleThree(first_name, last_name, companyName, formatValue, domain, filename):
    newname = first_name + "." + last_name
    if domain != '':
        newname = newname+"@"+domain
        write(companyName, formatValue, newname, filename)
    else:
        write(companyName, formatValue, newname, filename)
    return newname


def mangleFour(first_name, last_name, companyName, formatValue, domain, filename):
    newname = last_name + "." + first_name
    if domain != '':
        newname = newname+"@"+domain
        write(companyName, formatValue, newname, filename)
    else:
        write(companyName, formatValue, newname, filename)
    return newname

def mangleFive(first_name, last_name, companyName, formatValue, domain, filename):
    newname = first_name + "_" + last_name
    if domain != '':
        newname = newname+"@"+domain
        write(companyName, formatValue, newname, filename)
    else:
        write(companyName, formatValue, newname, filename)
    return newname

def mangleSix(first_name, last_name, companyName, formatValue, domain, filename):
    newname = last_name + "_" + first_name
    if domain != '':
        newname = newname+"@"+domain
        write(companyName, formatValue, newname, filename)
    else:
        write(companyName, formatValue, newname, filename)
    return newname


def mangleSeven(first_name, last_name, companyName, formatValue, domain, filename):
    newname = first_name[0] + last_name
    if domain != '':
        newname = newname+"@"+domain
        write(companyName, formatValue, newname, filename)
    else:
        write(companyName, formatValue, newname, filename)
    return newname

def mangleEight(first_name, last_name, companyName, formatValue, domain, filename):
    newname = last_name[0] + first_name
    if domain != '':
        newname = newname+"@"+domain
        write(companyName, formatValue, newname, filename)
    else:
        write(companyName, formatValue, newname, filename)
    return newname

def mangleNine(first_name, last_name, companyName, formatValue, domain, filename):
    newname = first_name + last_name[0]
    if domain != '':
        newname = newname+"@"+domain
        write(companyName, formatValue, newname, filename)
    else:
        write(companyName, formatValue, newname, filename)
    return newname


def mangleTen(first_name, last_name, companyName, formatValue, domain, filename):
    newname = first_name[0] + "." + last_name
    if domain != '':
        newname = newname+"@"+domain
        write(companyName, formatValue, newname, filename)
    else:
        write(companyName, formatValue, newname, filename)
    return newname

def mangleEleven(first_name, last_name, companyName, formatValue, domain, filename):
    newname = last_name[0] + "." + first_name
    if domain != '':
        newname = newname+"@"+domain
        write(companyName, formatValue, newname, filename)
    else:
        write(companyName, formatValue, newname, filename)
    return newname

def mangleTwelve(first_name, last_name, companyName, formatValue, domain, filename):
    newname = last_name[0:3] + first_name[0:2]
    if domain != '':
        newname = newname+"@"+domain
        write(companyName, formatValue, newname, filename)
    else:
        write(companyName, formatValue, newname, filename)
    return newname


def mangleThirteen(first_name, last_name, companyName, formatValue, domain, filename):
    newname = last_name[0:4] + first_name[0:3]
    if domain != '':
        newname = newname+"@"+domain
        write(companyName, formatValue, newname, filename)
    else:
        write(companyName, formatValue, newname, filename)
    return newname

def mangleFourteen(first_name, last_name, companyName, formatValue, domain, filename):
    newname = first_name[0] + last_name[0:7]
    if domain != '':
        newname = newname+"@"+domain
        write(companyName, formatValue, newname, filename)
    else:
        write(companyName, formatValue, newname, filename)
    return newname

def mangleFifteen(first_name, last_name, companyName, formatValue, domain, filename):
    newname = last_name + first_name[0]
    if domain != '':
        newname = newname+"@"+domain
        write(companyName, formatValue, newname, filename)
    else:
        write(companyName, formatValue, newname, filename)
    return newname

def mangleSixteen(first_name, last_name, companyName, formatValue, domain, filename):
    newname = last_name[0:3] + first_name[0:2]
    if domain != '':
        newname = newname+"@"+domain
        write(companyName, formatValue, newname, filename)
    else:
        write(companyName, formatValue, newname, filename)
    return newname

def mangleAll(first_name, last_name, companyName, formatValue, domain, filename):
    newname = mangleOne(first_name, last_name, companyName, formatValue, domain, filename)
    print(newname)
    newname = mangleTwo(first_name, last_name, companyName, formatValue, domain, filename)
    print(newname)
    newname = mangleThree(first_name, last_name, companyName, formatValue, domain, filename)
    print(newname)
    newname = mangleFour(first_name, last_name, companyName, formatValue, domain, filename)
    print(newname)
    newname = mangleFive(first_name, last_name, companyName, formatValue, domain, filename)
    print(newname)
    newname = mangleSix(first_name, last_name, companyName, formatValue, domain, filename)
    print(newname)
    newname = mangleSeven(first_name, last_name, companyName, formatValue, domain, filename)
    print(newname)
    newname = mangleEight(first_name, last_name, companyName, formatValue, domain, filename)
    print(newname)
    newname = mangleNine(first_name, last_name, companyName, formatValue, domain, filename)
    print(newname)
    newname = mangleTen(first_name, last_name, companyName, formatValue, domain, filename)
    print(newname)
    newname = mangleEleven(first_name, last_name, companyName, formatValue, domain, filename)
    print(newname)
    newname = mangleTwelve(first_name, last_name, companyName, formatValue, domain, filename)
    print(newname)
    newname = mangleThirteen(first_name, last_name, companyName, formatValue, domain, filename)
    print(newname)
    newname = mangleFourteen(first_name, last_name, companyName, formatValue, domain, filename)
    print(newname)
    newname = mangleFifteen(first_name, last_name, companyName, formatValue, domain, filename)
    print(newname)
    newname = mangleSixteen(first_name, last_name, companyName, formatValue, domain, filename)
    print(newname)

if __name__ == '__main__':
    pass
