import os

os.system('clear')

path = r'/home/jasmin/Documents/project/learning_python2023/20-01-2023/'
f = input("Enter your name ")
file_path = path+f+".txt"
# print(file_path)
fn = f+".txt"
# print(fn)

with open(file_path, 'w') as fp:
    fp.write(f)

 


x = ["Hey you \n", "are you crazy \n", "or insane"]
x = 5
e = []


while (x > 0):
    print("How are you feeling write now ?")
    print("Tell me 5 feelings")
    n = input(f'{x} :')
    e.append(f'{n} \n')
    x = x-1


s = open(fn, 'w')
s.writelines(e)
s.close()


s = open(fn)
l = s.readlines()
for n in l:
    print(n)

s.close()
