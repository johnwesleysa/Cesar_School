"""Por conta da pandemia, o CEF (Curso Estudante Feliz) adotou o Google Classroom como ferramenta para auxiliar o ensino remoto. Para acessá-lo, os estudantes precisam logar com e-mail institucional e senha. A senha inicial, enviada pela Agenda Digital, é gerada automaticamente a partir da data de nascimento do aluno, do seguinte modo:
○ mm + "$" + dd(invertido) + "#" + dd + "!" + mm(invertido) + "*" + aaaa
Escreva um programa que leia o dia, mês e ano de nascimento de um estudante e
informe a senha de acordo com a formatação acima."""

dia = input("Dia nascimento: ")
mes = input("Mês nascimento: ")
ano = input("Ano nascimento: ")

senha = mes  + '$' + dia[::-1] + '#' + dia + '!' + mes[::-1] + '*' + ano

print(f"Sua senha é: {senha}")
