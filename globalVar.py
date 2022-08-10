# text = 'shirin'  # Global var
#
# def meva():
#     # return text
#     txt = 'achchiq'  # local var
#
# # print(txt)  # error
#
# print('Meva tami', meva())

count = 0

def f():
    global count
    count += 1

f()
f()
f()
print(count)


