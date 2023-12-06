import time

count = 1
start = time.time()
for i in range(1, 1000000):
   count += i
end = time.time()

print(end - start, count)