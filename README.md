


## Integrantes do Projeto

| Nº | Aluno(a) | Matrícula |
|----|----------|------------|
| 1 | Leandro Nascimento de Sousa | 202303752181 |
| 2 | Guilherme Correa da Cruz Marques | 202408700938 |
| 3 | Caian Ribeiro Carvalho | 202402365746 |
| 4 | Luan Souza Ferreira de Jesus | 202408557566 |
| 5 | Gustavo Jorge Santana Castro | 202402365886 |
| 6 | João Paulo Rodrigues Cerqueira | 202403601052 |


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
python3 main.py
```

## Usuários de exemplo (criados pelo banco.sql)

| Usuário | Senha    |
|---------|----------|
| admin   | admin123 |
| joao    | joao123  |
| leandro | leo123   |

