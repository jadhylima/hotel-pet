class Animal:
    contador_id = 0

    def __init__(self, nome: str, peso: float, idade: int, peso_refeicao: int):
        self.__nome = nome
        self._peso = peso
        self._idade = idade
        self.horario_refeicao = []  # lista que contém o horário em que as refeições deverão ser dadas ao animal
        self.peso_refeicao = peso_refeicao  # peso que cada animal precisa comer
        self.refeicoes_dadas = []  # lista que contém o horário em que cada refeição foi dada
        Animal.contador_id += 1
        self.contador_id = Animal.contador_id

    def __repr__(self) -> str:
        return f'ID: {self.contador_id} | Nome: {self.__nome} | Raça: {type(self).__name__} | idade {self._idade}'

    @property
    def nome(self):
        return self.__nome

    @property
    def peso(self):
        return self._peso

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, nova_idade):
        if nova_idade >= 0:
            self._idade = nova_idade
            return (True)
        else:
            return (False)
    
    @peso.setter
    def peso(self, novo_peso):
        if novo_peso >= 0:
            self._peso = novo_peso
            return (True)
        else:
            return (False)

    def iniciar_dia(self):
        self.refeicoes_dadas.clear()

    def dar_refeicao(self, horario):
        if (0 <= horario <= 23) and (self.checar_alimento(horario) == True):
            tupla = (horario, (len(self.horario_refeicao) - (len(self.refeicoes_dadas) + 1)))
            self.refeicoes_dadas.append(tupla)
            return f'Refeição dada: {tupla[0]}h | Restam: {tupla[1]} refeições'
        else:
            return False

    def checar_alimento(self, horario):
        for item in self.horario_refeicao:
            if ((horario == item) or (horario == (item + 1)) or (horario == (item - 1))):
                return True
        return False


class Mamiferos(Animal):
    def __init__(self, nome: str, peso: float, idade: int, peso_refeicao: int, sexo: str, castrado: bool, social: bool):
        super().__init__(nome, peso, idade, peso_refeicao)
        self.sexo = sexo
        self.castrado = castrado
        self.social = social


class Gato(Mamiferos):
    def __init__(self, nome: str, peso: float, idade: int, peso_refeicao: int, sexo: str, castrado: bool, social: bool,
                 fiv: bool, felv: bool):
        super().__init__(nome, peso, idade, peso_refeicao, sexo, castrado, social)
        self.fiv = fiv
        self.felv = felv


class Cachorro(Mamiferos):
    def __init__(self, nome: str, peso: float, idade: int, peso_refeicao: int, sexo: str, castrado: bool, social: bool,
                 ultimo_banho: str, parvovirose: bool):
        super().__init__(nome, peso, idade, peso_refeicao, sexo, castrado, social)
        self.ultimo_banho = ultimo_banho
        self.parvovirose = parvovirose


class Ave(Animal):
    def __init__(self, nome: str, peso: float, idade: int, peso_refeicao: int):
        super().__init__(nome, peso, idade, peso_refeicao)


class Peixe(Animal):
    def __init__(self, nome: str, peso: float, idade: int, peso_refeicao: int):
        super().__init__(nome, peso, idade, peso_refeicao)


class FuncionarioPadrao:
    def __init__(self, nome : str, salario : int):
        self.nome = nome
        self.salario = salario


class Cuidador(FuncionarioPadrao):
    def __init__(self, nome : str, salario : int, supervisor, gato = None, cachorro = None, ave = None, peixe = None):
        super().__init__(nome, salario)
        self.__supervisor = supervisor
        self.animais = [] #lista de animais que está cuidando, apenas animais dos tipos definidos em tipo_animais 
        #podem ser incluídos na lista, e não deve ter valores repetidos.
        self._tipo_animais = [gato, cachorro, ave, peixe] #apenas Gato, Peixe, Cachorro e Ave podem ser incluídos na lista, e não deve ter valores repetidos.
        self.supervisor.cuidadores.append(self)

    def __repr__(self):
        return f'Cuidador: {self.nome} | Supervisor: {self.__supervisor.nome}'

    def verificar_tipo_animal(self, animal):
        if type(animal).__name__ in self._tipo_animais:
            self.animais.append(animal)
            self.supervisor.animais.append(animal)  

    def alimentar(self, nome : str, hora : int):
        Alimentar.alimentando(nome, hora, self.animais)

    @property
    def tipo_animais(self):
        return self._tipo_animais

    @tipo_animais.setter
    def tipo_animais(self, lista_nova : list):
        for especie in lista_nova:
            if not especie in self._tipo_animais:
                self._tipo_animais.append(especie)

    @property
    def supervisor(self):
        return self.__supervisor


class Alimentar:
    #Se algum animal com esse nome estiver sob sua responsabilidade,
    #chama o método dar_refeicao desse animal, retornando True. Caso contrário, retorna False.
    def alimentando(nome : str, hora : int, animais : list):
        for bicho in animais:
            if nome == bicho.nome:
                bicho.dar_refeicao(hora)
                return True
            else:
                return (f'{nome} não está sobre responsbilidade desse cuidador.')    


class Supervisor(FuncionarioPadrao):
    def __init__(self, nome : str, salario : int, bonus):
        super().__init__(nome, salario)
        self.bonus = bonus
        self.cuidadores = [] #lista de cuidadores sob sua responsabilidade. Inicia vazio, e automaticamente é incluído na criação do cuidador.
        self.animais = []

    def __repr__(self):
        return f'Supervisor: {self.nome}'

    def alimentar(self, nome : str, hora : int):
        Alimentar.alimentando(nome, hora, self.animais)


superv = Supervisor('Ewerton', 10000, 5000)
cuida = Cuidador('Jade', 1000, superv, 'Gato', 'Ave', 'Cachorro')
gato1 = Gato('Carly', 2.0, 3, 150, 'f', True, True, False, False)
ave1 = Ave('Piu', 0.1, 1, 50)
cachorro1 = Cachorro('Izi', 3, 17, 150, 'Feminino', True, False, '12/01', False)
peixe1 = Peixe('Dory', 0.2, 1, 50)
cuida2 = Cuidador('Leticia', 1000, superv, 'Peixe')
cuida.verificar_tipo_animal(gato1)
cuida2.verificar_tipo_animal(peixe1)
print(superv.animais)
print(cuida.animais)
print(cuida2.animais)
gato1.horario_refeicao = [15, 18]
cuida.alimentar('Carly', 15)
superv.alimentar('Carly', 18)
print(gato1.refeicoes_dadas)
