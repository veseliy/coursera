# print(list(filter(lambda x: x>2,[1,2,3,4])))


class multifilter():
    def judge_half(pos, neg):
        if pos>=neg:
            return True
        else:
            return False
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)

    def judge_any(pos, neg):
        if pos>=1:
            return True
        else:
            return False
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)

    def judge_all(pos, neg):
        if neg==0:
            return True
        else:
            return False
        # допускает элемент, если его допускают все функции (neg == 0)


    def __init__(self, iterable, *funcs, judge=judge_any):
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция
        self.iterable=iterable
        self.funcs=funcs
        self.judge=judge

    def __iter__(self):
        return self

        # возвращает итератор по результирующей последовательности


a = [i for i in range(31)] # [0, 1, 2, ... , 30]

def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0

print(list(multifilter(a, mul2, mul3, mul5)))


