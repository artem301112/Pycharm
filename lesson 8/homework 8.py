import time

def quick_function():
    return "Quick"

def slow_function():
    time.sleep(1)
    return "Slow"

def test_runtime(func, *args, **kwargs):
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    return end_time - start_time

print ("========== Quick test===========")
print("Quick function runtime:", test_runtime(quick_function))

print ("==========Slow test===========")
print("Slow function runtime:", test_runtime(slow_function))