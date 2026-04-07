import requests

arquivos = {
    'static/js/jquery.mask.min.js':
        'https://cdn.jsdelivr.net/npm/jquery-mask-plugin@1.14.16/dist/jquery.mask.min.js',
}

for destino, url in arquivos.items():
    print(f'Baixando {destino}...')
    resposta = requests.get(url)
    with open(destino, 'wb') as f:
        f.write(resposta.content)
    print(f'  ✓ Salvo ({len(resposta.content) // 1024} KB)')

print('✅ Máscara baixada!')