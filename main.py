from flask import Flask, request, render_template
app = Flask(__name__)
import datetime
import json

# сохраняем сообщения в файл
DB_FILE = "data/db.json"
def load_messages():
  json_file = open(DB_FILE, "r") #открываем файл
  data = json.load(json_file) #загружаем содержимое в формат json
  return data["messages"]

#список всех сообщений
all_messages = load_messages()

def save_messages():
  data = {
    "messages": all_messages
  }
  json_file = open(DB_FILE, "w")
  json.dump(data, json_file)
  return


#объявляем функцию "принт_мессадж", которая принимает один аргумент: мсг
def print_message(msg):
  print(f"{msg['sender']}: {msg['text']} / {msg['time']}")

#функция для добавления нового сообшения
def add_message (sender, text):
#создать структуру нового сообщения
  new_message = {
    "sender": sender,
    "text": text,
    "time": datetime.datetime.now().strftime("%H:%M:%S"),
  }
#добавить ее в список all_messages
  all_messages.append(new_message)
  save_messages()

add_message("Andrey", "wasaup")
add_message("Ilya", "OMG")

#для каждого сообщения в списке сообщений
#for message in all_messages:
 # print_message (message)

@app.route("/get_messages")
def get_massegaes():
  return{"messages": all_messages}

@app.route("/")
def main_page():
  return "Hello, it's me"

@app.route("/send_message")
def send_message():
  sender = request.args["sender"]
  text = request.args["text"]
  add_message(sender, text)
  return "OK"
 # http://127.0.0.1:5000/send_message?sender=Mike&text=Hello - тестовое сообщение

@app.route("/chat")
def display_chat():
    return render_template("form.html")


app.run(host="0.0.0.0", port=80)


