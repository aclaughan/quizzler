import logging

from get_questions import get_questions
from quiz_brain import QuizBrain
from ui import QuizInterface

logging.basicConfig(level=logging.INFO, filename='quizzler.log')

NUM_QUESTIONS = 10


def main():
    question_data = get_questions(NUM_QUESTIONS)
    quiz = QuizBrain(question_data)
    quiz.ui = QuizInterface(quiz)


if __name__ == '__main__':
    main()

# logging.debug(stuff)
