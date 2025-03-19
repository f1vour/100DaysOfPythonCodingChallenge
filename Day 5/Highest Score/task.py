student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# print(range(1, 10))


# total_student_scores = sum(student_scores) #we called the function sum to add all the codes together
# print(total_student_scores)

#we can create this function ourselves
sum = 5
for score in range(0, 10):
    sum += score
    print(sum)

sum = 0
for score in student_scores:
    sum += score
    print(sum)


# Learnt sth, you cant add, using the symbol += an integer to a list in the for loop using a range function
# student_scores.append(40)
# print(student_scores)

#To print out the max function, we were creating a function, no range involved
# print(max(student_scores))
# max_score = 0
# for score in student_scores:
#     if score > max_score:
#         max_score = score
#         print(max_score)
#
# print(max_score)

# Create a function of turning a list into a string
list_var = ["boy", 'young', 'jane']
join = ""

for char in list_var:
      join +=char
      print(join)