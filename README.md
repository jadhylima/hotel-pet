Gerenciamento de Animais em um Hotel de Pets
Este é um sistema de gerenciamento de animais em um zoológico, desenvolvido em Python. Ele permite registrar informações sobre animais e funcionários (cuidadores e supervisores), bem como gerenciar a alimentação dos animais.

Funcionalidades:
1. Cadastro de Animais: Suporte para mamíferos (gatos e cachorros), aves e peixes.
2. Cadastro de Funcionários: Suporte para cuidadores e supervisores.
3. Gerenciamento de Refeições: Registro e controle de refeições dos animais.
4. Atribuição de Animais a Cuidadores: Apenas tipos específicos de animais podem ser atribuídos a cuidadores.

Estrutura do Código:

Classes:
Animal
   Classe base para todos os animais. Armazena informações como nome, peso, idade e horários de refeição.

Métodos:
__init__: Inicializa um novo animal.
__repr__: Representação textual do animal.
iniciar_dia: Limpa a lista de refeições dadas.
dar_refeicao: Registra uma refeição.
checar_alimento: Verifica se o horário da refeição está correto.
------------------------------------------------------------------------------------------------------------------
Mamiferos (herda de Animal)
Classe base para mamíferos. Adiciona informações específicas de mamíferos como sexo, castração e sociabilidade.

Gato (herda de Mamiferos)
Classe para gatos. Adiciona informações sobre FIV e FeLV.

Cachorro (herda de Mamiferos)
Classe para cachorros. Adiciona informações sobre o último banho e parvovirose.

Ave (herda de Animal)
Classe para aves.

Peixe (herda de Animal)
Classe para peixes.
------------------------------------------------------------------------------------------------------------------
FuncionarioPadrao
Classe base para todos os funcionários. Armazena nome e salário.

Cuidador (herda de FuncionarioPadrao)
Classe para cuidadores. Gerencia os animais sob sua responsabilidade.

Métodos:
  __init__: Inicializa um novo cuidador.
  __repr__: Representação textual do cuidador.
  verificar_tipo_animal: Verifica e adiciona animais ao cuidador.
  alimentar: Alimenta um animal sob sua responsabilidade.
------------------------------------------------------------------------------------------------------------------
Supervisor (herda de FuncionarioPadrao)
Classe para supervisores. Gerencia os cuidadores e animais sob sua supervisão.

Métodos:
__init__: Inicializa um novo supervisor.
__repr__: Representação textual do supervisor.
alimentar: Alimenta um animal sob sua supervisão.
------------------------------------------------------------------------------------------------------------------
Alimentar
  Classe auxiliar para gerenciar a alimentação dos animais.

Métodos:
  alimentando: Alimenta um animal se ele estiver sob responsabilidade do funcionário.
------------------------------------------------------------------------------------------------------------------
EXEMPLO DE USO

# Criação de um supervisor
superv = Supervisor('Ewerton', 10000, 5000)

# Criação de cuidadores
cuida = Cuidador('Jade', 1000, superv, 'Gato', 'Ave', 'Cachorro')
cuida2 = Cuidador('Leticia', 1000, superv, 'Peixe')

# Criação de animais
gato1 = Gato('Carly', 2.0, 3, 150, 'f', True, True, False, False)
ave1 = Ave('Piu', 0.1, 1, 50)
cachorro1 = Cachorro('Izi', 3, 17, 150, 'Feminino', True, False, '12/01', False)
peixe1 = Peixe('Dory', 0.2, 1, 50)

# Atribuição de animais a cuidadores
cuida.verificar_tipo_animal(gato1)
cuida2.verificar_tipo_animal(peixe1)

# Alimentação dos animais
gato1.horario_refeicao = [15, 18]
cuida.alimentar('Carly', 15)
superv.alimentar('Carly', 18)

# Verificação das refeições dadas
print(gato1.refeicoes_dadas)
---------------------------------------------------------------------------------------------------------------------
Requisitos:
Python 3.x

Melhorias Futuras:
1. Implementar persistência dos dados em um banco de dados ou arquivo.
2. Adicionar validação de entrada para os dados dos animais e funcionários.
3. Melhorar a interface do usuário, talvez com uma interface gráfica.
