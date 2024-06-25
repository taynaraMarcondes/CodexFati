<div align="center">
    <img src="./CodexFati_logo.svg" alt="Logo" width="400">
    <h1>Linguagem Codex Fati</h1>
</div>

<details>
  <summary>Sumário</summary>
  <ol>
    <li>
      <a href="#sobre-o-projeto">Sobre o projeto</a>
      <ul>
        <li><a href="#tecnologias">Tecnologias</a></li>
      </ul>
    </li>
    <li>
      <a href="#introdução">Introdução</a>
      <ul>
        <li><a href="#instalação">Instalação</a></li>
        <li><a href="#como-rodar">Como rodar</a></li>
      </ul>
    </li>
    <li><a href="#desenvolvimento">Desenvolvimento</a></li>
  </ol>
</details>

## Sobre o projeto

Essa linguagem foi construída para a disciplina de Compiladores da Universidade Federal de Itajubá. Ela visa ser uma linguagem baseada nas cartas de Tarô.

A documentação completa está presente no arquivo [Documentacao - Cadex Fati](https://drive.google.com/file/d/1Lx0d2KeWiftHK-ltPhCwVvXCdbJWJOfU/view?usp=sharing), neste arquivo encontram-se as definições realizadas para a linguagem, bem como as expressões regulares e autômatos desenvolvidos para ela.

### Tecnologias

Para construir essa linguagem foi utilizado da linguagem python.

<a href="https://www.python.org/" target="_blank"><img src="https://www.python.org/static/img/python-logo@2x.png" width="150"></a>

## Introdução

Nesta seção será apresentado como instalar todos os itens necessários e como utilizar o programa.

### Instalação

<details>
    <summary>Como instalar o Python no Windows</summary>
    
A instalação do Python no Windows segue o padrão da maioria dos programas instalados no sistema operacional em questão com uma única ressalva: no início do processo de instalação, deve-se selecionar a opção “Add Python (version) to PATH”. Com isso, o Windows saberá onde está localizado o interpretador do Python e, assim, conseguiremos utilizá-lo sem problemas.

1. Acesse a [página oficial](https://www.python.org/downloads/) para realizar o download do instalador do Python na versão desejada
2. Vá até a pasta na qual foi feito o download do instalador do Python
3. Clique com o botão direito em cima do instalador e clique na opção “Executar como Administrador”.
4. Com o instalador aberto tenha a certeza de ter marcado as opções “Add Python (version) to PATH” para que o comando python fique disponível.
5. Por fim clique em “Install Now” e siga o processo padrão de instalação de programas no Windows (next, next, next, finish).

</details>

<details>
    <summary>Como instalar o Python no Linux</summary>
    
Os sistemas GNU/Linux mais recentes já possuem uma versão do Python instalada junto com o sistema operacional. Podemos checar com o seguinte comando:

`which python3`

- Debian e Ubuntu: Através do gerenciador de pacotes, é possível instalar versões específicas do Python. No exemplo abaixo, é instalada a versão, por exemplo, 3.9 do Python.

  `sudo apt-get install python3.9`

- RedHat e CentOS: Assim como no tópico anterior, é possível instalar versões específicas do Python. No comando abaixo, é instalada a versão, por exemplo, 3.9 do Python.

  `sudo yum install python3.9`

</details>

<details>
  <summary>Instalação de bibliotecas</summary>
O projeto também conta com algumas bibliotecas para correta execução do código. Sendo assim, tanto para o Windows quanto para o Linux é necessário abrir o terminal e digitar os seguinte comandos para instalar as bibliotecas necessárias:

- `pip install ply`

- `pip install numpy`

</details>

### Como rodar

Vários exemplos de algoritmos da linguagem foram criados e podem ser encontrados no arquivo [example](/example.py). Neste arquivo encontra-se um variável denominada _example_ que é uma lista com os exemplos na linguagem Codex Fati.

Sendo assim, para executar a tradução da linguagem Codex Fati para C++ basta executar no terminal o seguinte comando:

> `python3 codexFati_yacc.py`

Com este comando, o código traduzido estará presente no arquivo _temp\_x.cpp_ onde x é o número do exemplo de acordo com sua posição na lista de exemplos. Como se trata de um código C++ pode ser executado pelo seguinte comando no terminal:

> `g++ temp_x.cpp`

Por fim, o arquivo executável pode ser aberto para visualizar o resultado do código interpretado.

- No Windows: `./a.exe`
- No Linux: `./a.out`

Além disso, serão gerados arquivos _lexer\_x.txt_ que contém a análise léxica de cada exemplo, onde x é o número do exemplo de acordo com sua posição na lista de exemplos.

## Desenvolvimento

Esse projeto foi desenvolvido por:

- Taynara Marcondes Pereira Silva - [@taynaraMarcondes](https://github.com/taynaraMarcondes)
- Guilherme De Freitas Marques - [@Guifrema](https://github.com/Guifrema)
- Pedro Di Luca Martins Chaves  - [@PedroWChaves](https://github.com/PedroWChaves)
