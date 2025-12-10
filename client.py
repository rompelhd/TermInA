#!/usr/bin/env python3
import sys
import requests
import json

INIT_PROMPT = """Eres TermInA, un asistente que solo da comandos reales de Linux o Windows,
sin inventar bibliotecas ni funciones que no existen.
Solo responde con codigo funcional y comentarios necesarios con #.
No agregues explicaciones fuera del codigo.
Ejemplo:
Usuario: Como actualizar paquetes con apt
TermInA:
```bash
sudo apt update
sudo apt upgrade -y
```"""


def main():
    if len(sys.argv) < 2:
        print("Uso: python3 script.py <mensaje_del_usuario>")
        sys.exit(1)

    USER_PROMPT = " ".join(sys.argv[1:])

    payload = {
        "model": "phi3",
        "prompt": f"{INIT_PROMPT}\nUsuario: {USER_PROMPT}\nTermInA: ",
        "max_tokens": 150,
        "stream": True
    }

    response = requests.post("http://localhost:11434/v1/completions",
                             headers={"Content-Type": "application/json"},
                             data=json.dumps(payload),
                             stream=True)

    for line in response.iter_lines():
        if not line:
            continue
        decoded_line = line.decode("utf-8")
        if decoded_line == "data: [DONE]":
            break
        try:
            chunk = json.loads(decoded_line.replace("data: ", ""))['choices'][0].get('text', '')
            print(chunk, end='', flush=True)
        except (json.JSONDecodeError, KeyError):
            continue
    print()

if __name__ == "__main__":
    main()
