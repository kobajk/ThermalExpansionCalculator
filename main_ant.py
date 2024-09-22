import math as m

def dil(a,L,T):
  d = a * L * T
  return d

def format():
  global format, compx, largy, altz, diam
  print(' Qual o formato do objeto? '
        '\n (1) Polígono'
        '\n (2) Cilindrico')
  format = int(input())
  while format != 1 and format != 2:
    print(' Opção inválida: Escolha uma das alternativas do menu.')
    print(' Qual o formato do objeto? '
          '\n (1) Polígono'
          '\n (2) Cilindrico')
    format = int(input())

  if format == 1:
    print('\n Quais são as dimensões desse polígono? Em metros! \n')
    print('                   X                      Z  ')
    print('    *****************************       *****')
    print('    *                           *       *   *')
    print('    *                           *       *   *')
    print(' Y  *                           *       *   *')
    print('    *                           *       *   *')
    print('    *                           *       *   *')
    print('    *****************************       *****')
    compx = float(input('\n Qual o comprimento(x) do polígono? Em metros: '))
    while compx <= 0:
        print(' Comprimento inválido! Menor ou igual a zero! ')
        compx = float(input('\n Qual o comprimento(x) do polígono? Em metros: '))
    largy = float(input('\n Qual a largura(y) do polígono? Em metros: '))
    while largy <= 0:
        print(' Largura inválida! Menor ou igual a zero! ')
        largy = float(input('\n Qual a largura(y) do polígono? Em metros: '))
    altz = float(input('\n Qual a altura/espessura (z) do polígono? Em metros: '))
    while altz <= 0:
        print(' Altura inválida! Menor ou igual a zero! ')
        altz = float(input('\n Qual a altura/espessura (z) do polígono? Em metros: '))

  else:
    print('\n Quais são as dimensões desse cilindro? Em metros! \n')
    print('       Ø   ')
    print('    *******')
    print('    *     *')
    print('    *     *')
    print(' Z  *     *')
    print('    *     *')
    print('    *     *')
    print('    *******')

    diam = float(input('\n Qual o diâmetro do cilindro? Em metros: '))
    while diam <= 0:
        print(' Diâmetro inválido! Menor ou igual a zero! ')
        diam = float(input('\n Qual o diâmetro do cilindro? Em metros: '))
    altz = float(input('\n Qual a altura(z) do cilindro? Em metros: '))
    while altz <= 0:
        print(' Altura inválida! Menor ou igual a zero! ')
        altz = float(input('\n Qual a altura/espessura (z) do polígono? Em metros: '))

  print('\n Obrigado por fornecer as dimensões do seu objeto! ')

matp = ['ABS', 'PP', 'PA', 'PS', 'PC', 'Outro']
ap = [(90 * 10**-6), (140 * 10**-6), (110 * 10**-6), (65 * 10**-6), (67.5 * 10**-6)]
tempmaxp = [100, 160, 160, 100, 150]
matm = ['Alumínio', 'Cobre', 'Ouro', 'Prata', 'Titânio', 'Outro']
am = [(23.6 * 10**-6), (17.6 * 10**-6), (14.2 * 10**-6), (19.8 * 10**-6), (8.64 * 10**-6)]
tempmaxm = [660, 1084, 1064, 961.78, 1668]


print('---------------------------------------------------------------------------------------'
      '\n Bem-vindo ao programa especializado em TERMODINÂMICA: DILATAÇÃO TÉRMICA DE CORPOS')

print('\n Por favor, escolha qual método você quer utilizar nosso programa: '
      '\n (1) Calcular a expansão térmica de um objeto.'
      '\n (2) Definir material a partir de uma necessidade de temperatura específica.')
met = int(input())
while met != 1 and met != 2:
  print(' Opção inválida: Escolha uma das alternativas do menu.')
  print('\n Por favor, escolha qual método você quer utilizar nosso programa: '
      '\n (1) Calcular a expansão térmica de um objeto.'
      '\n (2) Definir material a partir de uma necessidade de temperatura específica.')
  met = int(input())

if met == 1:
  print(' Você escolheu a opção de calcular a expansão térmica de um objeto!')
  print('\n Qual grupo de materiais seu objeto pertence? '
      '\n (1) Metais'
      '\n (2) Plásticos'
      '\n (3) Outros')
  tmat = int(input())
  while tmat != 1 and tmat != 2 and tmat != 3:
    print(' Opção inválida: Escolha uma das alternativas do menu.')
    print('\n Qual grupo de materiais seu objeto pertence? '
        '\n (1) Metais'
        '\n (2) Plásticos'
        '\n (3) Outros')
    tmat = int(input())

  if tmat == 1:
    print(' Você escolheu a classe dos metais! ')
    print(' Escreva o material que deseja utlizar, da lista: ', matm)
    x = str(input(''))
    while x not in matm:
        print(' O material digitado não está na lista!')
        print(matm)
        x = str(input(' Escreva o material que deseja utlizar, da lista: '))
    if x == 'Outro':
        nome = str(input('Qual o nome do material? '))
        matm[5] = nome
        print(matm)
        amesp = float(input(' Qual o coeficiente de dilatação térmica linear do material utlizado? (°C): '))
        while amesp <= 0:
            print(' Valor inválido: Menor ou igual a zero!')
            amesp = float(input(' Qual o coeficiente de dilatação térmica linear do material utlizado? (°C): '))
        am.append(amesp)
        tesp = float(input(' Qual a temperatura máxima que o material especificado se mantém sólido? (°C): '))
        tempmaxm.append(tesp)
        x = nome
    x = matm.index(x)
    a = am[x]

  elif tmat == 2:
    print(' Você escolheu a classe dos plásticos! ')
    print(' Escreva o material que deseja utlizar, da lista: ', matp)
    x = str(input(''))
    while x not in matp:
        print(' O material digitado não está na lista!')
        print(matp)
        x = str(input(' Escreva o material que deseja utlizar, da lista: '))
    if x == 'Outro':
        nome = str(input('Qual o nome do material? '))
        matp[5] = nome
        print(matp)
        apesp = float(input(' Qual o coeficiente de dilatação térmica linear do material utlizado? (°C): '))
        while apesp <= 0:
            print(' Valor inválido: Menor ou igual a zero!')
            apesp = float(input(' Qual o coeficiente de dilatação térmica linear do material utlizado? (°C): '))
        ap.append(apesp)
        tesp = float(input(' Qual a temperatura máxima que o material especificado se mantém sólido? (°C): '))
        tempmaxp.append(tesp)
        x = nome
    x = matp.index(x)
    a = ap[x]

  else:
    print(' Você escolheu a classe dos materiais personalizados! ')
    aesp = float(input(' Qual o coeficiente de dilatação térmica linear do material utlizado? (°C): '))
    while aesp <= 0:
        print(' Valor inválido: Menor ou igual a zero!')
        aesp = float(input(' Qual o coeficiente de dilatação térmica linear do material utlizado? (°C): '))
    a = aesp

  print('\n Material do objeto definido com sucesso! ')

  format()

  print('\n Agora é a ultima etapa! O range de temperatura que o objeto será exposto. ')

  t1 = float(input('\n Qual a temperatura inicial que o objeto será exposto? °C: '))
  if tmat == 1:
    while t1 >= tempmaxm[x]:
      print(f' Temperatura inválida! A temperatura deve manter o material sólido, para {matm[x]} a temperatura máxima é {tempmaxm[x]}°C')
      t1 = float(input('\n Qual a temperatura inicial que o objeto será exposto? °C: '))
  elif tmat == 2:
    while t1 >= tempmaxp[x]:
      print(f' Temperatura inválida! A temperatura deve manter o material sólido, para {matp[x]} a temperatura máxima é {tempmaxp[x]}°C')
      t1 = float(input('\n Qual a temperatura inicial que o objeto será exposto? °C: '))

  t2 = float(input(' Qual a temperatura final que o objeto será exposto? °C: '))
  if tmat == 1:
    while t2 >= tempmaxm[x]:
      print(f' Temperatura inválida! A temperatura deve manter o material sólido, para {matm[x]} a temperatura máxima é {tempmaxm[x]}°C.')
      t2 = float(input('\n Qual a temperatura inicial que o objeto será exposto? °C: '))
  elif tmat == 2:
    while t2 >= tempmaxp[x]:
      print(f' Temperatura inválida! A temperatura deve manter o material sólido, para {matp[x]} a temperatura máxima é {tempmaxp[x]}°C.')
      t2 = float(input('\n Qual a temperatura inicial que o objeto será exposto? °C: '))

  if format == 1:
    dilalt = dil(a,t2-t1,altz)
    dilcomp = dil(a,t2-t1,compx)
    dillarg = dil(a,t2-t1,largy)
    print('\n\n\n A dilatação do seu objeto será: '
          '\n No eixo X: %.4f m (comprimento final de %.4f m)'
          '\n No eixo Y: %.4f m (comprimento final de %.4f m)'
          '\n No eixo Z: %.4f m (comprimento final de %.4f m)' %(dilcomp , dilcomp+compx, dillarg , dillarg+largy, dilalt , dilalt+altz))
  else:
    dilalt = dil(a,t2-t1,altz)
    dildiam = dil(a,t2-t1,diam)
    print('\n\n\n A dilatação do seu objeto será: '
          '\n No diâmetro: %.4f m (comprimento final de %.4f m)'
          '\n No eixo Z: %.4f m (comprimento final de %.4f m)' %(dildiam , dildiam+diam, dilalt , dilalt+altz))

else:
  print(' Você escolheu a opção de definir o material a partir de uma temperatura! ')
  
  format()

  tempmax = float(input(' Informe a temperatura máxima que esse material vai ser submetido: '))
  matpossiveis = []
  dilatacaoalt = []
  dilatacaocomp = []
  dilatacaolarg = []
  dilatacaodiam = []
  for i in range (0,5):
      if tempmaxp[i] > tempmax:
        matpossiveis.append(matp[i])
        if format == 1:
            dilatacaoalt.append(dil(ap[i], tempmax, altz))
            dilatacaocomp.append(dil(ap[i], tempmax, compx))
            dilatacaolarg.append(dil(ap[i], tempmax, largy))
        else:
            dilatacaodiam.append(dil(ap[i], tempmax, diam))
            dilatacaoalt.append(dil(ap[i], tempmax, altz))
      if tempmaxm[i] > tempmax:
        matpossiveis.append(matm[i])
        if format == 1:
            dilatacaoalt.append(dil(am[i], tempmax, altz))
            dilatacaocomp.append(dil(am[i], tempmax, compx))
            dilatacaolarg.append(dil(am[i], tempmax, largy))
        else:
            dilatacaodiam.append(dil(am[i], tempmax, diam))
            dilatacaoalt.append(dil(am[i], tempmax, altz))
  print(' Os materiais resistentes a essa temperatura, presentes no nosso banco de dados, são: ',matpossiveis)

  for i in range(0,len(matpossiveis)):
      if format == 1:
        print(f'\n Para o material {matpossiveis[i]} a diltação no eixo X(comprimento) será de: {dilatacaocomp[i]:.4f}m')
        print(f' Para o material {matpossiveis[i]} a diltação no eixo Y(largura) será de: {dilatacaolarg[i]:.4f}m')
        print(f' Para o material {matpossiveis[i]} a diltação no eixo Z(altura) será de: {dilatacaoalt[i]:.4f}m \n')
        sofremais = dilatacaocomp.index(max(dilatacaocomp))
        sofremenos = dilatacaocomp.index(min(dilatacaocomp))
      else:
        print(f'\n Para o material {matpossiveis[i]} a diltação no diâmetro será de: {dilatacaodiam[i]:.4f}')
        print(f'\n Para o material {matpossiveis[i]} a diltação no eixo Z(altura) será de: {dilatacaoalt[i]:.4f}m \n')
      sofremais = dilatacaoalt.index(max(dilatacaoalt))
      sofremenos = dilatacaoalt.index(min(dilatacaoalt))
  print(f' O material que *mais* sofre com a dilatação é o {matpossiveis[sofremais]}')
  print(f' O material que *menos* sofre com a dilatação é o {matpossiveis[sofremenos]}')
