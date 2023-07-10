from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

text1 = requests.get("https://www.dominos.co.in/menu/veg-pizzas")
text_non_veg = requests.get("https://www.dominos.co.in/menu/non-veg-pizzas")
text_sides = requests.get("https://www.dominos.co.in/menu/side-orders")

print(text1)
print(text_non_veg)
print(text_sides)

veg_pizza = []
non_veg_pizzaa = []
sides = []

soup = bs(text1.text,'html.parser')
name = soup.find_all(class_ = "row")
v_des = []
for i in name:
    name =  i.find('h3')
    na = i.find('p')
    fii = na.text
    final = name.a.text
    veg_pizza.append(final)
    v_des.append(fii)

soup = bs(text_non_veg.text,'html.parser')
name = soup.find_all(class_ = "row")
n_des = []
for i in name:
    name =  i.find('h3')
    na = i.find('p')
    fii = na.text
    final = name.a.text
    non_veg_pizzaa.append(final)
    n_des.append(fii)
    
soup = bs(text_sides.text,'html.parser')
name = soup.find_all(class_ = "row")
s_des = []
for i in name:
    name =  i.find('h3')
    na = i.find('p')
    fii = na.text
    final = name.a.text
    sides.append(final)
    s_des.append(fii)

# # for x in name:
# #     na = x.find('p')
# #     print(na)
# print(des)
    
our_data1 = pd.DataFrame({"veg_Pizza Names":veg_pizza,"Description":v_des})
our_data1.to_csv("/Users/jarvis/pymycod/automation/csvinfo/veg_dominoes_pizza.csv")

our_data2 = pd.DataFrame({"non_Pizza Names":non_veg_pizzaa,"Description":n_des})
our_data2.to_csv("/Users/jarvis/pymycod/automation/csvinfo/non_dominoes_pizza.csv")

our_data3 = pd.DataFrame({"sides_Names":sides,"Description":s_des})
our_data3.to_csv("/Users/jarvis/pymycod/automation/csvinfo/sides_dominoes_pizza.csv")
