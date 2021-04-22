import logging

from get_questions import get_questions
from quiz_brain import QuizBrain
from art import logo
from ui import QuizInterface

logging.basicConfig(level=logging.INFO, filename='quizzler.log')

NUM_QUESTIONS = 10


def main():
    #print(logo)

    question_data = get_questions(NUM_QUESTIONS)

    quiz = QuizBrain(question_data)
    quiz.ui = QuizInterface(quiz)


    # print(
    #     f"I have downloaded {NUM_QUESTIONS} random questions " \
    #     f"to ask you.\n    Good luck :)\n")
    #
    # while question_data:
    #     if quiz.question(question_data.pop()):
    #         quiz.score += 1
    #         print(
    #             f'\n  Correct, you earn a point [{quiz.score}/{NUM_QUESTIONS}]\n')
    #
    #     else:
    #         print('\n  That is incorrect\n')
    #
    # print(f"final score: {quiz.score}/{NUM_QUESTIONS}")


if __name__ == '__main__':
    main()

# logging.debug(stuff)
