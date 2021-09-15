from time import sleep

t = int(input("Enter seconds: "))
text = input("Enter text: ")

while t != 0:
    print(t)
    t -= 1
    sleep(1)
print(text)