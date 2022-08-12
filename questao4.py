def porcentagem (estado, total):
    return round(((100*estado)/total),2)

sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

total = sp + rj + mg + es + outros

print("==========================================================")
print("Porcentagem do faturamento de SP: " + str(porcentagem(sp, total)) + '%')
print("==========================================================")
print("Porcentagem do faturamento de RJ: " + str(porcentagem(rj, total)) + '%')
print("==========================================================")
print("Porcentagem do faturamento de MG: " + str(porcentagem(mg, total)) + '%')
print("==========================================================")
print("Porcentagem do faturamento de ES: " + str(porcentagem(es, total)) + '%')
print("==========================================================")
print("Porcentagem de outros faturamentos: " + str(porcentagem(outros, total)) + '%')
print("==========================================================")