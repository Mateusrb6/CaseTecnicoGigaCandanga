# Configuração Automatizada de Bonds de Rede

Script na linguagem de programação Python para automatizar configuração, aplicação e teste de interfaces de rede com agregação de interfaces (bonds) em servidores Ubuntu 22.04 usando Netplan.

## Visão Geral

O script realiza as seguintes operações:
**1.** Escreve configuração de rede pronta no arquivo YAML usado para o Netplan.

```bash
network:
  version: 2
  renderer: networkd 

  ethernets:
    eno1:
      dhcp4: no
      dhcp6: no
    enp4s0:
      dhcp4: no
      dhcp6: no
    enp1s0f0:
      dhcp4: no
      dhcp6: no
    enp1s0f1:
      dhcp4: no
      dhcp6: no

  bonds:
    bond0:
      interfaces: [eno1, enp1s0f0]
      addresses: [10.1.0.1/24]
      routes:
        - to: default
          via: 10.1.0.0
          table: 100 
      routing-policy:
        - from: 10.1.0.0/24
          table: 100 
      nameservers:
        addresses: [10.1.0.100] 
      parameters:
        mode: 802.3ad 
        mii-monitor-interval: 100
        lacp-rate: fast

    bond1:
      interfaces: [enp4s0, enp1s0f1]
      addresses: [10.2.0.1/24]
      routes:
        - to: default
          via: 10.2.0.0
          table: 200 
      routing-policy:
        - from: 10.2.0.0/24
          table: 200 
      parameters: 
        mode: 802.3ad
        mii-monitor-interval: 100
        lacp-rate: fast
```

**2.** Aplica configuração usando `netplan apply`.
```
configuração netplan escrita em /etc/netplan/02-giga-interfaces.yaml
aplicando configuração netplan...
configuração aplicada com sucesso!
```
**3.** Verifica status das interfaces bond criadas.
```
verificando status das interfaces:
bond0: endereço ip correto
bond0 status operacional: Up
bond1: endereço ip correto
bond1 status operacional: Up
```
**5.** Realiza testes de ping para dns e loopback para os bonds.

```
testando conectividade:
  testando 10.1.0.1 -> 10.1.0.100 (servidor dns)...
conectividade ok
  testando bond0 -> 10.1.0.1 (loopback)...
conectividade ok
  testando bond1 -> 10.2.0.1 (loopback)...
conectividade ok
```

## Pré-requisitos

- Ubuntu 22.04
- Acesso root (script deve ser executado como superusuário)
- Interfaces de rede físicas nomeadas conforme configuração (eno1, enp4s0, enp1s0f0, enp1s0f1)
- Netplan instalado 
- Python instalado

## Como instalar e utilizar o programa

**1.** Baixe o arquivo do código `configyaml.py`
**2.** Entre no diretório em que o arquivo do código foi baixado

**Exemplo:**  
```bash
  cd Downloads
```

**3.**  No terminal do Ubuntu, execute o script como `root`:

```bash   
  sudo python3 configyaml.py
```

## Observações 
- As interfaces físicas utilizadas nos bonds devem estar conectadas corretamente.
- O script **sobrescreve** qualquer configuração anterior do Netplan no arquivo `/etc/netplan/02-giga-interfaces.yaml`.



### Autor
Mateus Reis Bastos — Engenharia de Redes, UnB

