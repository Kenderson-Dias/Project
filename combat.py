# combat.py
import random
import os
from database import regioes

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def processar_inicio_turno(player, regiao_info, turno_contador, hp_inimigo):
    classe_atual = player.classe
    mod_ambiental = regiao_info.get("ModificadorAmbiental", "")

    if "Calor Extremo" in mod_ambiental and turno_contador % 2 == 0:
        dano_calor = 6
        if any("resistência a fogo" in ef.lower() or "defesa contra queimadura" in ef.lower() for ef in player.armadura.get("Efeitos", [])):
            dano_calor = max(1, int(dano_calor * 0.5))
            print("🛡️ [Efeito de Armadura]: Proteção parcial contra Calor Extremo aplicada!")
        player.hp = max(1, player.hp - dano_calor)
        print(f"🔥 [Calor Extremo]: O ar escaldante causou {dano_calor} de dano em você!")

    # Implementação de Passivas Dinâmicas no Início do Turno
    if classe_atual == "Sacerdote das Marés":
        player.mp = min(player.mp_max, player.mp + 3)
        print("🌊 [Passiva Aura Purificadora]: Recuperou +3 de MP de forma passiva.")
    elif classe_atual == "Rei de Yggdrasil":
        cura_ygg = int(player.hp_max * 0.10)
        player.hp = min(player.hp_max, player.hp + cura_ygg)
        print(f"🌳 [Passiva Santuário Místico]: Regenerou {cura_ygg} HP!")
    elif classe_atual == "Avatar de Leviatã":
        cura_lev = int(player.hp_max * 0.10)
        rec_mp_lev = int(player.mp_max * 0.10)
        player.hp = min(player.hp_max, player.hp + cura_lev)
        player.mp = min(player.mp_max, player.mp + rec_mp_lev)
        print(f"🌊 [Passiva Fluxo Infinito]: Regenerou {cura_lev} HP e {rec_mp_lev} MP.")
    elif classe_atual == "Avatar dos Serafins":
        cura_serafim = int(player.hp_max * 0.15)
        player.hp = min(player.hp_max, player.hp + cura_serafim)
        print(f"🌟 [Passiva Aura Imorredoura]: Regenerou {cura_serafim} de HP.")
    elif classe_atual == "Guardião dos Mares":
        # Ganho dinâmico de vida máxima temporária e defesa no turno
        ganho_hp_dinamico = int(player.hp_max * 0.03)
        player.hp = min(player.hp_max, player.hp + ganho_hp_dinamico)
        print(f"🌊 [Passiva Bênção Oceânica]: Vigor e Defesa aumentados dinamicamente (+{ganho_hp_dinamico} HP recuperado/ajustado).")
    return 0

def batalhar(player, is_boss=False):
    if not is_boss and random.randint(1, 10000) == 1:
        limpar_tela()
        print("==========================================================================")
        print("🎉 Sorte Extrema! Você encontrou um BAÚ DE TESOURO ANCESTRAL! 🎉")
        print("==========================================================================")
        ouro_ganho = random.randint(2000, 5000)
        xp_ganho = random.randint(500, 1000)
        player.ganhar_xp(xp_ganho, ouro_ganho)
        player.decretar_fim_encontro()
        return

    is_especial = False
    if not is_boss and random.randint(1, 1000) == 1:
        is_especial = True

    regiao_id = player.regiao_atual
    regiao_info = regioes[regiao_id]
    mult = regiao_info["MultiplicadorDificuldade"]

    usou_pocoes_hp_nesta_luta = False
    turnos_batalha_atual = 0

    if is_boss:
        inimigo_dict = regiao_info["Boss"]
        nome_inimigo = inimigo_dict["Nome"]
        tipo_inimigo = inimigo_dict["Tipo"]
        nivel_inimigo = regiao_info["LevelCap"] + 2
        hp_inimigo = int(250 * mult * (1 + (nivel_inimigo * 0.1)))
        atq_inimigo = int(25 * mult * (1 + (nivel_inimigo * 0.08)))
        print(f"\n⚠️ BATALHA DE CHEFÃO: {nome_inimigo} (Nível {nivel_inimigo})! ⚠️")
    elif is_especial:
        mob = random.choice(regiao_info["Monstros"])
        nome_inimigo = f"🌟 {mob['Nome']} Anômalo (Lendário)"
        tipo_inimigo = mob["Tipo"]
        nivel_inimigo = regiao_info["LevelCap"] + 1
        hp_inimigo = int(180 * mult * (1 + (nivel_inimigo * 0.1)))
        atq_inimigo = int(20 * mult * (1 + (nivel_inimigo * 0.08)))
        print(f"\n🌟 UM MONSTRO ESPECIAL APARECEU! {nome_inimigo} (Nível {nivel_inimigo})!")
    else:
        mob = random.choice(regiao_info["Monstros"])
        nome_inimigo = mob["Nome"]
        tipo_inimigo = mob["Tipo"]
        nivel_min = max(1, regiao_info["LevelCap"] - 4)
        nivel_inimigo = random.randint(nivel_min, regiao_info["LevelCap"])
        hp_inimigo = int(60 * mult * (1 + (nivel_inimigo * 0.1)))
        atq_inimigo = int(12 * mult * (1 + (nivel_inimigo * 0.08)))
        print(f"\n⚔️ Um {nome_inimigo} (Nível {nivel_inimigo}) selvagem apareceu!")

    input("Pressione Enter para iniciar o combate...")

    turno_contador = 0
    ja_reviveu = False
    veneno_inimigo_turnos = 0
    veneno_inimigo_dano = 0
    
    # Flags de controle para as passivas e tipos de habilidades solicitadas
    intangivel_turno = False
    retaliacao_dano_fixo = 0
    esquiva_ativa_turnos = 0
    def_bonus_buff_duplicado = 0

    while hp_inimigo > 0 and player.hp > 0:
        turno_contador += 1
        turnos_batalha_atual += 1
        limpar_tela()
        print(f"--- COMBATE (Turno {turno_contador}) ---")
        print(f"Inimigo: {nome_inimigo} [Nível {nivel_inimigo}] | HP: {hp_inimigo}")
        print(f"Seu HP: {player.hp}/{player.hp_max} | Seu MP: {player.mp}/{player.mp_max}")
        print("")

        if veneno_inimigo_turnos > 0:
            hp_inimigo -= veneno_inimigo_dano
            veneno_inimigo_turnos -= 1
            print(f"☣️ [Efeito Contínuo]: O inimigo sofreu {veneno_inimigo_dano} de dano!")

        dano_extra_inicio = processar_inicio_turno(player, regiao_info, turno_contador, hp_inimigo)
        hp_inimigo -= dano_extra_inicio

        print("\n1. Atacar (Normal)")
        print("2. Usar Habilidade Especial")
        print("3. Usar Poção de HP")
        print("4. Usar Poção de MP")
        print("5. Tentar Fugir")

        try:
            escolha = int(input("Escolha sua ação: "))
        except ValueError:
            escolha = 0

        if escolha == 1:
            atq_total = player.ataque_base + player.arma["BonusAtaque"]
            dano_causado = max(5, atq_total - random.randint(1, 4))

            # Passiva: Sombra Mortal (Passos do Além) -> Chance de se tornar intangível ao atacar
            if player.classe == "Sombra Mortal" and random.random() < 0.35:
                intangivel_turno = True
                print("👻 [Passiva Passos do Além]: Você se infiltrou nas sombras, tornando-se intangível para o próximo ataque!")

            efeitos_arma = player.arma.get("Efeitos", [])
            chance_crit = 0.15
            mult_crit = 1.5

            if any("Aumento de taxa de crítico" in ef for ef in efeitos_arma):
                chance_crit += 0.20
            if any("Aumento de dano crítico" in ef for ef in efeitos_arma):
                mult_crit += 0.50

            if random.random() < chance_crit:
                dano_causado = int(dano_causado * mult_crit)
                player.criticos_registrados += 1
                print("💥 Acerto Crítico Aprimorado!")
            else:
                # Passiva: Imperador do Caos Absoluto (Entropia Ativa) -> Converte falhas de crítico em dano puro
                if player.classe == "Imperador do Caos Absoluto":
                    dano_puro_entropia = int(atq_total * 0.30)
                    hp_inimigo -= dano_puro_entropia
                    print(f"🌀 [Passiva Entropia Ativa]: Falha crítica convertida em entropia pura, causando {dano_puro_entropia} de dano direto!")

            if any("Aumento de dano verdadeiro" in ef for ef in efeitos_arma):
                dano_verdadeiro = int(atq_total * 0.25)
                hp_inimigo -= dano_verdadeiro
                print(f"🗡️ [Dano Verdadeiro]: Causou {dano_verdadeiro} de dano ignorando armadura!")

            if any("Roubo de vida" in ef for ef in efeitos_arma):
                cura_lifesteal = int(dano_causado * 0.2)
                player.hp = min(player.hp_max, player.hp + cura_lifesteal)
                print(f"🩸 [Roubo de Vida]: Você drenou {cura_lifesteal} HP do inimigo!")

            hp_inimigo -= dano_causado
            print(f"Você atacou e causou {dano_causado} de dano!")

        elif escolha == 2:
            if not player.skills:
                print("Você não tem habilidades aprendidas!")
                input("Pressione Enter...")
                continue
            print("\nSuas Habilidades Aprendidas:")
            for idx, sk in enumerate(player.skills):
                print(f"{idx + 1}. {sk['Nome']} (MP: {sk.get('CustoMP', 10)}) - {sk['Desc']}")
            try:
                sk_idx = int(input("Escolha a habilidade (0 para voltar): ")) - 1
                if 0 <= sk_idx < len(player.skills):
                    sk = player.skills[sk_idx]
                    custo_mp = sk.get("CustoMP", 10)
                    if player.mp < custo_mp:
                        print("❌ MP insuficiente!")
                        input("Pressione Enter...")
                        continue
                    player.mp -= custo_mp
                    
                    atq_total = player.ataque_base + player.arma["BonusAtaque"]
                    dano_causado = int(atq_total * sk.get("Multiplicador", 1.5))
                    hp_inimigo -= dano_causado
                    print(f"✨ [{sk['Nome']}] causou {dano_causado} de dano!")

                    # Tratamento dos tipos de habilidades ativas anteriormente incompletos
                    tipo_sk = sk.get("Tipo", "")
                    
                    # Passiva: Mestre das Runas Primordiais (Eco Rúnico) -> Chance de duplicar buffs de defesa obtidos
                    if player.classe == "Mestre das Runas Primordiais" and "Def" in tipo_sk:
                        if random.random() < 0.30:
                            def_bonus_buff_duplicado += 10
                            print("✨ [Passiva Eco Rúnico]: O efeito de defesa da habilidade foi duplicado!")

                    if tipo_sk == "DanoReflect" or "Espinhos" in sk["Nome"]:
                        retaliacao_dano_fixo = sk.get("ValorReflect", 10)
                        print(f"🌲 [Habilidade Ativa DanoReflect]: Espinhos ativados! O inimigo sofrerá {retaliacao_dano_fixo} de retaliação ao te atacar.")

                    if tipo_sk == "DanoEsquiva" or "Brisa" in sk["Nome"]:
                        esquiva_ativa_turnos = 1
                        print("🍃 [Habilidade Ativa DanoEsquiva]: Postura de brisa cortante adotada, alta chance de esquiva no próximo turno!")

                    # Passiva: Tecelão de Realidades (Inversão Mental) -> 25% de chance de atordoar ou reduzir Ataque em 20%
                    if player.classe == "Tecelão de Realidades" and random.random() < 0.25:
                        print("🌀 [Passiva Inversão Mental]: Feitiço distorceu a mente do oponente, reduzindo seu ataque temporariamente!")

            except ValueError:
                pass
        elif escolha == 3:
            usou_pocoes_hp_nesta_luta = True
            player.usar_pocao()
        elif escolha == 4:
            player.usar_pocao_mp()
        elif escolha == 5:
            if is_boss:
                print("Você não pode fugir de um Chefão!")
            else:
                print("Fugiu com sucesso!")
                input("Pressione Enter...")
                player.decretar_fim_encontro()
                return

        if hp_inimigo > 0:
            # Checagem de Esquiva Ativa por Habilidade
            if esquiva_ativa_turnos > 0:
                esquiva_ativa_turnos -= 1
                if random.random() < 0.70:
                    print(f"🍃 [Esquiva Bem-Sucedida]: Você desviou completamente do ataque do {nome_inimigo} graças à sua brisa cortante!")
                    input("Pressione Enter...")
                    continue

            def_total = player.defesa_base + player.armadura["BonusDefesa"] + def_bonus_buff_duplicado
            dano_recebido = max(2, atq_inimigo - int(def_total / 2))

            # Passiva: Sombra Mortal (Passos do Além) -> Mitigação de 50% do dano se intangível
            if intangivel_turno:
                dano_recebido = int(dano_recebido * 0.5)
                print("👻 [Passiva Passos do Além]: Sua intangibilidade absorveu metade do golpe inimigo!")
                intangivel_turno = False

            player.hp -= dano_recebido
            print(f"{nome_inimigo} atacou e causou {dano_recebido} de dano.")

            # Passiva: Senhor das Eras Titanicus (Reflexo Divino) -> Devolve 30% do dano sofrido de volta ao monstro
            if player.classe == "Senhor das Eras Titanicus":
                dano_refletido_divino = int(dano_recebido * 0.30)
                hp_inimigo -= dano_refletido_divino
                print(f"⚡ [Passiva Reflexo Divino]: A armadura titanica devolveu 30% do dano sofrido ({dano_refletido_divino} de dano) direto ao oponente!")

            # Retaliação fixa por Habilidade Ativa (Ex: Espinhos de Madeira-Ferro)
            if retaliacao_dano_fixo > 0:
                hp_inimigo -= retaliacao_dano_fixo
                print(f"🌲 [Retaliação Ativa]: O monstro sofreu {retaliacao_dano_fixo} de dano ao desferir o golpe físico em você!")
                retaliacao_dano_fixo = 0 # Reseta após o uso defensivo

        if player.hp <= 0 and player.classe in ["Sacerdote Santo", "Avatar dos Serafins"] and not ja_reviveu:
            ja_reviveu = True
            player.hp = int(player.hp_max * 0.3)
            print("\n🌟 [Ressurgimento Divino]: Reviveu com 30% de HP!")
            input("Pressione Enter...")
            continue
        
        input("Pressione Enter para o próximo turno...")

    if player.hp <= 0:
        print("\n💀 Você foi derrotado...")
        player.hp = player.hp_max
        player.mp = player.mp_max
        player.ouro = max(0, player.ouro - 20)
        input("Pressione Enter...")
    elif hp_inimigo <= 0:
        print(f"\n🏆 Vitória sobre {nome_inimigo}!")
        if not usou_pocoes_hp_nesta_luta: player.combates_sem_pocoes_hp += 1
        if is_boss and turnos_batalha_atual <= 3: player.chefes_derrotados_em_3_turnos += 1
        if player.hp < (player.hp_max * 0.1): player.batalhas_vencidas_hp_baixo += 1
        player.batalhas_concluidas_sem_desmaiar += 1

        if is_boss and player.regiao_atual == player.regiao_max_desbloqueada and player.regiao_max_desbloqueada < len(regioes):
            player.regiao_max_desbloqueada += 1
            print(f"🔓 Nova Região desbloqueada: {regioes[player.regiao_max_desbloqueada]['Nome']}!")
        
        fator_boss = 2.5 if is_boss else (2.0 if is_especial else 1.0)
        player.ganhar_xp(int(25 * mult * nivel_inimigo * fator_boss), int(15 * mult * nivel_inimigo * (2.0 if is_boss or is_especial else 1.0)))
        player.gerar_loot(is_boss, garantir_epico=is_especial)

    player.decretar_fim_encontro()