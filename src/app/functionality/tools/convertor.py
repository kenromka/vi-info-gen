from tag import create_tag
import json

j = json.loads(input())

doc = create_tag()
quiz = create_tag('quiz')
doc.appendChild(quiz)

question = create_tag('question', None, {"type": "category"})
category = create_tag('category')
text = create_tag('text', j["category"])
category.appendChild(text)
question.appendChild(category)
quiz.appendChild(question)

for q in j["questions"]:
    question = create_tag('question', None, {"type": j["question_type"]})
    name = create_tag('name')
    text = create_tag('text', q["question_name"])
    name.appendChild(text)
    question.appendChild(name)
    
    questiontext = create_tag('questiontext', None, {"format": "html"})
    if "question_media" in q:
        text = create_tag('text', "<p>" + q["question_text"] + "</p>" + q["question_media"], cdata = True)
    else:
        text = create_tag('text', "<p>" + q["question_text"] + "</p>", cdata = False)
    questiontext.appendChild(text)
    question.appendChild(questiontext)

    answer = create_tag('answer', None, {"fraction": "100", "format": "moodle_auto_format"})
    text = create_tag('text', str(q["question_answer"]))
    answer.appendChild(text)
    question.appendChild(answer)
    quiz.appendChild(question)

print(doc.toprettyxml(indent = "  "))
