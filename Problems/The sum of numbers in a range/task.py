def range_sum(numbers, start, end):
    return sum([i for i in numbers if start <= i <= end])

    
input_numbers = list(map(int, input().split()))
a, b = list(map(int, input().split()))
print(range_sum(input_numbers, a, b))
