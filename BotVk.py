import vk_api
import time


class VkBot:
    def bot(self):
        token = "fa804c84d0f722ec41819722652f0aceed51cf5ad2e3bc14f016a8a8090dd44bc95467328eb9c2d1e74c0"
        self.vk = vk_api.VkApi(token=token)
        self.vk._auth_token()
        art2012 = "photo-59224384_395098605,photo-59224384_395098420,photo-59224384_395098427," \
                  "photo-59224384_395098428,photo-59224384_395098429,photo-59224384_395098432,photo-59224384_395098441," \
                  "photo-59224384_395098467,photo-59224384_395098484,photo-59224384_395098603"
        art2013 = "photo-59224384_395099065,photo-59224384_395099074,photo-59224384_395099076,photo-59224384_395099079," \
                  "photo-59224384_395099082,photo-59224384_395099085,photo-59224384_395099092,photo-59224384_395099099," \
                  "photo-59224384_395099105,photo-59224384_395099113"
        art22013 = "photo-59224384_395099117,photo-59224384_395099124,photo-59224384_395099128,photo-59224384_395099130," \
                   "photo-59224384_395099133,photo-59224384_395099138,photo-59224384_395099152,photo-59224384_395099157," \
                   "photo-59224384_395099202,photo-59224384_395099450"
        art2014 = "photo-59224384_395099387,photo-59224384_395099389,photo-59224384_395099391,photo-59224384_395099392," \
                  "photo-59224384_395099393,photo-59224384_395099396"
        art2015 = "photo-59224384_395099599,photo-59224384_405298310"
        art2016 = "photo-59224384_414173605,photo-59224384_414414875,photo-59224384_423919234photo-59224384_456239021"
        art2017 = "photo-59224384_456239027,photo-59224384_456239022"

        def command():

            self.vk.method("messages.send", {"peer_id": id,
                                        "message": "Привет, здесь ты можешь узнать какие арты я рисовала в 2012-2017 году, "
                                                   "для этого напиши например: 'арты 2012' (можно написать любой год от 2012 до 2017), "
                                                   "и я вышлю тебе рисунки за этот год. Также ты можешь заказать здесь рисунок, "
                                                   "для этого напиши 'хочу арт', после чего появится несколько вариантов."})


        while True:
            try:
                messages = self.vk.method("messages.getConversations", {"offset": 0, "count": 200})
                if messages["count"] >= 1:
                    id = messages["items"][0]["last_message"]["from_id"]
                    body = messages["items"][0]["last_message"]["text"]
                    if body.lower() == "привет":
                        command()
                    elif body.lower() == "команды":
                        command()
                    elif body.lower() == "арты 2012":
                        self.vk.method("messages.send", {"peer_id": id, "message": "2012", "attachment": art2012})
                    elif body.lower() == "арты 2013":
                        self.vk.method("messages.send", {"peer_id": id, "message": "2013", "attachment": art2013})
                        self.vk.method("messages.send", {"peer_id": id, "message": "2013", "attachment": art22013})
                    elif body.lower() == "арты 2014":
                        self.vk.method("messages.send", {"peer_id": id, "message": "2014", "attachment": art2014})
                    elif body.lower() == "арты 2015":
                        self.vk.method("messages.send", {"peer_id": id, "message": "2015", "attachment": art2015})
                    elif body.lower() == "арты 2016":
                        self.vk.method("messages.send", {"peer_id": id, "message": "2016", "attachment": art2016})
                    elif body.lower() == "арты 2017":
                        self.vk.method("messages.send", {"peer_id": id, "message": "2017", "attachment": art2017})
                    elif body.lower() == "хочу арт":
                        self.vk.method("messages.send", {"peer_id": id, "message": "Портрет (200 р)"
                                                                                   "По пояс (500 р)"
                                                                                   "В полный рост (700 р)"
                                                                                "Чтобы выбрать напиши 'Портрет'/'По пояс'/'В полный рост'"})
                    elif body.lower() == "портрет":
                        self.vk.method("messages.send", {"peer_id": id, "message": "Вы заказали портрет. Стоимость 200 рублей. Дождитесь пока я свяжусь с вами."})
                    elif body.lower() == "по пояс":
                        self.vk.method("messages.send", {"peer_id": id, "message": "Вы заказали арт по пояс. Стоимость 500 рублей. Дождитесь пока я свяжусь с вами."})
                    elif body.lower() == "в полный рост":
                        self.vk.method("messages.send", {"peer_id": id, "message": "Вы заказали арт в полный рост. Стоимость 700 рублей. Дождитесь пока я свяжусь с вами."})
                    else:
                        self.vk.method("messages.send", {"peer_id": id, "message": "Я тебя не понимаю"})
            except Exception as E:
                time.sleep(1)





bot = VkBot()
bot.bot()
