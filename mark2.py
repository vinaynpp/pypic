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
    if code == "d_v_p":
        fdir = "export/nssday2020/participants/" + fname + ".png"
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

        PON = POF + POL

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
