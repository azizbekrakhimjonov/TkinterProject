# text = 'shirin'
#
# def mevaTami():
#     return text


# text =text 'shirin'  # global var

# def mevaTami():
#     global text
#     text = 'achchiq'  # local var
#
#
# print('olma', text)
# mevaTami()



count = 0

def msg():
    global count
    count+=1

msg()
msg()
print(count)  # 2

