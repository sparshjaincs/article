from django import template

register = template.Library()

@register.filter
def replace(value):
    return value.replace(" ","_")

@register.filter
def split(value,field):
    return value.split(field)

@register.filter
def remove(value):
    return value.split(",")

@register.filter
def strip(value):
    return value.strip(" ")

@register.filter
def remove(value):
    return value.split(",")


@register.filter
def addhyphen(value):
    return "_".join(value.split(" "))

@register.filter
def getlatest(value):
    value = list(value)
    value.sort(key=lambda x:(x.date,x.time),reverse = True)
    if len(value) == 0:
        value = ["Write Your First Anwser.."]
    else:
        value = value
    return value

@register.filter
def latest(value):
    value = list(value)
    value.sort(key=lambda x:(x.date,x.time),reverse = True)
    if len(value) == 0:
        value = ["Write Your First Anwser.."]
    else:
        value = [value[0]]
    return value