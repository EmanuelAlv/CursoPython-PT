
# def myfunc (*args):
#     mylist = []
#     for i in args:
#         if i%2 == 0:
#             mylist.append(i)
#         else:
#             pass
#     # return mylist
#     print(mylist)            

# myfunc(1,2,3,4,5,6,7,8,9)



cadena = 'parangaracutirimicuaro'
def myfunc (cadena):
    resultado =''
    for i in range(len(cadena)):
        if i%2 == 0:
            resultado += cadena[i].upper()
        else:
            resultado += cadena[i].lower()
    return cadena

myfunc(cadena)