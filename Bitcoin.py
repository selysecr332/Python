import requests
import time

# global variables

api_kay = 'eae6b318-43ee-4129-8a31-8a5c30309af1'
bot_kay = '1862183157:AAEBWJO6tcKdIyGnjIbM8XYIdD8NXWrYI8U'
chat_id = '1038663932'
# سعر العملة
limit  = 50000
limit2 = 10000
# limit2 = 10000
# يعمل الفحص كل اد اية
time_interval  = 60
time_interval2 = 60*5




def get_price():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

#الحاجات الي هطلبها من الموقع
    parameters = \
    {
        'start': '1',
        'limit': '2',
        'convert': 'USD'
    }
#الطريقة الي هنكلم بيها الموقع
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_kay,
    }



    response = requests.get(url, headers=headers, params=parameters).json()
    btc_price = response['data'][0]['quote']['USD']['price']

    return btc_price

#سعر العملة الثانية



#الدلة بتاعتك ارسال رسالة لي في حال زيادة السعر

def send_update(chat_id, msg):
    url = f" https://api.telegram.org/bot{bot_kay}/sendMessage?chat_id={chat_id}&text={msg}"
    requests.get(url)


#هنعمل الطريق الي هيغ الطريقة ظي

def main():
    while True:
        price = get_price()
        print(price)
        if price < limit:
            send_update(chat_id, f"The Price of Bitcoin is:\n{ price}")

    # هنستخدك مكتبة الوقت لكي نرسل اشعار كل مده معينه

        time.sleep(time_interval)



main()




name = input("Enter your name pls: ")
