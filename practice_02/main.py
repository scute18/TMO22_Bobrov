def average_speed(distance, hours):
    if hours == 0:
        return "На ноль делить нельзя"
    return distance / hours

assert average_speed(180, 3) == 60.0

assert average_speed(180, 0) == "На ноль делить нельзя"

assert average_speed(100, 2) == 50.0

words = ["лес", "парк", "площадь"]
sorted_words = sorted(words, key=lambda word: len(word))

print(sorted_words)
