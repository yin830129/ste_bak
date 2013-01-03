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
<body>
"""

footer = u"""
</body>
</html>
"""


f = open("output.html","w")
f.write(header.encode('ascii'))
for item in ingredients:
    f.write("<li>%s</li>\n" % item.encode('ascii','xmlcharrefreplace'))
f.write(footer.encode('ascii'))
f.close()

import webbrowser
import os
webbrowser.open("file:///"+os.path.abspath("output.html"))
