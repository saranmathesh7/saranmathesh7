svg = open("info-card.svg", "w", encoding="utf-8")

svg.write("""<?xml version="1.0" encoding="UTF-8"?>

<svg xmlns="http://www.w3.org/2000/svg"
     width="520"
     height="330"
     viewBox="0 0 520 330">

<!-- Background -->
<rect x="5" y="5"
      width="510"
      height="320"
      rx="14"
      fill="#0d1117"
      stroke="#30363d"
      stroke-width="2"/>

<!-- Title Bar -->
<rect x="5"
      y="5"
      width="510"
      height="38"
      rx="14"
      fill="#161b22"/>

<!-- Mac Buttons -->
<circle cx="25" cy="24" r="6" fill="#ff5f56"/>
<circle cx="45" cy="24" r="6" fill="#ffbd2e"/>
<circle cx="65" cy="24" r="6" fill="#27c93f"/>

<!-- Prompt -->
<text x="95"
      y="30"
      font-family="Courier New"
      font-size="15"
      fill="#39d353">

saran@github:~$ neofetch

</text>

<!-- Name -->
<text x="20"
      y="70"
      font-family="Courier New"
      font-size="15"
      fill="white">

Name        : Saran Mathesh

</text>

<!-- Branch -->
<text x="20"
      y="95"
      font-family="Courier New"
      font-size="15"
      fill="white">

Branch      : CSE

</text>

<!-- Languages -->
<text x="20"
      y="120"
      font-family="Courier New"
      font-size="15"
      fill="white">

Languages   : C++, Python, Java

</text>

<!-- GitHub -->
<text x="20"
      y="145"
      font-family="Courier New"
      font-size="15"
      fill="white">

GitHub      : saranmathesh7

</text>

<!-- Interests -->
<text x="20"
      y="170"
      font-family="Courier New"
      font-size="15"
      fill="white">

Interests   : AI | Projects | Software Dev | Sports

</text>

<!-- Divider -->
<line x1="20"
      y1="195"
      x2="490"
      y2="195"
      stroke="#30363d"
      stroke-width="1"/>

<!-- Tech Stack -->
<text x="20"
      y="220"
      font-family="Courier New"
      font-size="15"
      fill="#39d353">

Tech Stack

</text>

<text x="20"
      y="245"
      font-family="Courier New"
      font-size="15"
      fill="white">

✔ C++

</text>

<text x="120"
      y="245"
      font-family="Courier New"
      font-size="15"
      fill="white">

✔ Java

</text>

<text x="220"
      y="245"
      font-family="Courier New"
      font-size="15"
      fill="white">

✔ Python

</text>

<text x="340"
      y="245"
      font-family="Courier New"
      font-size="15"
      fill="white">

✔ Git

</text>

<!-- Footer -->
<line x1="20"
      y1="270"
      x2="490"
      y2="270"
      stroke="#30363d"
      stroke-width="1"/>

<text x="20"
      y="295"
      font-family="Courier New"
      font-size="13"
      fill="#8b949e">

SRM Institute of Science and Technology

</text>

</svg>
""")

svg.close()