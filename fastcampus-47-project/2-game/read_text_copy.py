import random

f = open("cloud.txt", "r", encoding='UTF-8')
raw_data = f.read()
f.close()

data_list = raw_data.split("\n")

r_index = random.randrange(0, len(data_list))
word = data_list[r_index].replace(u"\xa0", u" ").split(" ")[0]
text = data_list[r_index].split()[1:]

print(word)
print(" ".join(text))