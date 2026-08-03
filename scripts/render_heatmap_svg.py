import json

# -----------------------------
# Read contributions
# -----------------------------
with open("data/contributions.json", "r") as file:
    contributions = json.load(file)

# -----------------------------
# GitHub color palette
# -----------------------------
palette = {
    0: "#161b22",
    1: "#0e4429",
    2: "#006d32",
    3: "#26a641",
    4: "#39d353",
    5: "#69f0a0"
}

# -----------------------------
# Create SVG
# -----------------------------
svg = open("contrib-heatmap.svg", "w", encoding="utf-8")

svg.write("""<?xml version="1.0" encoding="UTF-8"?>

<svg xmlns="http://www.w3.org/2000/svg"
width="900"
height="200">

<rect
width="900"
height="200"
fill="#0d1117"/>

""")

# -----------------------------
# Month labels
# -----------------------------
months = [
    ("Aug", 40),
    ("Sep", 100),
    ("Oct", 165),
    ("Nov", 230),
    ("Dec", 295),
    ("Jan", 360),
    ("Feb", 425),
    ("Mar", 490),
    ("Apr", 555),
    ("May", 620),
    ("Jun", 685),
    ("Jul", 750)
]

for month, pos in months:

    svg.write(f'''
<text
x="{pos}"
y="18"
font-size="10"
fill="#8b949e"
font-family="Arial">
{month}
</text>
''')

# -----------------------------
# Day labels
# -----------------------------
days = [
    ("Mon",55),
    ("Wed",83),
    ("Fri",111)
]

for day,ypos in days:

    svg.write(f'''
<text
x="5"
y="{ypos}"
font-size="10"
fill="#8b949e"
font-family="Arial">
{day}
</text>
''')

# -----------------------------
# Draw Heatmap
# -----------------------------
x = 30
y = 30

for item in contributions:

    level = int(item["level"])

    if level not in palette:
        level = 0

    color = palette[level]

    svg.write(f'''
<rect
x="{x}"
y="{y}"
width="10"
height="10"
rx="2"
fill="{color}"/>
''')

    y += 14

    if y > 114:
        y = 30
        x += 14

# -----------------------------
# Legend
# -----------------------------
svg.write('''
<text
x="650"
y="175"
font-size="10"
fill="#8b949e"
font-family="Arial">
Less
</text>
''')

legend_colors = [
"#161b22",
"#0e4429",
"#006d32",
"#26a641",
"#39d353"
]

legend_x = 680

for color in legend_colors:

    svg.write(f'''
<rect
x="{legend_x}"
y="165"
width="10"
height="10"
rx="2"
fill="{color}"/>
''')

    legend_x += 14

svg.write('''
<text
x="760"
y="175"
font-size="10"
fill="#8b949e"
font-family="Arial">
More
</text>
''')

# -----------------------------
# Footer
# -----------------------------
svg.write(f'''
<text
x="30"
y="175"
font-size="12"
fill="#8b949e"
font-family="Arial">
{len(contributions)} days loaded
</text>
''')

svg.write("</svg>")

svg.close()