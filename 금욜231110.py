
result={'Alice':85,'Bob':90,'Charlie':95}
for res in result.keys():
    print (res,result[res])
    
print("###") #
result['David']=80
for res in result.keys():
    print (res,result[res])

    print("###") #

result['Alice']=88
for res in result.keys():
    print (res,result[res])

print("###") #
result.pop['Bob']
for res in result.keys():
    print (res,result[res])