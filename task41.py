class Counter:

    def __init__(self, current=1, min_value=0, max_value=10):
        self.min_value = min_value
        self.max_value = max_value
        self.current = current

    def set_current(self, start):
        if start < self.min_value or start > self.max_value:
            raise ValueError("Поточне значення поза межами лічильника")
        self.current = start

    def set_max(self, max_max):
        if max_max < self.min_value:
            raise ValueError("Максимум не може бути меншим за мінімум")
        self.max_value = max_max
        if self.current > self.max_value:
            self.current = self.max_value

    def set_min(self, min_min):
        if min_min > self.max_value:
            raise ValueError("Мінімум не може бути більшим за максимум")
        self.min_value = min_min
        if self.current < self.min_value:
            self.current = self.min_value

    def step_up(self):
        if self.current >= self.max_value:
            raise ValueError("Досягнуто максимуму")
        self.current += 1

    def step_down(self):
        if self.current <= self.min_value:
            raise ValueError("Досягнуто мінімуму")
        self.current -= 1

    def get_current(self):
        return self.current




counter = Counter()

counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()

assert counter.get_current() == 10, 'Test1'

try:
    counter.step_up()
except ValueError as e:
    print(e)  

assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()

assert counter.get_current() == 7, 'Test3'

try:
    counter.step_down()
except ValueError as e:
    print(e)  

assert counter.get_current() == 7, 'Test4'