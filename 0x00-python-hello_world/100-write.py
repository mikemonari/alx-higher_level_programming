#!/usr/bin/python3
f = open("new.txt", "w")
f.write("and that piece of art is useful - Dora Korpar, 2015-10-19")
f = open("new.txt", "r")
print(f.read())
f.close()
