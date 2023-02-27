# KBC
questions = [
    ["Which language was used to create fb?",
        "Python", "CS", "J s ", "PHP", "None", 4],
    ["Which language was used to create fb?",
        "Python", "CS", "J s ", "PHP", "None", 4],
    ["Which language was used to create fb?",
        "Python", "CS", "J s ", "PHP", "None", 4],
    ["Which language was used to create fb?",
        "Python", "CS", "J s ", "PHP", "None", 4],
    ["Which language was used to create fb?",
        "Python", "CS", "J s ", "PHP", "None", 4],
    ["Which language was used to create fb?",
        "Python", "CS", "J s ", "PHP", "None", 4],
    ["Which language was used to create fb?",
        "Python", "CS", "J s ", "PHP", "None", 4],
    ["Which language was used to create fb?",
        "Python", "CS", "J s ", "PHP", "None", 4],
    ["Which language was used to create fb?",
        "Python", "CS", "J s ", "PHP", "None", 4],
    ["Which language was used to create fb?",
        "Python", "CS", "J s ", "PHP", "None", 4],
    ["Which language was used to create fb?",
        "Python", "CS", "J s ", "PHP", "None", 4],
    ["Which language was used to create fb?",
        "Python", "CS", "J s ", "PHP", "None", 4],
    ["Which language was used to create fb?",
        "Python", "CS", "J s ", "PHP", "None", 4],
    ["Which language was used to create fb?",
        "Python", "CS", "J s ", "PHP", "None", 4],
    ["Which language was used to create fb?",
        "Python", "CS", "J s ", "PHP", "None", 4],
    ["Which language was used to create fb?",
        "Python", "CS", "J s ", "PHP", "None", 4],
    ["Which language was used to create fb?",
        "Python", "CS", "J s ", "PHP", "None", 4],
    ["Which language was used to create fb?",
        "Python", "CS", "J s ", "PHP", "None", 4],
    ["Which language was used to create fb?",
        "Python", "CS", "J s ", "PHP", "None", 4],
    ["Which language was used to create fb?",
        "Python", "CS", "J s ", "PHP", "None", 4],
    ["Which language was used to create fb?",
        "Python", "CS", "J s ", "PHP", "None", 4],
    ["Which language was used to create fb?",
        "Python", "CS", "J s ", "PHP", "None", 4],
    ["Which language was used to create fb?",
        "Python", "CS", "J s ", "PHP", "None", 4],
    ["Which language was used to create fb?",
        "Python", "CS", "J s ", "PHP", "None", 4],
    ["Which language was used to create fb?",
        "Python", "CS", "J s ", "PHP", "None", 4],
    ["Which language was used to create fb?",
        "Python", "CS", "J s ", "PHP", "None", 4],
    ["Which language was used to create fb?",
        "Python", "CS", "J s ", "PHP", "None", 4],
    ["Which language was used to create fb?",
        "Python", "CS", "J s ", "PHP", "None", 4],
    ["Which language was used to create fb?",
        "Python", "CS", "J s ", "PHP", "None", 4],
    ["Which language was used to create fb?",
        "Python", "CS", "J s ", "PHP", "None", 4],
    ["Which language was used to create fb?",
        "Python", "CS", "J s ", "PHP", "None", 4],
    ["Which language was used to create fb?",
        "Python", "CS", "J s ", "PHP", "None", 4],
    ["Which language was used to create fb?",
        "Python", "CS", "J s ", "PHP", "None", 4],
    ["Which language was used to create fb?",
        "Python", "CS", "J s ", "PHP", "None", 4],
    ["Which language was used to create fb?",
        "Python", "CS", "J s ", "PHP", "None", 4],
    ["Which language was used to create fb?",
        "Python", "CS", "J s ", "PHP", "None", 4],
    ["Which language was used to create fb?",
        "Python", "CS", "J s ", "PHP", "None", 4],
    ["Which language was used to create fb?",
        "Python", "CS", "J s ", "PHP", "None", 4],


]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 50000, 160000, 500000, 1000000]

money = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(f"question for rs{levels[i]} ")
    print(
        f"a. {question[1]}     b. {question[2]}   c. {question[3]} d. {question[4]}  ")
    reply = int(input("enter your answer (1-4) or press 0 to quit"))
    if (reply == 0):
        money = levels[i-1]
        break
    if (reply == question[-1]):
        print(
            f"correct answer, you have won Rs.{levels[i]}"
        )
        if (i == 4):
            money = 10000
        elif (i == 9):
            money = 320000
        elif (i == 14):
            money = 3200000
    else:
        print(
            "wrong answer "
        )
        break

print(f"your take home money is {money}")
