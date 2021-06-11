from flask import Flask, request, render_template, url_for, redirect
from score import Score
from questions import Questions
from time import sleep
from clock import Clock


score = Score()
app = Flask(__name__)
NUM_OF_QUESTIONS = 20
questions = Questions(amount=NUM_OF_QUESTIONS)
clock = Clock()


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if request.form.get("category") == "Random":
            questions.start(category=questions.random_category())
        else:
            questions.start(category=request.form.get("category"))
        clock.start()
        score.restart()
        return redirect(url_for("game", num_of_question=0))
    return render_template("index.html")


@app.route("/game/<int:num_of_question>", methods=["GET", "POST"])
def game(num_of_question):
    if NUM_OF_QUESTIONS > num_of_question >= 0:
        answers = questions.get_all_answers(num_of_question)
        correct_answer = questions.get_correct_answer(num_of_question)
        question = questions.get_question(num_of_question)
        if request.method == "POST":
            user_answer = request.form.get("user_answer")
            if user_answer == "correct":
                score.up()
            sleep(1)
            return redirect(url_for("game", num_of_question=num_of_question + 1))
        return render_template("game.html",
                               question=question,
                               answers=answers,
                               score=score,
                               current_question=num_of_question,
                               correct=correct_answer)
    else:
        final_score = score.get()
        final_time = clock.end_and_get_final_time()
        return render_template("final.html", final_score=final_score, final_time=final_time)


if __name__ == "__main__":
    app.run(debug=True)
