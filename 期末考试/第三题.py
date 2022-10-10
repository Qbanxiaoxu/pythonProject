dicta = {"a":1,"b":2,"c":3,"d":4,"g":"hello"}
dictb = {"b":3,"d":5,"e":7,"f":"abc","g":"world"}
dictc={}
print(dicta)
print(dictb)
for key_a in dicta.keys():
    if key_a not in dictb.keys():
        dictc[key_a]=dicta[key_a]
for key_b in dictb.keys():
    if key_b not in dicta.keys():
        dictc[key_b]=dictb[key_b]
for key_ab in dicta.keys():
    if key_ab not in dictc:
        if type(dicta[key_ab])==str:
            dictc[key_ab]=dicta[key_ab]+dictb[key_ab]
        else:
            dictc[key_ab] = dicta[key_ab] - dictb[key_ab]
print("两个字典相加:")
print(dictc)