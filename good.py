print("Hi to everyone")
magicians = ['alice', 'david', 'crolina']
for magician in magicians:
    print(magician)
    print(f"{magician.title()}, it was a great trick!")
    print(f"I can't wait to see you, {magician.title()}!\n")
for value in range(6):
    print(value)
number = list(range(1,20,3))
print(number)
squares = []
for value in range(1,11):
    squares.append(value**3)
print(squares)
digitals = [1,2,3,4,5,6,7,8,9]
print(max(digitals))
print(min(digitals))
print(sum(digitals))