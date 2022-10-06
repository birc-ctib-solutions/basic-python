
# Print the pattern
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
x = []
for _ in range(5):
    x.append('*')
    print(*x)
while x:
    x.pop()
    print(*x)
