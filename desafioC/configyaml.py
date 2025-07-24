import os
import subprocess
import time
import sys

netplan_config = """
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
"""

def main():
    # verificar permissões de root
    if os.geteuid() != 0:
        print("erro: este script deve ser executado como root!")
        sys.exit(1)
    
    # escrever configuração do netplan
    config_path = "/etc/netplan/02-giga-interfaces.yaml"
    try:
        with open(config_path, "w") as f:
            f.write(netplan_config.strip())
        print(f"configuração netplan escrita em {config_path}")
    except Exception as e:
        print(f"erro ao escrever arquivo netplan: {str(e)}")
        sys.exit(1)

    # aplicar configuração
    try:
        print("aplicando configuração netplan...")
        result = subprocess.run(
            ["netplan", "apply"],
            capture_output=True,
            text=True,
            timeout=60
        )
        if result.returncode != 0:
            print(f"erro ao aplicar configuração do netplan:\n{result.stderr}")
            sys.exit(1)
        print("configuração aplicada com sucesso!")
    except subprocess.TimeoutExpired:
        print("erro: timeout ao aplicar configuração do netplan")
        sys.exit(1)
    except Exception as e:
        print(f"erro inesperado: {str(e)}")
        sys.exit(1)

    # dar tempo para interfaces subirem
    time.sleep(5)

    # verificar interfaces de bond
    print("\nverificando status das interfaces:")
    bonds_to_check = ["bond0", "bond1"]
    for bond in bonds_to_check:
        try:
            # verificar se interface existe
            subprocess.check_call(["ip", "link", "show", bond], stdout=subprocess.DEVNULL)
            
            # verificar endereços ip
            ip_result = subprocess.run(
                ["ip", "-4", "addr", "show", bond],
                capture_output=True,
                text=True
            )
            if "10.1.0.1/24" in ip_result.stdout and bond == "bond0":
                print(f"{bond}: endereço ip correto")
            elif "10.2.0.1/24" in ip_result.stdout and bond == "bond1":
                print(f"{bond}: endereço ip correto")
            else:
                print(f"{bond}: endereço ip ausente ou incorreto")
            
            # verificar status do bond
            with open(f"/sys/class/net/{bond}/operstate") as f:
                status = f.read().strip()
                print(f"{bond} status operacional: {status.capitalize()}")
                
        except subprocess.CalledProcessError:
            print(f"{bond}: interface não encontrada")
        except Exception as e:
            print(f"erro ao verificar {bond}: {str(e)}")

    # testar conectividade de rede
    print("\ntestando conectividade:")
    test_cases = [
        ("10.1.0.1", "10.1.0.100", "servidor dns"),
        ("bond0", "10.1.0.1", "loopback")
        ("bond1", "10.2.0.1", "loopback")
    ]
    
    for interface, target, description in test_cases:
        try:
            print(f"  testando {interface} -> {target} ({description})...")
            result = subprocess.run(
                ["ping", "-c", "3", "-I", interface, target],
                capture_output=True,
                text=True,
                timeout=15
            )
            
            if "3 received" in result.stdout:
                print(f"conectividade ok")
            else:
                print(f"falha na conectividade")
                print(f"detalhes: {result.stdout.strip() or result.stderr.strip()}")
                
        except subprocess.TimeoutExpired:
            print(f"timeout ao testar {target}")
        except Exception as e:
            print(f"erro inesperado: {str(e)}")

if __name__ == "__main__":
    main()