
#print(True and True)
#print(True and False)
#print(True or True)
#print(True or False)


saldo = 1000
limite = 200
saque = 100
conta_especial = True

#Sem parenteses 
exp = saldo >= saque and saque <= limite or conta_especial and saque >= saque
print(exp)

#Com parenteses mais organizado 
exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saque >= saque)
print(exp_2)

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque 

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)