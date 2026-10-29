# database.py

ramo_por_classe = {
    "Guerreiro": "Guerreiro", "Cavaleiro Rúnico": "Guerreiro", "Berserker": "Guerreiro", "Guardião Vanguarda": "Guerreiro", "Espachim da Tempestade": "Guerreiro",
    "Mestre das Runas Primordiais": "Guerreiro", "Soberano da Fúria": "Guerreiro", "Fortalecedor Inquebrável": "Guerreiro", "Lorde das Vendavais": "Guerreiro",
    "Titã de Aço Negro": "Guerreiro", "Senhor das Eras Titanicus": "Guerreiro", "Mestre do Vento Ancestral": "Guerreiro",
    
    "Mago": "Mago", "Arquimago": "Mago", "Mago do Caos": "Mago", "Ilusionista Arcano": "Mago", "Criomante": "Mago",
    "Mestre dos Elementos": "Mago", "Imperador do Caos Absoluto": "Mago", "Tecelão de Realidades": "Mago", "Mestre do Zero Absoluto": "Mago",
    "Arcano do Cosmos": "Mago", "Fantasma do Abismo Estelar": "Mago", "Soberano do Inverno ETERNO": "Mago",

    "Ladino": "Ladino", "Assassino": "Ladino", "Mestre dos Gatunos": "Ladino", "Dançarino das Sombras": "Ladino", "Sabotador Engenheiro": "Ladino",
    "Sombra Mortal": "Ladino", "Rei dos Ladris": "Ladino", "Maestro Noturno": "Ladino", "Mestre dos Artifícios": "Ladino",
    "Espectro Fantasma": "Ladino", "Monarca do Vazio Obscuro": "Ladino", "Arquiteto da Aniquilação": "Ladino",

    "Clérigo": "Clérigo", "Paladino": "Clérigo", "Sumo Sacerdote": "Clérigo", "Inquisidor da Luz": "Clérigo", "Sacerdote das Marés": "Clérigo",
    "Guardião Celestial": "Clérigo", "Sacerdote Santo": "Clérigo", "Carrasco Santo": "Clérigo", "Guardião dos Mares": "Clérigo",
    "Avatar dos Serafins": "Clérigo", "Flagelo Divino dos Céus": "Clérigo", "Avatar de Leviatã": "Clérigo",

    "Patrulheiro": "Patrulheiro", "Atirador de Elite": "Patrulheiro", "Senhor das Feras": "Patrulheiro", "Mestre dos Venenos": "Patrulheiro", "Franco-Atirador Tático": "Patrulheiro",
    "Francatirador Lendário": "Patrulheiro", "Invocador Ancestral": "Patrulheiro", "Ceifador Venenoso": "Patrulheiro", "Sentinela de Alvo Fixo": "Patrulheiro",
    "Senhor do Horizonte Primordial": "Patrulheiro", "Flagelo da Hidra de Sangue": "Patrulheiro", "Olho do Destino Interdimensional": "Patrulheiro",

    "Bárbaro": "Bárbaro", "Devastador": "Bárbaro", "Senhor da Guerra": "Bárbaro", "Bárbaro Frenético": "Bárbaro", "Guardião Xamânico": "Bárbaro",
    "Titã Indomável": "Bárbaro", "Conquistador Supremo": "Bárbaro", "Destruidor Incontrolável": "Bárbaro", "Xamã das Tribos Primordiais": "Bárbaro",
    "Berserker do Cataclismo": "Bárbaro", "Soberano do Frenesi Sangrento": "Bárbaro", "Espiritualista do Caos Primal": "Bárbaro",

    "Piromântico": "Piromântico", "Piro-Mago": "Piromântico", "Invocador de Magma": "Piromântico", "Bruxo de Chamas Negras": "Piromântico", "Alquimista Volátil": "Piromântico",
    "Arcano do Inferno": "Piromântico", "Avatar do Vulcão": "Piromântico", "Senhor do Purgatório": "Piromântico", "Mestre das Explosões Alquímicas": "Piromântico",
    "Senhor das Cinzas Primordiais": "Piromântico", "Imperador do Inferno Abissal": "Piromântico", "Criador da Pedra Filosofal": "Piromântico",

    "Druida": "Druida", "Druida da Floresta": "Druida", "Metamorfo": "Druida", "Druida Tempestuoso": "Druida", "Guardião dos Seres Místicos": "Druida",
    "Guardião da Natureza": "Druida", "Behemoth Primal": "Druida", "Invocador de Tempestades": "Druida", "Mestre das Bestas Míticas": "Druida",
    "Avatar da Grande Árvore-Mãe": "Druida", "Senhor dos Elementos Primordiais": "Druida", "Rei de Yggdrasil": "Druida"
}

sk_tree_database = {
    "Guerreiro": {
        2: [
            {"Nome": "Glifo de Fortificação", "ClasseReq": "Cavaleiro Rúnico", "CustoOuro": 150, "CustoMP": 20, "Tipo": "BuffDef", "Elemento": "Neutro", "Valor": 12, "Multiplicador": 0, "Desc": "Ergue uma barreira de runas que concede +12 de Defesa por 3 turnos."},
            {"Nome": "Grito de Guerra Voraz", "ClasseReq": "Berserker", "CustoOuro": 150, "CustoMP": 18, "Tipo": "BuffAtqHpCost", "Elemento": "Fisico", "Valor": 0.40, "CustoHP": 5, "Multiplicador": 1.4, "Desc": "Aumenta o dano do próximo ataque em 40%, gastando 5 de HP."},
            {"Nome": "Postura Defensiva", "ClasseReq": "Guardião Vanguarda", "CustoOuro": 140, "CustoMP": 15, "Tipo": "ReducaoDano", "Elemento": "Neutro", "Valor": 0.35, "Multiplicador": 0, "Desc": "Reduz todo o dano recebido no próximo turno em 35%."},
            {"Nome": "Estocada Vendaval", "ClasseReq": "Espachim da Tempestade", "CustoOuro": 160, "CustoMP": 22, "Tipo": "DanoEspecial", "Elemento": "Ar", "Multiplicador": 2.20, "Desc": "Causa 220% de dano rápido com chance de crítica."}
        ],
        3: [
            {"Nome": "Runa do Julgamento", "ClasseReq": "Mestre das Runas Primordiais", "CustoOuro": 400, "CustoMP": 38, "Tipo": "DanoEspecial", "Elemento": "Neutro", "Multiplicador": 3.40, "Desc": "Expulsiona energia rúnica causando 340% de dano mágico/físico."},
            {"Nome": "Corte Frenético", "ClasseReq": "Soberano da Fúria", "CustoOuro": 420, "CustoMP": 35, "Tipo": "DanoPenetracao", "Elemento": "Fisico", "IgnoraArmor": 0.20, "Multiplicador": 3.60, "Desc": "Causa 360% de dano físico e ignora 20% da armadura do monstro."},
            {"Nome": "Carga do Bastião", "ClasseReq": "Fortalecedor Inquebrável", "CustoOuro": 380, "CustoMP": 30, "Tipo": "DanoBaseDef", "Elemento": "Fisico", "Multiplicador": 2.80, "Desc": "Causa 280% de dano calculados a partir da Defesa Total do herói."},
            {"Nome": "Dança dos Ventos", "ClasseReq": "Lorde das Vendavais", "CustoOuro": 450, "CustoMP": 40, "Tipo": "DanoEspecial", "Elemento": "Ar", "Multiplicador": 3.70, "Desc": "Desfere 3 golpes rápidos causando um total de 370% de dano."}
        ],
        4: [
            {"Nome": "Impacto de Adamantium", "ClasseReq": "Titã de Aço Negro", "CustoOuro": 1200, "CustoMP": 60, "Tipo": "DanoPuroPermDef", "Elemento": "Fisico", "ValorPermDef": 5, "Multiplicador": 4.80, "Desc": "Causa 480% de dano puro e aumenta permanentemente sua Defesa em +5."},
            {"Nome": "Ira dos Titãs Ancestrais", "ClasseReq": "Senhor das Eras Titanicus", "CustoOuro": 1350, "CustoMP": 65, "Tipo": "DanoReflexao", "Elemento": "Neutro", "ValorReflete": 0.50, "Multiplicador": 4.50, "Desc": "Causa 450% de dano e reflete 50% do dano recebido nos próximos 2 turnos."},
            {"Nome": "Furacão Devastador", "ClasseReq": "Mestre do Vento Ancestral", "CustoOuro": 1300, "CustoMP": 60, "Tipo": "DanoStun", "Elemento": "Ar", "Multiplicador": 4.90, "Desc": "Causa 490% de dano de ar, paralisando a ação do inimigo no próximo turno."}
        ]
    },
    "Mago": {
        2: [
            {"Nome": "Raio Arcano Concentrado", "ClasseReq": "Arquimago", "CustoOuro": 160, "CustoMP": 25, "Tipo": "DanoEspecial", "Elemento": "Arcano", "Multiplicador": 2.30, "Desc": "Causa 230% de dano mágico concentrado."},
            {"Nome": "Orbe da Instabilidade", "ClasseReq": "Mago do Caos", "CustoOuro": 150, "CustoMP": 20, "Tipo": "DanoCaotico", "Elemento": "Caos", "MultMin": 1.50, "MultMax": 3.20, "Desc": "Causa entre 150% e 320% de dano caótico aleatório."},
            {"Nome": "Dublê Espectral", "ClasseReq": "Ilusionista Arcano", "CustoOuro": 170, "CustoMP": 22, "Tipo": "ReducaoPrecisao", "Elemento": "Psiquico", "Multiplicador": 1.20, "Desc": "Cria uma miragem que reduz a precisão do ataque inimigo."},
            {"Nome": "Estalactite Profunda", "ClasseReq": "Criomante", "CustoOuro": 150, "CustoMP": 24, "Tipo": "DanoDebuffAtq", "Elemento": "Gelo", "Valor": 0.10, "Multiplicador": 2.10, "Desc": "Causa 210% de dano de gelo e reduz o ataque inimigo em 10%."}
        ],
        3: [
            {"Nome": "Explosão Elemental", "ClasseReq": "Mestre dos Elementos", "CustoOuro": 450, "CustoMP": 42, "Tipo": "DanoEspecial", "Elemento": "Elemental", "Multiplicador": 3.70, "Desc": "Causa 370% de dano combinando Fogo, Gelo e Raios."},
            {"Nome": "Singularidade Entrópica", "ClasseReq": "Imperador do Caos Absoluto", "CustoOuro": 480, "CustoMP": 45, "Tipo": "DanoDrainMP", "Elemento": "Caos", "Valor": 0.20, "Multiplicador": 3.90, "Desc": "Causa 390% de dano e converte 20% do dano causado em MP."},
            {"Nome": "Distorção Mental", "ClasseReq": "Tecelão de Realidades", "CustoOuro": 430, "CustoMP": 38, "Tipo": "DanoCura", "Elemento": "Psiquico", "ValorCura": 30, "Multiplicador": 3.40, "Desc": "Causa 340% de dano psíquico e cura 30 de HP."},
            {"Nome": "Zero Absoluto", "ClasseReq": "Mestre do Zero Absoluto", "CustoOuro": 460, "CustoMP": 40, "Tipo": "DanoEscudo", "Elemento": "Gelo", "ValorEscudo": 40, "Multiplicador": 3.60, "Desc": "Causa 360% de dano gelado e ergue uma barreira de gelo com 40 de HP."}
        ],
        4: [
            {"Nome": "Hipernova Universal", "ClasseReq": "Arcano do Cosmos", "CustoOuro": 1400, "CustoMP": 70, "Tipo": "DanoEspecial", "Elemento": "Cosmico", "Multiplicador": 5.20, "Desc": "Causa 520% de dano cósmico devastador."},
            {"Nome": "Aniquilação da Razão", "ClasseReq": "Fantasma do Abismo Estelar", "CustoOuro": 1350, "CustoMP": 65, "Tipo": "DanoPenetracao", "Elemento": "Abissal", "IgnoraArmor": 1.00, "Multiplicador": 5.00, "Desc": "Causa 500% de dano ignorando inteiramente a resistência mágica."},
            {"Nome": "Glaciação Apocalíptica", "ClasseReq": "Soberano do Inverno ETERNO", "CustoOuro": 1380, "CustoMP": 68, "Tipo": "DanoRestauraEscudo", "Elemento": "Gelo", "Multiplicador": 4.80, "Desc": "Causa 480% de dano de gelo supremo e restaura 100% do escudo de gelo."}
        ]
    },
    "Ladino": {
        2: [
            {"Nome": "Golpe na Artéria", "ClasseReq": "Assassino", "CustoOuro": 160, "CustoMP": 20, "Tipo": "DanoEspecial", "Elemento": "Fisico", "Multiplicador": 2.20, "Desc": "Causa 220% de dano físico e garante 30% de chance de acerto crítico."},
            {"Nome": "Bomba de Cobre", "ClasseReq": "Mestre dos Gatunos", "CustoOuro": 130, "CustoMP": 15, "Tipo": "DanoRouboOuro", "Elemento": "Mecanico", "Multiplicador": 1.80, "Desc": "Causa 180% de dano e rouba um bônus extra de ouro do alvo."},
            {"Nome": "Passo Elegante", "ClasseReq": "Dançarino das Sombras", "CustoOuro": 150, "CustoMP": 18, "Tipo": "DanoEsquiva", "Elemento": "Sombra", "Multiplicador": 2.00, "Desc": "Causa 200% de dano e aumenta a esquiva para o turno seguinte."},
            {"Nome": "Granada de Espinhos", "ClasseReq": "Sabotador Engenheiro", "CustoOuro": 140, "CustoMP": 22, "Tipo": "DanoEspecial", "Elemento": "Mecanico", "Multiplicador": 2.10, "Desc": "Causa 210% de dano mecânico imediato."}
        ],
        3: [
            {"Nome": "Lâmina do Vazio", "ClasseReq": "Sombra Mortal", "CustoOuro": 420, "CustoMP": 30, "Tipo": "DanoSombra", "Elemento": "Sombra", "Multiplicador": 3.50, "Desc": "Causa 350% de dano oculto com bônus crítico em alvos com vida cheia."},
            {"Nome": "Golpe da Ganância", "ClasseReq": "Rei dos Ladris", "CustoOuro": 400, "CustoMP": 28, "Tipo": "DanoRecuperaMP", "Elemento": "Fisico", "ValorMP": 20, "Multiplicador": 3.20, "Desc": "Causa 320% de dano e recupera 20 de MP ao acertar."},
            {"Nome": "Sinfonia Sombria", "ClasseReq": "Maestro Noturno", "CustoOuro": 440, "CustoMP": 32, "Tipo": "DanoEspecial", "Elemento": "Sombra", "Multiplicador": 3.60, "Desc": "Causa 360% de dano veloz e aplica um efeito de sangramento maciço."},
            {"Nome": "Mina de Napalm", "ClasseReq": "Mestre dos Artifícios", "CustoOuro": 410, "CustoMP": 35, "Tipo": "DanoEspecial", "Elemento": "Fogo", "Multiplicador": 3.40, "Desc": "Causa 340% de dano em área/explosivo."}
        ],
        4: [
            {"Nome": "Lâmina do Fim do Mundo", "ClasseReq": "Espectro Fantasma", "CustoOuro": 1300, "CustoMP": 55, "Tipo": "DanoEspecial", "Elemento": "Sombra", "Multiplicador": 4.70, "Desc": "Causa 470% de dano com multiplicador crítico dobrado."},
            {"Nome": "Sombra Devoradora de Almas", "ClasseReq": "Monarca do Vazio Obscuro", "CustoOuro": 1350, "CustoMP": 60, "Tipo": "DanoLifesteal", "Elemento": "Sombra", "ValorPct": 0.25, "Multiplicador": 4.90, "Desc": "Causa 490% de dano e recupera 25% do dano causado em HP."},
            {"Nome": "Bomba Núcleo-Sombria", "ClasseReq": "Arquiteto da Aniquilação", "CustoOuro": 1400, "CustoMP": 65, "Tipo": "DanoPuro", "Elemento": "Demolicao", "Multiplicador": 5.10, "Desc": "Causa 510% de dano de demolição puro."}
        ]
    },
    "Clérigo": {
        2: [
            {"Nome": "Golpe da Justiça Divina", "ClasseReq": "Paladino", "CustoOuro": 150, "CustoMP": 20, "Tipo": "DanoBuffDef", "Elemento": "Sagrado", "ValorDef": 5, "Multiplicador": 2.00, "Desc": "Causa 200% de dano sagrado e aumenta a defesa do herói em +5."},
            {"Nome": "Oração de Renovação", "ClasseReq": "Sumo Sacerdote", "CustoOuro": 160, "CustoMP": 25, "Tipo": "CuraHoT", "Elemento": "Sagrado", "ValorCura": 50, "HoT": 10, "HoTTurnos": 2, "Desc": "Cura 50 de HP instantaneamente e restaura +10 de HP nos próximos turnos."},
            {"Nome": "Reticência Purificadora", "ClasseReq": "Inquisidor da Luz", "CustoOuro": 150, "CustoMP": 22, "Tipo": "DanoEspecial", "Elemento": "Sagrado", "Multiplicador": 2.20, "Desc": "Causa 220% de dano sagrado em demônios/monstros corrompidos."},
            {"Nome": "Gota Vital", "ClasseReq": "Sacerdote das Marés", "CustoOuro": 140, "CustoMP": 18, "Tipo": "CuraHPMed", "Elemento": "Agua", "ValorCura": 40, "ValorMP": 15, "Desc": "Cura 40 de HP e restaura 15 de MP."}
        ],
        3: [
            {"Nome": "Bênção dos Céus", "ClasseReq": "Guardião Celestial", "CustoOuro": 420, "CustoMP": 32, "Tipo": "BuffDefReflect", "Elemento": "Sagrado", "ValorDef": 20, "ValorReflect": 0.25, "Desc": "Aumenta a Defesa em +20 e reflete 25% do dano direto recebido."},
            {"Nome": "Milagre da Cura Plena", "ClasseReq": "Sacerdote Santo", "CustoOuro": 450, "CustoMP": 40, "Tipo": "CuraPlena", "Elemento": "Sagrado", "ValorCura": 160, "Desc": "Restaura 160 de HP e remove todos os efeitos negativos."},
            {"Nome": "Martelo da Punição", "ClasseReq": "Carrasco Santo", "CustoOuro": 430, "CustoMP": 35, "Tipo": "DanoPenetracao", "Elemento": "Sagrado", "IgnoraArmor": 1.00, "Multiplicador": 3.60, "Desc": "Causa 360% de dano sagrado ignorando defesas mágicas."},
            {"Nome": "Cascata da Restauração", "ClasseReq": "Guardião dos Mares", "CustoOuro": 410, "CustoMP": 30, "Tipo": "CuraImunidade", "Elemento": "Agua", "ValorCura": 110, "Desc": "Cura 110 de HP e concede imunidade no turno."}
        ],
        4: [
            {"Nome": "Ira dos Seis Asas", "ClasseReq": "Avatar dos Serafins", "CustoOuro": 1350, "CustoMP": 65, "Tipo": "DanoEspecialCura", "Elemento": "Sagrado", "ValorCura": 100, "Multiplicador": 4.80, "Desc": "Causa 480% de dano sagrado supremo e cura 100 de HP simultaneamente."},
            {"Nome": "Julgamento do Arcanjo", "ClasseReq": "Flagelo Divino dos Céus", "CustoOuro": 1380, "CustoMP": 68, "Tipo": "DanoPuro", "Elemento": "Luz", "Multiplicador": 5.00, "Desc": "Causa 500% de dano de luz puro."},
            {"Nome": "Dilúvio Purificador Primordial", "ClasseReq": "Avatar de Leviatã", "CustoOuro": 1320, "CustoMP": 60, "Tipo": "DanoRestauraFull", "Elemento": "Agua", "Multiplicador": 4.60, "Desc": "Causa 460% de dano e restaura 100% de HP e MP."}
        ]
    },
    "Patrulheiro": {
        2: [
            {"Nome": "Tiro no Coração", "ClasseReq": "Atirador de Elite", "CustoOuro": 150, "CustoMP": 18, "Tipo": "DanoEspecial", "Elemento": "Fisico", "Multiplicador": 2.10, "Desc": "Causa 210% de dano com chance aumentada de crítico."},
            {"Nome": "Ataque de Águia", "ClasseReq": "Senhor das Feras", "CustoOuro": 140, "CustoMP": 16, "Tipo": "DanoEspecial", "Elemento": "Natureza", "Multiplicador": 1.80, "Desc": "O espírito da ave ataca o alvo causando 180% de dano direto."},
            {"Nome": "Flecha Peçonhenta", "ClasseReq": "Mestre dos Venenos", "CustoOuro": 150, "CustoMP": 20, "Tipo": "DanoPoison", "Elemento": "Veneno", "Multiplicador": 1.70, "Desc": "Causa 170% de dano e envenena o monstro por 2 turnos."},
            {"Nome": "Disparo da Distância", "ClasseReq": "Franco-Atirador Tático", "CustoOuro": 160, "CustoMP": 22, "Tipo": "DanoPenetracao", "Elemento": "Fisico", "IgnoraArmor": 0.50, "Multiplicador": 2.20, "Desc": "Causa 220% de dano ignorando a armadura básica."}
        ],
        3: [
            {"Nome": "Disparo de Perfurante", "ClasseReq": "Francatirador Lendário", "CustoOuro": 430, "CustoMP": 32, "Tipo": "DanoPenetracao", "Elemento": "Fisico", "IgnoraArmor": 0.80, "Multiplicador": 3.80, "Desc": "Causa 380% de dano direto perfurando armaduras."},
            {"Nome": "Invocação do Urso Espectral", "ClasseReq": "Invocador Ancestral", "CustoOuro": 410, "CustoMP": 35, "Tipo": "DanoBuffDef", "Elemento": "Natureza", "ValorDef": 15, "Multiplicador": 3.40, "Desc": "Causa 340% de dano e concede um escudo temporário de +15 Defesa."},
            {"Nome": "Injeção de Neurotoxina", "ClasseReq": "Ceifador Venenoso", "CustoOuro": 420, "CustoMP": 30, "Tipo": "DanoPoisonMassivo", "Elemento": "Veneno", "Multiplicador": 3.30, "Desc": "Causa 330% de dano e envenena intensamente o alvo."},
            {"Nome": "Tiro de Precisão Absoluta", "ClasseReq": "Sentinela de Alvo Fixo", "CustoOuro": 440, "CustoMP": 34, "Tipo": "DanoInfallible", "Elemento": "Fisico", "Multiplicador": 3.70, "Desc": "Causa 370% de dano garantido sem chance de erro ou esquiva."}
        ],
        4: [
            {"Nome": "Saraivada Cósmica", "ClasseReq": "Senhor do Horizonte Primordial", "CustoOuro": 1300, "CustoMP": 60, "Tipo": "DanoEspecial", "Elemento": "Cosmico", "Multiplicador": 4.90, "Desc": "Dispara 5 flechas estelares causando 490% de dano total."},
            {"Nome": "Toxina de Ouroboros", "ClasseReq": "Flagelo da Hidra de Sangue", "CustoOuro": 1350, "CustoMP": 62, "Tipo": "DanoPoisonIrreversivel", "Elemento": "Veneno", "Multiplicador": 4.80, "Desc": "Causa 480% de dano com envenenamento irreversível."},
            {"Nome": "Sniper Dimensional", "ClasseReq": "Olho do Destino Interdimensional", "CustoOuro": 1400, "CustoMP": 65, "Tipo": "DanoPenetracao", "Elemento": "Dimensional", "IgnoraArmor": 1.00, "Multiplicador": 5.20, "Desc": "Causa 520% de dano ignorando 100% da armadura do inimigo."}
        ]
    },
    "Bárbaro": {
        2: [
            {"Nome": "Pisotear Sísmico", "ClasseReq": "Devastador", "CustoOuro": 140, "CustoMP": 15, "Tipo": "DanoDebuffAtq", "Elemento": "Terra", "Valor": 0.10, "Multiplicador": 1.90, "Desc": "Causa 190% de dano e reduz o ataque do monstro."},
            {"Nome": "Grito de Comando", "ClasseReq": "Senhor da Guerra", "CustoOuro": 150, "CustoMP": 18, "Tipo": "BuffAtqBase", "Elemento": "Fisico", "ValorAtq": 5, "Desc": "Aumenta seu próprio Ataque Base em +5 durante o combate."},
            {"Nome": "Golpe Duplo Selvagem", "ClasseReq": "Bárbaro Frenético", "CustoOuro": 160, "CustoMP": 20, "Tipo": "DanoEspecial", "Elemento": "Fisico", "Multiplicador": 2.20, "Desc": "Causa 220% de dano distribuído em dois acertos rápidos."},
            {"Nome": "Totem da Rocha", "ClasseReq": "Guardião Xamânico", "CustoOuro": 140, "CustoMP": 16, "Tipo": "BuffDefCura", "Elemento": "Terra", "ValorDef": 8, "ValorCura": 10, "Desc": "Concede um bônus de +8 de Defesa e regenera 10 de HP."}
        ],
        3: [
            {"Nome": "Pancada do Colosso", "ClasseReq": "Titã Indomável", "CustoOuro": 420, "CustoMP": 32, "Tipo": "DanoEspecial", "Elemento": "Fisico", "Multiplicador": 3.60, "Desc": "Causa 360% de dano bruto."},
            {"Nome": "Esmagar Crânio", "ClasseReq": "Conquistador Supremo", "CustoOuro": 440, "CustoMP": 35, "Tipo": "DanoDebuffDef", "Elemento": "Fisico", "ValorDef": 15, "Multiplicador": 3.70, "Desc": "Causa 370% de dano e reduz a Defesa do alvo em 15 pontos."},
            {"Nome": "Frenesi Sanguinário", "ClasseReq": "Destruidor Incontrolável", "CustoOuro": 430, "CustoMP": 28, "Tipo": "DanoLifesteal", "Elemento": "Fisico", "ValorPct": 0.20, "Multiplicador": 3.50, "Desc": "Causa 350% de dano e cura o jogador em 20% do dano causado."},
            {"Nome": "Benção do Vigor Ancestral", "ClasseReq": "Xamã das Tribos Primordiais", "CustoOuro": 400, "CustoMP": 30, "Tipo": "CuraHPMP", "Elemento": "Espiritual", "ValorCura": 80, "ValorMP": 30, "Desc": "Cura 80 de HP e restaura 30 de MP."}
        ],
        4: [
            {"Nome": "Golpe da Fúria Apocalíptica", "ClasseReq": "Berserker do Cataclismo", "CustoOuro": 1350, "CustoMP": 55, "Tipo": "DanoEspecial", "Elemento": "Fisico", "Multiplicador": 5.00, "Desc": "Causa 500% de dano crítico."},
            {"Nome": "Carnificina Imparável", "ClasseReq": "Soberano do Frenesi Sangrento", "CustoOuro": 1380, "CustoMP": 58, "Tipo": "DanoImunidadeMorte", "Elemento": "Fisico", "Multiplicador": 5.10, "Desc": "Causa 510% de dano e concede imunidade a derrotas no mesmo turno."},
            {"Nome": "Convocação dos Deuses Totêmicos", "ClasseReq": "Espiritualista do Caos Primal", "CustoOuro": 1300, "CustoMP": 60, "Tipo": "DanoElementalEscudo", "Elemento": "Elemental", "ValorEscudo": 50, "Multiplicador": 4.70, "Desc": "Causa 470% de dano elemental variado e ergue barreira defensiva de 50 de escudo."}
        ]
    },
    "Piromântico": {
        2: [
            {"Nome": "Chama Concentrada", "ClasseReq": "Piro-Mago", "CustoOuro": 150, "CustoMP": 22, "Tipo": "DanoEspecial", "Elemento": "Fogo", "Multiplicador": 2.20, "Desc": "Causa 220% de dano de fogo puro."},
            {"Nome": "Pássaro de Fogo", "ClasseReq": "Invocador de Magma", "CustoOuro": 160, "CustoMP": 25, "Tipo": "DanoBurn", "Elemento": "Fogo", "Multiplicador": 2.10, "Desc": "Invoca uma fênix de magma causando 210% de dano e aplicando queimadura."},
            {"Nome": "Chama Macabra", "ClasseReq": "Bruxo de Chamas Negras", "CustoOuro": 170, "CustoMP": 24, "Tipo": "DanoPenetracao", "Elemento": "FogoSombrio", "IgnoraArmor": 0.50, "Multiplicador": 2.30, "Desc": "Causa 230% de dano de fogo sombrio ignorando escudos."},
            {"Nome": "Bomba de Pólvora", "ClasseReq": "Alquimista Volátil", "CustoOuro": 140, "CustoMP": 18, "Tipo": "DanoEspecial", "Elemento": "Fogo", "Multiplicador": 2.00, "Desc": "Causa 200% de dano de fogo instantâneo."}
        ],
        3: [
            {"Nome": "Pilar de Fogo Purgatorial", "ClasseReq": "Arcano do Inferno", "CustoOuro": 460, "CustoMP": 42, "Tipo": "DanoEspecial", "Elemento": "Fogo", "Multiplicador": 3.90, "Desc": "Causa 390% de dano extremo de fogo."},
            {"Nome": "Erupção Terrestre", "ClasseReq": "Avatar do Vulcão", "CustoOuro": 440, "CustoMP": 38, "Tipo": "DanoBuffDef", "Elemento": "Fogo", "ValorDef": 15, "Multiplicador": 3.70, "Desc": "Causa 370% de dano e cria uma armadura escaldante de +15 Defesa."},
            {"Nome": "Chamas Negras do Aniquilamento", "ClasseReq": "Senhor do Purgatório", "CustoOuro": 470, "CustoMP": 40, "Tipo": "DanoEspecial", "Elemento": "FogoSombrio", "Multiplicador": 3.80, "Desc": "Causa 380% de dano de fogo profano."},
            {"Nome": "Cocktail do Apocalipse", "ClasseReq": "Mestre das Explosões Alquímicas", "CustoOuro": 420, "CustoMP": 32, "Tipo": "DanoRecuperaMP", "Elemento": "Fogo", "ValorMP": 20, "Multiplicador": 3.50, "Desc": "Causa 350% de dano e restaura 20 de MP ao explodir."}
        ],
        4: [
            {"Nome": "Incineração Total do Existir", "ClasseReq": "Senhor das Cinzas Primordiais", "CustoOuro": 1400, "CustoMP": 68, "Tipo": "DanoEspecial", "Elemento": "Fogo", "Multiplicador": 5.30, "Desc": "Causa 530% de dano de cinzas primordiais."},
            {"Nome": "Chamas do Vazio Devorador", "ClasseReq": "Imperador do Inferno Abissal", "CustoOuro": 1450, "CustoMP": 70, "Tipo": "DanoDrainMPFull", "Elemento": "FogoSombrio", "ValorMP": 50, "Multiplicador": 5.40, "Desc": "Causa 540% de dano e drena 50 de MP do monstro/restaura o seu."},
            {"Nome": "Transmutação Ígnea Suprema", "ClasseReq": "Criador da Pedra Filosofal", "CustoOuro": 1350, "CustoMP": 55, "Tipo": "DanoEspecial", "Elemento": "Alquimia", "Multiplicador": 4.90, "Desc": "Causa 490% de dano e multiplica seus frascos de poção."}
        ]
    },
    "Druida": {
        2: [
            {"Nome": "Espinhos de Madeira-Ferro", "ClasseReq": "Druida da Floresta", "CustoOuro": 140, "CustoMP": 18, "Tipo": "DanoReflect", "Elemento": "Natureza", "ValorReflect": 5, "Multiplicador": 1.90, "Desc": "Causa 190% de dano e devolve 5 de dano físico a quem atacar."},
            {"Nome": "Pancada de Urso", "ClasseReq": "Metamorfo", "CustoOuro": 150, "CustoMP": 20, "Tipo": "DanoEspecial", "Elemento": "Fisico", "Multiplicador": 2.10, "Desc": "Causa 210% de dano físico bruto na forma bestial."},
            {"Nome": "Brisa Cortante", "ClasseReq": "Druida Tempestuoso", "CustoOuro": 150, "CustoMP": 22, "Tipo": "DanoEsquiva", "Elemento": "Ar", "Multiplicador": 2.00, "Desc": "Causa 200% de dano de vento e concede esquiva."},
            {"Nome": "Espírito Curativo", "ClasseReq": "Guardião dos Seres Místicos", "CustoOuro": 160, "CustoMP": 24, "Tipo": "Cura", "Elemento": "Natureza", "Valor": 45, "Desc": "Invoca uma fada que cura 45 de HP."}
        ],
        3: [
            {"Nome": "Abraço de Gaia", "ClasseReq": "Guardião da Natureza", "CustoOuro": 420, "CustoMP": 32, "Tipo": "CuraBuffDef", "Elemento": "Natureza", "ValorCura": 120, "ValorDef": 10, "Desc": "Restaura 120 de HP e aumenta a Defesa em +10 por 2 turnos."},
            {"Nome": "Carga do Behemoth", "ClasseReq": "Behemoth Primal", "CustoOuro": 430, "CustoMP": 35, "Tipo": "DanoEspecial", "Elemento": "Fisico", "Multiplicador": 3.70, "Desc": "Causa 370% de dano físico colossal."},
            {"Nome": "Furacão Elétrico", "ClasseReq": "Invocador de Tempestades", "CustoOuro": 440, "CustoMP": 38, "Tipo": "DanoEspecial", "Elemento": "Raio", "Multiplicador": 3.60, "Desc": "Causa 360% de dano de natureza e raio."},
            {"Nome": "Investida da Fera Mítica", "ClasseReq": "Mestre das Bestas Míticas", "CustoOuro": 450, "CustoMP": 40, "Tipo": "DanoEspecial", "Elemento": "Natureza", "Multiplicador": 3.80, "Desc": "Invoca uma fera arcana que desfere 380% de dano."}
        ],
        4: [
            {"Nome": "Bênção de Yggdrasil Prima", "ClasseReq": "Avatar da Grande Árvore-Mãe", "CustoOuro": 1350, "CustoMP": 62, "Tipo": "DanoEspecialCura", "Elemento": "Natureza", "ValorCura": 150, "Multiplicador": 4.80, "Desc": "Causa 480% de dano e restaura 150 de HP instantaneamente."},
            {"Nome": "Vento Divino da Criação", "ClasseReq": "Senhor dos Elementos Primordiais", "CustoOuro": 1380, "CustoMP": 65, "Tipo": "DanoEspecial", "Elemento": "Elemental", "Multiplicador": 5.10, "Desc": "Causa 510% de dano de tempestade primordial."},
            {"Nome": "Lança das Raízes do Mundo", "ClasseReq": "Rei de Yggdrasil", "CustoOuro": 1400, "CustoMP": 64, "Tipo": "DanoRestauraMPFull", "Elemento": "Natureza", "Multiplicador": 5.00, "Desc": "Causa 500% de dano silvestre absoluto e regenera todo o MP."}
        ]
    }
}

passivas_info = {
    "Cavaleiro Rúnico": "Carcaça de Runas: Concede absorção de escudo mágico baseada na Defesa Base no início do combate.",
    "Berserker": "Fúria Sanguinária: Aumenta o dano causado conforme a batalha avança.",
    "Guardião Vanguarda": "Provocação Inabalável: Reduz o dano recebido em 15% quando o HP estiver acima de 70%.",
    "Espachim da Tempestade": "Passo Veloz: Tem 15% de chance de realizar um contra-ataque imediato ao ser atingido.",
    "Mestre das Runas Primordiais": "Eco Rúnico: Chance de duplicar os buffs de defesa obtidos durante o combate.",
    "Soberano da Fúria": "Êxtase Destrutivo: Recebe dano fixo por turno para manter a fúria no máximo.",
    "Fortalecedor Inquebrável": "Muralha Viva: Converte 25% da Defesa Total em dano para os seus ataques normais.",
    "Lorde das Vendavais": "Lâmina Célere: Aumenta a velocidade de ataque, garantindo um segundo golpe leve no 3º turno.",
    "Titã de Aço Negro": "Corpo de Adamantium: Reduz todo o dano recebido permanentemente em 25%.",
    "Senhor das Eras Titanicus": "Reflexo Divino: Devolve 30% de todo o dano físico ou mágico sofrido de volta ao inimigo.",
    "Mestre do Vento Ancestral": "Esquiva Tempestuosa: Concede 25% de chance de esquiva completa de ataques físicos normais.",
    "Arquimago": "Concentração Arcana: A cada 3 turnos, o próximo ataque mágico causa dano crítico garantido.",
    "Mago do Caos": "Instabilidade Arcana: Cada feitiço lançado tem chance aleatória de custar 50% menos MP.",
    "Ilusionista Arcano": "Espelho de Magia: Cria uma cópia no início do combate que absorve o primeiro ataque do inimigo.",
    "Criomante": "Toque Congelante: Reduz o ataque dos inimigos em 10% através da sensação de frio extremo.",
    "Mestre dos Elementos": "Fluxo Elemental: Acumula cargas a cada turno que explodem em dano massivo no 4º turno.",
    "Imperador do Caos Absoluto": "Entropia Ativa: Converte falhas de crítico em dano puro.",
    "Tecelão de Realidades": "Inversão Mental: Seus feitiços têm 25% de chance de atordoar ou reduzir o Ataque do inimigo em 20%.",
    "Mestre do Zero Absoluto": "Armadura de Gelo: Concede regeneração periódica de escudo rígido de gelo igual a 10% do HP Máximo.",
    "Arcano do Cosmos": "Compreensão Universal: Reduz o custo de MP de todas as habilidades em 40%.",
    "Fantasma do Abismo Estelar": "Distorção Cósmica: Faz com que 1 a cada 4 ataques do inimigo erre completamente.",
    "Soberano do Inverno ETERNO": "Era Glacial: Congela o oponente a cada 4 turnos, fazendo-o perder o turno de ação.",
    "Assassino": "Instinto Oculto: Chance aumentada de críticos letais em alvos com mais de 50% de HP.",
    "Mestre dos Gatunos": "Mãos Leves: Rouba ouro do inimigo a cada ataque bem-sucedido.",
    "Dançarino das Sombras": "Movimento Fluido: Aumenta em 15% a chance de acerto crítico e esquiva em turnos ímpares.",
    "Sabotador Engenheiro": "Carga Explosiva: Seus ataques normais aplicam uma marca que explode no turno seguinte causando dano extra.",
    "Sombra Mortal": "Passos do Além: Chance de se tornar intangível ao atacar, reduzindo o dano recebido em 50%.",
    "Rei dos Ladris": "Fortuna do Submundo: Aumenta o ouro recebido e a chance de loots raros.",
    "Maestro Noturno": "Passos Fantasma: Quando acerta um crítico, recupera 10% do MP máximo instantaneamente.",
    "Mestre dos Artifícios": "Bomba de Fumaça: Reduz o ataque dos monstros em 15% devido à cegueira tática.",
    "Espectro Fantasma": "Passos na Eternidade: O primeiro ataque de cada combate causa sempre dano crítico de 300%.",
    "Monarca do Vazio Obscuro": "Véu das Sombras Eternas: Torna o jogador imune a efeitos negativos e aumenta os danos críticos em +50%.",
    "Arquiteto da Aniquilação": "Reação em Cadeia: Todas as suas habilidades causam dano em área (ou dano duplo fixo no alvo principal).",
    "Paladino": "Baluarte de Fé: Parte da Defesa total é somada ao poder de ataque físico.",
    "Sumo Sacerdote": "Graça Divina: Aumenta a eficácia de poções e curas em 50%.",
    "Inquisidor da Luz": "Fervor Sagrado: Converte 20% do MP gasto em dano adicional nos seus ataques.",
    "Sacerdote das Marés": "Aura Purificadora: Recupera 3 de MP a cada turno de forma passiva.",
    "Guardião Celestial": "Muralha dos Céus: Reflete porcentagem de dano recebido de volta ao agressor.",
    "Sacerdote Santo": "Ressurgimento Sagrado: Revive automaticamente uma vez por luta com 30% de HP se o HP zerar.",
    "Carrasco Santo": "Julgamento Divino: Causa 25% de dano extra contra monstros do tipo Esqueleto, Demônio ou Caído.",
    "Guardião dos Mares": "Bênção Oceânica: Aumenta a defesa e a vida máxima de forma dinâmica durante o combate.",
    "Avatar dos Serafins": "Aura Imorredoura: Regenera 15% do HP máximo no início de cada turno.",
    "Flagelo Divino dos Céus": "Justiça Implacável: Seus ataques ignoram 40% da defesa e da resistência mágica dos inimigos.",
    "Avatar de Leviatã": "Fluxo Infinito: Restaura 10% de HP e MP no final de cada turno.",
    "Atirador de Elite": "Mira Milimétrica: Bônus acumulativo de ataque a cada turno consecutivo usando ataques normais.",
    "Senhor das Feras": "Instinto da Matilha: Um espírito de fera ataca passivamente a cada turno.",
    "Mestre dos Venenos": "Toxina Aguda: Seus ataques causam dano de veneno contínuo equivalente a 5% do HP do alvo por 2 turnos.",
    "Franco-Atirador Tático": "Posicionamento Tático: Concede +10% de taxa de crítico em combates de longa distância/primeiro turno.",
    "Francatirador Lendário": "Tiro Perfurante: Ataques e habilidades ignoram grande parte da defesa inimiga.",
    "Invocador Ancestral": "Comando Selvagem: A fera invocada aplica sangramento contínuo.",
    "Ceifador Venenoso": "Veno-Erosão: O veneno reduz a defesa do inimigo progressivamente.",
    "Sentinela de Alvo Fixo": "Foco Absoluto: A cada turno sem sofrer dano, aumenta seu dano em +10%.",
    "Senhor do Horizonte Primordial": "Olho da Fera Mítica: Ataques ignoram totalmente a armadura de monstros comuns e reduzem em 50% a de chefões.",
    "Flagelo da Hidra de Sangue": "Névoa Tóxica Pura: O inimigo perde 10% do seu HP atual a cada turno por envenenamento incurável.",
    "Olho do Destino Interdimensional": "Visão do Vazio: Seus ataques nunca erram e sempre ignoram 50% de todas as defesas inimigas.",
    "Devastador": "Pele de Rocha: Reduz o dano físico recebido de monstros comuns.",
    "Senhor da Guerra": "Presença Dominante: Reduz o ataque dos inimigos no início do combate.",
    "Bárbaro Frenético": "Ataque Frenético: Aumenta a velocidade e dá 10% de chance de atacar duas vezes seguidas.",
    "Guardião Xamânico": "Espírito Ancestral: Reduz em 10% o dano mágico recebido através de totens de proteção.",
    "Titã Indomável": "Vigor Titânico: Maior regeneração natural por turno quanto menor for o HP atual.",
    "Conquistador Supremo": "Ira Incontrolável: Transforma dano sofrido em poder ofensivo para os próximos golpes.",
    "Destruidor Incontrolável": "Sede de Sangue: Recupera 15% do dano causado como vida a cada ataque normal.",
    "Xamã das Tribos Primordiais": "Totem de Vitalidade: Regenera 5% de HP e MP a cada 2 turnos em batalha.",
    "Berserker do Cataclismo": "Sangue de Fúria Eterna: Quanto menor o HP atual, maior o multiplicador de crítico.",
    "Soberano do Frenesi Sangrento": "Imortalidade Frenética: Se o HP chegar a zero, continua lutando por 2 turnos inteiros antes de desmaiar.",
    "Espiritualista do Caos Primal": "Escudo dos Ancestrais: Absorve 20% de todo dano recebido e converte em MP.",
    "Piro-Mago": "Chamas Intensas: Aumenta significativamente o dano de fogo.",
    "Invocador de Magma": "Corpo Vulcânico: Dano de fogo reduzido e contra-ataque escaldante.",
    "Bruxo de Chamas Negras": "Fogo Maldito: O dano de fogo ignora barreiras de defesa e escudos normais.",
    "Alquimista Volátil": "Mistura Explosiva: Usar poções concede um bônus temporário de +15% no Ataque durante 2 turnos.",
    "Arcano do Inferno": "Inferno Devastador: Queima o inimigo continuamente.",
    "Avatar do Vulcão": "Erupção Passiva: Chance de explodir em chamas ao receber dano.",
    "Senhor do Purgatório": "Chamas Eternas: Inimigos queimados não conseguem recuperar vida ou receber cura de habilidades.",
    "Mestre das Explosões Alquímicas": "Reação em Cadeia: Suas poções de cura também causam dano ao inimigo e suas poções de MP curam vida.",
    "Senhor das Cinzas Primordiais": "Fogo Fátuo: Inimigos que atacam o jogador sofrem dano de queimadura contínuo.",
    "Imperador do Inferno Abissal": "Consumação das Almas: Cada inimigo queimado restaura 20% do MP Máximo do jogador.",
    "Criador da Pedra Filosofal": "Transmutação Perfeita: Torna os efeitos de todas as poções 200% mais eficientes.",
    "Druida da Floresta": "Espírito da Natureza: Regenera HP e MP gradualmente.",
    "Metamorfo": "Forma Bestial: Aumenta vida e defesa base em combate.",
    "Druida Tempestuoso": "Vento Espiritual: Concede 10% de esquiva extra e aumenta a eficácia de magias de vento/raio.",
    "Guardião dos Seres Místicos": "Invocação de Espíritos: Invoca um pequeno espírito da floresta que absorve 10% do dano recebido.",
    "Guardião da Natureza": "Escudo de Espinhos: Devolve dano físico aos atacantes.",
    "Behemoth Primal": "Pisotear Pesado: Golpes têm chance de atordoar o inimigo.",
    "Invocador de Tempestades": "Cólera dos Céus: A cada 3 turnos, um raio atinge o inimigo causando dano de natureza extra.",
    "Mestre das Bestas Míticas": "Companheiro Mágico: O espírito da floresta evolui para uma dríade que cura o jogador a cada 2 turnos.",
    "Avatar da Grande Árvore-Mãe": "Raízes de Gaia: Aumenta a cura recebida de todas as fontes em 100%.",
    "Senhor dos Elementos Primordiais": "Dominium Elemental: Reduz o dano elemental recebido em 50% e aumenta o dano de raio/vento em 40%.",
    "Rei de Yggdrasil": "Santuário Místico: Dá imunidade total a venenos, atordoamentos e regenera 10% do HP a cada turno."
}

# REGIOES COM MONSTROS ESTRUTURADOS COMO DICIONÁRIOS (Requisito 4)
regioes = {
    1: {
        "Nome": "Floresta Sombria",
        "LevelCap": 5,
        "MultiplicadorDificuldade": 1.0,
        "Monstros": [
            {"Nome": "Goblin", "Tipo": "Humanoide"},
            {"Nome": "Esqueleto", "Tipo": "Esqueleto"},
            {"Nome": "Lobo Selvagem", "Tipo": "Fera"},
            {"Nome": "Orc", "Tipo": "Humanoide"}
        ],
        "Boss": {"Nome": "Rei Goblin Corrompido", "Tipo": "Demonio"},
        "Descricao": "Uma floresta densa e perigosa envolta em neblina espessa.",
        "ModificadorAmbiental": "Neblina Densa: Chance de ataques normais errarem o alvo ligeiramente.",
        "FraquezaElemental": "Fogo",
        "ResistenciaElemental": "Natureza",
        "DropsPrincipais": ["Arma/Armadura Comum ou Rara", "Espada do Rei Caído (Boss/Rota Secreta)"]
    },
    2: {
        "Nome": "Caverna Vulcânica",
        "LevelCap": 12,
        "MultiplicadorDificuldade": 1.8,
        "Monstros": [
            {"Nome": "Salamandra de Fogo", "Tipo": "Elemental"},
            {"Nome": "Golem de Magma", "Tipo": "Construto"},
            {"Nome": "Orc do Inferno", "Tipo": "Caido"},
            {"Nome": "Morcego de Chamas", "Tipo": "Fera"}
        ],
        "Boss": {"Nome": "Senhor do Magma", "Tipo": "Elemental"},
        "Descricao": "Túneis subterrâneos escaldantes onde rios de lava fluem constantemente.",
        "ModificadorAmbiental": "Calor Extremo: Dano contínuo de fogo leve em combates muito longos.",
        "FraquezaElemental": "Gelo",
        "ResistenciaElemental": "Fogo",
        "DropsPrincipais": ["Arma/Armadura Rara ou Épica", "Machado de Guerra de Magma Pura", "Brasa do Coração do Mundo"]
    },
    3: {
        "Nome": "Ruínas Ancestrais",
        "LevelCap": 20,
        "MultiplicadorDificuldade": 2.6,
        "Monstros": [
            {"Nome": "Cavaleiro Espectral", "Tipo": "Esqueleto"},
            {"Nome": "Gárgula de Pedra", "Tipo": "Construto"},
            {"Nome": "Múmia Antiga", "Tipo": "Esqueleto"},
            {"Nome": "Sombra Errante", "Tipo": "Caido"}
        ],
        "Boss": {"Nome": "Faraó Caído", "Tipo": "Caido"},
        "Descricao": "Restos esquecidos de uma civilização antiga assombrada por maldições.",
        "ModificadorAmbiental": "Aura de Maldição: Custo de MP levemente aumentado ao castar habilidades.",
        "FraquezaElemental": "Sagrado",
        "ResistenciaElemental": "Sombra",
        "DropsPrincipais": ["Arma/Armadura Épica", "Adaga da Lua Sangrenta", "Escudo da Origem", "Cálice da Luz Eterna"]
    },
    4: {
        "Nome": "Cidadela Celestial",
        "LevelCap": 30,
        "MultiplicadorDificuldade": 3.5,
        "Monstros": [
            {"Nome": "Anjo Caído", "Tipo": "Caido"},
            {"Nome": "Sentinela Dourada", "Tipo": "Construto"},
            {"Nome": "Quimera Astral", "Tipo": "Fera"},
            {"Nome": "Valquíria Corrompida", "Tipo": "Demonio"}
        ],
        "Boss": {"Nome": "DRAGÃO ANCESTRAL SUPREMO", "Tipo": "Dragao"},
        "Descricao": "Fortaleza mítica nos céus, o lar de entidades divinas corrompidas.",
        "ModificadorAmbiental": "Gravidade Mística: Aumenta a eficácia de acertos críticos para ambos os lados.",
        "FraquezaElemental": "Dimensional",
        "ResistenciaElemental": "Cosmico",
        "DropsPrincipais": ["Arma/Armadura Lendária", "Arco de Ossos de Dragão", "Orbe do Vazio Estelar", "Itens Divinos de Tier 4"]
    }
}

tier3_evolucoes = {
    "Cavaleiro Rúnico": {"Nome": "Mestre das Runas Primordiais"},
    "Berserker": {"Nome": "Soberano da Fúria"},
    "Guardião Vanguarda": {"Nome": "Fortalecedor Inquebrável"},
    "Espachim da Tempestade": {"Nome": "Lorde das Vendavais"},
    "Arquimago": {"Nome": "Mestre dos Elementos"},
    "Mago do Caos": {"Nome": "Imperador do Caos Absoluto"},
    "Ilusionista Arcano": {"Nome": "Tecelão de Realidades"},
    "Criomante": {"Nome": "Mestre do Zero Absoluto"},
    "Assassino": {"Nome": "Sombra Mortal"},
    "Mestre dos Gatunos": {"Nome": "Rei dos Ladris"},
    "Dançarino das Sombras": {"Nome": "Maestro Noturno"},
    "Sabotador Engenheiro": {"Nome": "Mestre dos Artifícios"},
    "Paladino": {"Nome": "Guardião Celestial"},
    "Sumo Sacerdote": {"Nome": "Sacerdote Santo"},
    "Inquisidor da Luz": {"Nome": "Carrasco Santo"},
    "Sacerdote das Marés": {"Nome": "Guardião dos Mares"},
    "Atirador de Elite": {"Nome": "Francatirador Lendário"},
    "Senhor das Feras": {"Nome": "Invocador Ancestral"},
    "Mestre dos Venenos": {"Nome": "Ceifador Venenoso"},
    "Franco-Atirador Tático": {"Nome": "Sentinela de Alvo Fixo"},
    "Devastador": {"Nome": "Titã Indomável"},
    "Senhor da Guerra": {"Nome": "Conquistador Supremo"},
    "Bárbaro Frenético": {"Nome": "Destruidor Incontrolável"},
    "Guardião Xamânico": {"Nome": "Xamã das Tribos Primordiais"},
    "Piro-Mago": {"Nome": "Arcano do Inferno"},
    "Invocador de Magma": {"Nome": "Avatar do Vulcão"},
    "Bruxo de Chamas Negras": {"Nome": "Senhor do Purgatório"},
    "Alquimista Volátil": {"Nome": "Mestre das Explosões Alquímicas"},
    "Druida da Floresta": {"Nome": "Guardião da Natureza"},
    "Metamorfo": {"Nome": "Behemoth Primal"},
    "Druida Tempestuoso": {"Nome": "Invocador de Tempestades"},
    "Guardião dos Seres Místicos": {"Nome": "Mestre das Bestas Míticas"}
}

drop_fontes_itens = {
    "Espada do Rei Caído": "Rei Goblin Corrompido (Chefe - Região 1)",
    "Escudo da Origem": "Faraó Caído (Chefe - Região 3)",
    "Fragmento do Huracán": "Quimera Astral (Monstro - Região 4)",
    "Orbe do Vazio Estelar": "DRAGÃO ANCESTRAL SUPREMO (Chefe - Região 4)",
    "Espelho das Sombras Arcanas": "Sombra Errante (Monstro - Região 3)",
    "Coração do Glaciar": "Faraó Caído (Chefe - Região 3)",
    "Adaga da Lua Sangrenta": "Faraó Caído (Chefe - Região 3)",
    "Adaga do Eclipse Profundo": "Valquíria Corrompida (Monstro - Região 4)",
    "Núcleo do Autômato Ancestral": "Sentinela Dourada (Monstro - Região 4)",
    "Cálice da Luz Eterna": "Anjo Caído (Monstro - Região 4)",
    "Selo do Julgador Supremo": "Valquíria Corrompida (Monstro - Região 4)",
    "Lágrima do Oceano Primordial": "Senhor do Magma (Chefe - Região 2)",
    "Arco de Ossos de Dragão": "DRAGÃO ANCESTRAL SUPREMO (Chefe - Região 4)",
    "Presa da Hidra Imorredoura": "Salamandra de Fogo (Monstro - Região 2)",
    "Lente do Rastreador Estelar": "Sentinela Dourada (Monstro - Região 4)",
    "Machado de Guerra de Magma Pura": "Senhor do Magma (Chefe - Região 2)",
    "Coração do Bárbaro Ancestral": "Gárgula de Pedra (Monstro - Região 3)",
    "Totem dos Cinco Espíritos": "Cavaleiro Espectral (Monstro - Região 3)",
    "Brasa do Coração do Mundo": "Senhor do Magma (Chefe - Região 2)",
    "Chama Negra do Abismo": "Orc do Inferno (Monstro - Região 2)",
    "Pedra Filosofal Incompleta": "Morcego de Chamas (Monstro - Região 2)",
    "Semente da Criação Primordial": "Múmia Antiga (Monstro - Região 3)",
    "Cajado do Vento Ancestral": "Quimera Astral (Monstro - Região 4)",
    "Galho do Tronco do Mundo (Yggdrasil)": "DRAGÃO ANCESTRAL SUPREMO (Chefe - Região 4)"
}

tier4_evolucoes = {
    "Soberano da Fúria": {
        "Nome": "Titã de Aço Negro",
        "Requisitos": lambda p: p.ataque_base >= 55 and "Espada do Rei Caído" in p.inventario_itens and p.combates_sem_pocoes_hp >= 5,
        "TextoReq": "Ataque Base >= 55, item 'Espada do Rei Caído' e 5+ combates sem poções de HP."
    },
    "Fortalecedor Inquebrável": {
        "Nome": "Senhor das Eras Titanicus",
        "Requisitos": lambda p: p.defesa_base >= 60 and "Escudo da Origem" in p.inventario_itens,
        "TextoReq": "Defesa Base >= 60, item 'Escudo da Origem'."
    },
    "Lorde das Vendavais": {
        "Nome": "Mestre do Vento Ancestral",
        "Requisitos": lambda p: p.ataque_base >= 50 and "Fragmento do Huracán" in p.inventario_itens,
        "TextoReq": "Ataque Base >= 50, item 'Fragmento do Huracán'."
    },
    "Mestre dos Elementos": {
        "Nome": "Arcano do Cosmos",
        "Requisitos": lambda p: p.mp_max >= 200 and "Orbe do Vazio Estelar" in p.inventario_itens and p.chefes_derrotados_em_3_turnos >= 1,
        "TextoReq": "MP Max >= 200, item 'Orbe do Vazio Estelar' e derrotar chefão em até 3 turnos."
    },
    "Tecelão de Realidades": {
        "Nome": "Fantasma do Abismo Estelar",
        "Requisitos": lambda p: p.mp_max >= 220 and "Espelho das Sombras Arcanas" in p.inventario_itens,
        "TextoReq": "MP Max >= 220, item 'Espelho das Sombras Arcanas'."
    },
    "Mestre do Zero Absoluto": {
        "Nome": "Soberano do Inverno ETERNO",
        "Requisitos": lambda p: p.hp_max >= 250 and "Coração do Glaciar" in p.inventario_itens,
        "TextoReq": "HP Max >= 250, item 'Coração do Glaciar'."
    },
    "Sombra Mortal": {
        "Nome": "Espectro Fantasma",
        "Requisitos": lambda p: p.criticos_registrados >= 15 and "Adaga da Lua Sangrenta" in p.inventario_itens,
        "TextoReq": "15+ Acertos críticos registrados, item 'Adaga da Lua Sangrenta'."
    },
    "Maestro Noturno": {
        "Nome": "Monarca do Vazio Obscuro",
        "Requisitos": lambda p: p.criticos_registrados >= 20 and "Adaga do Eclipse Profundo" in p.inventario_itens,
        "TextoReq": "20+ Críticos registrados, item 'Adaga do Eclipse Profundo'."
    },
    "Mestre dos Artifícios": {
        "Nome": "Arquiteto da Aniquilação",
        "Requisitos": lambda p: p.ouro >= 1000 and "Núcleo do Autômato Ancestral" in p.inventario_itens,
        "TextoReq": "Ouro acumulado >= 1000, item 'Núcleo do Autômato Ancestral'."
    },
    "Guardião Celestial": {
        "Nome": "Avatar dos Serafins",
        "Requisitos": lambda p: p.hp_max >= 300 and "Cálice da Luz Eterna" in p.inventario_itens and p.dano_curado_total >= 500,
        "TextoReq": "HP Max >= 300, item 'Cálice da Luz Eterna' e curar 500+ de HP total."
    },
    "Sacerdote Santo": {
        "Nome": "Avatar dos Serafins",
        "Requisitos": lambda p: p.hp_max >= 300 and "Cálice da Luz Eterna" in p.inventario_itens and p.dano_curado_total >= 500,
        "TextoReq": "HP Max >= 300, item 'Cálice da Luz Eterna' e curar 500+ de HP total."
    },
    "Carrasco Santo": {
        "Nome": "Flagelo Divino dos Céus",
        "Requisitos": lambda p: p.ataque_base >= 55 and "Selo do Julgador Supremo" in p.inventario_itens,
        "TextoReq": "Ataque Base >= 55, item 'Selo do Julgador Supremo'."
    },
    "Guardião dos Mares": {
        "Nome": "Avatar de Leviatã",
        "Requisitos": lambda p: p.mp_max >= 200 and "Lágrima do Oceano Primordial" in p.inventario_itens,
        "TextoReq": "MP Max >= 200, item 'Lágrima do Oceano Primordial'."
    },
    "Francatirador Lendário": {
        "Nome": "Senhor do Horizonte Primordial",
        "Requisitos": lambda p: p.arma["Raridade"] == "Lendário" and "Arco de Ossos de Dragão" in p.inventario_itens,
        "TextoReq": "Arma Lendária equipada e item 'Arco de Ossos de Dragão'."
    },
    "Ceifador Venenoso": {
        "Nome": "Flagelo da Hidra de Sangue",
        "Requisitos": lambda p: p.arma["Raridade"] in ["Épico", "Lendário"] and "Presa da Hidra Imorredoura" in p.inventario_itens,
        "TextoReq": "Arma com efeito de status e item 'Presa da Hidra Imorredoura'."
    },
    "Sentinela de Alvo Fixo": {
        "Nome": "Olho do Destino Interdimensional",
        "Requisitos": lambda p: p.nivel >= 25 and "Lente do Rastreador Estelar" in p.inventario_itens,
        "TextoReq": "Nível >= 25, item 'Lente do Rastreador Estelar'."
    },
    "Titã Indomável": {
        "Nome": "Berserker do Cataclismo",
        "Requisitos": lambda p: p.batalhas_vencidas_hp_baixo >= 3 and "Machado de Guerra de Magma Pura" in p.inventario_itens,
        "TextoReq": "Vencer 3+ lutas com <10% de HP e item 'Machado de Guerra de Magma Pura'."
    },
    "Destruidor Incontrolável": {
        "Nome": "Soberano do Frenesi Sangrento",
        "Requisitos": lambda p: p.ataque_base >= 65 and "Coração do Bárbaro Ancestral" in p.inventario_itens,
        "TextoReq": "Ataque Base >= 65, item 'Coração do Bárbaro Ancestral'."
    },
    "Xamã das Tribos Primordiais": {
        "Nome": "Espiritualista do Caos Primal",
        "Requisitos": lambda p: p.defesa_base >= 45 and "Totem dos Cinco Espíritos" in p.inventario_itens,
        "TextoReq": "Defesa Base >= 45, item 'Totem dos Cinco Espíritos'."
    },
    "Arcano do Inferno": {
        "Nome": "Senhor das Cinzas Primordiais",
        "Requisitos": lambda p: p.chefes_fogo_apenas >= 1 and "Brasa do Coração do Mundo" in p.inventario_itens,
        "TextoReq": "Derrotar chefão com magias de fogo e item 'Brasa do Coração do Mundo'."
    },
    "Senhor do Purgatório": {
        "Nome": "Imperador do Inferno Abissal",
        "Requisitos": lambda p: p.mp_max >= 210 and "Chama Negra do Abismo" in p.inventario_itens,
        "TextoReq": "MP Max >= 210, item 'Chama Negra do Abismo'."
    },
    "Mestre das Explosões Alquímicas": {
        "Nome": "Criador da Pedra Filosofal",
        "Requisitos": lambda p: p.pocoes >= 20 and "Pedra Filosofal Incompleta" in p.inventario_itens,
        "TextoReq": "Ter 20+ poções acumuladas, item 'Pedra Filosofal Incompleta'."
    },
    "Guardião da Natureza": {
        "Nome": "Avatar da Grande Árvore-Mãe",
        "Requisitos": lambda p: p.defesa_base >= 50 and "Semente da Criação Primordial" in p.inventario_itens and p.batalhas_concluidas_sem_desmaiar >= 5,
        "TextoReq": "Defesa Base >= 50, item 'Semente da Criação Primordial' e 5+ explorações sem desmaiar."
    },
    "Invocador de Tempestades": {
        "Nome": "Senhor dos Elementos Primordiais",
        "Requisitos": lambda p: p.nivel >= 25 and "Cajado do Vento Ancestral" in p.inventario_itens,
        "TextoReq": "Nível >= 25, item 'Cajado do Vento Ancestral'."
    },
    "Mestre das Bestas Míticas": {
        "Nome": "Rei de Yggdrasil",
        "Requisitos": lambda p: p.hp_max >= 280 and "Galho do Tronco do Mundo (Yggdrasil)" in p.inventario_itens,
        "TextoReq": "HP Max >= 280, item 'Galho do Tronco do Mundo'."
    }
}

class_tree = {
    "Guerreiro": {"OpcoesAvancadas": ["Cavaleiro Rúnico", "Berserker", "Guardião Vanguarda", "Espachim da Tempestade"], "NivelEvolucao": 5, "HPBase": 120, "MPBase": 30, "AtaqueBase": 12, "DefesaBase": 8},
    "Mago": {"OpcoesAvancadas": ["Arquimago", "Mago do Caos", "Ilusionista Arcano", "Criomante"], "NivelEvolucao": 5, "HPBase": 80, "MPBase": 90, "AtaqueBase": 20, "DefesaBase": 3},
    "Ladino": {"OpcoesAvancadas": ["Assassino", "Mestre dos Gatunos", "Dançarino das Sombras", "Sabotador Engenheiro"], "NivelEvolucao": 5, "HPBase": 95, "MPBase": 40, "AtaqueBase": 16, "DefesaBase": 4},
    "Clérigo": {"OpcoesAvancadas": ["Paladino", "Sumo Sacerdote", "Inquisidor da Luz", "Sacerdote das Marés"], "NivelEvolucao": 5, "HPBase": 110, "MPBase": 70, "AtaqueBase": 10, "DefesaBase": 7},
    "Patrulheiro": {"OpcoesAvancadas": ["Atirador de Elite", "Senhor das Feras", "Mestre dos Venenos", "Franco-Atirador Tático"], "NivelEvolucao": 5, "HPBase": 100, "MPBase": 45, "AtaqueBase": 15, "DefesaBase": 5},
    "Bárbaro": {"OpcoesAvancadas": ["Devastador", "Senhor da Guerra", "Bárbaro Frenético", "Guardião Xamânico"], "NivelEvolucao": 5, "HPBase": 130, "MPBase": 20, "AtaqueBase": 18, "DefesaBase": 2},
    "Piromântico": {"OpcoesAvancadas": ["Piro-Mago", "Invocador de Magma", "Bruxo de Chamas Negras", "Alquimista Volátil"], "NivelEvolucao": 5, "HPBase": 85, "MPBase": 80, "AtaqueBase": 19, "DefesaBase": 3},
    "Druida": {"OpcoesAvancadas": ["Druida da Floresta", "Metamorfo", "Druida Tempestuoso", "Guardião dos Seres Místicos"], "NivelEvolucao": 5, "HPBase": 105, "MPBase": 65, "AtaqueBase": 13, "DefesaBase": 6}
}