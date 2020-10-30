import re
user_input = input("Enter an email address")

pattern = "([0-9a-zA-z$#!]+)@(google|hotmail|gmail).(com)"
ans = re.match(pattern, user_input)

print(ans.group(2))


# ([0-9a-zA-z$#!]{8})@(google|hotmail|gmail).(com)