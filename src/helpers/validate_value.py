import re
import datetime

# valid return the value, or return null string
def validateValue(value, valueType):
    validated_value = ''
    if valueType == 'recipient':
        pattern = re.compile("^\w+$")
        if pattern.match(value) and len(value) == 9:
            validated_value = value
    elif valueType == 'zipcode':
        pattern = re.compile("^\d+$")
        if pattern.match(value) and len(value) >= 5:
            validated_value = value[:5]
    elif valueType == 'year':
        try:
            datetime.datetime(year=int(value[4:]),month=int(value[:2]),day=int(value[2:4]))
            correctDate = True
        except ValueError:
            correctDate = False
        pattern = re.compile("^\d+$")
        if pattern.match(value) and len(value) == 8 and correctDate:
            validated_value = value[4:]
    elif valueType == 'name':
        pattern = re.compile("^([a-zA-Z]+)[,]([a-zA-Z\s]+)+$")
        if pattern.match(value):
            validated_value = value
    elif valueType == 'amount':
        pattern = re.compile("^\d*[.]?\d{0,2}$")
        if pattern.match(value):
            validated_value = value
    return validated_value