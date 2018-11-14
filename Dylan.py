import pyautogui as pg
import webbrowser as wb
import time as t

points = 0
show = pg.prompt ("what is your favorite show?")

if show == "hannah montana":
    pg.alert ("OMG LOL xD")
    poins += 8
elif show == "The Office":
    pg.alert ("Dwight K Schrute")
    points -= 8
    t.sleep(1)
    wb.open("https://www.youtube.com/watch?v=GU2W_nlijx0")
elif show == "ESPN":
    pg.alert ("syntax error")
    points += 8
    wb.open("https://www.youtube.com/watch?v=u1ceVE8mOXg")
elif show == "Twitch":
    pg.alert ("Website Blocked")
    points += 7
    wb.open("https://www.youtube.com/watch?v=52wJFClbSeg")
elif show == "news":
    pg.alert ("why would you watch the news")
    points += 1.6
elif show == "Parks and Rec":
    pg.alert ("false")
    points -= 4.3
    t.sleep(1)
    wb.open("https://www.youtube.com/watch?v=ClzJkv3dpY8")
else:
    pg.alert ("your favorite show is" + show)

animal = pg.prompt ("what is your favorite animal?")

if animal == "Chuck-E-Cheese":
    pg.alert ("maybe")
    points += 214
elif animal == "dog":
    pg.alert ("no")
    points -= 7
    wb.open("https://www.youtube.com/watch?v=31v2DpFQdzU")
elif animal == "squirrel":
    pg.alert ("koola bear")
    points += 17
elif animal == "rat":
    pg.alert ("omg lol xD")
    points += 452
    wb.open("https://www.youtube.com/watch?v=v-1MQ0Cnbhs")
elif animal == "donkey":
    pg.alert ("congrats you like donkeys")
    points += 16
    t.sleep(1)
    wb.open("https://www.youtube.com/watch?v=ixQ_X6dScNE")
elif animal == "loot llama":
    pg.alert ("fortnite is dying")
    points -= 13
    t.sleep(1)
    wb.open("https://www.youtube.com/watch?v=pytQ1AUzhA8")
else:
    pg.alert ("your favorite animal is " + animal)

videogame = pg.prompt ("what is your favorite videogame?")

if videogame == "fortnite":
    pg.alert ("website blocked")
    points += 19
    t.sleep(1)
    wb.open("https://www.youtube.com/watch?v=3yQqNCOYfJo")
elif videogame == "2k":
    pg.alert ("ok")
    points += 17
elif videogame == "PUBG":
    pg.alert ("omg lol xD")
    points += 41
    wb.open("https://www.youtube.com/watch?v=sB-ncASj-Vk")
elif videogame == "minecraft":
    pg.alert ("omg lol xD")
    points += 623
    t.sleep (1)
    wb.open("https://www.youtube.com/watch?v=iL2emBaEtRo")
elif videogame == "Madden":
    pg.alert ("no")
    points -= 43
elif videogame == "tennis":
    pg.alert ("Zachary Toback is too good")
    points +=  1
    wb.open("https://www.youtube.com/watch?v=M8KmqaJvgpE")

else:
    pg.alert ("your favorite video game is" + videogame)

dessert = pg.prompt ("what is your favorite dessert")

if dessert == "ice cream":
    pg.alert ("decent")
    points += 2
elif dessert == "cake":
    pg.alert ("no")
    points -= 21
    t.sleep(1)
    wb.open("https://www.youtube.com/watch?v=fOwXHbxn2zg")
elif dessert == "cupcake":
    pg.alert ("maybe")
    points += 21
    t.sleep(1)
    wb.open("https://www.youtube.com/watch?v=YU2l6ZX-e4I")
    wb.open("https://www.youtube.com/watch?v=3DMF3ORG6Xg")
elif dessert == "cookies":
    pg.alert ("omg lol xD")
    points += 36
elif dessert == "milk":
    pg.alert ("syntax error")
elif dessert == "cheescake":
    pg.alert ("congrats you win +6 points")
    points = -6
    wb.open("https://www.youtube.com/watch?v=8H16SWHUAuM")
else:
    pg.alert ("your favorite animal is " + dessert)

shoebrand = pg.prompt ("what is your favorite shoebrand")

if shoebrand == "nike":
    pg.alert ("omg lol xD")
    points += 2
    wb.open("https://www.youtube.com/watch?v=0f-HOXTHxok")
elif shoebrand == "broooks":
    pg.alert ("Zach Toback")
    points -= 21
    wb.open("https://www.youtube.com/watch?v=cnuUfv4YJO0")
elif shoebrand == "adidas":
    pg.alert ("syntax error")
    points += 21
elif shoebrand == "puma":
    pg.alert ("Mo Bamba")
    points += 36
    t.sleep(1)
    wb.open("https://www.youtube.com/watch?v=BwIbsyQSFmI")
elif shoebrand == "reebok":
    pg.alert ("syntax error")
    t.sleep(1)
    wb.open("https://www.youtube.com/watch?v=SOKkz1mvkV0")
elif shoebrand == "Joma":
    pg.alert ("congrats you win +6 points")
    points = -6
else:
    pg.alert ("your favorite animal is " + shoebrand)

pg.alert (points)
