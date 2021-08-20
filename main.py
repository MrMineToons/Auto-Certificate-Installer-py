import os
import subprocess
import sys
from glob import glob
import ctypes

# pyinstaller "Instalador de Certificados.py" --onefile --uac-admin


def is_admin_function():
    try:
        is_admin = os.getuid() == 0
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

    if is_admin is True:
        pass
    else:
        print("\n\n**************ATENÇÃO**************")
        print("Voce não tem Privilégios Administrativos.")
        print("Por Favor, execute o programa novamente como Administrador.")
        input("\nPressione ENTER para finalizar...\n\n")
        sys.exit()


def verifier():
    if os.path.exists("./Todos"):
        pass
    else:
        print("\n\n**************ATENÇÃO**************")
        print("Parece que a pasta 'Todos' não está no mesmo diretório que o executavel. "
              "Por Favor, cria a paste e adicione os certificados a serem instalados dentro dela.")
        print("Inicie o programa novamente para instalar!")
        input("\nPressione ENTER para finalizar...\n\n")
        sys.exit()


def main():
    certificados = []
    os.chdir("./Todos")
    # Formatos Conhecidos: .cer, .crt, .p7b, .pem, .der, .pfx
    file_types = glob("*.crt") + glob("*.cer") + glob("*.p7b") + glob("*.pem") + glob("*.der") + glob("*.pfx")

    for file in file_types:
        certificados.append(str(file))
        # print(f"Adicionando : {file} em {certificados}\n")

    print("\n\n***************************************")
    print(f"Lista Completa dos Certificados: \n{certificados}")
    print("***************************************\n\n")

    for instala in certificados:
        print("*****************************************************************************************************************")
        try:
            command = ["certutil", "-enterprise", "-f",
                       "-addstore", "Root", f"{instala}"]
            output, error = subprocess.Popen(
                command, universal_newlines=True,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
            ).communicate()
            print(f"Output = {output}\n\nError = {error}")
        except Exception as e:
            print("***************************************")
            print(f"Instalacao de {instala} falhou! Erro: {e}")
            print("***************************************")
        finally:
            print("*****************************************************************************************************************\n")
            pass

    os.listdir("./")
    print("\n\nInstalacao finalizada!")
    input("Pressione ENTER para finalizar...\n\n")


if __name__ == "__main__":
    is_admin_function()
    verifier()
    main()
