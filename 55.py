import re
user = input()

pattern = "\d+"
ans = re.findall(pattern, user)
print(ans)
