from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank =[]
for new in question_data:
    q_text = new["text"]
    q_answer = new["answer"]
    new_question = Question(q_text, q_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():

    quiz.next_question()

print("You have completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
