budget = int(input())

if budget < 23:
    print("None")
elif 23 <= budget < 678:
    print(budget // 23, "chicken" if budget // 23 == 1 else "chickens")
elif 678 <= budget < 1296:
    print(budget // 678, "goat" if budget // 678 == 1 else "goats")
elif 1296 <= budget < 3848:
    print(budget // 1296, "pig" if budget // 1296 == 1 else "pigs")
elif 3848 <= budget < 6769:
    print(budget // 3848, "cow" if budget // 3848 == 1 else "cows")
else:
    print(budget // 6769, "sheep")
