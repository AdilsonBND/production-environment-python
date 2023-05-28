# Ambiente de produção e testes padronizados Python

Ambiente de produção pré-configurado.
Como utilizar:

1 - instale gerenciador chocolatey:

* no powershell com poderes de administrador execute os comandos:

a) Get-ExecutionPolicy
b) Set-ExecutionPolicy AllSigned
c) Set-ExecutionPolicy Bypass -Scope Process
d) Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

2) - instale a ferramente Make:

* no powershell com poderes de administrador execute o comando:

a) choco install make

3) agora basta baixar o repositório e instalar como o comando "make install". Lista de comandos:

a) make install: instala todas as dependências
b) make cleam: exclue dependências
c) make test: executa os testes

O ambiente irá realizar testes de verificação do codigo quando da realização do git commit em conformidade com as configurações pré-determinadas em poetry.toml, .yamllint e pre-commit-config.yaml
