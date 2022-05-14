import requests

def telegram_bot_sendtext(bot_message):

   bot_token = '5376762930:AAEr09cQy9qVMuqkjEDPn72Sdb40MqIh6y0'
   bot_chatID = '1078833160'
   send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

   response = requests.get(send_text)

   return response.json()


test = telegram_bot_sendtext("Testing Telegram bot")
print(test)


https://api.telegram.org/bot5376762930:AAEr09cQy9qVMuqkjEDPn72Sdb40MqIh6y0/sendMessage?chat_id=@testing1151&text=mani