import re
user_input = input("Enter an email address")

pattern = "(\w+)@((\w+\.)+(com))"
ans = re.match(pattern, user_input)

print(ans.group(1))

# email = user_input.split('@')
# print(email[0])