# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), (https://keepachangelog.com/pt-BR/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [Unreleased]
- Evitar execução caso o programa não tenha Privilégios Administrativos
- Adicionar verificação se o arquivo é de certificados ou não.

## [0.0.2] - 2021-08-19
### Changed
- PyUAC Removido, e agora utilizando a opção --uac-admin no PyInstaller


## [0.0.1] - 2021-08-19
### Added
- Leitura do diretório "TODOS" para coletar todos os certificados digitais do diretório.
- Instalação dos certificados digitais utilizando subprocess para chamar "certutil" no Windows.
- Automaticamente solicita Privilégios Administrativos, com PyUAC


[0.0.2]: https://github.com/MrMineToons/Auto-Certificate-Installer-py/releases/tag/0.0.2
[0.0.1]: unreleased
