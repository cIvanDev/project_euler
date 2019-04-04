class Fibo():

    def __init__(self):
        self.fibo = {}

    def calculate(self,n):
        if n == 1:
            return 1
        elif n == 2:
            return 2

        # return fibo[n] if n in self.fibo.values()
        if n in self.fibo.keys(): return self.fibo[n]

        self.fibo[1] = 1
        self.fibo[2] = 2

        value = 0
        for i in range(3, n+1):
            value = self.calculate(i-1) + self.calculate(i-2)
            self.fibo[i] = value

        return value

    def sum_even(self):
        # result = filter(lambda x: x%2 == 0, list( self.fibo.values() ))
        # print( result )
        result = 0
        for number in self.fibo.values():
            if number % 2 == 0:
                result+=number

        return result



fibo = Fibo()
fibo.calculate(4000000)
print(fibo.sum_even())

