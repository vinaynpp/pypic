# import required classes

from PIL import Image, ImageDraw, ImageFont

# create Image object with the input image




image = Image.open('source/images/college_winner.png')

# initialise the drawing context with
# the image object as background

draw = ImageDraw.Draw(image)
# desired size

font = ImageFont.truetype('source/fonts/Roboto-Bold.ttf', size=15)

# starting position of the message

(x, y) = (280, 245)
message = "SHREE L. R. TIWARI COLLEGE OF ENGINEERING "
color = 'rgb(0, 0, 0)'  # black color
draw.text((x, y), message, fill=color, font=font)

# save the edited image
d_p_p = "export/nssday2020/po/"+message + ".png"
d_p_w = "export/nssday2020/po/winner/"+message + ".png"
d_v_p = "export/nssday2020/participants/"+message + ".png"
d_v_w = "export/nssday2020/participants/winner/"+message + ".png"
d_c = "export/nssday2020"+message + ".png"

image.save(d_c)
