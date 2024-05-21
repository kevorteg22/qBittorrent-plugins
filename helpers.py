import requests


def retrieve_url(url):
    """
    Recupera el contenido HTML de una URL dada.
    """
    response = requests.get(url)
    response.raise_for_status()  # Lanza una excepción si ocurre un error
    return response.text


def download_file(url, filename=None):
    """
    Descarga un archivo desde una URL dada.
    Si no se proporciona un nombre de archivo, se utiliza el nombre del archivo en la URL.
    """
    local_filename = filename or url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename
