import vk_api
import time


class VkBot:
    def bot(self):
        token = "fa804c84d0f722ec41819722652f0aceed51cf5ad2e3bc14f016a8a8090dd44bc95467328eb9c2d1e0000"
        self.vk = vk_api.VkApi(token=token)
        self.vk._auth_token()

        while True:
            try:
                messages = self.vk.method("messages.getConversations", {"offset": 0, "count": 200})
                if messages["count"] >= 1:
                    id = messages["items"][0]["last_message"]["from_id"]
                    body = messages["items"][0]["last_message"]["text"]
                    if body.lower() == "привет":
                        from VkBot import com
                        com = com()
                        com.bot()
                    elif body.lower() == "команды":
                        from VkBot import com
                        com = com()
                        com.bot()
                    else:
                        self.vk.method("messages.send", {"peer_id": id, "message": "Я вас не понимаю. Напишите 'привет' или 'команды'\n\n"
                                                                                   "Если вы видите это сообщение при повторном заказе арта: \n"
                                                                                   "Заказывать несколько артов нельзя, дождитесь пока я приму заказ и свяжусь с вами. \n"
                                                                                   "Если вы передумали и хотите что-то другое, то вам снова нужно ввести 'привет' или 'команды'. \n"
                                                                                   "Хочу обратить внимание, что учитывается ваш последний заказ."})
            except Exception as E:
                time.sleep(1)





bot = VkBot()
bot.bot()
