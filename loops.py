'''LOOP OPERATORS
    (1) For Loop
    (2) break and else in loops
    (3) while Loop
    '''

print("=======For Loop========")
# For Loop >> for item in iterable:
# iterable >> list, tuple, set, dict, string
# for loop bunda iterable ichidagi har bir item uchun kod bajariladi
text = "MIT"
numbs = [10, 7, 3, 4]
car_obj = dict(brand="BMW", model="X5", year=2020)
range_obj = range(5)

for letter in text:
    print(f"the letter: {letter}")

for num in numbs:
    print(f"the number: {num}")

for key in car_obj:
    # {car_obj.get(key)} ham xuddi shunday natija beradi
    print(f"the key: {key} and the value: {car_obj[key]}")

for i in range_obj:
    print(f"the number: {i}")

print("=======break and else in loops========")

for i in range(1, 20, 5):  # range(start, stop, step) bunda start dan boshlab stop gacha step qadam bilan sonlar olinadi yani 1, 3, 5, 7, 9 chiqadi
    print(f"the number: {i}")
    if i > 100:
        print("the number is greater than 100")
        break  # break operator bunda loop to'xtatiladi yani 1, 3, 5, 7, 9 chiqadi va loop to'xtaydi
else:
    # else operator bunda loop to'xtatilganda bajariladi yani bu kod bajariladi va "the loop is finished" chiqadi
    print("the loop is finished")

print("=======while Loop========")
# while Loop >> while condition:
# while loop bunda condition "Tuethy" bo'lsa, ya'ni bu shart bajarilsa, quyidagi kod bajariladi va
# shart "Falsy" bo'lsa, ya'ni bu shart bajarilmasa, loop to'xtatiladi
#  takrorlanishning miqdori oldindan ma'lum bo'lmagan holatlarda while loop ishlatiladi,
#  masalan foydalanuvchi to'g'ri javobni topguncha yoki ma'lum bir shart bajarilguncha takrorlanadi
numb = 40
while numb > 0:
    numb -= 10  # bunda numb ning qiymati 10 ga kamaytiriladi yani 40, 30, 20, 10 chiqadi va loop to'xtaydi
    print(f"the number: {numb}")

print("-"*10)
count = 0
while True:
    count += 1
    x = int(input("Enter a number: "))

    if x == 41:
        print(f"You found the number in {count} attempts")
        break
    else:
        print("Try again")
