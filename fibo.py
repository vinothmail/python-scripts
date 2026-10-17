a, b, c = 0, 1, 0

for i in range(5):
   c = a + b
   print(f"{a} + {b} = {c}")
   a = b
   b = c
    