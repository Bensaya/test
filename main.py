def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        return (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        return sorted_numbers[n // 2]
def calculate_variance(numbers):
    average = calculate_average(numbers)
    squared_differences = [(x - average) ** 2 for x in numbers]
    return calculate_average(squared_differences)
def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)

data = [1, 2, 3, 4, 5]
median = calculate_median(data)
average = calculate_average(data)
print(f"Median: {median}")
print(f"Median: {average}")