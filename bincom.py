from collections import Counter
import random



colors_week = [
    "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN",
    "ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE",
    "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE",
    "BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN",
    "GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE"
]


colors = []

for i in colors_week:
    items = i.split(",")
    for n in items:
        color = n.strip().upper()

        # BLEW and ARSH
        if color == "BLEW":
            color = "BLUE"
        if color == "ARSH":
            continue

        colors.append(color)


color_count = Counter(colors)



# 1: Mean color
most_common_color = color_count.most_common(1)[0][0]
print("Mean color:", most_common_color)


# 2: most worn color
print("Most worn color:", most_common_color)


# 3: Median color
sorted_colors = sorted(colors)
middle_index = len(sorted_colors) // 2
median_color = sorted_colors[middle_index]
print("Median color:", median_color)



# 4: Variance
frequencies = list(color_count.values())
mean = sum(frequencies) / len(frequencies)

variance = 0
for num in frequencies:
    variance += (num - mean) ** 2

variance = variance / len(frequencies)
print("Variance:", variance)



# 5: Probability of red
total_colors = len(colors)
red_count = color_count.get("RED", 0)

probability_red = red_count / total_colors
print("Probability of choosing RED:", probability_red)



# 7: Recursive search
def search_number(lst, target, index=0):
    if index >= len(lst):
        return False
    if lst[index] == target:
        return True
    return search_number(lst, target, index + 1)


numbers = [1, 2, 3, 4, 5, 6]
print("Search for 4:", search_number(numbers, 4))



# 8: Random binary → base 10
binary_number = ""

for _ in range(4):
    binary_number += str(random.randint(0, 1))

decimal_number = int(binary_number, 2)

print("Binary: ", binary_number, " Decimal: ", decimal_number)



# 9: Sum first 50 Fibonacci numbers
def fibonacci_sum(n):
    a = 0
    b = 1
    total = 0

    for _ in range(n):
        total += a
        a, b = b, a + b

    return total

print("The sum of first 50 Fibonacci numbers:", fibonacci_sum(50))