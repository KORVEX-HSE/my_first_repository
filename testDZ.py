def message_fib(s:str):
    if s == "" : 
      return 0 
    result = 1 
    count = 1 
    fib_1 = 1 
    fib_2 = 1 
    for i in range(len(s) - 1): 
      if (int(s[i ] + s[i + 1]) > 9 and int(s[i] + s[i + 1]) < 34): 
        count += 1 
        fib_2 += fib_1 
        fib_1 = fib_2 - fib_1 
      else: 
        result = result * fib_2 
        fib_1 = fib_2 = 1 
        count = 1 
    result = result * fib_2 
    return result


def fibonacci(n):
    if n <= 1:
       return n
    else:
       return fibonacci(n-1) + fibonacci(n-2)


def message(s: str):
    if s == '':
       return 0
    link = []
    chain = 1
    for i in range(len(s) -1):
        link.append(s[i])
        if s[i] == '0' or int(s[i] + s[i+1]) > 33:
            chain *= fibonacci(len(link)+1)
            link = []
    return chain


print(message_fib('123422552074321843'))
print(message('123422552074321843'))
print(fibonacci(2))