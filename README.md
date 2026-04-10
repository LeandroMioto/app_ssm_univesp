# 🚀 Sistema de Gestão SSM (Sítio São Marcos) - Univesp

Este projeto é um Mini-ERP desenvolvido para a gestão operacional e financeira do Sítio São Marcos. O sistema centraliza o controle de pecuária, produção de café e fluxo de caixa em uma interface web dinâmica e responsiva.

---

## 📊 Dashboard e Interface
O sistema conta com um **Dashboard Principal** que utiliza cards informativos para exibição de métricas em tempo real:
* **Cards de Resumo:** Visualização rápida de saldo em caixa, total de despesas, total de sacas de café e cabeças de gado.
* **Interface Responsiva:** Desenvolvida com Bootstrap para garantir usabilidade em desktops e dispositivos móveis.
* **Navegação Dinâmica:** Módulos de Pecuária, Café, Financeiro e Pessoal integrados.

---

## 🛠️ Stack Tecnológica

* **Linguagem:** Python 3.10+
* **Web Framework:** Flask
* **Banco de Dados:** SQLite3 (Persistência no arquivo banco.db)
* **Geração de Relatórios:**
    * **Excel:** Pandas e Openpyxl (Exportação de dados para auditoria em CSV/XLSX)
    * **PDF:** FPDF / ReportLab (Emissão de recibos e folhas de rosto)
* **Front-end:** HTML5, CSS3, Bootstrap 5 e Jinja2 Templates

---

## 📋 Módulos do Sistema

1. **Dashboard de Indicadores:** Painel com cards de métricas financeiras e de produção.
2. **Módulo Pecuária:** Gestão de manejo (nascimentos, mortes), compras e vendas de gado.
3. **Módulo Café:** Controle de colheita, beneficiamento e movimentação de estoque.
4. **Gestão Financeira:** Lançamento de despesas, controle de salários/vales e fluxo bancário.
5. **Segurança e Auditoria:** Sistema de logs que registra todas as alterações feitas pelos usuários.

---

## ⚙️ Instalação e Execução

Para rodar o projeto localmente, siga estes passos no seu terminal:

### 1. Preparar o Ambiente
Certifique-se de ter o Python instalado e configurado no seu PATH.

### 2. Instalar Dependências
Execute o comando para instalar as bibliotecas necessárias:
pip install flask pandas openpyxl fpdf

### 3. Banco de Dados
O arquivo banco.db já contém a estrutura de tabelas. Scripts auxiliares:
* setup_banco.py: Inicialização do esquema.
* ajustar_banco.py: Migrações e correções de campos.

### 4. Iniciar a Aplicação
Comando para rodar:
python app.py

Acesse em: http://127.0.0.1:5000

---

## 🔐 Níveis de Acesso (RBAC)
O controle de permissões é baseado na tabela pessoal:
* **Super Admin:** Acesso irrestrito a configurações, usuários e logs de auditoria.
* **Admin:** Acesso total aos módulos operacionais e financeiros.
* **Comum:** Permissão restrita a consultas e lançamentos básicos.

---

## 👥 Equipe de Desenvolvimento (Univesp)
* **Leandro Mioto** - Lead Developer
* **Mayza** - Coordenadora do projeto
* 
*
* 
*
*
*
---
*Dúvidas ou problemas na execução? Entre em contato com o Leandro via grupo do projeto.*
