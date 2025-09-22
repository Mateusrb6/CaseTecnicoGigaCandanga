# Case Técnico GigaCandanga 
---

## Desafio A - Pesquisa e Aquisição de Componentes
- Os servidores da GigaNuvem são construídos a partir de componentes commodities que estão sujeitos às flutuações do mercado, como preço e disponibilidade em estoque. Neste contexto, a cada nova aquisição e montagem de um servidor, se faz necessário pesquisar pelas melhores ofertas e, mesmo sendo uma boa prática a padronização dos componentes dentre os servidores, muitas vezes é preciso adaptar a compra à realidade do mercado. Para tanto, a partir das informações apresentadas na tabela 1, faça um levantamento dos melhores componentes em termos de qualidade, preço e disponibilidade no mercado brasileiro.

Componente          |        Quantidade
--------------------|---------------------------
Placa mãe           |      1
Processador         |        1
Memória (128 GB)    |        4
SSD M.2 (1TB)       |        1
Placa de Rede (dual)|        1
Placa de Rede (single)|      1
Cooler                |     1
Fonte ATX             |     1
Quantidade            |      1

### Entregáveis:

1) Uma planilha que relacione os componentes, fabricantes, modelos, especificações, quantidades, preços e fornecedores, bem como, o valor total da aquisição para um
servidor de processamento da GigaNuvem. Exporte a planilha como pdf e o nomeie como SeuNome_SeuSobrenome_Desafio_A.pdf
Considere o valor máximo de R$18.000,00 disponível para essa aquisição;
2) Faça o levantamento com pelo menos 3 fornecedores do mercado brasileiro.
3) Escolha 1 das cotações e explique, brevemente, o porquê dela ser a sua escolha.


## Desafio B - Configuração de Rede do Servidor
- Os servidores da GigaNuvem são conectados a duas redes LAN: uma de acesso e outra de clusterização. A primeira é responsável por permitir acesso às máquinas pelos técnicos para configuração e manutenção. Já a segunda é responsável por comunicar os servidores entre si, permitindo a clusterização dos nós físicos da GigaNuvem. Para tanto, esses servidores têm à disposição 4 interfaces de rede: uma onboard (disponibilizada pela placa mãe), uma single port e outra dual port. Essas interfaces são agregadas em pares, via LACP, sendo um par para cada rede LAN. Essa arquitetura garante a redundância de conexão às redes: caso uma interface falhe, a outra mantém a conectividade. A figura 1 ilustra a arquitetura detalhada.

![Figura 1 - Esquemático de rede de um servidor da GigaNuvem](https://github.com/Mateusrb6/CaseTecnicoGigaCandanga/blob/main/assets/print_desafioB.png)

- Para este desafio, considere que um servidor da GigaNuvem foi configurado com um sistema operacional Ubuntu 22.04 que dispõe do Netplan (https://netplan.io), um software utilitário desenvolvido e mantido pela Canonical que permite a configuração de rede no Ubuntu a partir de um arquivo YAML. Para tanto, pesquise e escreva um arquivo YAML com as configurações necessárias para agregar, via LACP, um par de interfaces em cada rede proposta na figura 1 e, também, gere uma documentação com o passo a passo para aplicar, via Netplan, e validar tais configurações no Ubuntu 22.04.

![Tabela 2 - Agregação de Interfaces](https://github.com/Mateusrb6/CaseTecnicoGigaCandanga/blob/main/assets/tabela2_desafioB.png)

![Tabela 3 - Definições para as agregações](https://github.com/Mateusrb6/CaseTecnicoGigaCandanga/blob/main/assets/tabela3_desafioB.png)

### Entregáveis:

1) Arquivo YAML, destinado ao Netplan, com a configuração para as 4 interfaces de rede instaladas em um servidor Ubuntu 22.04 de acordo com a arquitetura da figura 1 e as informações das tabelas 2 e 3. Nomeie este entregável como SeuNome_SeuSobrenome_Desafio_B.yaml.
2) Documentação com o passo a passo para aplicar as configurações do arquivo YAML via Netplan e como validar se as configurações foram aplicadas no Ubuntu 22.04. Exporte essa documentação como PDF e a nomeie como SeuNome_SeuSobrenome_Desafio_B.pdf;

## Desafio C - Automação de Processos

- No cotidiano dos colaboradores de TIC existem diversos problemas que podem ser automatizados ou ao menos facilitados, como por exemplo, o processo de configuração das interfaces de rede de um servidor, assim como proposto no desafio anterior. Para esse desafio, tome como base a documentação gerada no DESAFIO B e programe um script, na linguagem de programação da sua escolha, que automatize os procedimentos de configuração, aplicação e teste das interfaces de rede de um servidor Ubuntu 22.04.

### Entregáveis:
1) Arquivo de texto do script programado.
2) Readme com a documentação de como instalar e executar o programa.
3) Compile o script e o readme em um arquivo ZIP e o nomeie como SeuNome_SeuSobrenome_Desafio_C.zip.

### Considerações:
- O script não precisa ser 100% automatizado, ou seja, o nome das interfaces, das bonds de agregação e os endereços IPs podem ser passados como argumentos para o programa desenvolvido.
