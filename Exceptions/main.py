def avg(numbers):
    assert len(numbers) != 0, "List is empty"
    return sum(numbers) / len(numbers)
t = [4, 7, 5, 8]
print("Average value is: ", avg(t))
t = []
print("Average value is: ", avg(t))


