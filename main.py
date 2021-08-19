import os
import subprocess

#pyinstaller "Instalador de Certificados.py" --onefile --uac-admin


def main():
    certificados = []
    os.chdir("./Todos")

    for file in os.listdir("./"):
        certificados.append(str(file))
        print(f"Adicionando : {file} em {certificados}\n")

    print("\n\n\n***************************************")
    print(f"Lista Completa : \n{certificados}")
    print("***************************************\n\n\n")

    for instala in certificados:
        print("\n*****************************************************************************************************************")
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
    input("Pressione ENTER para finalizar...")


if __name__ == "__main__":
    main()
