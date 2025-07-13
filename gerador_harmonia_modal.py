import random

# Notas possíveis (com sustenidos)
notas = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

# Tipos de acorde (maior ou menor)
tipos = ['', 'm']

# Extensões e variações possíveis
extensoes = ['', '7', '7M',
                'dim', 'aug', '6', '9', '11', '13', 'sus2', 'sus4', 'add9'
]

pesos_extensoes = [
    10, 10, 10,  # comuns
    5, 5, 5, 4, 4, 3, 3, 3, 2  # menos comuns
]


def gerar_acorde():
    nota = random.choice(notas)
    tipo = random.choice(tipos)
    extensao = random.choices(extensoes, weights=pesos_extensoes, k=1)[0]
    

    if tipo == 'm' and extensao == 'sus2' or 'sus4' or 'dim':
        tipo = ''

    acorde = nota + tipo + extensao

    return acorde

def main():
    print("🎹 Gerador de Acordes Aleatórios")
    print("Pressione Enter para gerar um novo acorde.")
    print("Digite 'f' e pressione Enter para sair.\n")

    while True:
        entrada = input()
        if entrada == 'f':
            print("Encerrando o gerador. Até logo!")
            break
        acorde = gerar_acorde()
        # Volta para o começo da linha e imprime o acorde
        print(f"🎵 {acorde}")

if __name__ == '__main__':
    main()
