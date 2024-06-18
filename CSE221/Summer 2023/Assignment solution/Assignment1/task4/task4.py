fi4 =  open('input4.txt', 'r')
fo4 = open('output4.txt', 'w')
N = fi4.readline()

N = int(N)
texts = ['']*N
for i in range(N):
  texts[i] = fi4.readline().strip()

for i in range(len(texts)):

  for j in range(0, len(texts) - i - 1):

    txt1 = texts[j].split(' ')
    txt2 = texts[j + 1].split(' ')

    if (txt1[0] > txt2[0]):

      texts[j], texts[j+1] = texts[j+1], texts[j]

    elif txt1[0] == txt2[0] and txt1[-1] < txt2[-1]:
      tmp = texts[j]
      texts[j] = texts[j+1]
      texts[j+1] = tmp


for line in texts:
  fo4.write(line + "\n")
fi4.close()
fo4.close()
