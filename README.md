# PasswordCracker
Quebrador de senhas com o intuito de informar e ensinar às pessoas o quão frágil sua senha pode ser e como se deve fazer uma senha realmente forte .

* Projeto com uma interface intuitiva
* O usuário coloca uma senha imaginária para teste
* O programa usa uma tática de força bruta utilizando itertools e multi-threading.
* O programa utiliza o dicionário RockYou com senhas adicionais utilizando um set() e variações de uma mesma senha (maiusculo, minusculo, capitalize)

Documentação:

"""""
1º atribuição da variável arquivo ao "RockYou" (Dicionário de senhas comuns).
Atribuição da variavel dicionário  ao resultado da função carregar_dicionario(arquivo) utilizando o arquivo RockYou.

======= Operação da função carregar_dicionario(arquivo) =======================
try: 
dicionario = set()
a variável dicionário é criada como set() para garantir valores únicos

O arquivo do rockyou é aberto como f.
Cada linha do rockyou  é  atribuída á variável teste (teste = linha.strip().lower()) e armazenada na variável dicionario já com suas variações de escrita (CAPSLOCK, minusculo e Captalizada)

  with open(arquivo, 'r', encoding='latin-1') as f:
          for linha in f:
               teste = linha.strip().lower()
               if teste:  # Verifica se a linha não está vazia
                  dicionario.add(teste)
                  dicionario.add(teste.upper())
                  dicionario.add(teste.capitalize())

O dicionário é retornado.
em casos de erro :
    except FileNotFoundError:
        print(f"Erro: Arquivo {arquivo} não encontrado.")
        return dicionario
====================================================================================


2° A condição if __name__ == "__main__": garante uma inicialização correta das funções

A biblioteca multiprocessing conta quantos cores de cpu o dispositivo possui disponíveis.
Desta quantidade, serão criadas uma quantidade de (cores - 1) threads se o numero de cores disponivel não for
igual a 1. Garantindo que o programa não use todos os núcleos de cpu

O numero de threads criadas  estará entre (cores - 1) e 8 (sendo este o limite de threads criadas).
O valor escolhido para definir a quantidade será o menor dentre eles.

3º Chamada da função  quebrar_senha(), especificando: valor da senha, chars = (numeros,letra_e_numero, letras, simbolos_lite, tudo, tudo_lite)
e o numero de threads = (cores - 1) 


========== Operação da função quebrar_senha() ===========================

def quebrar_senha(senha,chars= 'numeros', num_threads=4):
    '''senha = palavra chave a ser advinhada pelo programa
       chars = caracteres a serem usados (padrão numeros) mas podem ser (numeros,letra_e_numero, letras, simbolos_lite, tudo, tudo_lite)
       num_threads = numeros de threads simultâneas (padrão 4)'''

Variavel Dicionario definida com global para que as Threads naveguem nela e possam  a alterar.

inicio do timer do cronômetro.

A senha que o usuário definiu é procurada por toda a variavel  set(dicionario) (definida préviamente por carregar-arquivo(), etapa 1º)
caso for encontrada o programa se encerra ali. 
    if senha in dicionario:
        fim = time.time()
        mensagem = f"Senha adivinhada: {senha} Tempo: {fim - inicio:.2f} segundos! Tentativas: 0 (tão fraca que estava no dicionário)"
        return mensagem 


Checagem da escolha de caracteres feita pelo usuário na definição da função utilizando dicionário.
    conjuntos_caracteres = {
        "numeros": numeros,
        "letra_e_numero": letra_e_numero,
        "letras": letras,
        "simbolos_lite": simbolos_lite,
        "tudo": tudo,
        "tudo_lite": tudo_lite
    }

   Pega o conjunto de caracteres escolhido pelo usuario
  chars_escolhidos = conjuntos_caracteres.get(chars, numeros)  # padrão = numeros


Realização de tentativas chamando a função  quebrar_senha_multithread()
    tentativa = quebrar_senha_multithread(senha, chars_escolhidos, num_threads)

========== Operação da função quebrar_senha_multithread() ============================

def quebrar_senha_multithread(senha, chars, num_threads=4):
    ""
    Gerencia múltiplas threads para quebrar a senha.
    ""

define a variavel senha_encontrada como global para que as threads possam alterá-la
define a variavel senha_encontrada como None (Null).

obtém o numero total de combinações possiveis usando a quantidade de tal char (escolhido pelo usuario) elevado ao tamanho da senha
   total_combinacoes = len(chars) ** len(senha) 

O tamanho do chunk é atribuido à repartição igualitária entre o total de combinações possíveis  e as threads  existentes.
Assim o trabalho é dividido igualmente entre elas. (Representa quantas combinações cada thread será responsável por testar.)
   chunk_size = total_combinacoes // num_threads

Criação de uma lista vazia chamada Threads
Para cada i em uma range do numero de threads : (Ex: for i in (0,1,2,3,4)) A variável i tambem poderia ser substituída por thread_id

  for i in range(num_threads):
        inicio = i * chunk_size
        fim = inicio + chunk_size if i != num_threads - 1 else total_combinacoes
        t = threading.Thread(target=gerar_tentativas, args=(senha, chars, inicio, fim, i)) --> cria uma nova thread para executar a função gerar_tentativas() args=(senha, chars, inicio, fim, i):
        Esse parâmetro define os argumentos que serão passados para a função especificada no target
        threads.append(t)
        t.start()
        
Criação das threads:
A lista threads será usada para armazenar todas as threads criadas.
for thread_id in range(num_threads): Este laço cria num_threads threads. Para cada thread, um índice único (thread_id) é atribuído.
Intervalo de tentativas: Cada thread processa um intervalo específico de tentativas. Os valores de inicio e fim são calculados com base no chunk_size:
Para cada thread, o índice inicial é thread_id * chunk_size.
O índice final é o inicio + chunk_size, mas para a última thread (quando thread_id == num_threads - 1), o fim será igual a total_combinacoes, para garantir que todas as combinações sejam cobertas.
Criação da thread:
A thread é criada com threading.Thread, onde o alvo (função a ser executada pela thread) é gerar_tentativas, e os parâmetros passados para a função são:
senha, chars, inicio, fim, thread_id, num_tentativas e barrier.
A thread é adicionada à lista threads e, em seguida, é iniciada com t.start().

O método join() é chamado para cada thread em threads. Esse método bloqueia a execução da função principal até que cada thread termine sua execução. Ou seja, a função quebrar_senha_multithread só retornará após todas as threads completarem o trabalho de tentativa.

Exemplo (quando total_combinacoes = 9, num_threads = 4):

Thread 0: inicio = 0 * 2 = 0, fim = 0 + 2 = 2.
Thread 1: inicio = 1 * 2 = 2, fim = 2 + 2 = 4.
Thread 2: inicio = 2 * 2 = 4, fim = 4 + 2 = 6.
Thread 3: inicio = 3 * 2 = 6, fim = total_combinacoes = 9 (ajuste para a última thread)


========== Operação da função gerar_tentativas() ============================

Define a variável senha_encontrada como global.

Inicializa o contador em 0.

Inicializa o inicio do cronômetro .

Usa itertools.product para criar todas as combinações possíveis de chars com o mesmo comprimento da senha.

printa os status das threads : print(f"[Thread-{thread_id + 1}] Iniciada.")  # Exibe quando a thread começa
                               print(f"[Thread-{thread_id}] Intervalo de trabalho: {inicio} a {fim}")

A função itertools.product(chars, repeat=len(senha)) gera todas as combinações possíveis de caracteres em chars, com comprimento igual ao da senha (len(senha)). O enumerate adiciona um contador ao iterador combinacoes, começando em 0 por padrão. Assim, em cada iteração, ele retorna dois valores:O laço for faria as seguintes iterações:

i = 0, tentativa = ('a', 'a')
i = 1, tentativa = ('a', 'b')
i = 2, tentativa = ('b', 'a')
i = 3, tentativa = ('b', 'b')



 if i < inicio:
     continue 
Esse trecho é usado para garantir que apenas as tentativas dentro do intervalo de trabalho de cada thread sejam processadas. garantindo que cada uma delas execute um intervalo específico de tentativas e ignore as outras.


if i >= fim:
 break  # Sair se a faixa da thread foi atingida
Este bloco assegura que a thread só processe até o índice fim. Quando o índice i atingir ou ultrapassar o valor de fim, a thread interrompe o laço e para de tentar novas combinações.

Verifica se o número de tentativas feitas pela thread atingiu o limite_tentativas configurado.
Se o limite for atingido, o tempo total da execução da thread é calculado, e uma mensagem é exibida.
contador: Conta as tentativas feitas pela thread.


tentativa = ''.join(tentativa)
Converte a tupla de caracteres tentativa em uma string com ''.join(tentativa) e imprime a tentativa atual no formato de string


with lock:
    if senha_encontrada:  # Outra thread já encontrou a senha
        return
A verificação é feita dentro de um bloco with lock para garantir que o acesso à variável global senha_encontrada seja seguro entre múltiplas threads (evitando condições de corrida).
Se a senha já foi encontrada (ou seja, senha_encontrada é True), a execução da thread é encerrada com return, evitando que a thread continue tentando.

: Compara a tentativa gerada pela thread com a senha. Se a tentativa for igual à senha:
A senha é armazenada em senha_encontrada e a execução é protegida por um lock para garantir que o acesso seja seguro entre threads.
O tempo de execução da thread é calculado e exibido.
return: Após encontrar a senha, o return interrompe a execução da thread, indicando que o trabalho foi concluído com sucesso. ""
