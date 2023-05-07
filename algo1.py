import time
import sys
execution_times = []
def dynamic_fib(n):
    fib_list = [0, 1]
    if n <= 1:
        return fib_list[n]
    else:
        for i in range(2, n+1):
            fib_list.append(fib_list[i-1] + fib_list[i-2])
        return fib_list[n]
    

limit = sys.getrecursionlimit()
print('==============for dynamic_fib================')
print(limit)
print(dynamic_fib(limit))
for n in range(10,110,10):
    start_time = time.time()
    result = dynamic_fib(n)
    end_time = time.time()
    execution_time = end_time - start_time
    execution_times.append(execution_time)
    print(f"n={n}, result={result}, execution_time={execution_time:.10f} seconds")

print('==============for dynamic_fib n == 51================')
n = 51
start_time = time.time()
result = dynamic_fib(n)
end_time = time.time()
execution_time = end_time - start_time
execution_times.append(execution_time)
print(f"n={n}, result={result}, execution_time={execution_time:.10f} seconds")



#plt.plot([10, 20, 30, 40,50,60,70,80,90,100], execution_times, 'o-')
# plt.xlabel('n')
# plt.ylabel('Execution time (seconds)')
# plt.show()