                "DevOps": 15000,
                "QA": 10000,
                "Mobile": {
                    "Android": 12000,
                    "iOS": 14000
                }
            },
            "Suporte": {
                "HelpDesk": 8000,
                "Monitoramento": 6000
            }
        },
        "RH": {
            "Recrutamento": 10000,
            "Treinamento": 12000,
            "Cultura": {
                "Eventos": 5000,
                "Brindes": 2000,
                "Campanhas": 3500
            }
        },
        "Financeiro": {
            "Auditoria": 18000,
            "Contabilidade": 22000,
            "FolhaPagamento": 40000
        },
        "Logistica": {
            "Transportes": {
                "Frota": 30000,
                "Combustivel": 12000
            },
            "Estoque": {
                "Armazem": 20000,
                "Controle": 8000
            }
        }
    }
}


import time
from functools import wraps


def auditor(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()

        print("========== AUDITORIA DE ORÇAMENTO ==========")
        print("Iniciando processamento da estrutura financeira...")
        print(f"Departamentos ignorados: {args[1:]}")
        print(f"Parâmetros financeiros: {kwargs}")
        print("--------------------------------------------")

        resultado = func(*args, **kwargs)

        fim = time.time()
        tempo_execucao = fim - inicio

        print("--------------------------------------------")
        print(f"Processamento concluído com sucesso.")
        print(f"Tempo total de execução: {tempo_execucao:.6f} segundos")
        print("============================================\n")

        return resultado

    return wrapper


@auditor
def calcular_orcamento(estrutura, *departamentos_ignorados, **kwargs):
    taxa_cambio = kwargs.get("taxa_cambio", 1)
    moeda_destino = kwargs.get("moeda_destino", "USD")

    def soma_recursiva(no, caminho=""):
        total = 0

        if isinstance(no, dict):
            for departamento, valor in no.items():

                # Ignora departamento inteiro se estiver na lista
                if departamento in departamentos_ignorados:
                    print(f"Ignorando departamento: {caminho}/{departamento}")
                    continue

                total += soma_recursiva(valor, f"{caminho}/{departamento}")

        elif isinstance(no, (int, float)):
            total += no

        return total

    total_original = soma_recursiva(estrutura)
    total_convertido = total_original * taxa_cambio

    print(f"Total consolidado em {moeda_destino}: {total_convertido:,.2f}")

    return total_convertido


orcamento_final = calcular_orcamento(
    empresa_data,
    "RH",               # Ignora RH
    "Logistica",        # Ignora Logística
    moeda_destino="BRL",
    taxa_cambio=5.20
)

print(f"Orçamento final convertido: R$ {orcamento_final:,.2f}")