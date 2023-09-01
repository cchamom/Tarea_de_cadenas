precio=input("Introduce precio del producto: ")

print("Euros: ",precio[:precio.find(".")], "Centimos: ",precio[precio.find("."):])
