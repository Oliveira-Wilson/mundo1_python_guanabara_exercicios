# digite um nome de uma cidade e verifique se o nome começa com Santo

cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')

