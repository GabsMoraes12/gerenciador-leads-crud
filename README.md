# Gerenciador de Leads de Marketing (Sistema CRUD Completo)

Este projeto marca a minha transição para o desenvolvimento de sistemas dinâmicos integrados a Bancos de Dados (desenvolvimento Back-End e Full-Stack). Trata-se de uma aplicação web robusta no padrão **CRUD** desenvolvida para capturar, armazenar, listar e excluir informações de potenciais clientes (*Leads*) focada em operações digitais e inteligência de marketing.

---

## Tecnologias e Arquitetura

* **Python & Flask:** Framework minimalista e potente utilizado para gerenciar as rotas do servidor, processar requisições HTTP e intermediar a comunicação com o banco.
* **SQLite:** Banco de dados relacional leve e embutido, configurado para persistência de dados em tempo real.
* **HTML5 & CSS3:** Interface responsiva e limpa criada para simular um dashboard administrativo interno de agência.
* **Jinja2:** Motor de renderização do Flask utilizado para injetar dinamicamente os dados do banco dentro do código HTML.

---

## Operações CRUD Implementadas

O sistema executa de forma nativa as quatro operações essenciais da Engenharia de Software:
1. **Create (Criar):** Através do formulário, novos leads são validados e inseridos via comando SQL `INSERT INTO` no banco.
2. **Read (Ler):** O servidor realiza a consulta `SELECT * FROM leads` e renderiza a lista atualizada em tela de forma decrescente (leads mais novos primeiro).
3. **Update (Atualizar):** Estrutura modular preparada para futuras atualizações de dados.
4. **Delete (Excluir):** Remove registros indesejados diretamente do banco de dados através da rota ativa de exclusão com comando `DELETE WHERE id`.

---

## Contexto de Engenharia e Negócios

Diferente de scripts isolados, este projeto simula a infraestrutura real de um sistema corporativo. Ele consolida os conceitos fundamentais aprendidos na graduação de **Ciência da Computação** (modelagem de banco de dados, persistência de arquivos, arquitetura cliente-servidor) aplicados a uma dor latente do mercado de **Marketing Digital** e vendas.
