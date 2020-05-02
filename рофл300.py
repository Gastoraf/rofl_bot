import vk_api
import random
import time

token = "Ваш токен"


vk = vk_api.VkApi(token=token)

vk._auth_token()

dz = "дз нет"


while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if body.lower() == "привет":
                vk.method("messages.send", {"peer_id": id, "message": "Ты дурачок?! Напиши лучше 300", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "300":
                vk.method("messages.send", {"peer_id": id, "message": "Отсоси у тракториста", "random_id": random.randint(1, 2147483647)})

            else:
                vk.method("messages.send", {"peer_id": id, "message": "Ты дурачок?! Напиши лучше 300", "random_id": random.randint(1, 2147483647)})
    except Exception as E:
        time.sleep(1)


