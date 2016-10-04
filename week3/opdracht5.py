try:
 st = 10 * [0]
 x = st[9]
 print("Done ")
except IndexError:
 print("Index out of bound")
else:
 print("Nothing is wrong")
finally:
 print("Finally we are here")
print("Continue")
print(st)