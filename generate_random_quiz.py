import random

capitals={India:Delhi,ArunachalPradesh:Itanagar,Assam:Dispur,Bihar:Patna,Goa:Panaji,Gujarat:Gandhinagar,Haryana:Chandigarh,HimachalPradesh:Shimla}
for quiz in range(5):
    quiz1= open('capitalquiz%s.txt' %  (quiz+1),'w')
    answer1 = open('capitalquizanswer%s.txt' %  (quiz+1),'w')
    states =list(states.keys())
    random.shuffle(states)

    for qn in range(8):
        correct_answer= capitals[states[qn]]
        wrong_answers = list(capitals.values())
        del wrong_answers[wrong_answers.index(correct_answer)]
        wrong_answers = random.sample(wrong_answers)
        answer_options= [correct_answer] + wrong_answers
        random.shuffle(answer_options)
        capitalquiz1.write("%s what is the capital of %s?\n" (qn+1,states[qn]))
        capitalquiz1.write()
        for i in range(4):
            print(" %s %s\n " %('ABCD'[i],answer_options[i]))

        answer1.write("%s %s\n",(qn+1),'ABCD'[answerOptions.index(correct_answer)])
        capitalquiz1.close()
        answer1.close()


