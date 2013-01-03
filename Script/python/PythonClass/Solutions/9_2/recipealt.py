# recipe.py

ingredients = [
    u"Avocado",
    u"Tomato",
    u"Red Onion",
    u"Jalape\u00f1o pepper",
    u"Cilantro",
    u"Sea Salt",
]

header = u"""
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head>
<body>
"""

footer = u"""
</body>
</html>
"""

import io

f = io.open("output.html","w",encoding="utf-8")
f.write(header)
for item in ingredients:
    f.write(u"<li>%s</li>\n" % item)
f.write(footer)
f.close()

import webbrowser
import os
webbrowser.open("file:///"+os.path.abspath("output.html"))
