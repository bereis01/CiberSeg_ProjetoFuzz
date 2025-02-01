# **Projeto de Programação 1:** Testes de Fuzzing com OSS-Fuzz

**Universidade Federal de Minas Gerais | Departamento de Ciência da Computação | 2024/02**

**Alunos:** Bernardo Reis, Guilherme Mendonça, Rubens Castro

**Professora:** Michele Nogueira Lima

**Disciplina:** DCC030 Cibersegurança

Neste trabalho, foi realizado um estudo de aplicação do “OSS-Fuzz”, uma ferramenta de fuzzing desenvolvida pela Google para a validação de software de código aberto. A ideia desta técnica, “fuzzing”, consiste em executar um código-alvo com inputs aleatórios e avaliar o seu comportamento, buscando encontrar bugs, erros, “crashes” e/ou vulnerabilidades. O OSS-Fuzz, na verdade, faz parte de um projeto mais amplo da empresa mencionada para a disponibilização de uma infraestrutura de validação baseada em fuzzing, na qual sistemas de código aberto podem ser integrados, contribuindo para a construção de um ecossistema “open-source” mais seguro. Diversos códigos já foram integrados ao fuzzer em estudo e a grande diversidade desses projetos mostra o quão importante é a aplicação da técnica de fuzzing para a melhoria da integridade e corretude dos programas envolvidos.

Dada essa noção inicial sobre “fuzzing”, este trabalho teve por objetivo a integração de uma base de código inédita ao ambiente do OSS-Fuzz, porém de maneira local. Como já mencionado, a Google oferece uma infraestrutura para a validação automática de código aberto na qual projetos podem se inscrever. Entretanto, também há a possibilidade de se instalar e executar de maneira local toda essa infraestrutura, permitindo o fuzzing manual de códigos arbitrários. Para isso, primeiro, é necessário a escolha de um projeto para ser testado. Em seguida, deve-se clonar o repositório do OSS-Fuzz e configurar os arquivos necessários para a integração desse projeto. O próximo passo consiste na escrita das funções que realizarão o fuzzing - os “fuzz targets” -, o que envolve a definição de quais partes do código-alvo serão testadas. Com tudo preparado, deve-se executar o “fuzzer” propriamente dito, o qual irá gerar diversos resultados relacionados a bugs, erros ou “crashes”. Esses resultados, por fim, serão analisados e discutidos.
