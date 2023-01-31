class Question:
    def __int__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):
        return self.answer == answer


q1 = Question('which one is best language', ['c', 'java', 'python'], 'c')
q2 = Question('which one is best name', ['ahmet', 'mali', 'sina'], 'ahmet')
q3 = Question('which one is best color', ['blue', 'green', 'yellow'], 'blue')
print(q1.checkAnswer('c'))
'''
class Quiz:
    def __int__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def diplayQ(self):
        question = self.getQuestion()
        print(f'Question {self.questionIndex + 1} :{question.text}')
        for q in question.choices:
            print('*' + q)
        answer = input('Answer : ')
        self.guess(answer)

    def guess(self, answer):
        question = self.getQuestion()
        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1
        self.diplayQ()

    def loadQ(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.diplayProgress()
            self.diplayQ()

    def showScore(self):
        print('score:', self.score)

    def displayProgress(self):
        totalQ = len(self.questions)
        questionNumber = self.questionIndex + 1

        if questionNumber > totalQ:
            print('Quiz done')
        else:
            print(f'question{questionNumber} of {totalQ}'.center(100), '*')


q1 = Question('which one is best language', ['c', 'java', 'python'], 'c')
q2 = Question('which one is best name', ['ahmet', 'mali', 'sina'], 'ahmet')
q3 = Question('which one is best color', ['blue', 'green', 'yellow'], 'blue')
questions = [q1, q2, q3]
quiz = Quiz(questions)
quiz.loadQ()
'''
