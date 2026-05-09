from flask import Flask, render_template

app = Flask(__name__)

# =====================================================
# Dados estáticos do portfólio (sem DB / sem API externa)
# =====================================================

# Perfil
perfil = {
    'nome': 'Jonas Miguel de Oliveira',
    'idade': 22,
    'curso': 'Desenvolvimento de Software Multiplataforma',
    'instituicao': 'Fatec Jessen Vidal — São José dos Campos',
    'semestre': 6,
    'foto': 'perfil.png',
    'titulo': 'Desenvolvedor Full Stack · Power Platform',
    'bio_curta': 'Desenvolvedor Junior 2 na ProNext há 2 anos e 4 meses, atuando em Power Platform, APIs C#, banco Azure e soluções com IA. No 6º semestre de DSM na Fatec São José dos Campos.',
    'localizacao': 'São José dos Campos, SP',
    'email': 'jonaasmigueldeoliveira@gmail.com',
    'github': 'https://github.com/Jonasoliver',
    'linkedin': 'https://www.linkedin.com/in/jonas-miguel-ol/',
    'instagram': 'https://www.instagram.com/jonaasmiguel/',
}

# Experiência profissional
experiencia = [
    {
        'empresa': 'ProNext',
        'logo': 'pronext-logo.png',
        'cargo': 'Desenvolvedor Junior 2',
        'periodo': '2 anos e 4 meses · atual',
        'descricao_curta': 'Desenvolvimento de software para empresas — Power Platform, APIs C#, banco Azure e soluções com IA.',
        'atividades': [
            'Desenvolvimento de aplicações em Power Platform do início ao fim',
            'Manutenção e evolução de apps em produção',
            'Desenvolvimento e manutenção de APIs em C#',
            'Operação de bancos de dados em produção hospedados no Azure',
            'Levantamento de requisitos e validação direta com clientes',
            'Prototipação de interfaces no Figma',
            'Desenvolvimento de soluções com IA — de protótipos a projetos reais',
        ],
        'destaque': 'Um aplicativo desenvolvido por mim do zero foi premiado pelo hall global da empresa cliente por eficiência de processo.',
        'tecnologias': ['Power Platform', 'Power Apps', 'Power Automate', 'C#', '.NET', 'Azure', 'SQL', 'Figma', 'IA / LLMs'],
    },
]

# Trabalhos / Projetos API
trabalhos = [
    {
        'titulo': 'Projeto API 1DSM — segundo semestre de 2023',
        'ano': '2023',
        'semestre': '1º DSM',
        'papel': 'Full Stack',
        'descricao': 'A aplicação foi desenvolvida para fornecer informações sobre hospitais no Brasil que atendem crianças com problemas renais crônicos. Ela permite que os usuários consultem dados como nome, endereço, telefone e especialidades de cada hospital, além de filtrar por localização e especialização. A plataforma também inclui um fórum de discussões, com chat ao vivo e a possibilidade de envio de imagens com comentários, facilitando a troca de informações entre pacientes, familiares e profissionais de saúde. Para garantir a segurança, há moderação de conteúdo e controles de privacidade, além de autenticação para acesso às funcionalidades. Com design responsivo, a aplicação visa fornecer informações úteis e promover um espaço de apoio e interação para quem enfrenta desafios relacionados à saúde renal infantil.',
        'tecnologias': 'Tecnologias utilizadas:',
        'tecno': 'Python, Flask, Docker, AWS, MySQL, JavaScript',
        'contribuicao': 'Contribuições pessoais',
        'cont': 'No desenvolvimento deste projeto, uma das contribuições mais significativas foi focar na otimização de processos e no equilíbrio das cargas de trabalho para garantir a melhor performance da aplicação, mesmo com requisitos de hardware limitados. Ao longo do desenvolvimento, busquei melhorar continuamente a estrutura de codificação e a integração dos diversos módulos, visando garantir uma comunicação eficiente e escalável, crucial para o bom funcionamento das funcionalidades em tempo real, como o chat e o envio de imagens.',
        'hard': 'Hard Skills Efetivamente desenvolvidas:',
        'hardD': 'Python, CSS, HTML, JavaScript, Docker, MySQL, Flask',
        'soft': 'Soft Skills Efetivamente desenvolvidas:',
        'so': 'Autonomia e adaptação. O processo de otimizar a infraestrutura e garantir a disponibilidade da plataforma em diferentes cenários demandou uma grande capacidade de adaptação e tomada de decisões de forma independente. Esse imprevisto me forçou a desenvolver ainda mais a minha resiliência e paciência diante de imprevistos.',
        'imagem': 'api.jpeg'
    },
    {
        'titulo': 'Projeto API 2DSM — primeiro semestre de 2024',
        'ano': '2024',
        'semestre': '2º DSM',
        'papel': 'Full Stack',
        'descricao': 'O projeto API 2DSM foi desenvolvido com o objetivo de criar uma plataforma de atendimento ao cliente, focada em um sistema de gestão de tickets e chat em tempo real. Utilizando React no frontend, a aplicação oferece três tipos de acesso: Cliente, Atendente e Administrador. A interface foi construída para ser intuitiva e responsiva, utilizando HTML, CSS e Bootstrap. No backend, o sistema foi implementado com Node.js, garantindo a manipulação eficiente de requisições e comunicação com o banco de dados MySQL. A plataforma permite a criação e gestão de tickets, onde os atendentes podem auxiliar os clientes com seus problemas relacionados a produtos e serviços.',
        'tecnologias': 'Tecnologias utilizadas:',
        'tecno': 'Node.js, React, HTML, CSS, MySQL, JavaScript, Bootstrap',
        'contribuicao': 'Contribuições pessoais',
        'cont': 'No desenvolvimento deste projeto, concentrei meus esforços em criar uma experiência de usuário fluida e eficiente, utilizando React para garantir uma interface interativa e com desempenho otimizado. Trabalhei na implementação do sistema de tickets e chat, essenciais para a comunicação eficaz entre clientes e atendentes. A escolha de Node.js para o backend foi crucial para garantir respostas rápidas e escaláveis.',
        'hard': 'Hard Skills Efetivamente desenvolvidas:',
        'hardD': 'Node.js, React, HTML, CSS, JavaScript, MySQL, Bootstrap',
        'soft': 'Soft Skills Efetivamente desenvolvidas:',
        'so': 'Trabalho em equipe e gestão de tempo. Durante o desenvolvimento, fui capaz de colaborar eficientemente com outros membros da equipe, mantendo o foco nas prioridades e gerenciando o tempo de maneira eficaz para cumprir os prazos de entrega da aplicação.',
        'imagem': 'Api2024.png'
    },
    {
        'titulo': 'Projeto API 3DSM — segundo semestre de 2024',
        'ano': '2024',
        'semestre': '3º DSM',
        'papel': 'Backend',
        'descricao': 'O Projeto API 3DSM foi desenvolvido para o cliente AFAPG com o objetivo de criar um portal de transparência, onde são exibidos detalhadamente os gastos realizados com doações empresariais em projetos sociais. Utilizando o framework Spring no backend com Java, a aplicação oferece segurança e escalabilidade para o gerenciamento dos dados. A plataforma foi projetada para garantir que todas as informações financeiras sejam acessíveis ao público de forma clara e transparente, permitindo que os usuários visualizem os projetos realizados, os valores recebidos e como os recursos foram aplicados. A interface foi construída com React, enquanto o banco de dados MySQL armazena as informações. A autenticação é feita via JWT.',
        'tecnologias': 'Tecnologias utilizadas:',
        'tecno': 'Java, Spring, React, MySQL, JWT',
        'contribuicao': 'Contribuições pessoais',
        'cont': 'Durante o desenvolvimento deste projeto, meu foco esteve na criação de uma aplicação escalável e segura. Trabalhei na implementação do backend com Java e Spring, criando uma estrutura robusta para o gerenciamento e exposição de dados financeiros. A integração com MySQL foi crucial para armazenar as informações de forma estruturada, enquanto JWT garantiu que apenas usuários com permissões adequadas pudessem acessar dados sensíveis.',
        'hard': 'Hard Skills Efetivamente desenvolvidas:',
        'hardD': 'Java, Spring, React, MySQL, JWT',
        'soft': 'Soft Skills Efetivamente desenvolvidas:',
        'so': 'Responsabilidade e foco em resultados. A criação de um portal de transparência exigiu grande atenção aos detalhes e capacidade de assumir responsabilidades para garantir informações claras, precisas e seguras. Essa experiência de negociação de segurança de dados foi fundamental para meu desenvolvimento profissional.',
        'imagem': 'projeto3dsm.png'
    },
    {
        'titulo': 'Projeto API 4DSM — primeiro semestre de 2025',
        'ano': '2025',
        'semestre': '4º DSM',
        'papel': 'Full Stack + IoT',
        'descricao': 'Desenvolvido por alunos do 4º semestre de DSM para o cliente Tecsus, este projeto realiza a coleta e processamento de dados de Estações Meteorológicas. O sistema permite inserção e busca de dados, além da exibição de estatísticas em gráficos interativos. Atende à demanda da Tecsus para monitoramento ambiental, utilizando sensores de baixo custo para medir vento, chuva, umidade, temperatura e pressão. Os dados são transmitidos para um servidor e exibidos em um portal com dashboards e relatórios.',
        'tecnologias': 'Tecnologias utilizadas:',
        'tecno': 'React, Node.js, TypeScript, PostgreSQL, Docker, IoT',
        'contribuicao': 'Contribuições pessoais',
        'cont': 'Contribuí significativamente para a arquitetura do sistema de coleta e processamento de dados meteorológicos. Trabalhei na integração dos sensores IoT com o backend, garantindo a transmissão confiável e em tempo real dos dados coletados. Implementei APIs RESTful para gerenciar a inserção e recuperação de dados, além de desenvolver dashboards interativos utilizando React e bibliotecas de visualização de dados.',
        'hard': 'Hard Skills Efetivamente desenvolvidas:',
        'hardD': 'React, Node.js, TypeScript, PostgreSQL, Docker, IoT, APIs RESTful, Data Visualization',
        'soft': 'Soft Skills Efetivamente desenvolvidas:',
        'so': 'Trabalho em equipe e resolução de problemas. O projeto exigiu colaboração estreita entre diferentes áreas (hardware, backend, frontend), desenvolvendo habilidades de comunicação técnica e coordenação de esforços. A experiência com cliente real (Tecsus) aprimorou habilidades de gestão de expectativas e apresentação de resultados.',
        'imagem': 'tecsus-2.png',
        'galeria': ['tecsus-2.png'],
    },
    {
        'titulo': 'Projeto API 5DSM — Sistema da Guarnição de Caçapava (segundo semestre de 2025)',
        'ano': '2025',
        'semestre': '5º DSM',
        'papel': 'Product Owner',
        'descricao': 'Sistema de Gestão Administrativa desenvolvido para a Guarnição de Caçapava com interfaces web e mobile. Projeto acadêmico realizado por alunos do 5º semestre de DSM com o objetivo de digitalizar e automatizar a gestão de almoxarifado, substituindo controles manuais e descentralizados que dificultavam o rastreamento de itens. A solução oferece controle em tempo real de estoque, histórico de movimentações, gestão de requisições, fornecedores, ordens de compra, validades e relatórios gerenciais. O projeto foi apresentado diretamente para o General, Coronel e Tenentes da guarnição e foi escolhido para ser implantado oficialmente no Exército Brasileiro. Como reconhecimento pela contribuição, fui condecorado com a medalha de honra da unidade.',
        'tecnologias': 'Tecnologias utilizadas:',
        'tecno': 'Flutter, Dart, Vue.js, PostgreSQL, Java, Python, Git',
        'contribuicao': 'Product Owner',
        'cont': 'Como Product Owner, minha principal responsabilidade foi garantir o alinhamento entre as necessidades da Guarnição de Caçapava e a solução desenvolvida pela equipe. Conduzi o levantamento de requisitos junto aos stakeholders militares, priorizei o backlog do produto e defini as funcionalidades essenciais para cada sprint. Trabalhei na elaboração de user stories detalhadas, critérios de aceitação e validação das entregas. Apresentei o projeto diretamente ao General, Coronel e Tenentes da guarnição em sessão de avaliação. O reconhecimento veio com a escolha do sistema para implantação oficial no Exército Brasileiro e com a entrega da medalha de honra da unidade pela contribuição prestada.',
        'hard': 'Hard Skills Efetivamente desenvolvidas:',
        'hardD': 'Gestão de Produto, Metodologias Ágeis, Scrum, Levantamento de Requisitos, Priorização de Backlog, User Stories, Apresentação Executiva, Flutter, Vue.js, PostgreSQL',
        'soft': 'Soft Skills Efetivamente desenvolvidas:',
        'so': 'Liderança, visão estratégica e comunicação executiva. Como Product Owner, desenvolvi fortemente a capacidade de liderar sem autoridade formal e de apresentar resultados a stakeholders de alto escalão (General, Coronel, Tenentes). A gestão de stakeholders militares exigiu habilidades avançadas de negociação, postura e clareza. A experiência de traduzir necessidades militares complexas em funcionalidades de software desenvolveu minha empatia, capacidade de adaptação a contextos organizacionais distintos e responsabilidade pelo impacto das entregas.',
        'imagem': 'guarnicao-web.png',
        'galeria': ['guarnicao-web.png', 'guarnicao-mobile.png', 'guarnicao-apresentacao.png', 'guarnicao-medalha.png'],
        'destaques': [
            'Projeto escolhido para implantação oficial no Exército Brasileiro',
            'Apresentação direta para General, Coronel e Tenentes da guarnição',
            'Recebimento de medalha de honra da unidade como reconhecimento',
            'Interfaces web e mobile integradas',
        ],
    },
    {
        'titulo': 'Projeto API 6DSM — Atlas (Visiona, primeiro semestre de 2026)',
        'ano': '2026',
        'semestre': '6º DSM',
        'papel': 'Full Stack',
        'descricao': 'Sistema desenvolvido para a empresa Visiona — Atlas é um chatbot com Processamento de Linguagem Natural (PLN) que atende em linguagem humana e está conectado a dados geoespaciais oficiais. Para qualquer pergunta sobre queimadas, desmatamento, áreas rurais e outros indicadores territoriais, o chat retorna o mapa do estado de São Paulo com todas as informações relevantes — áreas delimitadas por polígonos, ID de cada região e o registro completo dos sites oficiais geoespaciais. O sistema também se integra ao QGIS, fornecendo dados estruturados para consulta e análise por especialistas. O Atlas combina LLMs, busca semântica via embeddings (pgvector) e dados espaciais (PostGIS / GeoServer) numa única interface conversacional.',
        'tecnologias': 'Tecnologias utilizadas:',
        'tecno': 'Python, FastAPI, SQLAlchemy, Alembic, Pydantic, PostgreSQL, PostGIS, pgvector, GeoServer, QGIS, React',
        'contribuicao': 'Contribuições pessoais',
        'cont': 'Atuo como desenvolvedor Full Stack no projeto, contribuindo na arquitetura do backend em Python/FastAPI, modelagem do banco com SQLAlchemy + Alembic, integração com PostGIS e pgvector para busca espacial e semântica, configuração do GeoServer para servir camadas geoespaciais e construção da interface conversacional em React. Trabalho também na ingestão e tratamento dos dados oficiais de fontes geoespaciais, garantindo consistência entre o que o chat responde e o que o mapa exibe.',
        'hard': 'Hard Skills Efetivamente desenvolvidas:',
        'hardD': 'Python, FastAPI, SQLAlchemy, Alembic, Pydantic, PostgreSQL, PostGIS, pgvector, GeoServer, QGIS, React, PLN, LLMs, Embeddings, GIS',
        'soft': 'Soft Skills Efetivamente desenvolvidas:',
        'so': 'Pensamento sistêmico e aprendizado contínuo. Trabalhar com dados geoespaciais e LLMs simultaneamente exige a capacidade de transitar entre domínios distintos (GIS, IA, engenharia de dados, frontend) e manter a visão do todo. A interlocução com a Visiona — empresa especializada no setor espacial — exigiu rigor técnico, comunicação precisa e disciplina para manter o ritmo de entrega.',
        'imagem': 'atlas.png',
        'galeria': ['atlas.png'],
        'destaques': [
            'Chatbot com PLN integrado a dados geoespaciais oficiais',
            'Mapa do estado de SP com polígonos, IDs e registros completos',
            'Integração com QGIS para análise por especialistas',
            'Stack moderno: FastAPI + PostGIS + pgvector + GeoServer + React',
        ],
    },
]

# Áreas de Atuação
areas_atuacao = [
    {
        'titulo': 'Power Platform &amp; Low-code',
        'descricao': 'Atuação profissional na ProNext desenvolvendo apps em Power Platform — Power Apps, Power Automate e integrações. Apps em produção em clientes corporativos, com um deles premiado pelo hall global do cliente por eficiência de processo.',
        'tecnologias': ['Power Apps', 'Power Automate', 'Dataverse', 'SharePoint', 'C#', 'Azure'],
        'icone': 'product',
    },
    {
        'titulo': 'Desenvolvimento Full Stack Web',
        'descricao': 'Projeto e construção de aplicações web completas, do banco de dados à interface do usuário. Foco em arquitetura escalável, código limpo e experiência consistente. Atualmente trabalhando com FastAPI + React + PostGIS no projeto Atlas (Visiona).',
        'tecnologias': ['React', 'Vue.js', 'Node.js', 'Python', 'FastAPI', 'Flask', 'Java', 'Spring', 'PostgreSQL'],
        'icone': 'fullstack',
    },
    {
        'titulo': 'IA &amp; PLN',
        'descricao': 'Desenvolvimento de soluções com inteligência artificial — desde protótipos até projetos em produção. Integração com LLMs, busca semântica via embeddings (pgvector) e chatbots conversacionais com PLN.',
        'tecnologias': ['LLMs', 'PLN', 'pgvector', 'Embeddings', 'Python', 'FastAPI'],
        'icone': 'ai',
    },
    {
        'titulo': 'Front-end &amp; Interfaces',
        'descricao': 'Construção de interfaces responsivas, acessíveis e com performance. Atenção a UX/UI, animações e usabilidade em diferentes dispositivos.',
        'tecnologias': ['HTML5', 'CSS3', 'JavaScript', 'TypeScript', 'React', 'Vue.js'],
        'icone': 'frontend',
    },
    {
        'titulo': 'Back-end &amp; APIs',
        'descricao': 'Desenvolvimento de APIs REST, autenticação, segurança e regras de negócio. Modelagem de dados e integração com serviços externos.',
        'tecnologias': ['Node.js', 'Python', 'Flask', 'Java', 'Spring', 'JWT', 'REST'],
        'icone': 'backend',
    },
    {
        'titulo': 'Banco de Dados',
        'descricao': 'Modelagem relacional, escrita de queries otimizadas e garantia de integridade. Experiência com bancos transacionais em projetos reais.',
        'tecnologias': ['PostgreSQL', 'MySQL', 'SQL'],
        'icone': 'database',
    },
    {
        'titulo': 'Mobile Multiplataforma',
        'descricao': 'Construção de aplicativos com Flutter, com foco em UI nativa, integração com APIs e fluxo de dados consistente entre Android e iOS.',
        'tecnologias': ['Flutter', 'Dart'],
        'icone': 'mobile',
    },
    {
        'titulo': 'Gestão de Produto &amp; Agile',
        'descricao': 'Atuação como Product Owner, com levantamento de requisitos, priorização de backlog, user stories e validação com stakeholders. Metodologias ágeis na prática.',
        'tecnologias': ['Scrum', 'Kanban', 'User Stories', 'Backlog'],
        'icone': 'product',
    },
]

# Stack tecnológico (autoavaliação)
stack = [
    {'categoria': 'Linguagens', 'itens': ['JavaScript', 'TypeScript', 'Python', 'Java', 'Dart', 'SQL']},
    {'categoria': 'Front-end', 'itens': ['React', 'Vue.js', 'HTML5', 'CSS3']},
    {'categoria': 'Back-end', 'itens': ['Node.js', 'Flask', 'Spring']},
    {'categoria': 'Banco de Dados', 'itens': ['PostgreSQL', 'MySQL']},
    {'categoria': 'DevOps &amp; Tools', 'itens': ['Git', 'Docker', 'AWS', 'Linux', 'Vercel']},
    {'categoria': 'Mobile', 'itens': ['Flutter']},
    {'categoria': 'Práticas', 'itens': ['Scrum', 'Code Review', 'REST APIs']},
]

# Soft skills
soft_skills = [
    'Liderança', 'Comunicação clara', 'Visão estratégica',
    'Trabalho em equipe', 'Negociação', 'Resolução de problemas',
    'Pensamento crítico', 'Gestão de tempo', 'Adaptação',
    'Empatia', 'Atenção a detalhes', 'Aprendizado contínuo',
]

# Trajetória / Timeline
trajetoria = [
    {'periodo': '2023 · 2º semestre', 'titulo': '1º DSM — Primeiros passos com Python &amp; Flask',
     'descricao': 'Plataforma de informações sobre hospitais pediátricos com chat em tempo real. Fundamentos de backend, banco de dados e DevOps com Docker e AWS.'},
    {'periodo': '2024 · 1º semestre', 'titulo': '2º DSM — Full Stack com Node.js + React',
     'descricao': 'Sistema de tickets e atendimento em tempo real. Aprofundei o ecossistema JavaScript, autenticação, autorização e responsividade.'},
    {'periodo': '2024 · 2º semestre', 'titulo': '3º DSM — Java, Spring &amp; segurança',
     'descricao': 'Portal de transparência para a AFAPG, com Spring no backend, JWT para autenticação e React no front. Foco em segurança e dados sensíveis.'},
    {'periodo': '2025 · 1º semestre', 'titulo': '4º DSM — IoT &amp; visualização de dados',
     'descricao': 'Plataforma de estações meteorológicas para a Tecsus. Sensores IoT, APIs RESTful em Node.js + TypeScript e dashboards em React.'},
    {'periodo': '2025 · 2º semestre', 'titulo': '5º DSM — Product Owner',
     'descricao': 'App de gestão administrativa para a Guarnição de Caçapava. Liderança de backlog, requisitos, stakeholders e entregas.'},
    {'periodo': '2026 · 1º semestre', 'titulo': '6º DSM — Hoje',
     'descricao': 'Foco em arquitetura, performance e qualidade de software. Aplicando boas práticas de engenharia em projetos pessoais e acadêmicos.'},
]


# =====================================================
# Rotas
# =====================================================

@app.route('/')
def apresentacao():
    return render_template(
        'apresentacao.html',
        perfil=perfil,
        experiencia=experiencia,
        stack=stack,
        soft_skills=soft_skills,
        trajetoria=trajetoria,
    )

@app.route('/projetos')
def projetos():
    return render_template('projetos.html', trabalhos=trabalhos, perfil=perfil)

@app.route('/atuacao')
def atuacao():
    return render_template('atuacao.html', areas=areas_atuacao, perfil=perfil)

# Aliases para compatibilidade com rotas antigas
@app.route('/sobremim')
def sobremim_redirect():
    return apresentacao()

@app.route('/trabalhos')
def trabalhos_redirect():
    return projetos()


if __name__ == '__main__':
    app.run(debug=True)
