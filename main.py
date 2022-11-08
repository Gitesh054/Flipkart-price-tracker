import requests
from bs4 import BeautifulSoup
import smtplib

LOGIN_ID = "gitesh16patidar@gmail.com"
PASSWORD = "laddla@123"
URL = "https://www.flipkart.com/hp-pavilion-ryzen-5-hexa-core-5600h-8-gb-512-gb-ssd-windows-10-4-graphics-nvidia-geforce-gtx-1650-144-hz-15-ec2004ax-gaming-laptop/p/itm98c94bbf9bc20?pid=COMG5GZXPWMGTNWS&lid=LSTCOMG5GZXPWMGTNWSQE9WVW&marketplace=FLIPKART&q=hp+pavilion&store=6bo%2Fb5g&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=45237486-a5d7-42b5-9da8-15fa2e232939.COMG5GZXPWMGTNWS.SEARCH&ppt=sp&ppn=sp&ssid=sovce15lrk0000001662740386758&qH=aa80261108f076e0"
response = requests.get(URL)
print(response.status_code)
flipkart_data = response.text

soup = BeautifulSoup(flipkart_data, "html.parser")
# print(soup.prettify)

price_div = soup.find(name = "div", class_="_30jeq3 _16Jk6d")
price = price_div.getText()

print(price)
for p in price:
    if p

# price_list = []
# total = 0
# for i in range(len(price)):
#     if i==0:
#         pass
#     else:
#         price_list.append(price[i])
#
# # print(price_list)
# final_price = price_list[0]+price_list[1]+price_list[2]
# # final_price = int(final_price)
# print(final_price)

# if final_price < 603:
#     with smtplib.SMTP("smtp.gmail.com", port= 587) as connection :
#         connection.starttls()
#         connection.login(user=LOGIN_ID, password=PASSWORD)
#         connection.sendmail(from_addr=LOGIN_ID, to_addrs="gitesh16patidar@yahoo.com",
#                             msg=f"Flipkart price drop alert\n Wildcraft bag now available below 603 !\n Link:{URL}")



