# Ambiente de produção e testes padronizados Python
<br>
Ambiente de produção pré-configurado. <br>
Como utilizar:<br>
<br>
1 - instale gerenciador chocolatey:<br>
<br>
* no powershell com poderes de administrador execute os comandos:<br>
<br>
a) Get-ExecutionPolicy<br>
b) Set-ExecutionPolicy AllSigned<br>
c) Set-ExecutionPolicy Bypass -Scope Process<br>
d) Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))<br>

2) - instale a ferramente Make:<br>
<br>
* no powershell com poderes de administrador execute o comando:<br>
<br>
a) choco install make<br>
<br>
3) agora basta baixar o repositório e instalar como o comando "make install". Lista de comandos:<br>
<br>
a) make install: instala todas as dependências<br>
b) make cleam: exclue dependências<br>
c) make test: executa os testes<br>
<br>
O ambiente irá realizar testes de verificação do codigo quando da realização do git commit em conformidade com as configurações pré-determinadas em poetry.toml, .yamllint e pre-commit-config.yaml
