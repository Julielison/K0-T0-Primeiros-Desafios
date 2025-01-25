def fibonacci(prev, current):
  return prev + current

prev = 1
current = 2
sum = 0

while current <= 4_000_000:
  if current % 2 == 0:
    sum += current

  next = fibonacci(prev, current)
  prev = current
  current = next

print(sum)
