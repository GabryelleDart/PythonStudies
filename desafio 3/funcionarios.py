'''
gerar lista de funcionários que trablham a noite e tem carro, que trabalham de dia  e tem carro e lista dos que não tem carro
'''
funcionarias_Macela1=['Kátia','Amanda','Maísa','Débora','D. Maria','Ana Cláudia']
funcionarias_dia=['Kátia','Amanda','Débora', 'Maísa']
funcionarias_noite=['D. Maria','Ana Cláudia','Claudene']
funcionarias_c_carro=['Ana Cláudia', 'Maísa','Kátia','Claudene']
funcionarias_dia_carro=[]
funcionarias_noite_carro=[]
funcionarias_sem_carro=[]
for pessoa in funcionarias_dia :
    if(pessoa in funcionarias_c_carro):
        funcionarias_dia_carro.append(pessoa)
    else:
         funcionarias_sem_carro.append(pessoa)

for pessoa in funcionarias_noite :
    if(pessoa in funcionarias_c_carro):
        funcionarias_noite_carro.append(pessoa)
    else:
         funcionarias_sem_carro.append(pessoa)

print(sorted(funcionarias_dia_carro))
print(sorted(funcionarias_noite_carro))
print(sorted(funcionarias_sem_carro))