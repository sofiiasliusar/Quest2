def intro():
    print("Вітаю у грі!")

    print("Ви потрапили в квест кімнату.")

    print("Для того, щоб вийти вам потрібно пройти 3 рівні.")

    choice1 = input("Ви готові? \n1 - Так \n2 -Ні \n")

    if choice1 == "1":
        level1()
    elif choice1 == "2":
        print("Треба завжди бути напоготові!")
        gamelost()
    else: 
        print("Введіть лише цифру.")
        intro()

def level1():
    print("Перший рівень - це камінь-ножиці-папір.")

    print("Зробіть свій вибір:")

    print("1 - Камінь")

    print("2 - Ножиці")

    print("3 - Папір")

    choice2 = input("\n")

    if choice2 == "1":
        print("Ваш суперник обрав ножиці і ви перемогли!")

        level2()
    elif choice2 == "2":
        print("Ваш суперник обрав камінь і ви програли!")

        print("Спробуйте знову.")

        level1()
    elif choice2 == "3":
        print("Ваш суперник обрав ножиці і ви програли!")

        print("Спробуйте знову.")

        level1()

    else:
        print("Введіть лише цифру.")
        level1()

def level2():
    print("Вітаю! Ви перейшли до другого рівня.")

    print("Відгадайте загадку:")

    print("Що збільшується, але ніколи не зменшується?")

    print("1 - Думки")

    print("2 - Домашнє завдання")

    print("3 - Вік")

    choice3 = input("\n")

    if choice3 == "1":
        print("Не вгадали!")

        print("Спробуйте знову.")

        level2()

    elif choice3 == "2":
        print("Не вгадали!")
        
        print("Спробуйте знову.")

        level2()

    elif choice3 == "3":
        print("Правильно!")

        level3()

    else:
        print("Введіть лише цифру.")
        level2()

def level3():
    print("Вітаю! Ви перейшли до третього рівня.")

    print("Ви можете виграти :) або програти усю гру :(")

    print("Вам потрібно вгадати мелодію ;)")

    print("1 - Цей сон")

    print("2 - Shape of My Heart")

    print("3 - А липи цвітуть")

    choice4 = input("\n")

    if choice4 == "1":
        print("Ви вгадали!")

        gamewon()
    elif choice4 == "2":
        print("Не вгадали!")

        gamelost()
    elif choice4 == "3":
        print("Не вгадали!")
        
        gamelost()
    else:
        print("Введіть лише цифру.")
        level3()

def gamewon():
    print("Ви перемогли! Гру закінчено!")

def gamelost():
    print("Ви програли! Гру закінчено!")

intro()