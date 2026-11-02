cm = 170
total_inches = round(cm / 2.54)
# calculate the number of feet (division without remainder)
feet = total_inches // 12
# the inches that are left (remainder of the division)
inches = total_inches % 12

print(f'I am {cm}cm tall, i.e. {feet} feet and {inches} inches')
