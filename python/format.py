a = 'João'
b = 'Victor'
c = 'Maine'
string = '1={nome1} 2={nome2} 3={sobrenome}'
formato = string.format(
    nome1=a, nome2=b, sobrenome=c
)

print(formato)