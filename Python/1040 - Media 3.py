ns = str(input()).split()
n1 = float(ns[0])
n2 = float(ns[1])
n3 = float(ns[2])
n4 = float(ns[3])

media = (n1*2+n2*3+n3*4+n4*1)/10

if media >= 7.0:
      print('Media: {:.1f}'.format(media))
      print('Aluno aprovado.')
elif media < 5.0:
      print('Media: {:.1f}'.format(media))
      print('Aluno reprovado.')
else:
      nf = float(input())
      print('Media: {:.1f}'.format(media))
      print('Aluno em exame.')
      print('Nota do exame: {:.1f}'.format(nf))
      media = (media + nf )/2
      if media >= 5.0:
            print('Aluno aprovado.')
            print('Media final: {:.1f}'.format(media))
      else:
            print('Aluno reprovado.')
            print('Media final: {:.1f}'.format(media))
