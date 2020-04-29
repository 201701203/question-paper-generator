from enum import Enum

from flask import url_for
from flask_login import current_user

default_instructions = [
    "Write your name and student number in the space provided",
    "Make sure your mobile phone is switched off and place it at the front together with\
                         any bags, books, coats etc. Then find your seat.",
    "Remember that talking is not allowed at any time in the exam hall.",
    "Listen carefully to instructions. Students are required to comply with\
                         the instructions of invigilators at all times.",
    "You are not permitted to share stationery, \
                        calculators or any other materials during the examination.",
    "If you have a question or need more papers, raise your hand and a teacher\
                         will come to you. Teachers will not give hints or answers, so please do not ask for them.",
    "Stop writing immediately when the teacher says it is the end of the exam.",
    "Leave the exam hall quickly and quietly. Remember to take all your belongings with you.\
                         (Remember to collect all your belongings from holding rooms.)\
                          You must remain silent until after you have exited the building.",
    "Remember! Any form of cheating is not allowed and action will be taken.",
]


class CognitiveEnum(Enum):
    Knowledge = 1
    Comprehension = 2
    Application = 3


class DifficultyEnum(Enum):
    Easy = 1
    Medium = 2
    Hard = 3


def DifficultyLevel(value):
    translate = {"easy": DifficultyEnum.Easy,
                 "medium": DifficultyEnum.Medium,
                 "hard": DifficultyEnum.Hard}
    return translate[value]


def CognitiveLevel(value):
    translate = {"application": CognitiveEnum.Application,
                 "comprehension": CognitiveEnum.Comprehension,
                 "knowledge": CognitiveEnum.Knowledge}
    return translate[value]


def profile_path():
    return url_for("static",
                   filename="profile_pics/" + current_user.image_file)
