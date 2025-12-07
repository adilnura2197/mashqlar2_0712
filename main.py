#1-misol
r = input("Rang kirit: ")

if r == "qizil":
    print("To'xtang!")
elif r == "sariq":
    print("Tayyorlaning!")
elif r == "yashil":
    print("Yuring!")
else:
    print("Bunday rang yo'q")


#2-misol
t = int(input("Internet tezligini kirit: "))

if t > 100:
    print("Sizda yuqori tezlik!")
elif 50 <= t <= 100:
    print("Tezlik yaxshi, lekin yaxshilash kerak!")
elif 10 <= t <= 50:
    print("Tezlik past, provayder bilan bog'laning")
elif t < 10:
    print("Bu tezlik bilan internet ishlatib bo'lmaydi")


#3-misol
bal = int(input("Ball ni kirit: "))

if bal > 90:
    print("A’lo!")
elif 75 <= bal <= 89:
    print("Yaxshi!")
elif 50 <= bal <= 74:
    print("Qoniqarli")
elif bal < 50:
    print("Yiqildingiz!")
