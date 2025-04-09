# Sistema de Gestão de Contratos

Bem-vindo ao repositório do Sistema de Gestão de Contratos desenvolvido para o uso do dia a dia de maneira mais rápida. Este sistema foi construído para facilitar a gestão de contratos, controle de dados e autenticação de usuários.

---

## **Índice**
- [Sobre o Projeto](#sobre-o-projeto)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Requisitos do Sistema](#requisitos-do-sistema)
- [Instalação](#instalação)
- [Estrutura de Pastas](#estrutura-de-pastas)
- [Funcionalidades](#funcionalidades)
- [Contribuindo](#contribuindo)
- [Licença](#licença)
- [Início Automático](#início-automático)

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
apt-get install python3-venv
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências
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
python manage.py runserver 0.0.0.0:4500
```
Acesse o sistema em: http://localhost:4500

---

## **Estrutura de Pastas**
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

---

## **Funcionalidades**

✅ **Autenticação de Usuários**  
- Sistema de login seguro  
- Controle de acesso por perfil

✅ **Gestão de Contratos**  
- Cadastro de novos contratos  
- Edição e exclusão de registros  
- Visualização detalhada

✅ **Filtros e Busca**  
- Pesquisa dinâmica  
- Filtros avançados  
- Ordenação por colunas

✅ **Relatórios**  
- Exportação para PDF  
- Geração de relatórios personalizados

---
## **Contribuindo**

Siga estes passos para contribuir:

1. Faça um fork do projeto  
2. Crie sua branch: `git checkout -b feature/nova-funcionalidade`  
3. Commit suas mudanças: `git commit -m 'Adiciona nova funcionalidade'`  
4. Push para a branch: `git push origin feature/nova-funcionalidade`  
5. Abra um Pull Request

---

## **Licença**

Distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais informações.

---

## **Início Automático**

Configurando serviço para iniciar automaticamente no Linux utilizando **systemd**.

### 1. Criação do Arquivo de Serviço

Abra o terminal e crie o arquivo:
```bash
sudo nano /etc/systemd/system/Ccontratos.service
```

### 2. Conteúdo do Arquivo

```ini
[Unit]
Description=Inicia o sistema de gestão de contratos
After=network.target

[Service]
User=usuario   # substitua pelo seu usuário
Group=usuario  # substitua pelo seu grupo
WorkingDirectory=/var/www/html/Ccontratos
ExecStart=/var/www/html/Ccontratos/env/bin/python manage.py runserver 0.0.0.0:4500
Restart=always
Environment="PYTHONUNBUFFERED=1"

[Install]
WantedBy=multi-user.target
```

> **Dica:** No nano, use `CTRL+O` para salvar, `ENTER` para confirmar e `CTRL+X` para sair.

### 3. Recarregar e Habilitar o Serviço

```bash
sudo systemctl daemon-reload
sudo systemctl enable Ccontratos.service
sudo systemctl start Ccontratos.service
sudo systemctl status Ccontratos.service
```

### 4. Reinicie o Sistema

```bash
sudo reboot
```

### 5. Verificar Logs do Serviço

```bash
sudo journalctl -u Ccontratos.service
```

---

> **Observações importantes:**
> 1. Substitua `seu-usuario/seu-repositorio` pelo caminho real do seu repositório.
> 2. Adicione as imagens reais do projeto na pasta `static/images/`.
> 3. Ajuste os dados de contato conforme necessário.
> 4. Inclua um arquivo `LICENSE` na raiz do projeto.
