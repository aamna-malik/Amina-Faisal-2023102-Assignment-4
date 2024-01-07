class Question:
    def __init__(self, text, options, correct_option):
        self.text = text
        self.options = options
        self.correct_option = correct_option

    def display(self):
        print(self.text)
        for i, option in enumerate(self.options, start=1):
            print(f"{i}. {option}")

    def check_answer(self, user_answer):
        return user_answer == self.correct_option


class Quiz:
    def __init__(self, name, questions):
        self.name = name
        self.questions = questions
        self.user_scores = {}

    def take_quiz(self, user):
        print(f"Welcome to the {self.name} quiz, {user.name}!\n")
        score = 0

        for i, question in enumerate(self.questions, start=1):
            print(f"Question {i}:")
            question.display()
            user_answer = int(input("Your answer (enter the corresponding number): "))
            
            if question.check_answer(user_answer):
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer was {question.correct_option}\n")

        self.user_scores[user.name] = score
        print(f"Quiz completed! Your score: {score}/{len(self.questions)}\n")

    def display_scores(self):
        print(f"Quiz Scores for {self.name}:")
        for user, score in self.user_scores.items():
            print(f"{user}: {score}/{len(self.questions)}")


class User:
    def __init__(self, name):
        self.name = name

# Example usage
question1 = Question("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], 3)
question2 = Question("Which planet is known as the Red Planet?", ["Mars", "Jupiter", "Venus", "Saturn"], 1)

quiz = Quiz("General Knowledge", [question1, question2])

user1 = User("Alice")
user2 = User("Bob")

quiz.take_quiz(user1)
quiz.take_quiz(user2)

quiz.display_scores()
