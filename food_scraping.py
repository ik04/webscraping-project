from bs4 import BeautifulSoup as bs
import requests
import json

text1 = requests.get("https://www.dominos.co.in/menu/veg-pizzas")

soup = bs(text1.text, "html.parser")
row = soup.find_all(class_="row")

pizza_list = []

for i in row:
    name = i.find("h3")
    final = name.a.text

    desc = i.find("p").get_text()

    pizza = {"pizza_name": final, "description": desc}
    pizza_list.append(pizza)

output_dict = {"items": pizza_list}
json_output = json.dumps(output_dict, indent=4)

print(json_output)

with open("./output.json", "w") as fs:
    fs.write(json_output)
