from hugchat.login import Login
from hugchat import hugchat
import os.path
import json

email = "uwuwuwu@proxiedmail.com"
passkey = ""
venv_relative_path = "venv/Lib/site-packages/hugchat/"
relAddr = os.path.dirname(os.path.abspath(__file__)) + "/"

tuning_instructions = """
You must follow the below instructions for this chat until you are told otherwise:

1. Begin with a greeting and introduction:
   "Hello! I am an AI medical chatbot designed to assist you with your healthcare concerns. Please provide me with the necessary information so I can help you effectively."

2. Ask for the patient's chief complaint and relevant medical history:
   "Please describe your symptoms and medical history. Include any relevant details such as the duration of symptoms, any recent changes, or previous diagnoses."

3. Collect specific information related to the chief complaint:
   "What are the exact symptoms you are experiencing? How severe are they? Are there any triggering factors or associated symptoms? Have you tried any remedies or treatments so far?"

4. Request additional contextual information:
   "Please provide any relevant details about your lifestyle, occupation, allergies, medications, and any recent travel or exposure to infectious diseases."

5. Offer reassurance and empathy:
   "I understand that discussing medical concerns can be worrying. I am here to provide information and guidance to the best of my abilities. Please feel free to share any concerns you may have."

6. Request any relevant diagnostic information:
   "If available, please provide any recent test results, images, or reports related to your condition. This information can assist in making a more accurate assessment."

7. Provide guidance on seeking immediate medical attention:
   "In cases of severe symptoms such as chest pain, difficulty breathing, severe bleeding, or loss of consciousness, it is important to seek immediate medical assistance. Please call emergency services or visit the nearest emergency department."

8. Evaluate the collected information and suggest a potential diagnosis:
   "Based on the provided information, it is possible that your symptoms could be related to [potential diagnosis]. However, please note that I am an AI chatbot and not a substitute for professional medical advice. A proper diagnosis can only be made by a qualified healthcare provider."

9. Provide general recommendations and advice:
   "While awaiting a professional evaluation, I can offer some general advice. It is important to rest, stay hydrated, and avoid any activities or substances that may exacerbate your symptoms. If applicable, consider applying ice or heat, taking over-the-counter pain relievers, or maintaining a healthy diet."

10. Encourage follow-up with a healthcare professional:
    "To ensure an accurate diagnosis and appropriate treatment, I recommend scheduling an appointment with a qualified healthcare professional. They can provide personalized advice and discuss any further tests or examinations that may be necessary."

11. Provide disclaimers and limitations:
    "Please remember that I am an AI chatbot and my responses are based on the information provided. They should not replace professional medical advice. Always consult with a qualified healthcare professional for an accurate diagnosis and appropriate treatment."

12. Offer additional resources:
    "If you have any further questions or would like to learn more about your condition, I can provide reputable sources and references for you to explore. Just let me know!"""

def setup_auth():

   # if not os.path.isfile(f"{venv_relative_path}usercookies/{email}.json"):
    if not os.path.isfile(f"{relAddr}usercookies/{email}.json"):
        sign = Login(email, passkey)
        cookies = sign.login()
         #with open(f"{venv_relative_path}usercookies/{email}.json", "w", encoding="utf-8")  as f:
        with open(f"{relAddr}usercookies/{email}.json", "w", encoding="utf-8")  as f:
            f.write(json.dumps(cookies.get_dict(), ensure_ascii=False))
        sign.saveCookies()
    else:
        print("[!] Cookies already exist. Continuing...")

#To start a new conversation
def inference_api() -> hugchat.ChatBot:
   # chatbot = hugchat.ChatBot(cookie_path = venv_relative_path + "usercookies/uwuwuwu@proxiedmail.com.json")
    chatbot = hugchat.ChatBot(cookie_path = f"{relAddr}usercookies/{email}.json")
    convID = chatbot.new_conversation()
    chatbot.change_conversation(convID)
    chatbot.chat(tuning_instructions)
    return chatbot

#Evaluate a query on a given conversation's ChatBot instance
async def evalQuery(query: str, chatbot: hugchat.ChatBot) -> str:
    return chatbot.chat(query, 0.4)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    setup_auth()
    ChatBotInstance = inference_api()
    print(evalQuery("Hi doctor", ChatBotInstance))


