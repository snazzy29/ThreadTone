import os
import json

jsonpath = "json_output/"
svgpath = "svg_output/"

jsondata = []
for r, d, f in os.walk(jsonpath):
    for file in f:
        if ".json" in file:
            print(file)
            f = open(os.path.join(r, file), "r")

            corename,ext = os.path.splitext(os.path.basename(file))
            svgfile = svgpath+corename+'.svg'

            if f.mode == "r":
                pathdata = f.read()
                loadedlines = json.loads(pathdata)
                print(len(loadedlines))
                jsondata.append(loadedlines)
            f.close()


print(svgfile)
svgf = open(svgfile, "r")
svg = svgf.read()
#print(svg)
svgf.close()

htmlf = open("ThreadTone/template.html", "r")
template = htmlf.read()
htmlf.close()


html = template.replace("[[data]]", json.dumps(jsondata))
html = html.replace("[[svg]]", svg)
#print(html)

indexf = open("index.html", "w")
indexf.write(html)
indexf.close()