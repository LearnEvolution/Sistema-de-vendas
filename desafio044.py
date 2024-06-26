#  Elabore um progrma que calcule o valor a ser pago por um produto,
#  considerando o seu PREÇO Normal e CONDIÇÕES de Pagamento:
# -À vista dinheiro / cheque: 10% de desconto.
# -À vista no cartão: 5% de dsconto.
# -em até 2x no catão: preço normal.
# -3x ou mais no cartão: 20% de juros.

valor = float(input("DIGITE O PREÇO DO PRODUTO R$: "))
print("""OK, R${}
      
      # -À vista dinheiro / cheque: 10% de desconto.
      # -À vista no cartão: 5% de dsconto.
      # -em até 2x no catão: preço normal.
      # -3x ou mais no cartão: 20% de juros.

      ESCOLHA A SUA FORMA DE PAGAMENTO 
        [1] DINHEIRO 
        [2] CHEQUE    
        [3] CARTÂO""".format(valor))

x = int(input("DIGITE A SUA OPÇÃO >-- "))

if x == 3 :
  print("""
        [1]AVISTA 
        [2]PARCELADO """)
  i = int(input())
  if i == 2 :
      z = int(input("DIGITE EM QUANTAS VEZES >-- "))
      print()
      if z > 2 :
         print("VOCE ESCOLHEU EM {}x A COMPRA FICOU POR R${}".format(z , valor + (valor * 20 )/ 100))
      else:
         print("VOCE ESCOLHEU EM {}x A COMPRA FICOU POR R${}".format(z,valor))
  else:
    print("VOCE ESCOLHEU A VISTA TEVE UM DESCONTO DE 5% O PRODUTO FICOU POR  R${} ".format(valor - (valor * 5) / 100 ) )    
else:
     print()      
                   
if x == 1 or x == 2 :
    print("O VALOR DO PRODUTO R$:{}  TEVE UM DESCONTO DE 10%. SUA COMPRA FICOU R${}".format(valor , (valor - (valor * 10) / 100)))
else: 
    print("")
print("OBRIGADO PELA SUA PREFERENCIA ! VOLTE SEMPRE")        