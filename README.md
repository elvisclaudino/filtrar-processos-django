
# Filtro de processos

A partir de uma base de dados, o programa lista todos os processos pelos quais o advogado é responsável, onde o usuário através de um input digita o `ID` do advogado que deseja gerar um relatório.

## Desenvoldido por:

- [@elvisclaudino](https://github.com/elvisclaudino)

# Roteiro para a execução.

1. Criar uma conexão MySQL com `Hostname: 127.0.0.1` `Port: 3306` `Username: root` `password: (Não possui)`
   
![image](https://github.com/elvisclaudino/hash-table/assets/102040112/72d94052-337e-41c0-828d-b120e4c4aba7)

2. Criar a database utilizando o script do arquivo `escritorio.sql`

![image](https://github.com/elvisclaudino/filtrar-processos-django/assets/102040112/59ea44f5-dca2-4704-a8e0-8b4867fa5bb3)

4. Acessar o diretorio e no terminal realizar as migrations
   
```bash
  processFilter> python .\manage.py makemigrations
```
```bash
  processFilter> python .\manage.py migrate
```

4. Ainda através do terminal iniciar o servidor

```bash
  processFilter> python .\manage.py runserver
```

5. Assim que iniciar o servidor, será exibida uma tabela com todos os processos contidos no banco de dados

![image](https://github.com/elvisclaudino/hash-table/assets/102040112/43f506af-28b6-45c7-9f80-881abdf05765)

6. Através de um input o usuário pode digitar o ID de um advogado e gerar um relatório com todos os processos vinculados ao advogado selecionado

![image](https://github.com/elvisclaudino/hash-table/assets/102040112/2294e2dd-9133-4e33-9aff-bc2b7f8ffbbd)

![image](https://github.com/elvisclaudino/hash-table/assets/102040112/317eaf24-e842-4683-a5f5-098a509861c6)
