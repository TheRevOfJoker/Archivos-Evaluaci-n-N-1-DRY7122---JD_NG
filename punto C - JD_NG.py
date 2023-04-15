acl = int(input("Ingrese numero de ACL: "))

if acl >= 1 and acl <=99 or acl >= 1300 and acl <= 1999:
    print ("Su ACL Es Estandar")
elif acl >=100 and acl <=199 or acl >=2000 and acl <=2699:
    print("Su ACL Es Extendida")
else:
    print("Su ACL No Corresponde")