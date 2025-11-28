from flask import Flask, render_template

app = Flask(__name__)

# Lista de trabalhos
trabalhos = [
    {
        'titulo': 'Projeto API 1DSM segundo semestre de 2023',
        'descricao': 'A aplicação foi desenvolvida para fornecer informações sobre hospitais no Brasil que atendem crianças com problemas renais crônicos. Ela permite que os usuários consultem dados como nome, endereço, telefone e especialidades de cada hospital, além de filtrar por localização e especialização. A plataforma também inclui um fórum de discussões, com chat ao vivo e a possibilidade de envio de imagens com comentários, facilitando a troca de informações entre pacientes, familiares e profissionais de saúde. Para garantir a segurança, há moderação de conteúdo e controles de privacidade, além de autenticação para acesso às funcionalidades. Com design responsivo, a aplicação visa fornecer informações úteis e promover um espaço de apoio e interação para quem enfrenta desafios relacionados à saúde renal infantil. Além disso, o desenvolvimento dessa aplicação proporcionou uma oportunidade única de explorar práticas avançadas e comunicação em tempo real, o que contribuiu significativamente para o aprofundamento em tecnologias de sistemas interativos e seguros.',
        'tecnologias': 'Tecnologias utilizadas:',
        'tecno': 'Python, Flask, Docker, AWS, MySQL, JavaScript',
        'contribuicao': 'Contribuições pessoais',
        'cont': 'No desenvolvimento deste projeto, uma das contribuições mais significativas foi focar na otimização de processos e no equilíbrio das cargas de trabalho para garantir a melhor performance da aplicação, mesmo com requisitos de hardware limitados. Ao longo do desenvolvimento, busquei melhorar continuamente a estrutura de codificação e a integração dos diversos módulos, visando garantir uma comunicação eficiente e escalável, crucial para o bom funcionamento das funcionalidades em tempo real, como o chat e o envio de imagens. A implementação prática dessa aplicação demonstrou que, ao consolidar uma infraestrutura robusta e otimizada, conseguimos não apenas melhorar a experiência do usuário, mas também garantir a disponibilidade e a integridade dos dados, especialmente em um ambiente tão dinâmico e interativo. Além disso, com o aumento da complexidade da aplicação e a necessidade de lidar com grandes volumes de dados, foi essencial revisar e aprimorar os paralelismos nas operações de backend, como a busca e a visualização dos hospitais e o gerenciamento das interações no fórum. Isso levou a um refinamento no gerenciamento de recursos, assegurando que a plataforma se mantivesse eficiente mesmo sob uma maior carga de dados e usuários simultâneos. Por fim, a implementação de ferramentas OpenSource se mostrou uma estratégia de longo prazo viável, pois possibilitou maior flexibilidade e controle sobre a aplicação, além de facilitar futuros desenvolvimentos e melhorias contínuas no sistema.',
        'hard': 'Hard Skills Efetivamente desenvolvidas:',
        'hardD':'Python, CSS, HTML, JavaScript, Docker, MySQL, Flask',
        'soft': 'Soft Skills Efetivamente desenvolvidas:',
        'so': 'Autonomia e adaptação. O processo de otimizar a infraestrutura e garantir a disponibilidade da plataforma em diferentes cenários demandou uma grande capacidade de adaptação e tomada de decisões de forma independente, especialmente quando os requisitos de performance eram desafiadores. Contudo, ao longo do projeto, enfrentei desafios inesperados, como a necessidade de realizar ajustes rápidos em tempo real para otimizar o chat e o envio de imagens. Essa situação exigiu muito mais da minha capacidade de lidar com pressão e da habilidade de tomar decisões rápidas, além de manter uma comunicação clara com a equipe para que as soluções fossem implementadas de forma coordenada. Esse imprevisto me forçou a desenvolver ainda mais a minha resiliência e paciência diante de imprevistos, algo que não estava inicialmente planejado.',
        'imagem': '../static/api.jpeg'
    },

    {
        'titulo': 'Projeto API 2DSM primeiro semestre de 2024',
        'descricao': 'O projeto API 2DSM foi desenvolvido com o objetivo de criar uma plataforma de atendimento ao cliente, focada em um sistema de gestão de tickets e chat em tempo real. Utilizando React no frontend, a aplicação oferece três tipos de acesso: Cliente, Atendente e Administrador. A interface foi construída para ser intuitiva e responsiva, utilizando HTML, CSS e Bootstrap, garantindo uma experiência fluida e adaptável a diferentes dispositivos. No backend, o sistema foi implementado com Node.js, garantindo a manipulação eficiente de requisições e comunicação com o banco de dados MySQL. A plataforma permite a criação e gestão de tickets, onde os atendentes podem auxiliar os clientes com seus problemas relacionados a produtos e serviços. A comunicação em tempo real, através do chat, proporciona uma interação direta e ágil entre usuários e atendentes, otimizando o atendimento. A aplicação também conta com uma estrutura robusta de autenticação e controle de acesso, assegurando que cada usuário tenha a experiência adequada conforme seu perfil. O desenvolvimento deste projeto proporcionou uma imersão no aprimoramento de habilidades em full-stack, integração de sistemas interativos e construção de interfaces altamente responsivas.',
        'tecnologias': 'Tecnologias utilizadas:',
        'tecno': 'Node.js, React, HTML, CSS, MySQL, JavaScript, Bootstrap',
        'contribuicao': 'Contribuições pessoais',
        'cont': 'No desenvolvimento deste projeto, concentrei meus esforços em criar uma experiência de usuário fluida e eficiente, utilizando React para garantir uma interface interativa e com desempenho otimizado. Trabalhei na implementação do sistema de tickets e chat, essenciais para a comunicação eficaz entre clientes e atendentes. A escolha de Node.js para o backend foi crucial para garantir respostas rápidas e escaláveis, além de integrar de forma eficaz o banco de dados MySQL para gerenciar usuários e tickets de maneira organizada. No front-end, usei Bootstrap para garantir que a interface fosse responsiva e adaptável, melhorando a experiência em dispositivos móveis e desktops. A implementação de controles de acesso e segurança foi outra área em que me envolvi, utilizando autenticação e autorização para garantir que o sistema fosse seguro e que os dados dos usuários fossem protegidos. Este projeto me permitiu expandir meus conhecimentos em desenvolvimento full-stack, além de proporcionar uma maior compreensão sobre as práticas de otimização de sistemas interativos e comunicação em tempo real.',
        'hard': 'Hard Skills Efetivamente desenvolvidas:',
        'hardD': 'Node.js, React, HTML, CSS, JavaScript, MySQL, Bootstrap',
        'soft': 'Soft Skills Efetivamente desenvolvidas:',
        'so': 'Trabalho em equipe e gestão de tempo. Durante o desenvolvimento, fui capaz de colaborar eficientemente com outros membros da equipe, mantendo o foco nas prioridades e gerenciando o tempo de maneira eficaz para cumprir os prazos de entrega da aplicação. No entanto, houve um momento em que enfrentamos problemas com a sincronização de dados no sistema de tickets, o que exigiu uma comunicação intensa entre os membros da equipe e a habilidade de negociar e ouvir as diferentes opiniões. Esse desafio me ajudou a desenvolver habilidades em resolução de conflitos e negociação, que inicialmente não estavam previstas no escopo do projeto.',
        'imagem': '../static/Api2024.png'
    },

    {
        'titulo': 'Projeto API 3DSM segundo semestre de 2024',
        'descricao': 'O Projeto API 3DSM foi desenvolvido para o cliente AFAPG com o objetivo de criar um portal de transparência, onde são exibidos detalhadamente os gastos realizados com doações empresariais em projetos sociais. Utilizando o framework Spring no backend com Java, a aplicação oferece segurança e escalabilidade para o gerenciamento dos dados. A plataforma foi projetada para garantir que todas as informações financeiras sejam acessíveis ao público de forma clara e transparente, permitindo que os usuários visualizem os projetos realizados, os valores recebidos e como os recursos foram aplicados. A interface foi construída com React, garantindo uma experiência interativa e fluída, enquanto o banco de dados MySQL armazena as informações de maneira estruturada e segura. A autenticação é feita via JWT (JSON Web Token), garantindo que apenas usuários autorizados tenham acesso a funcionalidades específicas, como o gerenciamento de dados financeiros e projetos. A aplicação também foi desenvolvida com foco na segurança e privacidade dos dados, assegurando que informações sensíveis sejam protegidas durante todo o processo de navegação e interação.',
        'tecnologias': 'Tecnologias utilizadas:',
        'tecno': 'Java, Spring, React, MySQL, JWT',
        'contribuicao': 'Contribuições pessoais',
        'cont': 'Durante o desenvolvimento deste projeto, meu foco esteve na criação de uma aplicação escalável e segura, garantindo que as informações sobre os projetos e gastos fossem acessíveis ao público e bem organizadas. Trabalhei na implementação do backend com Java e Spring, criando uma estrutura robusta para o gerenciamento e exposição de dados financeiros de forma eficiente e segura. A integração com o banco de dados MySQL foi crucial para armazenar as informações de forma estruturada, enquanto a utilização de JWT para autenticação garantiu que apenas usuários com as permissões adequadas pudessem acessar dados sensíveis. No frontend, utilizei React para construir uma interface interativa e responsiva, proporcionando uma boa experiência de navegação. Este projeto me permitiu aprofundar meus conhecimentos em segurança de aplicações, desenvolvimento de APIs seguras e otimização de performance em sistemas que lidam com grandes volumes de dados. A experiência com Spring e JWT foi fundamental para aprimorar minha habilidade no desenvolvimento de sistemas corporativos e seguros.',
        'hard': 'Hard Skills Efetivamente desenvolvidas:',
        'hardD': 'Java, Spring, React, MySQL, JWT',
        'soft': 'Soft Skills Efetivamente desenvolvidas:',
        'so': 'Responsabilidade e foco em resultados. A criação de um portal de transparência exigiu uma grande atenção aos detalhes e a capacidade de assumir responsabilidades para garantir que as informações fossem apresentadas de forma clara, precisa e segura. No entanto, ao lidar com dados sensíveis e interações com o cliente, enfrentamos desafios inesperados relacionados à privacidade e segurança das informações. Isso me obrigou a desenvolver habilidades de comunicação assertiva, tanto para explicar o que poderia ser feito dentro dos limites de segurança quanto para negociar com a equipe sobre quais dados poderiam ser expostos ou não. Essa experiência de negociação de segurança de dados, embora não planejada, foi fundamental para meu desenvolvimento profissional.',
        'imagem': '../static/projeto3dsm.png'
    },

    {
        'titulo': 'Projeto API 4DSM primeiro semestre de 2025',
        'descricao': 'Desenvolvido por alunos do 4º semestre de Desenvolvimento de Software Multiplataforma para o API, este projeto visa a coleta e processamento de dados de Estações Meteorológicas. O sistema permite inserção e busca de dados, além da exibição de estatísticas em gráficos interativos. A iniciativa atende à demanda da Tecsus para o monitoramento ambiental, utilizando sensores de baixo custo para medir vento, chuva, umidade, temperatura e pressão. Os dados são transmitidos para um servidor e exibidos em um portal com dashboards e relatórios, promovendo também a aprendizagem baseada em problemas.',
        'tecnologias': 'Tecnologias utilizadas:',
        'tecno': 'React, Node.js, TypeScript, PostgreSQL, Docker, IoT',
        'contribuicao': 'Contribuições pessoais',
        'cont': 'Durante o desenvolvimento deste projeto, contribuí significativamente para a arquitetura do sistema de coleta e processamento de dados meteorológicos. Trabalhei na integração dos sensores IoT com o backend, garantindo a transmissão confiável e em tempo real dos dados coletados. Implementei APIs RESTful para gerenciar a inserção e recuperação de dados, além de desenvolver dashboards interativos utilizando React e bibliotecas de visualização de dados. A utilização de TypeScript permitiu maior segurança no desenvolvimento, enquanto o Docker facilitou a implantação e escalabilidade do sistema. Este projeto ampliou minha experiência em IoT, processamento de dados em tempo real e desenvolvimento de interfaces para visualização de grandes volumes de informações.',
        'hard': 'Hard Skills Efetivamente desenvolvidas:',
        'hardD': 'React, Node.js, TypeScript, PostgreSQL, Docker, IoT, APIs RESTful, Data Visualization',
        'soft': 'Soft Skills Efetivamente desenvolvidas:',
        'so': 'Trabalho em equipe e resolução de problemas. O projeto exigiu colaboração estreita entre diferentes áreas (hardware, backend, frontend), desenvolvendo habilidades de comunicação técnica e coordenação de esforços. A natureza prática do monitoramento ambiental trouxe desafios inesperados relacionados à confiabilidade dos sensores e tratamento de dados inconsistentes, o que me forçou a desenvolver pensamento crítico e adaptabilidade para encontrar soluções criativas em tempo hábil. A experiência de trabalhar com um cliente real (Tecsus) também aprimorou minhas habilidades de gestão de expectativas e apresentação de resultados.',
        'imagem': '../static/tecsus.png'
    },

    {
        'titulo': 'Projeto API 5DSM segundo semestre de 2025',
        'descricao': 'Aplicativo de Gestão Administrativa desenvolvido para a Guarnição de Caçapava. Projeto acadêmico realizado por alunos do 5º semestre de DSM com o objetivo de digitalizar e automatizar a gestão de almoxarifado, substituindo controles manuais e descentralizados que dificultam o rastreamento de itens e impactam a eficiência operacional. A solução oferece controle em tempo real de estoque, histórico de movimentações, gestão de requisições e relatórios gerenciais, promovendo maior transparência e eficiência nos processos administrativos da guarnição.',
        'tecnologias': 'Tecnologias utilizadas:',
        'tecno': 'Flutter, Dart, Vue.js, PostgreSQL, Java, Python, Git',
        'contribuicao': 'Product Owner',
        'cont': 'Como Product Owner deste projeto, minha principal responsabilidade foi garantir o alinhamento entre as necessidades da Guarnição de Caçapava e a solução desenvolvida pela equipe. Conduzi o levantamento de requisitos junto aos stakeholders, priorizei o backlog do produto e defini as funcionalidades essenciais para cada sprint. Trabalhei na elaboração de user stories detalhadas, critérios de aceitação e validação das entregas. Facilitei a comunicação entre a equipe de desenvolvimento e o cliente, garantindo que as expectativas fossem gerenciadas adequadamente e que o produto final atendesse às demandas operacionais. A experiência me permitiu desenvolver visão estratégica de produto, habilidades de negociação e capacidade de tomar decisões que equilibram viabilidade técnica com valor de negócio.',
        'hard': 'Hard Skills Efetivamente desenvolvidas:',
        'hardD': 'Gestão de Produto, Metodologias Ágeis, Scrum, Levantamento de Requisitos, Priorização de Backlog, User Stories, Flutter, Vue.js, PostgreSQL',
        'soft': 'Soft Skills Efetivamente desenvolvidas:',
        'so': 'Liderança e visão estratégica. Como Product Owner, desenvolvi fortemente a capacidade de liderar sem autoridade formal, influenciando a equipe através da visão clara do produto e da comunicação efetiva. A gestão de stakeholders exigiu habilidades avançadas de negociação, especialmente ao balancear expectativas do cliente com limitações técnicas e de tempo. Enfrentei desafios relacionados à mudança de prioridades e à necessidade de tomar decisões difíceis sobre escopo, o que aprimorou minha capacidade de pensamento crítico e tomada de decisão sob pressão. A experiência de traduzir necessidades militares complexas em funcionalidades de software também desenvolveu minha empatia e capacidade de compreender contextos organizacionais diferentes.',
        'imagem': '../static/guarnicao.png'
    },
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/trabalhos')
def mostrar_trabalhos():
    return render_template('trabalhos.html', trabalhos=trabalhos)

@app.route('/sobremim')
def sobre_mim():
    return render_template('sobremim.html')

if __name__ == '__main__':
    app.run(debug=True)
