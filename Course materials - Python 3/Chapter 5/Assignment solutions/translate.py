# 3.3 translate.py
# Turn a user's input into leetspeak

myText = input("Enter some text: ")

myText = myText.replace("a", "4")
myText = myText.replace("b", "8")
myText = myText.replace("e", "3")
myText = myText.replace("l", "1")
myText = myText.replace("o", "0")
myText = myText.replace("s", "5")
myText = myText.replace("t", "7")

print(myText)
