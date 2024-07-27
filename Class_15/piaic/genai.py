import time

class ExcecutionTimer():
    def __init__(self, func):  # constructor    
        self.func = func  # attribute

    def __call__(self, *args, **kwargs):
        start = time.perf_counter()   # it will count start time 
        result = self.func(*args, **kwargs)  # make attribute
        end = time.perf_counter()  # it will count end time 
        print(f"{self.func.__name__}() took {(end - start) * 1000:.4f} ms")
        return result 