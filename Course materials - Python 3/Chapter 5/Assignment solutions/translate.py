# 5.3 translate.py
# Turn a user's input into leetspeak

my_text = input("Enter some text: ")

my_text = my_text.replace("a", "4")
my_text = my_text.replace("b", "8")
my_text = my_text.replace("e", "3")
my_text = my_text.replace("l", "1")
my_text = my_text.replace("o", "0")
my_text = my_text.replace("s", "5")
my_text = my_text.replace("t", "7")

print(my_text)
