a, b, c = map(int, input().split())

if a == b:
  if b == c:
    print(10000+a*1000)
  else:
    print(1000+a*100)

elif b == c:
  print(1000+b*100)

elif c == a:
  print(1000+c*100)

else:
  if a>b:
    max = a
    if c>max:
      max = c
  else:
    max = b
    if c>max:
      max = c
  print(max*100)