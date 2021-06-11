import requests
import html
import random
TRIVIA_ENDPOINT = "https://opentdb.com/api.php"


class Questions:
    def __init__(self, amount):
        self.amount = amount
        self.categories = {
            "General Knowledge": 9,
            "Books": 10,
            "Films": 11,
            "Music": 12,
            "Musicals and Theatres": 13,
            "Television": 14,
            "Video Games": 15,
            "Board Games": 16,
            "Science and Nature": 17,
            "Computers": 18,
            "Mathematics": 19,
            "Mythology": 20,
            "Sports": 21,
            "Geography": 22,
            "Historic": 23,
            "Politics": 24,
            "Art": 25,
            "Celebrities": 26,
            "Animals": 27,
            "Vehicles": 28,
            "Comics": 29,
            "Gadgets": 30,
            "Anime and Manga": 31,
            "Cartoon and Animation": 32
        }

    def start(self, category):
        token = requests.get("https://opentdb.com/api_token.php?command=request").json()["token"]
        params = {
            "category": self.categories[category],
            "amount": self.amount,
            "type": "multiple",
            "token": token
        }
        self.questions = requests.get(TRIVIA_ENDPOINT, params=params).json()["results"]

    def get_all_answers(self, num_of_question):
        current_question = self.questions[num_of_question]
        answers = [html.unescape(incorrect) for incorrect in current_question["incorrect_answers"]]
        answers.append(html.unescape(current_question["correct_answer"]))
        random.shuffle(answers)
        return answers

    def get_question(self, num_of_question):
        return html.unescape(self.questions[num_of_question]["question"])

    def get_correct_answer(self, num_of_question):
        return html.unescape(self.questions[num_of_question]["correct_answer"])

    def random_category(self):
        category, value = random.choice(list(self.categories.items()))
        return category
