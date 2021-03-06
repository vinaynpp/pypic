import yagmail
import keyring
import csv
from PIL import Image, ImageDraw, ImageFont

contents = """Hello Sir/Madam
    Congratulations on your well - deserved success.
    The NSS unit of Universal College of Engineering would like to thank you
    for participating in Inter College Event organised on 24th September 2020.

    We have attached your certificate in this email.
    Wish you all the best for your future endeavours.

    Reagards,
    NSS UCoE."""

print("lets start")
meraemail = "nssucoearchive@gmail.com"
merapswd = "ucoerocx"

yagmail.register(meraemail, merapswd)

print("loggedin")
with yagmail.SMTP(meraemail) as yag:
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


    image = Image.open('source/images/college_winner.png')

    # initialise the drawing context with
    # the image object as background

    draw = ImageDraw.Draw(image)
    # desired size

    font = ImageFont.truetype('source/fonts/Roboto-Bold.ttf', size=15)
    (x, y) = (280, 245)
    message = "SHREE L. R. TIWARI COLLEGE OF ENGINEERING "
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), message, fill=color, font=font)
    image.save(dirgen("d_c", message))
    yag.send(meraemail, "NSS DAY CERTIFICATE", [contents, dirgen("d_c", message)])

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
                yag.send(E, "NSS DAY CERTIFICATE", [contents, dirgen("d_p_w", N)])
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
                    yag.send(E, "NSS DAY CERTIFICATE", [contents, dirgen("d_v_wp", N)])
                if event.count("Bingo") != 0:
                    (x, y) = (420, 240)
                    font = ImageFont.truetype('source/fonts/Sofia-Regular.ttf', size=14)
                    draw.text((x, y), "Virtual Bingo", fill=color, font=font)
                    image.save(dirgen("d_v_wb", N))
                    yag.send(E, "NSS DAY CERTIFICATE", [contents, dirgen("d_v_wb", N)])
                if event.count("Kaavyanjali") != 0:
                    (x, y) = (420, 240)
                    font = ImageFont.truetype('source/fonts/Sofia-Regular.ttf', size=14)
                    draw.text((x, y), "Kavyanjali", fill=color, font=font)
                    image.save(dirgen("d_v_wk", N))
                    yag.send(E, "NSS DAY CERTIFICATE", [contents, dirgen("d_v_wk", N)])
                if event.count("Step Up India") != 0:
                    (x, y) = (420, 240)
                    font = ImageFont.truetype('source/fonts/Sofia-Regular.ttf', size=14)
                    draw.text((x, y), "Step Up India", fill=color, font=font)
                    image.save(dirgen("d_v_ws", N))
                    yag.send(E, "NSS DAY CERTIFICATE", [contents, dirgen("d_v_ws", N)])
                if event.count("Act") != 0:
                    (x, y) = (420, 240)
                    font = ImageFont.truetype('source/fonts/Sofia-Regular.ttf', size=14)
                    draw.text((x, y), "Solo Act", fill=color, font=font)
                    image.save(dirgen("d_v_wa", N))
                    yag.send(E, "NSS DAY CERTIFICATE", [contents, dirgen("d_v_wa", N)])

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
            yag.send(POE, "NSS DAY CERTIFICATE", [contents, dirgen("d_p_p", PON)])

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
            yag.send(ES, "NSS DAY CERTIFICATE", [contents, dirgen("d_v_pb", NS)])

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
            yag.send(ES, "NSS DAY CERTIFICATE", [contents, dirgen("d_v_pk", NS)])

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
            yag.send(ES, "NSS DAY CERTIFICATE", [contents, dirgen("d_v_pp", NS)])

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
            yag.send(ES, "NSS DAY CERTIFICATE", [contents, dirgen("d_v_ps", NS)])

print("successfull")
