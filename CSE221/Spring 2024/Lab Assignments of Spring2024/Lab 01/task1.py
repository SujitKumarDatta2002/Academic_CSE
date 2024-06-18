inp = open("F:\Academic\CSE221\Lab Assignments of Spring2024\Lab 01\input1.txt", "r")
out = open("F:\Academic\CSE221\Lab Assignments of Spring2024\Lab 01\output1.txt", "w")
test = int(inp.readline())

i = 0
while(i<test):
  n = int(inp.readline())
  if n%2==0:
    res = f"{n} is Even\n"
  else:
    res = f"{n} is odd\n"

  out.write(res)
  i+=1

out.close()
inp.close()