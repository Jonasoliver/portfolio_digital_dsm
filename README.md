# Portfólio Digital — Jonas Miguel Oliveira

**Curso:** Desenvolvimento de Software Multiplataforma (DSM)
**Instituição:** Fatec Jessen Vidal — São José dos Campos
**Semestre atual:** 6º DSM (2026/01)

<p align="center">
  <img src="./assets/img/perfil.png" width="auto" height="250" alt="Jonas Miguel">
</p>

Portfólio acadêmico-profissional que reúne minha apresentação pessoal, experiência na ProNext,
projetos API desenvolvidos ao longo dos seis semestres do curso de DSM e as áreas em que atuo.

## Estrutura (3 seções, conforme orientação do professor)

1. **Apresentação Pessoal** — `index.html` — quem sou, foto profissional, stack, experiência ProNext, jornada DSM e soft skills.
2. **Projetos API** — `projetos.html` — todos os projetos das Atividades Práticas Integradoras (1º ao 6º semestre).
3. **Áreas de Atuação** — `atuacao.html` — áreas em que atuo profissionalmente e canais de contato.

## Tecnologias (100% client-side)

- **HTML5** — estrutura semântica
- **CSS3** — design system completo (variáveis, grid, animações, glassmorphism)
- **JavaScript vanilla** — cursor custom, partículas, scroll reveal, contadores, lightbox, filtros
- **Fontes self-hosted** — Inter, Space Grotesk, JetBrains Mono em `assets/fonts/`
- **Imagens estáticas** (PNG/JPG) em `assets/img/`

**Sem CDN externo. Sem backend. Sem build step.** Pode abrir direto no navegador.

## Conformidade com requisitos do professor

✅ Máximo 3 seções (Apresentação, Projetos, Atuação)
✅ Foto profissional na apresentação pessoal (MVP Conf)
✅ Inclusão obrigatória dos projetos API (1º ao 6º semestre)
✅ Processamento totalmente client-side (HTML5, CSS3, JS, PNG)
✅ Bibliotecas estáticas instaladas no repositório (`assets/fonts/`, `assets/css/`, `assets/js/`)
✅ Dados estáticos no próprio repositório (inline em cada HTML)
✅ Sem dependências externas (zero CDN)

## Estrutura de pastas

```
portfolio_digital_dsm/
├── index.html              1ª seção — Apresentação Pessoal
├── projetos.html           2ª seção — Projetos API
├── atuacao.html            3ª seção — Áreas de Atuação + Contato
├── assets/
│   ├── css/style.css       Design system
│   ├── js/main.js          Interatividade (cursor, partículas, animações)
│   ├── fonts/*.woff2       Fontes self-hosted
│   └── img/*.png|*.jpg     Imagens estáticas
├── mgt/
│   └── FIGMA.pdf           Mockup original
└── README.md
```

## Como rodar localmente

Por ser 100% estático, basta abrir o `index.html` no navegador. Para evitar restrições de
`file://` em alguns navegadores, recomenda-se servir com um servidor estático qualquer:

```powershell
# Python (já instalado no Windows)
python -m http.server 8000

# Ou via VS Code: extensão "Live Server"
```

Acesse `http://localhost:8000`.

## Deploy

Compatível com qualquer serviço de hospedagem estática:

- **GitHub Pages** (recomendado pelo professor) — push para o repositório institucional
- **Vercel / Netlify** — drag-and-drop da pasta
- **Cloudflare Pages** — conexão direta com o repositório

## Contato

- **Email:** jonaasmigueldeoliveira@gmail.com
- **LinkedIn:** [jonas-miguel-ol](https://www.linkedin.com/in/jonas-miguel-ol/)
- **GitHub:** [Jonasoliver](https://github.com/Jonasoliver)
