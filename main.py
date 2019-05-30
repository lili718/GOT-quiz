from Question import *
if __name__ == "__main__":
    questions = [
        Question("Who is Jon Snow's father?", "Ned Stark", "Aegon Targaryen", "Rhaegar Targaryen", "Robert Baratheon",
                 3),
        Question("What is coming?", "Spring", "Winter", "Fall", "Summer", 2),
        Question("Who has Sansa not been married or promised to", "Joffrey", "Tyrion", "Ramsey", "Little Finger", 4),
        Question("How tall is Tyrion Lanister?", "4ft 4in", "4 ft 2in", "4ft 5in", "4ft 3in", 1),
        Question("Who was Mance Rayder?", "The King of Dorne", "A faceless man", "A Hand of the King",
                 "The King beyond the wall", 4),
        Question("How did Tommen die?", "Explosion", "Suicide", "Poison", "In battle", 2),
        Question("Who inspired Game of Thrones' cat memes", "Cersei Lannister", "Sansa Stark", "Olenna Tyrell",
                 "Margaery Tyrell", 3),
        Question("Where did Tywin Lannister Die", "On the Toilet", "In battle", "The Sept of Baelor", "At Sea", 1),
        Question("What is Bran", "He who must not be named", "The heir to the iron throne", "The 3 eyed raven",
                 "The prophesied prince", 3),
        Question("What is Jon's true relationship to Sansa", "Brother", "Cousin", "Uncle", "None of the above", 2)
        ]
    p1 = 0
    p2 = 0
    print("Welcome to the Game of Thrones knowledge quiz")
    print("-"*45)
    player1 = True
    nums = ["1", "2", "3", "4"]
    for question in questions:
        if player1 == True:
            print("Player 1 here is your Question:")
            print(question)
            answer = input("Enter your answer\n")
            while answer not in nums:
                print("Error: your answer has to be a value between 1 and 4. Try again.")
                answer = input("Enter your answer\n")
            if int(answer) == question.getCorrectAnswer():
                print("Excellent! You score!")
                p1 += 1
            else:
                print("That is incorrect. Better luck with the next question.\n")
            player1 = False
        else:
            print("Player 2 here is your question:")
            print(question)
            answer = input("Enter your answer\n")
            while answer not in nums:
                print("Error: your answer has to be a value between 1 and 4. Try again.")
                answer = input("Enter your answer\n")
            if int(answer) == question.getCorrectAnswer():
                print("Excellent! You score!\n")
                p2 += 1
            else:
                print("That is incorrect. Better luck with the next question.\n")
            player1 = True
    print("And the final scores are:\nPlayer 1:", p1, "\nPlayer 2: ", p2,)
    if p1 > p2:
        print("\nPlayer 1 wins!")
    elif p1 < p2:
        print("\nplayer 2 wins!")
    else:
        print("\nPlayer 1 and player 2 tied!")