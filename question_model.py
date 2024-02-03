""" Create a class called question, where every new question is a object """
''' For every new object we have two attributes the actual question and its answer'''
'''We have initialized these attributes in Question class with init class, so that they can be accessed for all 
objects '''


class Question:
    def __init__(self, question, answer):
        self.text = question
        self.answer = answer


new_q = Question("varad", "true")
print(new_q.text)
