"""SPDX-License-Identifier: AGPL-3.0-only."""
def saludo(nombre='Marco'):
    return f'Hola, {nombre.strip() or "Marco"}. Tu entorno Python funciona.'
if __name__=='__main__':
    print(saludo())
