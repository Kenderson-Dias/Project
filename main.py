# main.py
import os
from database import class_tree, regioes, sk_tree_database, passivas_info, tier3_evolucoes, tier4_evolucoes, ramo_por_classe, drop_fontes_itens
from models import Player
from combat import batalhar

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def ler_inteiro_validado(mensagem, min_val=None, max_val=None):
    """Garante tratamento de erros robusto para entradas numéricas em menus (Requisito 5)."""
    while True:
        try:
            val = int(input(mensagem))
            if (min_val is not None and val < min_val) or (max_val is not None and val > max_val):
                print(f"⚠️ Por favor, digite um número entre {min_val} e {max_val}.")
                continue
            return val
        except ValueError:
            print("❌ Entrada inválida! Digite apenas números inteiros.")

def exibir_status(player):
    atq_total = player.ataque_base + player.arma["BonusAtaque"]
    def_total = player.defesa_base + player.armadura["BonusDefesa"]
    regiao_info = regioes[player.regiao_atual]

    print("==========================================================================")
    print(f" Herói: {player.nome} | Classe: {player.classe} (Tier {player.classe_nivel}) | Nível {player.nivel}")
    print(f" Região: {regiao_info['Nome']} (Level Cap: {regiao_info['LevelCap']})")
    print(f" HP: {player.hp}/{player.hp_max} | MP: {player.mp}/{player.mp_max}")
    print(f" Ataque Total: {atq_total} | Defesa Total: {def_total}")
    print(f" XP: {player.xp}/{player.xp_necessario} | Ouro: {player.ouro} 🪙 | Poções HP: {player.pocoes} | Poções MP: {player.pocoes_mp}")
    print("==========================================================================")

def usar_pergaminho_menu(player):
    while True:
        limpar_tela()
        print("==========================================================================")
        print("                    📜 INVENTÁRIO DE PERGAMINHOS 📜                      ")
        print("==========================================================================")
        print(f"1. Pergaminho de Status Base ({player.pergaminhos['StatusBase']} un)")
        print(f"2. Pergaminho da Bênção do Guerreiro ({player.pergaminhos['BencaoGuerreiro']} un)")
        print(f"3. Pergaminho da Sorte Sinistra ({player.pergaminhos['SorteSinistra']} un)")
        print(f"4. Pergaminho da Transmutação Primordial ({player.pergaminhos['TrocaTier1']} un)")
        print(f"5. Pergaminho do Espelho de Paridade ({player.pergaminhos['TrocaMesmoTier']} un)")
        print(f"6. Pergaminho da Reencarnação ({player.pergaminhos['ResetNivel1']} un)")
        print("0. Voltar")
        print("--------------------------------------------------------------------------")

        op = ler_inteiro_validado("Escolha um pergaminho: ", 0, 6)
        if op == 0:
            break
        elif op == 1 and player.pergaminhos["StatusBase"] > 0:
            player.pergaminhos["StatusBase"] -= 1
            player.ataque_base += 5
            player.defesa_base += 5
            player.hp_max += 30
            player.hp += 30
            player.mp_max += 20
            player.mp += 20
            print("\n✨ Status aumentados permanentemente!")
        input("Pressione Enter...")

def gerenciar_habilidades(player):
    while True:
        limpar_tela()
        ramo_jogador = ramo_por_classe.get(player.classe_base, "Guerreiro")
        tier_jogador = player.classe_nivel

        print("==========================================================================")
        print("                🌳 ÁRVORE DE HABILIDADES E EVOLUÇÃO 🌳                     ")
        print("==========================================================================")
        print(f" Herói: {player.nome} | Ramo: {ramo_jogador} | Classe: {player.classe} (Tier {tier_jogador})")
        print(f" Ouro: {player.ouro} 🪙 | Pontos de Skill: {player.pontos_skill}")
        print("--------------------------------------------------------------------------")
        print("1. Visualizar e Aprender Habilidades")
        print("2. Evoluir de Classe")
        print("3. Voltar")

        op = ler_inteiro_validado("Escolha: ", 1, 3)
        if op == 1:
            limpar_tela()
            print(f"=== HABILIDADES DO RAMO: {ramo_jogador.upper()} ===\n")
            habs_disponiveis = []
            ramo_dados = sk_tree_database.get(ramo_jogador, {})

            for t in range(2, tier_jogador + 1):
                if t in ramo_dados:
                    for sk in ramo_dados[t]:
                        if sk["ClasseReq"] == player.classe or player.classe_nivel >= t:
                            habs_disponiveis.append((t, sk))

            for idx, (t_nivel, sk) in enumerate(habs_disponiveis):
                aprendida = any(s["Nome"] == sk["Nome"] for s in player.skills)
                status = "✅ [APRENDIDA]" if aprendida else "❌ [NÃO APRENDIDA]"
                print(f"{idx + 1}. [Tier {t_nivel}] {sk['Nome']} - {status} (Custo: {sk['CustoOuro']} 🪙)")

            s_esc = ler_inteiro_validado("Escolha número para aprender (0 para cancelar): ", 0, len(habs_disponiveis))
            if s_esc > 0:
                t_esc, sk_sel = habs_disponiveis[s_esc - 1]
                if any(s["Nome"] == sk_sel["Nome"] for s in player.skills):
                    print("\n❌ Habilidade já aprendida!")
                elif player.ouro < sk_sel["CustoOuro"]:
                    print("\n❌ Ouro insuficiente!")
                else:
                    player.ouro -= sk_sel["CustoOuro"]
                    player.skills.append(sk_sel)
                    print(f"\n✨ Habilidade [{sk_sel['Nome']}] aprendida!")
            input("Enter...")
        elif op == 2:
            limpar_tela()
            if player.nivel >= 5 and player.classe_nivel == 1:
                opcoes = class_tree[player.classe_base]["OpcoesAvancadas"]
                for idx, av in enumerate(opcoes):
                    print(f"{idx + 1}. {av}")
                ev_esc = ler_inteiro_validado("Escolha a evolução: ", 1, len(opcoes)) - 1
                player.classe = opcoes[ev_esc]
                player.classe_nivel = 2
                print(f"\nEvoluído para {player.classe} (Tier 2)!")
            input("Enter...")
        elif op == 3:
            break

def biblioteca():
    while True:
        limpar_tela()
        print("==========================================================================")
        print("                    📚 BIBLIOTECA DE CONHECIMENTO 📚                      ")
        print("==========================================================================")
        print("1. Consultar Mapas e Regiões")
        print("2. Voltar")
        op = ler_inteiro_validado("Escolha: ", 1, 2)
        if op == 1:
            limpar_tela()
            for reg_id, r in regioes.items():
                print(f"📌 REGIÃO {reg_id}: {r['Nome']} (Cap Nível {r['LevelCap']})")
            input("\nEnter para continuar...")
        else:
            break

def loja(player):
    while True:
        limpar_tela()
        print("--- LOJA DA VILA ---")
        print(f"Ouro: {player.ouro} 🪙 | Poções HP: {player.pocoes}")
        print("1. Comprar Poção HP (20 Ouro)")
        print("2. Comprar Poção MP (20 Ouro)")
        print("3. Sair")
        op = ler_inteiro_validado("Escolha: ", 1, 3)
        if op == 1 and player.ouro >= 20:
            player.ouro -= 20; player.pocoes += 1; print("Poção comprada!")
        elif op == 2 and player.ouro >= 20:
            player.ouro -= 20; player.pocoes_mp += 1; print("Poção MP comprada!")
        elif op == 3:
            break
        input("Enter...")

def criar_personagem():
    limpar_tela()
    print("=== CRIAÇÃO DE PERSONAGEM ===")
    nome = input("Nome do herói: ")
    print("\nEscolha sua classe inicial:")
    classes = list(class_tree.keys())
    for idx, c in enumerate(classes):
        i = class_tree[c]
        print(f"{idx + 1}. {c} (HP: {i['HPBase']}, MP: {i['MPBase']}, Atq: {i['AtaqueBase']}, Def: {i['DefesaBase']})")
    
    esc = ler_inteiro_validado("Número da classe: ", 1, len(classes)) - 1
    return Player(nome, classes[esc])

def main():
    player = criar_personagem()
    while True:
        limpar_tela()
        exibir_status(player)
        print("\n=== MENU PRINCIPAL ===")
        print("1. Caçar Monstros Normais")
        print("2. Enfrentar Chefão da Região")
        print("3. Selecionar Região")
        print("4. Habilidades e Evolução")
        print("5. Compêndio")
        print("6. Visitar Loja")
        print("7. Inventário")
        print("0. Sair")

        opcao = ler_inteiro_validado("Escolha uma opção: ", 0, 7)

        if opcao == 1:
            batalhar(player, is_boss=False)
        elif opcao == 2:
            batalhar(player, is_boss=True)
        elif opcao == 3:
            limpar_tela()
            print("=== SELEÇÃO DE REGIÃO ===")
            for r_id in range(1, player.regiao_max_desbloqueada + 1):
                print(f"{r_id}. {regioes[r_id]['Nome']} (Cap Nível {regioes[r_id]['LevelCap']})")
            nova_reg = ler_inteiro_validado("Escolha a região: ", 1, player.regiao_max_desbloqueada)
            player.regiao_atual = nova_reg
            print(f"Região alterada!")
            input("Enter...")
        elif opcao == 4:
            gerenciar_habilidades(player)
        elif opcao == 5:
            biblioteca()
        elif opcao == 6:
            loja(player)
        elif opcao == 7:
            limpar_tela()
            print("=== INVENTÁRIO ===")
            print("1. Usar Poção de HP")
            print("2. Usar Poção de MP")
            print("3. Usar Pergaminhos")
            print("4. Ver Itens Raros")
            print("0. Voltar")
            inv_op = ler_inteiro_validado("Escolha: ", 0, 4)
            if inv_op == 1: player.usar_pocao(); input("Enter...")
            elif inv_op == 2: player.usar_pocao_mp(); input("Enter...")
            elif inv_op == 3: usar_pergaminho_menu(player)
            elif inv_op == 4:
                limpar_tela()
                print("=== ITENS ADQUIRIDOS ===")
                for item in player.inventario_itens:
                    print(f" • {item}")
                input("Enter...")
        elif opcao == 0:
            print("Saindo do jogo... Até logo!")
            break

if __name__ == "__main__":
    main()