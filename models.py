# models.py
import random
from database import class_tree, regioes, drop_fontes_itens, passivas_info, tier4_evolucoes

class Player:
    def __init__(self, nome, classe_base):
        self.nome = nome
        self.classe_base = classe_base
        self.classe = classe_base
        self.classe_nivel = 1
        self.nivel = 1
        self.xp = 0
        self.xp_necessario = 50
        self.ouro = 30
        
        info = class_tree.get(classe_base, class_tree["Guerreiro"])
        self.hp_max = info["HPBase"]
        self.hp = info["HPBase"]
        self.mp_max = info["MPBase"]
        self.mp = info["MPBase"]
        self.ataque_base = info["AtaqueBase"]
        self.defesa_base = info["DefesaBase"]
        
        self.pontos_skill = 0
        self.regiao_atual = 1
        self.regiao_max_desbloqueada = 1
        
        self.arma = {
            "Nome": "Espada de Madeira", 
            "BonusAtaque": 3, 
            "Raridade": "Comum", 
            "Efeitos": []
        }
        self.armadura = {
            "Nome": "Roupas de Pano", 
            "BonusDefesa": 2, 
            "Raridade": "Comum", 
            "Efeitos": []
        }
        
        self.skills = []
        self.pocoes = 3
        self.pocoes_mp = 2
        
        self.compras_pocoes_hp = 0
        self.compras_pocoes_mp = 0
        
        self.pergaminhos = {
            "StatusBase": 0,
            "BencaoGuerreiro": 0,
            "SorteSinistra": 0,
            "TrocaTier1": 0,
            "TrocaMesmoTier": 0,
            "ResetNivel1": 0
        }
        
        self.buffs_ativos = {}
        self.inventario_itens = []
        
        self.combates_sem_pocoes_hp = 0
        self.criticos_registrados = 0
        self.chefes_derrotados_em_3_turnos = 0
        self.dano_curado_total = 0
        self.batalhas_vencidas_hp_baixo = 0
        self.batalhas_concluidas_sem_desmaiar = 0
        self.chefes_fogo_apenas = 0

    def usar_pocao(self):
        if self.pocoes > 0:
            self.pocoes -= 1
            cura_base = int(self.hp_max * 0.35)
            bonus_regiao = self.regiao_atual * 10
            cura = cura_base + bonus_regiao

            if self.classe in ["Sumo Sacerdote", "Sacerdote Santo", "Avatar dos Serafins"]:
                cura = int(cura * 1.5)
            if self.classe == "Avatar da Grande Árvore-Mãe":
                cura = int(cura * 2.0)

            self.hp = min(self.hp_max, self.hp + cura)
            self.dano_curado_total += cura
            print(f"Você usou uma poção de HP e recuperou {cura} de HP!")
        else:
            print("Você não tem poções de HP!")

    def usar_pocao_mp(self):
        if self.pocoes_mp > 0:
            self.pocoes_mp -= 1
            recupera_mp = int(self.mp_max * 0.4) + (self.regiao_atual * 5)
            self.mp = min(self.mp_max, self.mp + recupera_mp)
            print(f"Você usou uma poção de MP e recuperou {recupera_mp} de MP!")
        else:
            print("Você não tem poções de MP!")

    def ganhar_xp(self, qtd_xp, qtd_ouro):
        regiao_info = regioes[self.regiao_atual]
        if self.classe == "Rei dos Ladris":
            qtd_ouro = int(qtd_ouro * 1.5)

        if self.nivel >= regiao_info["LevelCap"]:
            print(f"\n[AVISO] Você atingiu o Level Cap ({regiao_info['LevelCap']}) desta região! Ganho de XP bloqueado.")
            qtd_xp = 0
        
        self.xp += qtd_xp
        self.ouro += qtd_ouro
        print(f"\nVocê ganhou {qtd_xp} de XP e {qtd_ouro} de Ouro!")

        while qtd_xp > 0 and self.xp >= self.xp_necessario:
            self.nivel += 1
            self.xp -= self.xp_necessario
            self.xp_necessario = int(self.xp_necessario * 1.5)
            self.hp_max += 20
            self.hp = self.hp_max
            self.mp_max += 15
            self.mp = self.mp_max
            self.ataque_base += 3
            self.defesa_base += 2
            self.pontos_skill += 1
            print(f"\n*** SUBIU DE NÍVEL! Nível {self.nivel} alcançado! ***")

    def decretar_fim_encontro(self):
        for b in list(self.buffs_ativos.keys()):
            if self.buffs_ativos[b] > 0:
                self.buffs_ativos[b] -= 1

    def gerar_loot(self, is_boss, garantir_epico=False):
        print("\n--- DROP DE LOOT ---")
        regiao_id = self.regiao_atual
        mult_regiao = regioes[regiao_id]["MultiplicadorDificuldade"]

        if garantir_epico:
            raridades = ["Épico", "Lendário"]
            pesos = [70, 30]
        elif self.classe == "Rei dos Ladris":
            raridades = ["Raro", "Épico", "Lendário"]
            pesos = [10, 50, 40]
        else:
            raridades = ["Comum", "Raro", "Épico", "Lendário"]
            pesos = [55, 30, 12, 3] if not is_boss else [10, 30, 45, 15]

        raridade_escolhida = random.choices(raridades, weights=pesos, k=1)[0]
        tipo_item = random.choice(["Arma", "Armadura"])
        
        lista_efeitos_possiveis = [
            "Roubo de vida", "Aumento de taxa de crítico", "Aumento de dano crítico", 
            "Aumento de dano verdadeiro", "Chance de aplicar veneno por 2 rodadas", 
            "Chance de aplicar queimadura por 2 rodadas", "Chance de aplicar sangramento por 1 rodada", 
            "Chance de aplicar congelamento por 1 rodada", "Chance de contra-atacar o oponente", 
            "Aumentar a defesa contra queimadura", "Aumentar a defesa contra veneno", 
            "Aumentar a defesa contra sangramento", "Aumenta a defesa contra qualquer status anormal"
        ]

        efeitos_atribuidos = []
        if raridade_escolhida == "Raro" and random.random() < 0.35:
            efeitos_atribuidos.append(random.choice(lista_efeitos_possiveis))
        elif raridade_escolhida == "Épico":
            efeitos_atribuidos = random.sample(lista_efeitos_possiveis, k=random.randint(1, 2))
        elif raridade_escolhida == "Lendário":
            efeitos_atribuidos = random.sample(lista_efeitos_possiveis, k=random.randint(2, 5))

        nomes_armas = ["Espada", "Arco", "Cajado", "Adaga", "Machado"]
        nomes_armaduras = ["Armadura de Placas", "Manto Místico", "Túnica de Couro", "Cota de Malha"]

        if tipo_item == "Arma":
            nome_base = random.choice(nomes_armas)
            bonus_base = int((5 + (self.nivel * 2) * mult_regiao))
            if raridade_escolhida == "Raro": bonus_base = int(bonus_base * 1.3)
            elif raridade_escolhida == "Épico": bonus_base = int(bonus_base * 1.7)
            elif raridade_escolhida == "Lendário": bonus_base = int(bonus_base * 2.4)

            novo_item = {
                "Nome": f"{nome_base} da Região {regiao_id} ({raridade_escolhida})",
                "BonusAtaque": bonus_base,
                "Raridade": raridade_escolhida,
                "Efeitos": efeitos_atribuidos
            }
            print(f"🎁 Encontrou Arma: {novo_item['Nome']} (+{novo_item['BonusAtaque']} Atq)")
            if efeitos_atribuidos:
                print(f"   ✨ Efeitos Especiais: {', '.join(efeitos_atribuidos)}")
            
            if novo_item["BonusAtaque"] > self.arma["BonusAtaque"]:
                self.arma = novo_item
                print("✨ Nova arma equipada com sucesso!")
            else:
                print("Arma descartada por ser inferior.")
        else:
            nome_base = random.choice(nomes_armaduras)
            bonus_base = int((3 + (self.nivel * 1.5) * mult_regiao))
            if raridade_escolhida == "Raro": bonus_base = int(bonus_base * 1.3)
            elif raridade_escolhida == "Épico": bonus_base = int(bonus_base * 1.7)
            elif raridade_escolhida == "Lendário": bonus_base = int(bonus_base * 2.4)

            novo_item = {
                "Nome": f"{nome_base} da Região {regiao_id} ({raridade_escolhida})",
                "BonusDefesa": bonus_base,
                "Raridade": raridade_escolhida,
                "Efeitos": efeitos_atribuidos
            }
            print(f"🎁 Encontrou Armadura: {novo_item['Nome']} (+{novo_item['BonusDefesa']} Def)")
            if efeitos_atribuidos:
                print(f"   ✨ Efeitos Especiais: {', '.join(efeitos_atribuidos)}")

            if novo_item["BonusDefesa"] > self.armadura["BonusDefesa"]:
                self.armadura = novo_item
                print("✨ Nova armadura equipada com sucesso!")
            else:
                print("Armadura descartada por ser inferior.")

        if (is_boss or garantir_epico) and regiao_id >= 2:
            itens_possiveis = list(drop_fontes_itens.keys())
            item_raro_encontrado = random.choice(itens_possiveis)
            if item_raro_encontrado not in self.inventario_itens:
                self.inventario_itens.append(item_raro_encontrado)
                print(f"🌟 ITEM DE ROTA SECRETA ENCONTRADO: [{item_raro_encontrado}]!")