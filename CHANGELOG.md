# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), [Keep a Changelog PT-BR](https://keepachangelog.com/pt-BR/1.0.0/).


## [Unreleased]
- Separar pasta ROOT e PESSOAL. Para também ser possível instalar certificados pessoais. (Talvez mais alguns futuramente...).
- Avisar pastas vazias.
- Pensando em mais coisas para adicionar...

## [0.0.3] - 2021-08-20
### Added
- Evitar a execução se o programa não tem Privilégios Administrativos.
- Evitar a execução se a pasta "Todos" não foi encontrada.
- Na listagem dos certificados, apenas arquivos do tipo .cer, .crt, .p7b, .pem, .der, .pfx (Estes são os tipos que eu conheço).

## [0.0.2] - 2021-08-19
### Changed
- PyUAC Removido, e agora utilizando a opção --uac-admin no PyInstaller.


## [0.0.1] - 2021-08-19
### Added
- Leitura do diretório "TODOS" para coletar todos os certificados digitais do diretório.
- Instalação dos certificados digitais utilizando subprocess para chamar "certutil" no Windows.
- Automaticamente solicita Privilégios Administrativos, com PyUAC.

[0.0.3]: https://github.com/MrMineToons/Auto-Certificate-Installer-py/releases/tag/0.0.3
[0.0.2]: https://github.com/MrMineToons/Auto-Certificate-Installer-py/releases/tag/0.0.2
[0.0.1]: unreleased
