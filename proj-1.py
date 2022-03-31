#magicians + text
# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print (f"{magician.title()}, that was a great trick!")
#     print (f"I cant't wait to see your next trick, {magician.title()}. \n")
# print ("Thank you everyone, that was a great magic show! \n")

# #range
# for value in range(5):
#     print (value)

# #list range
# numbers = list(range(2,11,2))
# print (numbers)

# #squares
# squares = []
# for value in range(1,11):
#     squares.append(value**2)

# print (squares)

# #digits 
# digits = [1,2,3,4,5,6,7,8,9,0]
# print (min(digits))
# print (max(digits))
# print (sum(digits))

# #list comprehension
# squares2 = [value2**2 for value in range(1,11)]
# print (squares2)

# #task1
# for i in range (1,21):
#     print (i)

# #task2
# spisok = list(range(1,1000001))
# for i in spisok:
#     print(i)

# #task3
# spisok = list(range(1,1000001))
# print (f"Это минимум, {min(spisok)}, А это макисмум, {max(spisok)}.")
# print (f"А это сумма всех чисел последовательности spisok, {sum(spisok)}.")

# #task4 
# for i in range (1,20,2):
#     print (i)

# #task5
# for i in range(1,31):
#     if i % 3 == 0:
#         print (i)
    
# #task5 option 2
# for i in range(3,31,3):
#     print(i)

# #task6
# for i in range(1,11):
#     print (i**3)

# #task7
# kuby = [value**3 for value in range(1,11)]
# print (kuby)

# #players
# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print (players[0:3])

#perebor players
# players = ['charles', 'martina', 'michael', 'florence', 'eli']

# print ("Here are the first three players on my team:")
# for player in players[:3]:
#     print(player.title())

#foods
myFoods = ['pizza', 'sushi', 'pupushki']
friendFoods = myFoods[:]

print ('My favorite foods are:')
print (myFoods)

print ('\n My friends favorite foods are:')
print(friendFoods)

#zadacha1
print (f"The first three items in the list are: {myFoods[:3]}")

#zadacha2
seredina=int((len(myFoods)%2))
print (myFoods[seredina:seredina+2])
#print (f"Three items from the middle of the list are: {myFoods[seredina:seredina+2]}")




