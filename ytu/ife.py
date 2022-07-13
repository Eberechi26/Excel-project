


# user_lists = ["emma","josh","kalu","obi"]
# user_index = ["0","1","2","3"]
# for index in range(len(user_lists)):
#     if len(user_lists)  == len(user_index):
#         print(user_lists[index])
#     else:
#         print("error")    

# grade = 59
# if grade >= 90:
#     print("A")
# else:
#     if grade >= 80:
#         print("B")
#     else:
#         if grade >= 70:
#             print("C")
#         else:
#             if grade >= 60:
#                 print("D")
#             else:
#                 if grade >= 50:
#                     print("E")
#                 else:
#                     if grade < 50:
#                         print("F")


score1 = []
score2 = []
score3 = []
person = [
        {"name": "obi", "sex": "male",  "age": 45, "gender": "male", "courses": ["bio", "maths", "eng"], "grades": [45, 50, 90], "score": score1}, 
        {"name": "josh", "sex": "female",  "age": 47, "gender": "male", "courses": ["bio", "maths", "eng"], "grades": [35, 67, 97], "score": score2},
        {"name": "kalu", "sex": "male",  "age": 39, "gender": "female", "courses": ["bio", "maths", "eng"], "grades": [15, 85,98], "score": score3}
]
grades1 = [45, 50, 90]
for grade in grades1:
        if grade >= 90:
               score = "A"
        elif grade >= 80:
                score = "B"
        elif grade >= 70:
                score = "C"
        elif grade >= 60:
                score = "D"
        elif grade >= 50:
                score = "E"
        else:
                score = "F"
        score1.append(score)

grades2 = [35, 77, 97]
for grade in grades2:
        if grade >= 90:
                score = "A"
        elif grade >= 80:
                score = "B"
        elif grade >= 70:
                score = "C"
        elif grade >= 60:
                score = "D"
        elif grade >= 50:
                score = "E"
        else:
                score = "F"
        score2.append(score)

grades3 = [15, 55, 98]
for grade in grades3:
        if grade >= 90:
                score = "A"
        elif grade >= 80:
                score = "B"
        elif grade >= 70:
                score = "C"
        elif grade >= 60:
                score = "D"
        elif grade >= 50:
                score = "E"
        else:
                score = "F"
        score3.append(score)
print(person)