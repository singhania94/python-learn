import bs4 as bs

# tag - head, body, div, ol, li, h1, h3
# id - assigned unique across html - selected in css by #
# class - similar set - selected by .
# children - subset - selected by div > p
# descendants - selected by div p

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>First HTML page</title>
</head>
<body>
    <div id="first">
        <h3 data-example="yes">hi</h3>
        <p>more text.</p>
    </div>
    <ol>
        <li class="special">This list item is special.</li>
        <li class="special">This list item is also special.</li>
        <li>This list item is not special.</li>
    </ol>
    <div>bye</div>
</body>
</html>
"""

v = bs.BeautifulSoup(html, "html.parser")               # also supports XML
# Now we have several ways to navigate.
# 1. By Tag Name
# 2. Using find - returns one matching tag
# 3. final_all
# 4. select - using css selectors

# v.body
# v.body.div
v.find_all("div/li/body etc...")     # find by tag
print(v.find(id='first'))           # find by id
print(v.find_all(class_="special"))
print(v.find(attrs={"data-example": "yes"}))
# print(v.select("li/#first"))
print(v.select("[data-example]"))

s = v.select(".special")[0]
text = s.get_text         # inner text
n = s.name                # tag name
attr = s.attrs
attr = v.find("div")["id"]

v.body.contents     # prints all the contents including /n, goes one level down
data = v.body.contents[1]      # contents[1] refers to <div id='first'>
sibling = data.next_sibling.next_sibling        # /n and <ol> after that, goes through the list, previous_sibling
                                                # find_next_sibling() skips /n's, also takes in attrs, class_ or tags
parent = sibling.parent        # going one level up, also find_parent(), takes in params as find_next_sibling()
print(parent)

# web crawling


