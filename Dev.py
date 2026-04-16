import random
fn = ["Cooper",
      "Shaw",
      "Porter",
      "Mason"]

ln = ["Thomas",
      "Siemon",
      "Mays",
      "Bradley"]

fi = open("Dev.txt", "w")

for i in range (6):
    x = random.choice(fn)
    y = random.choice(ln)
    g_one=random.randint(50,100)
    g_two=random.randint(60,100)
    g_three=random.randint(70,100)
    fi.write(f'{x} {y} {g_one} {g_two} {g_three}')
    fi.close()

