# CNPJ Validator

Biblioteca Python para validação de CNPJ alfanumérico.

O objetivo deste projeto é fornecer uma implementação simples e reutilizável para conversão e validação de CNPJ, incluindo o cálculo dos dígitos verificadores.

## Sumário

- [Instalação](#instalação)
- [Uso](#uso)
- [Estrutura do projeto](#estrutura-do-projeto)
- [Tratamento de erros](#tratamento-de-erros)
- [Licença](#licença)

## Instalação

Clone o repositório:

```bash
git clone https://github.com/SEU_USUARIO/cnpj-validator.git
```

Entre no diretório:

```bash
cd cnpj-validator
```

Instale o projeto:

```bash
pip install .
```

## Uso

Exemplo de utilização:

```python
from cnpj import validar_cnpj

cnpj = "SEU_CNPJ_AQUI"

resultado = validar_cnpj(cnpj)

print(resultado)
```

Retorno:

- `True`: CNPJ válido
- `False`: CNPJ inválido

## Estrutura do projeto

```text
cnpj-validator/
│
├── cnpj/
│   ├── __init__.py
│   ├── converter.py
│   ├── validator.py
│   └── exceptions.py
│
├── tests/
├── README.md
└── LICENSE
```

## Tratamento de erros

A biblioteca possui uma exceção personalizada para erros relacionados ao formato do CNPJ.

Exemplo:

```python
from cnpj import validar_cnpj
from cnpj.exceptions import CNPJInvalidError

try:
    validar_cnpj("123")

except CNPJInvalidError as erro:
    print(erro)
```

Erros tratados:

- Quantidade de caracteres diferente de 14.
- Caracteres inválidos no CNPJ.

## Como funciona

O processo de validação é dividido em:

1. Conversão dos caracteres do CNPJ para valores numéricos.
2. Cálculo do primeiro dígito verificador.
3. Cálculo do segundo dígito verificador.
4. Comparação dos dígitos calculados com os valores informados.


## Licença

Este projeto está sob a licença MIT.
