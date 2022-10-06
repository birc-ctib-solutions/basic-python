
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
while len(x) > 1:
    x.pop()
    print(*x)
