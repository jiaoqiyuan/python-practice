import json

# 如果以前存储了用户名就加载它
# 否则，就提示用户输入用户名并存储它


filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your nane? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We will remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!")
