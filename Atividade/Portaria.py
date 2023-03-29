import copy

nome = input('Qual o seu nome? ')
vinc = input('Qual o seu vínculo com a Instituição? ')

class Pessoa:
    def __init__(self, nome, vinc):
        self.nome = nome
        self.vinc = vinc   

    def __str__(self):
        if(vinc == 'Aluno' or vinc == 'aluno'):
            print('Acesso permitido ao Aluno da Instituição, entre ' + self.nome)
        elif(vinc == 'Professor' or vinc == 'professor'):
            print('Acesso permitido ao Professor da Instituição, entre ' + self.nome)
        elif(vinc == 'Secretaria' or vinc == 'secretaria'):
            print('Acesso permitido para a Secretaria da Instituição, entre ' + self.nome) 
        else: 
            return f'Acesso negado, {self.nome}!'
        return ''
        
    def clone(self):
        return copy.copy(self)

class PessoaManager:
    def __init__(self):
       self.pessoas = {}
       
    def addPessoa(self, nome, vinc, id):
        pessoa = Pessoa(nome, vinc)
        self.pessoas[id] = pessoa
    
    def getPessoa(self, id):
        return self.pessoas[id].clone()
    
    
###################################################
manager = PessoaManager()

# Add Pessoas
manager.addPessoa(nome, vinc, 1)

# Clonar pessoas
pessoa1 = manager.getPessoa(1)
# pessoa2 = manager.getPessoa(2)

# Modificando informacoes

# pessoa1.idade = 25
# Print na tela

print(pessoa1)

edit = input('O que gostaria de editar: [nome] ou [Vinculo]')

if(edit == 'nome'):
    pessoa1.nome = input('Digite outro nome: ')          
if(edit == 'vinculo'):
    pessoa1.vinc = input('Digite outro vinculo: ')   
    
print(pessoa1)

