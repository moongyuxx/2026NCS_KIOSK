import time
#디자인 패턴 -> 데코레이터 원칙

def time_measure_decorator(f):
    # 데코레이터 패턴
    def wrapper(*args):
        s = time.time()
        r = f(*args)
        e = time.time()
        print(f"time : {e-s}")
        return r
    return wrapper

@time_measure_decorator
def one_to_n_loop(n): #반복문으로 직접 더함
    result = 0
    for i in range(1, n+1):
        result = result + i
    return result


def one_to_n_math(n): #수학 공식 사용
    r = n * (n + 1) // 2
    return r


number = int(input("Input number : "))
func = time_measure_decorator(one_to_n_math)
print(func(number))
print(one_to_n_loop(number))