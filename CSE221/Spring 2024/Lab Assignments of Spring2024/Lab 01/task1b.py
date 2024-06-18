inp = open("F:\Academic\CSE221\Lab Assignments of Spring2024\Lab 01\input1b.txt", "r")
out = open("F:\Academic\CSE221\Lab Assignments of Spring2024\Lab 01\output1b.txt", "w")
test = int(inp.readline())

i = 0
while(i<test):
  st = inp.readline().split()
  if "+" in st:
    res = f"The result of {st[1]} {st[2]} {st[3]} is {int(st[1]) + int(st[3])}\n"
  if "-" in st:
    res = f"The result of {st[1]} {st[2]} {st[3]} is {int(st[1]) - int(st[3])}\n"
  if "*" in st:
    res = f"The result of {st[1]} {st[2]} {st[3]} is {int(st[1]) * int(st[3])}\n"
  if "/" in st:
    res = f"The result of {st[1]} {st[2]} {st[3]} is {int(st[1]) / int(st[3])}\n"

  out.write(res)
  i += 1

out.close()
inp.close()
