string = "this is a string"
def slugify(s):
    slug = s.split(" ")
    slug = "-".join(slug)
    print(slug)

slugify(string)