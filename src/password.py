import sys

if len(sys.argv) != 2:
    print(f"{sys.argv[0]} expected exactly one argument.")
    sys.exit(1)

password = sys.argv[1]
is_valid = any(a.islower() for a in password) and \
    any(a.isupper() for a in password) and \
    any(a.isnumeric() for a in password) and \
    any(a in "$#@" for a in password) and \
    6 <= len(password) <= 16
print(is_valid)
