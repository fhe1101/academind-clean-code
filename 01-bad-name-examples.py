from datetime import datetime

# self is the this keyword in other languages such as C++
class Entity:
    def __init__(self, title, description, ymdhm):
        self.title = title
        self.description = description
        self.ymdhm = ymdhm
# Entity seems to be some kind of blog post. ymdhm is a date

# Tis is a function, not a method based on the indentation
# it prints blog post
## item name is better for blog_post
def output(item):
    print('Title: ' + item.title)
    print('Description: ' + item.description)
    print('Published: ' + item.ymdhm)


# summary is actually  title
summary = 'Clean Code Is Great!'
desc = 'Actually, writing Clean Code can be pretty fun. You\'ll see!'
# new_data is ok, but today or now is better
new_date = datetime.now()
# publish like a command, formatted_data is a better name
publish = new_date.strftime('%Y-%m-%d %H:%M')

item = Entity(summary, desc, publish)

output(item)
