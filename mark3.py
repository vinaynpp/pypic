import csv
from PIL import Image, ImageDraw, ImageFont

print("")
print("NOW MAIN TASK STARTS")
print("")


def dirgen(code, fname):
    global fdir
    if code == "d_p_p":
        fdir = "export/nssday2020/po/" + fname + ".png"
    if code == "d_p_w":
        fdir = "export/nssday2020/po/winner/" + fname + ".png"
    if code == "d_v_pb":
        fdir = "export/nssday2020/participants/Virtual Bingo/" + fname + ".png"
    if code == "d_v_pk":
        fdir = "export/nssday2020/participants/Kavyanjali/" + fname + ".png"
    if code == "d_v_pp":
        fdir = "export/nssday2020/participants/Poster Making/" + fname + ".png"
    if code == "d_v_ps":
        fdir = "export/nssday2020/participants/Step Up India/" + fname + ".png"
    if code == "d_v_w":
        fdir = "export/nssday2020/participants/winner/" + fname + ".png"
    if code == "d_c":
        fdir = "export/nssday2020" + fname + ".png"
    return fdir


with open("po.csv") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row

    for Ts, POF, POL, POE, POC, CN, QnA, views, rate, sug in reader:
        image = Image.open('source/images/po_particiption.png')
        draw = ImageDraw.Draw(image)
        color = 'rgb(0, 0, 0)'

        PON = POF + " " + POL

        (x, y) = (355, 260)
        font = ImageFont.truetype('source/fonts/Sofia-Regular.ttf', size=18)
        draw.text((x, y), PON, fill=color, font=font)

        (x, y) = (315, 285)
        font = ImageFont.truetype('source/fonts/Sofia-Regular.ttf', size=12)
        draw.text((x, y), CN, fill=color, font=font)

        (x, y) = (105, 300)
        font = ImageFont.truetype('source/fonts/Sofia-Regular.ttf', size=18)
        draw.text((x, y), "Virtual Quiz", fill=color, font=font)

        image.save(dirgen("d_p_p", PON))

with open("nsslist/Bingo.csv") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row

    for FS, LS, ES, CS, CN in reader:
        image = Image.open('source/images/nss_participation.png')
        draw = ImageDraw.Draw(image)
        color = 'rgb(0, 0, 0)'

        NS = FS + " " + LS

        (x, y) = (365, 245)
        font = ImageFont.truetype('source/fonts/Sofia-Regular.ttf', size=18)
        draw.text((x, y), NS, fill=color, font=font)

        (x, y) = (270, 275)
        font = ImageFont.truetype('source/fonts/Sofia-Regular.ttf', size=12)
        draw.text((x, y), CN, fill=color, font=font)

        (x, y) = (255, 300)
        font = ImageFont.truetype('source/fonts/Sofia-Regular.ttf', size=18)
        draw.text((x, y), "Virtual Bingo", fill=color, font=font)

        image.save(dirgen("d_v_pb", NS))


with open("nsslist/Kavyanjali.csv") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row

    for FS, LS, ES, CS, CN in reader:
        image = Image.open('source/images/nss_participation.png')
        draw = ImageDraw.Draw(image)
        color = 'rgb(0, 0, 0)'

        NS = FS + " " + LS

        (x, y) = (365, 245)
        font = ImageFont.truetype('source/fonts/Sofia-Regular.ttf', size=18)
        draw.text((x, y), NS, fill=color, font=font)

        (x, y) = (270, 275)
        font = ImageFont.truetype('source/fonts/Sofia-Regular.ttf', size=12)
        draw.text((x, y), CN, fill=color, font=font)

        (x, y) = (255, 300)
        font = ImageFont.truetype('source/fonts/Sofia-Regular.ttf', size=18)
        draw.text((x, y), "Kavyanjali", fill=color, font=font)

        image.save(dirgen("d_v_pk", NS))

with open("nsslist/Poster.csv") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row

    for FS, LS, ES, CS, CN in reader:
        image = Image.open('source/images/nss_participation.png')
        draw = ImageDraw.Draw(image)
        color = 'rgb(0, 0, 0)'

        NS = FS + " " + LS

        (x, y) = (365, 245)
        font = ImageFont.truetype('source/fonts/Sofia-Regular.ttf', size=18)
        draw.text((x, y), NS, fill=color, font=font)

        (x, y) = (270, 275)
        font = ImageFont.truetype('source/fonts/Sofia-Regular.ttf', size=12)
        draw.text((x, y), CN, fill=color, font=font)

        (x, y) = (255, 300)
        font = ImageFont.truetype('source/fonts/Sofia-Regular.ttf', size=18)
        draw.text((x, y), "Poster Making", fill=color, font=font)

        image.save(dirgen("d_v_pp", NS))

with open("nsslist/Step.csv") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row

    for FS, LS, ES, CS, CN in reader:
        image = Image.open('source/images/nss_participation.png')
        draw = ImageDraw.Draw(image)
        color = 'rgb(0, 0, 0)'

        NS = FS + " " + LS

        (x, y) = (365, 245)
        font = ImageFont.truetype('source/fonts/Sofia-Regular.ttf', size=18)
        draw.text((x, y), NS, fill=color, font=font)

        (x, y) = (270, 275)
        font = ImageFont.truetype('source/fonts/Sofia-Regular.ttf', size=12)
        draw.text((x, y), CN, fill=color, font=font)

        (x, y) = (255, 300)
        font = ImageFont.truetype('source/fonts/Sofia-Regular.ttf', size=18)
        draw.text((x, y), "Step Up India", fill=color, font=font)

        image.save(dirgen("d_v_ps", NS))