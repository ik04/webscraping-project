from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

text1 = requests.get("https://www.dominos.co.in/menu/veg-pizzas")

soup = bs(text1.text, "html.parser")
row = soup.find_all(class_="row")
pizza_names = []
des = []
for i in row:
    name = i.find("h3")
    final = name.a.text
    pizza_names.append(final)

print(pizza_names)

for x in row:
    desc = x.find("p").get_text()
    finakl = desc
    des.append(desc)


our_data = pd.DataFrame({"Pizza Names": pizza_names, "Description": des})
json_output = our_data.to_json()

print(json_output)
with open("./output.json", "w") as fs:
    fs.write(json_output)
