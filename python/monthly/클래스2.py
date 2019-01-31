class Calculator:

    def __init__(self):


        self.plus_count = 0
        self.min_count = 0
        self.mul_count = 0
        self.div_count = 0

    def Add(self, plus_a, plus_b):
        self.plus_a = plus_a
        self.plus_b = plus_b
        self.plus_count += 1
        return self.plus_b + self.plus_b

    def Min(self, min_a, min_b):
        self.min_a = min_a
        self.min_b = min_b
        self.min_count +=1
        return self.min_a + self.min_b

    def Mul(self, mul_a, mul_b):
        self.mul_a = mul_a
        self.mul_b = mul_b
        self.mul_count += 1
        return self.mul_a + self.mul_b

    def Div(self, div_a, div_b):
        self.div_a = div_a
        self.div_b = div_b
        self.div_count += 1
        return self.div_a + self.div_b

    def ShowCount(self):
        print(f"""덧셈 : {self.plus_count}
뺄셈 : {self.min_count}
곱셈 : {self.mul_count}
나눗셈 : {self.div_count}
        """)


cal = Calculator()
print("10 + 20 = %s" %cal.Add(10, 20))
print("10 - 20 = %s" %cal.Min(10, 20))
print("10 * 20 = %s" %cal.Mul(10, 20))
print("10 * 10 = %s" %cal.Mul(10, 10))
print("10 / 10 = %s" %cal.Div(10, 10))
cal.ShowCount()

