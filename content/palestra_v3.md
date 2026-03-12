---
Slide1: {
  titulo: "Debugando a Exaustão: IA, Saúde Mental e Performance sob a Lupa da Evidência Médica",
  subtitulo: "Dr. André Quadros",
  imagem: {
    posicao: "equerda central",
    descricao: "Uma imagem minimalista de dados (dice) flutuando sobre uma malha de circuitos neurais, simbolizando a união da sorte/aleatoriedade do mundo real com a precisão dos dados."
  }
}

---
Slide2: {
  titulo: "André – Médico e Programador",
  texto: {
"- Médico pela Universidade Federal do Estado do Rio de Janeiro
- Mais de 125 Tb de dados de saúde processados
- Atua em grandes projetos de tecnologias aplicadas a saúde desde 2020
- Desde 2022 faz parte do time de especialistas de IA em saúde no DASA
- Médico Tech Lead & Coordenador Médico de Qualidade em Evidência de Mundo Real (RWE)
- Criador da Ferramenta QUADROS DE SAÚDE de análise de dados"
  },
  imagem: [
    {
      posicao: "direita",
      descricao: "Foto de perfil profissional do palestrante."
    },
    {
      posicao: "inferior direita",
      descricao: "Qr code para o Instagram @dr.andreq"
    }
  ]
}

---
Slide3: {
  titulo: "Compliance",
  texto: {
"Estou aqui como André, as opiniões aqui veiculadas representam apenas minha opinião pessoal, as quais não se relacionam ou estão ligadas às empresas que represento."
  }
}

---
Slide4: {
  titulo: "Combinados",
  texto: {
"1) A apresentação é interativa e preciso que participem.
2) Tudo que eu falar está diretamente ligado a sua e a minha saúde.
3) Responderei com graus de certeza (como uma IA):
   - > 95% de certeza: Afirmo.
   - 60% a 95%: Digo 'Eu acho'.
   - < 60%: Digo 'Não sei responder agora'.
4) Novo software mental: A visão do mundo através de grafos de conhecimento."
  }
}

---
Slide5: {
  titulo: "O que é um grafo de conhecimento?",
  falas: {
"Imagine que o conhecimento não está em gavetas, mas em uma rede. Nós somos pontos (nós) e nossas interações são os fios (arestas).",
"Ele é uma forma de representar o mundo real de forma estruturada, sem perder a complexidade das relações."
  }
}

---
Slide6: {
  titulo: "O Elo Médico-Programador",
  mermaid: """
  graph TD
    No_Medico[Médico]
    No_Programador[Programador]
  """
}

---
Slide7: {
  titulo: "Médico VS Programador",
  falas: {
"Em um primeiro momento parece que essas coisas não tem ligação mas quero mostrar que tem tudo a ver.",
"Alguém sabe o que faz um médico? (aguarda e interage)"
  }
}

---
Slide8: {
  titulo: "Médico: cuida da saúde",
  falas: {
"Alguém sabe o que faz um programador? (aguarda resposta e interage)"
  }
}

---
Slide9: {
  titulo: "Programador: faz a máquina obedecer",
  falas: {
"Agora alguém chuta o que faz o médico programador? (aguarda e interage)"
  }
}

---
Slide10: {
  titulo: "Médico Programador: cuida da saúde e faz a máquina obedecer",
  texto: {
"Médico Programador: cuida da saúde das pessoas através do uso da tecnologia, análise de dados e algoritmos (faz a máquina obedecer)"
  },
  falas: {
"Existem algumas definições possíveis, mas a que eu gosto é: 'Médico programador é aquele que usa a tecnologia para cuidar da saúde'.",
"Parece obvio mas isso carrega um grande significado!"
  }
}

---
Slide11: {
  titulo: "A Conexão",
  mermaid: """
  graph TD
    No_Medico[Médico]
    No_Programador[Programador]
    
    No_Medico -- "Cuidar da saúde via tecnologia" --> No_Programador
    No_Programador -- "Estruturação de dados clínicos" --> No_Medico
  """,
  falas: {
"Agora temos o elo de ligação e o fluxo de dados entre as duas áreas."
  }
}

---
Slide12: {
  titulo: "O Surgimento da Evidência",
  mermaid: """
  graph TD
    No_Medico[Médico]
    No_Programador[Programador]
    No_Evidencia[Evidência / RWE]
    
    No_Medico & No_Programador --> No_Evidencia
    No_Evidencia -- "Validação do Algoritmo" --> No_Programador
    No_Evidencia -- "Segurança Clínica" --> No_Medico
  """,
  falas: {
"Eis que surge mais um nó em nosso grafo: A evidência. Ela é o que separa a 'opinião' do 'fato clínico'."
  }
}

---
Slide13: {
  titulo: "Evidência de Mundo Real (RWE)",
  texto: {
"O mundo real é caótico e repleto de variáveis."
  },
  falas: {
"Trabalho com RWE. Ao contrário da pesquisa controlada em laboratório, o mundo real envolve sono ruim, estresse e tecnologia omnipresente.",
"Gerar evidência é transformar o ruído de 125TB de dados em conhecimento que salva vidas."
  }
}

---
Slide14: {
  titulo: "A Hierarquia da Evidência",
  imagem: {
    posicao: "centro",
    descricao: "Uma pirâmide clássica de evidência médica (Evidence-Based Medicine Pyramid). No topo, 'Revisões Sistemáticas'. Na base, 'Opinião de Especialistas'.",
    referencia: "Busca sugerida: 'Medical evidence pyramid infographic'."
  },
  falas: {
"Quando falamos de IA e saúde mental, ainda estamos subindo essa pirâmide. Muita coisa hoje é baseada em observações iniciais que agora os dados estão confirmando."
  }
}

---
Slide15: {
  titulo: "O Panóptico Algorítmico",
  subtitulo: "A tecnologia como ferramenta de controle invisível",
  falas: {
"Foucault descreveu o Panóptico como um lugar onde você é vigiado sem saber. Hoje, vivemos o Panóptico Algorítmico.",
"Nossas métricas de produtividade (commits, tempo de tela, status online) são os guardas. Internalizamos a pressão de sermos 'sempre eficientes', transformando nossa mente em uma fábrica digital que nunca fecha."
  }
}

---
Slide16: {
  titulo: "O Retrato da Exaustão no Brasil",
  texto: {
"- 45% dos médicos apresentam transtornos mentais (2025).
- Quase 500 mil afastamentos por saúde mental em um ano (Recorde).
- 2º país com mais casos de Burnout no mundo."
  },
  link: "https://www.apm.org.br/45-dos-medicos-no-brasil-sofrem-com-ao-menos-um-tipo-de-transtorno-mental-taxa-atinge-mesmo-patamar-do-pos-pandemia-revela-novo-estudo/",
  falas: {
"Estes dados de 2025 mostram que o 'sistema' está sobrecarregado. E para nós, da tecnologia, o impacto é direto."
  }
}

---
Slide17: {
  titulo: "Technostress: A Insegurança Digital",
  texto: {
"O medo de ser substituído pela IA é o maior preditor de queda na qualidade de vida."
  },
  link: "https://pmc.ncbi.nlm.nih.gov/articles/PMC12024279/",
  falas: {
"A ciência chama isso de 'Techno-insecurity'. Esse sentimento é o que mais drena nossa satisfação pessoal e nos mantém em estado de alerta."
  }
}

---
Slide18: {
  titulo: "O Ciclo do FOMO e Burnout Digital",
  mermaid: """
  graph TD
    Estado_FOMO[FOMO: Medo de estar por fora]
    Estado_Ansiedade[Ansiedade Crônica]
    Estado_Hiperconexao[Uso Problemático / Hiperconectividade]
    Estado_Privacao[Privação de Sono / Falta de Recuperação]
    Estado_Burnout[Esgotamento / Burnout]

    Estado_FOMO --> Estado_Ansiedade
    Estado_Ansiedade --> Estado_Hiperconexao
    Estado_Hiperconexao --> Estado_Privacao
    Estado_Privacao --> Estado_Burnout
    Estado_Burnout -.-> Estado_Ansiedade
  """,
  link: "https://www.tandfonline.com/doi/full/10.1080/13548506.2025.2587974",
  falas: {
"O FOMO cria um estado de alerta crônico. O cérebro nunca entende que está seguro para descansar."
  }
}

---
Slide19: {
  titulo: "Memory Leak Cognitivo",
  texto: {
"Cognitive Offloading: Terceirizar o pensamento para a IA pode reduzir a conectividade neural em até 47%."
  },
  link: "https://www.media.mit.edu/projects/your-brain-on-chatgpt/overview/",
  falas: {
"Estamos sofrendo um 'Memory Leak' cognitivo. Alocamos a IA para pensar, mas não 'limpamos' ou consolidamos a informação em nosso hardware biológico.",
"Usuários passivos de IA apresentam uma redução drástica na conectividade em áreas cerebrais críticas."
  }
}

---
Slide20: {
  titulo: "Dívida Técnica e Memória",
  texto: {
"83% dos usuários de IA não lembram o que 'escreveram' minutos depois."
  },
  imagem: {
    posicao: "centro",
    descricao: "Uma representação visual de um cérebro com algumas áreas escurecidas.",
    referencia: "Procure por 'EEG connectivity brain map'."
  },
  falas: {
"Se o cérebro não faz o esforço de síntese, ele não armazena a informação. O usuário torna-se espectador do próprio trabalho, acumulando uma dívida técnica cerebral."
  }
}

---
Slide21: {
  titulo: "A Pirâmide de Maslow na Performance",
  texto: {
"Sem saúde na base, não existe produtividade no topo."
  },
  falas: {
"Precisamos cuidar do hardware antes do software. Para haver inovação, o colaborador precisa se sentir biologicamente seguro e descansado."
  }
}

---
Slide22: {
  titulo: "Protocolo de Restauração",
  yaml: """
  versao_protocolo: 1.0.0
  usuario: "Humano de Alta Performance"
  
  configuracoes_sono:
    parar_cafeina: 10_horas_antes
    parar_trabalho: 3_horas_antes
    parar_jantar: 2_horas_antes
    parar_telas: 1_hora_antes
    snooze_permitido: false

  metrica_recuperacao:
    meta_descanso_diario: "42%" # Regra dos Nagoski
    status: >
      Se tempo_descanso < meta:
        raise SystemBurnoutError
  """,
  falas: {
"Para o sistema nervoso resetar, precisamos de 10 horas de descanso (42% do dia). Se você não tirar o tempo para descansar, a doença tirará você do mercado."
  }
}

---
Slide23: {
  titulo: "O Domínio da Máquina",
  texto: {
"A IA aprendeu o que NÓS construímos. Nós detemos o 'Qualia'."
  },
  falas: {
"A IA é excelente para produção (Work), mas nós somos os donos da ética, da decisão (Action) e do sentir (Qualia). Essa é a chave para a paz mental."
  }
}

---
Slide24: {
  titulo: "Relato Pessoal: A Velocidade da Verdade",
  texto: {
"Clonagem de Voz: A tecnologia que nos obriga a desacelerar."
  },
  link: "https://www.youtube.com/watch?v=XpQfghMWkVc",
  falas: {
"Criminosos usam IA para clonar vozes. Isso me faz aceitar minha própria velocidade. Prefiro a profundidade do conhecimento do que a pressa do erro."
  }
}

---
Slide25: {
  titulo: "Obrigado!",
  subtitulo: "Dr. André Quadros",
  texto: {
"Não deixe seu hardware (biologia) falhar tentando rodar um software (IA) que nunca dorme."
  },
  imagem: [
    {
      posicao: "centro",
      descricao: "Foto do André"
    },
    {
      posicao: "inferior",
      descricao: "Instagram: @dr.andreq"
    }
  ]
}