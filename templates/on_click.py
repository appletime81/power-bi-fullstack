# add a <p> element to the document
def add_p(*ags, **kws):
    title = Element("Title")

    # add <p>
    p = Element("p")
    p.text = "This is a paragraph"
    title.append(p)


add_p()
