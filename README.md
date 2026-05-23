# Sistema de Estoque MVC

Sistema de controle de estoque com login de usuários, desenvolvido em Python com interface gráfica.

## O que o programa faz

- Cada usuário tem seu próprio login e só vê os seus produtos
- Permite cadastrar, listar, editar e remover produtos do estoque
- Armazena os dados em um banco MySQL

## Como rodar

**1. Crie o banco de dados**
```bash
mysql -u root -p < banco.sql
```

**2. Ajuste a senha do MySQL**

Abra `config/database.py` e troque `password="rootsecret"` pela sua senha.

**3. Instale as dependências**
```bash
pip install customtkinter mysql-connector-python
```

**4. Execute o programa**
```bash
python main.py
```

## Usuários de exemplo (criados pelo banco.sql)

| Usuário | Senha    |
|---------|----------|
| admin   | admin123 |
| joao    | joao123  |
| leandro | leo123   |

