import logging
import re
from html import unescape


# logging.basicConfig(level = logging.INFO)

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        self.page_width = 70

    def nice_text(self, question: str) -> str:
        if len(question) < self.page_width:
            return question

        spaces = []
        found_spaces = [c.start() for c in re.finditer(' ', question)]
        for position in found_spaces:
            if position < self.page_width:
                spaces.append(position)
        lastspace = spaces.pop()
        new_string = question[:lastspace] + '\n ' + question[lastspace:]
        return new_string

    def question(self) -> str:
        self.q_data = self.question_list[self.question_number]
        self.question_number += 1

        self.question_text = unescape(self.q_data['question'])

        logging.info(f"Question: {self.question_text}")
        logging.info(f"Answer: {self.q_data['correct_answer']}")

        return f"Question {self.question_number}:\n\n{self.question_text}"

    def category(self) -> str:
        return self.q_data['category']

    def difficulty(self) -> str:
        return self.q_data['difficulty']

    def is_correct(self, answer: str) -> bool:
        if self.question_list[self.question_number -1]['correct_answer'] == answer:
            self.score += 1
            return True
        else:
            return False


