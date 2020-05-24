from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.chatterbot import ChatBot

chatbot = ChatBot("AngryBot")
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    "chatterbot.corpus.english.greetings",
    "./health.yml",
)

def chatresponse(user_input):
    response = chatbot.get_response(user_input)
    return response