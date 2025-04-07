# Sistema de Gestão de Contratos - Unimed Vilhena

Bem-vindo ao repositório do Sistema de Gestão de Contratos desenvolvido para a Unimed Vilhena. Este sistema foi construído para facilitar a gestão de contratos, controle de dados e autenticação de usuários.

---

## **Índice**
- [Sobre o Projeto](#sobre-o-projeto)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Requisitos do Sistema](#requisitos-do-sistema)
- [Instalação](#instalação)
- [Estrutura de Pastas](#estrutura-de-pastas)
- [Funcionalidades](#funcionalidades)
- [Screenshots](#screenshots)
- [Contribuindo](#contribuindo)
- [Licença](#licença)

---

## **Sobre o Projeto**

O Sistema de Gestão de Contratos foi desenvolvido utilizando o framework Django. Ele oferece funcionalidades como:
- Gerenciamento e visualização de contratos.
- Login com autenticação de usuários.
- Busca dinâmica com filtros.
- Tela de login personalizada.

---

## **Tecnologias Utilizadas**

As tecnologias e bibliotecas utilizadas neste projeto incluem:
- **Sistema Operacional:** Debian 11
- **Linguagem de Programação:** Python 3.9
- **Framework:** Django 4.2
- **Banco de Dados:** SQLite3 (pode ser alterado para PostgreSQL)
- **Frontend:** Bootstrap 5, HTML5, CSS3
- **Outras Bibliotecas:**
  - `django-crispy-forms` (para estilizar formulários)
  - `Pillow` (para manipulação de imagens estáticas)

---

## **Requisitos do Sistema**

Antes de instalar o sistema, certifique-se de ter os seguintes requisitos:
- Debian 11 instalado.
- Python 3.9 ou superior.
- Gerenciador de pacotes `pip`.
- Git instalado.

---

## **Instalação**

Siga os passos abaixo para configurar o sistema:

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```
### 2. Crie e ative um ambiente virtual
```bash
python3 -m venv venv
source venv/bin/activate
```
3. Instale as dependências
```bash
pip install -r requirements.txt
```
### 4. Configure o banco de dados
```bash
python manage.py makemigrations
python manage.py migrate
```
### 5. Crie um superusuário (opcional)
```bash
python manage.py createsuperuser
```
### 6. Execute o servidor
```bash
python manage.py runserver
```
Acesse o sistema em: http://localhost:8000

### Estrutura de Pastas
```bash
gestao-contratos/
├── contratos/               # App principal
│   ├── migrations/          # Migrações do banco
│   ├── static/              # Arquivos estáticos
│   │   ├── css/             # Folhas de estilo
│   │   ├── js/              # Scripts JavaScript
│   │   └── images/          # Imagens do sistema
│   ├── templates/           # Templates HTML
│   ├── admin.py             # Configuração do admin
│   ├── apps.py              # Configuração do app
│   ├── models.py            # Modelos de dados
│   ├── tests.py             # Testes unitários
│   ├── urls.py              # URLs do app
│   └── views.py             # Lógica das views
├── gestao_contratos/        # Configurações do projeto
│   ├── settings.py          # Configurações
│   ├── urls.py              # URLs globais
│   └── wsgi.py              # Configuração WSGI
├── manage.py                # Script de gerenciamento
└── requirements.txt         # Dependências do projeto
```
### Funcionalidades
✅ Autenticação de Usuários

Sistema de login seguro

Controle de acesso por perfil

✅ Gestão de Contratos

Cadastro de novos contratos

Edição e exclusão de registros

Visualização detalhada

✅ Filtros e Busca

Pesquisa dinâmica

Filtros avançados

Ordenação por colunas

✅ Relatórios

Exportação para PDF

Geração de relatórios personalizados

### Screenshots
Tela de Login
Tela de login do sistema

Dashboard
Painel principal com lista de contratos

### Contribuindo
Siga estes passos para contribuir:

Faça um fork do projeto

Crie sua branch (git checkout -b feature/nova-funcionalidade)

Commit suas mudanças (git commit -m 'Adiciona nova funcionalidade')

Push para a branch (git push origin feature/nova-funcionalidade)

Abra um Pull Request

### Licença
Distribuído sob a licença MIT. Veja LICENSE para mais informações.
```bash

**Observações importantes:**
1. Substitua `seu-usuario/gestao-contratos-unimed` pelo caminho real do seu repositório
2. Adicione as imagens reais do projeto na pasta `static/images/`
3. Ajuste os dados de contato conforme necessário
4. Se tiver um arquivo LICENSE, inclua-o no repositório

Este arquivo está pronto para ser usado como README.md no seu projeto! Basta copiar todo o conteúdo acima e colar em um novo arquivo README.md na raiz do seu projeto.
```

### Configurando Serviço para Iniciar Automáticamente no Linux

Como configurar o serviço `Ccontratos.service` utilizando **systemd** no Linux para iniciar automaticamente após a reinicialização.

---
 Criação do Arquivo do Serviço

 **Abra o terminal e crie o arquivo de serviço:**
   ```bash
   sudo nano /etc/systemd/system/Ccontratos.service
```
**Adicione o seguinte conteúdo ao arquivo**
```bash
[Unit]
Description=Inicia o sistema de gestão de contratos
After=network.target

[Service]
User=user #subistitua pelo seu usuário
Group=user #substitua pelo seu grupo
WorkingDirectory=/var/www/html/Ccontratos
ExecStart=/var/www/html/Ccontratos/env/bin/python manage.py runserver 0.0.0.0:4500
Restart=always
Environment="PYTHONUNBUFFERED=1"

[Install]
WantedBy=multi-user.target
```
**Salve o arquivo e saia do editor:**
No nano, use **CTRL+O** para salvar, **ENTER** para confirmar e **CTRL+X** para sair.

Recarregar e Habilitar o Serviço
Após criar o arquivo, recarregue o systemd e habilite o serviço:
```bash
sudo systemctl daemon-reload
````
Habilitar o serviço para iniciar automaticamente:
```bash
sudo systemctl enable Ccontratos.service
````
Iniciar o serviço manualmente para testar:
```bash
sudo systemctl start Ccontratos.service
````
Verificar o status do serviço:
```bash
sudo systemctl status Ccontratos.service
````
Reinicie o sistema
Para confirmar que o serviço está configurado corretamente, reinicie o sistema:
```bash
sudo reboot
````
Verificar Logs do Serviço
```bash
sudo journalctl -u Ccontratos.service
````




