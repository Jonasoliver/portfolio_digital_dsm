# Portfólio Digital — Jonas Miguel Oliveira

**Curso:** Desenvolvimento de Software Multiplataforma (DSM)
**Instituição:** Fatec Jessen Vidal — São José dos Campos
**Semestre atual:** 6º DSM (2026/01)

<p align="center">
  <img src="./api/static/eu.jpg" width="auto" height="250" alt="Jonas Miguel">
</p>

Portfólio acadêmico-profissional que reúne minha apresentação pessoal, projetos API
desenvolvidos ao longo dos seis semestres do curso de DSM e as áreas em que atuo.

## Estrutura do portfólio (3 seções)

Conforme orientações do professor (máximo 3 seções):

1. **Apresentação Pessoal** (`/`) — quem sou, foto profissional, stack, jornada e soft skills.
2. **Projetos API** (`/projetos`) — todos os projetos das Atividades Práticas Integradoras (1º ao 6º semestre).
3. **Áreas de Atuação** (`/atuacao`) — áreas em que atuo profissionalmente e canais de contato.

## Tecnologias

- **Backend:** Python + Flask (renderização de templates Jinja com dados estáticos)
- **Frontend:** HTML5, CSS3, JavaScript vanilla
- **Fontes:** Inter, Space Grotesk, JetBrains Mono (self-hosted em `api/static/fonts/`)
- **Sem CDN externo** — todas as dependências armazenadas no repositório

## Como executar localmente

```powershell
# 1. Criar e ativar ambiente virtual
python -m venv venv
.\venv\Scripts\activate

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Rodar o servidor
cd api
python app.py
```

Acesse em `http://localhost:5000`.

## Estrutura de pastas

```
portfolio_digital_dsm/
├── api/
│   ├── app.py                  Flask + dados estáticos
│   ├── static/
│   │   ├── style.css           Design system (sem CDN)
│   │   ├── fonts/              Fontes self-hosted (woff2)
│   │   └── *.png / *.jpg       Imagens dos projetos e perfil
│   └── templates/
│       ├── base.html           Layout (navbar, footer, cursor, partículas)
│       ├── apresentacao.html   1ª seção — Apresentação Pessoal
│       ├── projetos.html       2ª seção — Projetos API
│       └── atuacao.html        3ª seção — Áreas de Atuação + Contato
├── mgt/
│   └── FIGMA.pdf               Mockup original
├── requirements.txt
├── vercel.json                 Deploy Vercel
└── README.md
```

## Conformidade com requisitos do professor

- ✅ Máximo 3 seções (Apresentação, Projetos, Atuação)
- ✅ Foto profissional na apresentação pessoal
- ✅ Inclusão dos projetos API (1º ao 6º semestre)
- ✅ Dependências armazenadas localmente no repositório (fontes WOFF2 self-hosted)
- ✅ Dados estáticos no próprio repositório (lista Python no `app.py`)
- ✅ Sem links externos para CDN

## Contato

- **Email:** jonaasmigueldeoliveira@gmail.com
- **LinkedIn:** [jonas-miguel-ol](https://www.linkedin.com/in/jonas-miguel-ol/)
- **GitHub:** [Jonasoliver](https://github.com/Jonasoliver)
