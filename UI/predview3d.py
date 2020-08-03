import bs4
import os
import sys

x=sys.argv[1]
filename = "predictedtrajectories/"+x
# load the file
with open("views/predview3dall.ejs") as inf:
    txt = inf.read()
    soup = bs4.BeautifulSoup(txt)

newinputp1="input id=\"filename\" type=\"hidden\" value=\""
newinputp2="\"/"

newinput='<'+newinputp1+filename+newinputp2+'>'
soup.body.input.replace_with(newinput)
# create new link
# print soup
# insert it into the document


# save the file again
with open("views/predview3dall.ejs", "w") as outf:
    outf.write(str(soup.encode(formatter=None)))