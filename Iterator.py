class A:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a > 0:
            x = self.a
            self.a = self.a + 1
            return x
        else:
            raise StopIteration

p1_obj = A()
iter_value = iter(p1_obj)
print(next(iter_value))
print(next(iter_value))