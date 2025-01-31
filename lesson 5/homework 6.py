result = []

def divider(a, b):
    if a < b:
        raise ValueError(f"a ({a}) is less than b ({b})")
    if b > 100:
        raise IndexError(f"b ({b}) is greater than 100")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except (ValueError, IndexError, ZeroDivisionError, TypeError) as e:
        print(f"Exception occurred: {e}")

print(result)
