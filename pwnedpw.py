#!/usr/bin/python3
import getpass
import hashlib
import requests



def num_leaks(pwd):
    sha1 = hashlib.sha1(pwd.encode('utf8')).hexdigest().upper()
    hashprefix = sha1[0:5]
    hashsuffix = sha1[5:]

    r = requests.get('https://api.pwnedpasswords.com/range/' + hashprefix)
    lines = r.text.split('\n')


    for line in lines:
        current_hash, counts = line.split(":")
        if hashsuffix == current_hash:
            return int(counts[0:-1])
    return 0
if __name__ == "__main__":

    pwd = getpass.getpass("password: ")
    leaks = num_leaks(pwd)
    if leaks == 0:
        print("your password has not been leaked.")
    elif leaks == 1:
        print("Your password has been leaked one time".format(leaks))
    elif leaks > 1:
        print("Your password has been leaked {} times".format(leaks))
    else:
        print("Error this should not happen")


