from PIL import Image

image = Image.open("white_bg.png")
image = image.resize((100,53))
image = image.convert("L")

ASCII_CHARS = " .`:-=+*cs#%@"

ascii_image = []

for y in range(image.height):
    row = ""

    for x in range(image.width):
        pixel = image.getpixel((x, y))

        index = pixel * (len(ASCII_CHARS)-1) // 255

        character = ASCII_CHARS[index]

        row += character

    ascii_image.append(row)
svg = open("avi-ascii.svg", "w")

svg.write("""<svg xmlns="http://www.w3.org/2000/svg"
width="900"
height="700"
style="background:black">
""")

y = 20
delay = 0

for row in ascii_image:

    svg.write(f'''
<text x="20"
      y="{y}"
      font-family="Courier New"
      font-size="10"
      fill="white"
      opacity="0">

{row}

<animate
attributeName="opacity"
from="0"
to="1"
begin="{delay}s"
dur="0.05s"
fill="freeze"/>

</text>
''')
    y += 12
delay += 0.05

svg.write("</svg>")

svg.close()                   