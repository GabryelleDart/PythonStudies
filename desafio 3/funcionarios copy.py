'''
gerar lista de funcionários que trablham a noite e tem carro, que trabalham de dia  e tem carro e lista dos que não tem carro
'''
funcionarias_M1=['Kátia','Amanda','Maísa','Débora','Claudene','D. Maria','Ana Cláudia']
funcionarias_dia=['Kátia','Amanda','Débora', 'Maísa']
funcionarias_noite=['D. Maria','Ana Cláudia','Claudene']
funcionarias_c_carro=['Ana Cláudia', 'Maísa','Kátia','Claudene']
funcionarias_dia_carro= set(funcionarias_dia).intersection(funcionarias_c_carro)
funcionarias_noite_carro=set(funcionarias_noite).intersection(funcionarias_c_carro)
funcionarias_sem_carro= set(funcionarias_M1).difference(funcionarias_c_carro)


print(sorted(funcionarias_dia_carro))
print(sorted(funcionarias_noite_carro))
print(sorted(funcionarias_sem_carro))