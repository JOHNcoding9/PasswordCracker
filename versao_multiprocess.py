import tkinter as tk
from PIL import Image, ImageTk
import webbrowser
import string
import itertools # Utilizado para gerar as combinações possíveis de senha
import time
 # Para usar múltiplas threads e realizar a execução paralela. Uma thread é uma unidade de execução que roda dentro de um processo, compartilhando recursos com outras threads.
import multiprocessing
 # Para determinar o número de núcleos disponíveis no sistema.
import sys
import threading
import ctypes

cor_1 = '#030303'  # Preto
cor_2 = '#ff1100'  # Vermelho
cor_3 = '#ffffff'  # Branco
cor_4 = '#bd1fbf'  # Roxo
cor_5 = '#616161'  # Cinza

# numero de tentativas por thread
num_tentativas = 10000000000

# Janela principal
janela = tk.Tk()

# Configuração da janela
janela.title("Avaliador de senhas")
janela.geometry("800x600")  # Largura x Altura
janela.configure(bg=cor_1)

# Criando a label principal
label = tk.Label(janela, text="Teste a segurança de sua senha!", font=("Arial", 16), bg=cor_1, fg=cor_2)
label.pack()

# Carregar e exibir a imagem
try:
    imagem_pillow = Image.open("background.jpg")
    imagem_redimensionada = imagem_pillow.resize((350, 350))
    imagem_tk = ImageTk.PhotoImage(imagem_redimensionada)

    label_imagem = tk.Label(janela, image=imagem_tk, bg=cor_1)
    label_imagem.pack()
except FileNotFoundError:
    label_imagem = tk.Label(janela, text="Imagem não encontrada", font=("Arial", 14), bg=cor_1, fg=cor_3)
    label_imagem.pack()

# Criar o frame principal
frame = tk.Frame(janela, width=600, height=150, bg=cor_1)
frame.pack(side="top", padx=10, pady=10)

# Todos os números existentes no teclado
numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Todas as letras existentes no teclado
letras = list(string.ascii_lowercase + string.ascii_uppercase + 'ç' + 'Ç')

# Todos os símbolos existentes no teclado
simbolos = [" ", "'", "!", "@", "#", "%", "¨", "&", "*", "(", ")", "-", "_", "=", "+", "´", "`", "[", "]", "{", "}", "~", "^", "?", '/', '"', ",", ".", "<", ">", ":", ";", '\\', "|", "¹", "²", "³", "¢", "¬", "¢", "§", "ª", "°", "₢", "/"]

simbolos_lite = ['.',"!", "#", "*", "-", "_", "?",',','+','-','=','%',"(", ")", "[", "]", "{", "}",'@',"|"]

# Colocar todos em uma única lista
tudo = simbolos + letras + numeros
tudo_lite = simbolos_lite + letras + numeros
letra_numero_min = list(string.ascii_lowercase + 'ç') + numeros
letra_numero_mai = list(string.ascii_uppercase + 'Ç') + numeros
letra_numero = list(string.ascii_lowercase + 'ç') + list(string.ascii_uppercase + 'Ç') + numeros


# Mapear a escolha dos caracteres
conjuntos_caracteres = {
            "numeros": numeros,
            "letra_numero_min": letra_numero_min,
            "letra_numero_mai": letra_numero_mai,
            'letra_numero': letra_numero,
            "letras": letras,
            "tudo": tudo_lite
         
        }


# Dicionário RockYou
def carregar_dicionario(arquivo):
    dicionario = set()
    try:
        with open(arquivo, 'r', encoding='latin-1') as f:
            for linha in f:
                teste = linha.strip().lower()
                if teste:  # Verifica se a linha não está vazia
                    dicionario.add(teste)
        return dicionario
    except FileNotFoundError:
        print(f"Erro: Arquivo {arquivo} não encontrado.")
        return dicionario
    

# Uso do dicionario
arquivo_rockyou = "rockyou.txt"
dicionario = carregar_dicionario(arquivo_rockyou)


# Layout ==================================================================================================================================
# Função para atualizar a tela
def atualizar_tela():
    # Limpar o conteúdo do frame atual
    for widget in frame.winfo_children():
        widget.destroy()

def Info():

    atualizar_tela()

    def abrir_link(url):
     webbrowser.open_new(url)

    texto = f"""Tenha em mente que este projeto simples foi feito por um estudante iniciante em engenharia de software. Se sua senha foi facilmente adivinhada, NUNCA considere seu uso em situações importantes.

⚠️ Da mesma forma, uma senha fraca (muito pequena e/ou com todos os caracteres do mesmo tipo) que não pôde ser quebrada pelo meu algoritmo não se traduz em uma senha segura.⚠️  

Procure sempre fazer uma senha com no mínimo 12 caracteres e alterne entre eles para criar uma senha forte, combinando letras MAIÚSCULAS, minúsculas, núm3r05 e símb*|*s, e faça isso sem seguir uma 0Rd3M eSp3c!f!c4.
(É possível personalizar o numero de tentativas por thread na linha 18)""" 
    
        # Links clicáveis na interface
    link_github = tk.Label(
        frame, 
        text="Github: https://github.com/JOHNcoding9", 
        font=("Arial", 12), 
        fg=cor_4, 
        cursor="hand2",
        bg=cor_1
    )
    link_github.pack(pady=5)
    link_github.bind("<Button-1>", lambda e: abrir_link("https://github.com/JOHNcoding9"))

    link_linkedin = tk.Label(
        frame, 
        text="Linkedin: https://shorturl.at/08FdV", 
        font=("Arial", 12), 
        fg=cor_4, 
        cursor="hand2",
        bg=cor_1
    )
    link_linkedin.pack(pady=5)
    link_linkedin.bind("<Button-1>", lambda e: abrir_link("https://shorturl.at/08FdV"))

    tk.Label(frame, text=texto, font=("Arial", 14), bg=cor_1, fg=cor_3, wraplength=500, justify="left").pack(padx=10, pady=20)
    botao = tk.Button(
    frame, 
    text="Voltar", 
    font=("Arial", 12), 
    command=tela_inicial, 
    fg=cor_3, 
    bg=cor_5,
    activebackground=cor_2,
    activeforeground=cor_1,
    relief="raised",
    bd=4
    )
    botao.pack(pady=10)


# Classe para redirecionar saída para o widget Text
class RedirectText:
    def __init__(self, widget):
        self.widget = widget

    def write(self, text):
        # Habilita a edição, insere o texto e desabilita novamente
        self.widget.configure(state='normal')
        self.widget.insert('end', text)
        self.widget.configure(state='disabled')
        # Rola para o final automaticamente
        self.widget.see('end')

    def flush(self):
        pass  # Necessário para compatibilidade com o comportamento de flush()

# Função para sincronizar o terminal
def sincronizar_terminal(terminal):
    sys.stdout = RedirectText(terminal)  # Redireciona stdout
    sys.stderr = RedirectText(terminal)  # Redireciona stderr


def tela_secundaria(caractere):


    atualizar_tela()

    chars = caractere

    # Criar elementos novos no frame
    tk.Label(frame, text="Digite sua senha:", font=("Arial", 14), bg=cor_1, fg=cor_3).pack(pady=10)
    entrada = tk.Entry(frame, font=("Arial", 14), width=30)
    entrada.pack(pady=5)

    def mostrar_texto(chars):
     
     senha = entrada.get()  # Obtém a senha digitada pelo usuário
     senha = senha.strip()
    
     if senha:
       
       if not all(c in conjuntos_caracteres[chars] for c in senha): # A função all() em Python é uma função embutida que recebe um iterável (como uma lista, tupla, string, etc.) e retorna True somente se todos os elementos do iterável forem avaliados como True. Caso algum elemento seja avaliado como False, ela retorna False.
           print('><'*20)
           print(f'Erro! senha não corresponde com caractere do tipo {chars}')    

       else:   
         if chars == 'letra_numero':
           if senha.isupper():
              chars = "letra_numero_mai"
              print('tudo Maiúsculo')
           if senha.islower():
              chars = "letra_numero_min"
              print('tudo minúsculo')


         print(f"Senha: {senha}")
         print("=-=" * 20)
         print("Tentando quebrar senha ...")
   
         def rodar_quebrador(senha_local):
          resultado = executar_quebrador(senha_local, chars, num_threads=num_cores)
          # Atualizar o terminal após o término
          terminal.configure(state='normal')
          terminal.insert('end', f"\n{resultado}\n")
          terminal.configure(state='disabled')
          terminal.see('end')
    
         # Rodar_quebrador em Thread separada para o programa não crashar
         threading.Thread(target=lambda: rodar_quebrador(senha), daemon=True).start()



    botao = tk.Button(
        frame, 
        text="Avaliar senha", 
        font=("Arial", 12), 
        command=lambda: mostrar_texto(chars), 
        fg=cor_3, 
        bg=cor_5,
        activebackground=cor_2,
        activeforeground=cor_1,
        relief="raised",
        bd=4
    )
    botao.pack(pady=10)

    botao_voltar = tk.Button(
        frame, 
        text="Voltar", 
        font=("Arial", 12), 
        command=tela_inicial, 
        fg=cor_3, 
        bg=cor_5,
        activebackground=cor_2,
        activeforeground=cor_1,
        relief="raised",
        bd=4
    )
    botao_voltar.pack(pady=10)


    terminal_frame = tk.Frame(frame, bg=cor_1)
    terminal_frame.pack(pady=10, fill='both', expand=True)

    terminal = tk.Text(terminal_frame, wrap='word', height=10, bg=cor_1, fg=cor_3, state='disabled',font=("Arial", 13))

    terminal.pack(fill='both', expand=True, padx=5, pady=5)

    # Sincronizar o terminal
    sincronizar_terminal(terminal)

    # calculo dos nucleos e definição das Threads
    num_cores = multiprocessing.cpu_count()
    print(f"Número de núcleos disponíveis: {num_cores}")

    if num_cores > 3:
     num_cores = num_cores - 2  # Utiliza todos os núcleos, menos 2
    else:
        num_cores = 1  # Garante pelo menos 1 thread em sistemas de núcleo único
        
    num_threads = min(num_cores, 8) # Escolhe o menor valor entre núcleos e o limite (8)
    print(f"Número de threads utilizadas: {num_threads}")

    print(f'Numero definido de tentativas por Thread: {num_tentativas}')


def tela_inicial():

    # Atualiza a tela e limpa widgets existentes no frame
    atualizar_tela()
    
    # Criar e posicionar os botões no frame
    for nome, comando, cor_texto, cor_fundo in botoes:
        botao = tk.Button(
            frame,
            text=nome,
            command=comando,
            fg=cor_texto,
            bg=cor_fundo,
            width=15,
            height=2,
            font=("Helvetica", 9, "bold"),
            activebackground=cor_2,
            activeforeground=cor_1,
            relief="raised",
            bd=4
        )

        # Posicionar os outros botões à esquerda
        botao.pack(side='left', padx=5)


# Lista de botões principais
botoes = [
    ('Letras',lambda: tela_secundaria('letras'), cor_3, cor_5),
    ('Números',lambda: tela_secundaria('numeros'), cor_3, cor_5),
    ('Letra e Número',lambda: tela_secundaria('letra_numero'), cor_3, cor_5),
    ('Tudo + Símbolos',lambda: tela_secundaria('tudo'), cor_3, cor_5),
    ('Info', Info, cor_3, cor_5)
]


# =======================================================================================================================================
# Aplicativo quebrador de senha
def indice_para_tentativa(i, chars, tamanho):
    base = len(chars)
    tentativa = [''] * tamanho
    for pos in range(tamanho - 1, -1, -1):
        i, resto = divmod(i, base)
        tentativa[pos] = chars[resto]
    return ''.join(tentativa)

def gerar_tentativas(senha, chars, inicio, fim, processo_id, limite_tentativas, senha_encontrada, senha_encontrada_flag):
    contador = 0
    tempo_inicio = time.time()
    tamanho = len(senha)

    print(f"[Processo-{processo_id + 1}] Iniciado.")
    print(f"[Processo-{processo_id + 1}] Intervalo: {inicio} a {fim}")

    for i in range(inicio, fim):
        if senha_encontrada_flag.value:
            return

        tentativa_str = indice_para_tentativa(i, chars, tamanho)

        if tentativa_str == senha:
            senha_encontrada.value = tentativa_str.encode('utf-8')
            senha_encontrada_flag.value = True
            tempo_fim = time.time()
            print(f"[Processo-{processo_id + 1}] Senha encontrada: {tentativa_str}")
            print(f"Tempo: {tempo_fim - tempo_inicio:.2f} segundos")
            return

        contador += 1

        if limite_tentativas is not None and contador >= limite_tentativas:
            tempo_fim = time.time()
            print(f"[Processo-{processo_id + 1}] Limite atingido. Última tentativa: {tentativa_str}")
            print(f"Tempo de execução: {tempo_fim - tempo_inicio:.2f} segundos")
            return



def criar_processos(senha, chars, num_processos=4, limite_tentativas=1000000000):
    senha_encontrada = multiprocessing.Value(ctypes.c_char_p, b'')
    senha_encontrada_flag = multiprocessing.Value('b', False)


    total_combinacoes = len(chars) ** len(senha)
    chunk_size = total_combinacoes // num_processos

    processos = []
    for processo_id in range(num_processos):
        inicio = processo_id * chunk_size
        fim = inicio + chunk_size if processo_id != num_processos - 1 else total_combinacoes
        p = multiprocessing.Process(
            target=gerar_tentativas,
            args=(senha, chars, inicio, fim, processo_id, limite_tentativas, senha_encontrada, senha_encontrada_flag)
        )
        processos.append(p)
        p.start()

    for p in processos:
        p.join()

    resultado = senha_encontrada.value.decode('utf-8')
    return resultado



def executar_quebrador(senha, chars='numeros', num_threads=4):
    '''senha = palavra chave a ser adivinhada pelo programa
       chars = caracteres a serem usados (padrão numeros)
       num_threads = numeros de threads simultâneas (padrão 4)'''
    
    try:
        inicio = time.time()

        # Verificação usando o dicionário (se ele existir)
        if dicionario:
            if (senha in dicionario or
                senha.lower() in dicionario or
                senha.upper() in dicionario or
                senha.capitalize() in dicionario):

                fim = time.time()
                mensagem = f"Senha adivinhada: {senha} Tempo: {fim - inicio:.2f} segundos! Tentativas: 0 (tão fraca que estava no dicionário)"
                return mensagem 
            else:
                print("Dicionário checado, nada encontrado ...")
                print("Tentando quebrar manualmente ....")

        # Pega o conjunto de caracteres escolhido
        chars_escolhidos = conjuntos_caracteres.get(chars, numeros)  # padrão = numeros

        # Tentando quebrar a senha usando multithreading
        tentativa = criar_processos(senha, chars_escolhidos, num_threads)
        fim = time.time()

        if tentativa:
            return f"Senha adivinhada: {tentativa} em {fim - inicio:.2f} segundos!"
        else:
            return f"Senha não encontrada. Tempo: {fim - inicio:.2f} segundos."
        
    except Exception as e:
        print(f"Erro inesperado na execução do quebrador: {e}")


if __name__ == '__main__':
    multiprocessing.freeze_support()
    # código que inicia seu programa, cria GUI, chama criar_processos etc.

    tela_inicial()

    # Inicializar o projeto
    janela.mainloop()
