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
    if code == "d_v_wa":
        fdir = "export/nssday2020/participants/winner/Solo Act/" + fname + ".png"
    if code == "d_v_wb":
        fdir = "export/nssday2020/participants/winner/Virtual Bingo/" + fname + ".png"
    if code == "d_v_wk":
        fdir = "export/nssday2020/participants/winner/Kavyanjali/" + fname + ".png"
    if code == "d_v_wp":
        fdir = "export/nssday2020/participants/winner/Poster Making/" + fname + ".png"
    if code == "d_v_ws":
        fdir = "export/nssday2020/participants/winner/Step Up India/" + fname + ".png"
    if code == "d_c":
        fdir = "export/nssday2020/" + fname + ".png"
    return fdir


with open("winner.csv") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row

    for F, L, E, C, CN, event, rank in reader:
        if event == "Virtual Quiz":
            image = Image.open('source/images/po_winner.png')
            draw = ImageDraw.Draw(image)
            color = 'rgb(0, 0, 0)'

            N = F + " " + L

            (x, y) = (365, 214)
            font = ImageFont.truetype('source/fonts/Sofia-Regular.ttf', size=18)
            draw.text((x, y), N, fill=color, font=font)

            (x, y) = (260, 235)
            font = ImageFont.truetype('source/fonts/Sofia-Regular.ttf', size=12)
            draw.text((x, y), CN, fill=color, font=font)

            (x, y) = (190, 250)
            font = ImageFont.truetype('source/fonts/Sofia-Regular.ttf', size=14)
            draw.text((x, y), "Virtual Quiz", fill=color, font=font)

            if rank == "1":
                (x, y) = (550, 230)
                font = ImageFont.truetype('source/fonts/Sofia-Regular.ttf', size=20)
                draw.text((x, y), "    ------", fill=color, font=font)

            if rank == "2":
                (x, y) = (550, 230)
                font = ImageFont.truetype('source/fonts/Sofia-Regular.ttf', size=20)
                draw.text((x, y), "--     ---", fill=color, font=font)

            if rank == "3":
                (x, y) = (550, 230)
                font = ImageFont.truetype('source/fonts/Sofia-Regular.ttf', size=20)
                draw.text((x, y), "----  ", fill=color, font=font)

            image.save(dirgen("d_p_w", N))
        else:
            image = Image.open('source/images/volunteer_winning.png')
            draw = ImageDraw.Draw(image)
            color = 'rgb(0, 0, 0)'

            N = F + " " + L

            (x, y) = (390, 220)
            font = ImageFont.truetype('source/fonts/Sofia-Regular.ttf', size=18)
            draw.text((x, y), N, fill=color, font=font)

            if rank == "1":
                (x, y) = (220, 235)
                font = ImageFont.truetype('source/fonts/Sofia-Regular.ttf', size=20)
                draw.text((x, y), "    ------", fill=color, font=font)

            if rank == "2":
                (x, y) = (220, 235)
                font = ImageFont.truetype('source/fonts/Sofia-Regular.ttf', size=20)
                draw.text((x, y), "---     ---", fill=color, font=font)

            if rank == "3":
                (x, y) = (220, 235)
                font = ImageFont.truetype('source/fonts/Sofia-Regular.ttf', size=20)
                draw.text((x, y), "----  ", fill=color, font=font)

            if event.count("Poster") != 0:
                (x, y) = (420, 240)
                font = ImageFont.truetype('source/fonts/Sofia-Regular.ttf', size=14)
                draw.text((x, y), "Poster Making", fill=color, font=font)
                image.save(dirgen("d_v_wp", N))
            if event.count("Bingo") != 0:
                (x, y) = (420, 240)
                font = ImageFont.truetype('source/fonts/Sofia-Regular.ttf', size=14)
                draw.text((x, y), "Virtual Bingo", fill=color, font=font)
                image.save(dirgen("d_v_wb", N))
            if event.count("Kaavyanjali") != 0:
                (x, y) = (420, 240)
                font = ImageFont.truetype('source/fonts/Sofia-Regular.ttf', size=14)
                draw.text((x, y), "Kavyanjali", fill=color, font=font)
                image.save(dirgen("d_v_wk", N))
            if event.count("Step Up India") != 0:
                (x, y) = (420, 240)
                font = ImageFont.truetype('source/fonts/Sofia-Regular.ttf', size=14)
                draw.text((x, y), "Step Up India", fill=color, font=font)
                image.save(dirgen("d_v_ws", N))
            if event.count("Act") != 0:
                (x, y) = (420, 240)
                font = ImageFont.truetype('source/fonts/Sofia-Regular.ttf', size=14)
                draw.text((x, y), "Solo Act", fill=color, font=font)
                image.save(dirgen("d_v_wa", N))




