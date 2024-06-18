f3 = open('input2.txt', 'r')
f4 = open('output2.txt', 'w')

count2 = f3.readline()
count2 = int(count2)

thlist1 = f3.readline().split(' ')

hlist1 = [0]*count2

for i in range(count2):
  hlist1[i] = int(thlist1[i])


jval = 0
jmax = 0
for j in range(1, count2+1):
  if j<count2:
    if jmax<(hlist1[j])**2:
      jmax = (hlist1[j]**2)
      jval = j

imax = hlist1[0]



for i in range(1,jval):


    if imax<hlist1[i-1]:

      imax = hlist1[i]



rslt = str(imax + jmax)
f4.write(rslt)

f3.close()
f4.close()
