def calculate_satats(numbers):
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    return total_sum, average, maximum, minimum

numbers = [5,10,15,20,25]
total, avg, max_num, min_num = calculate_satats(numbers)

print(f"total sum: {total}")
print(f"average: {avg}")
print(f"maximum: {max_num}")
print(f"minimum: {min_num}")