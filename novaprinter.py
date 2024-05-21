def prettyPrinter(torrent):
    """
    Imprime la información de un torrent en un formato legible.

    torrent: Un diccionario con información sobre el torrent.
    """
    print("Nombre: ", torrent.get('name', 'N/A'))
    print("Semillas: ", torrent.get('seeds', 'N/A'))
    print("Leechers: ", torrent.get('leech', 'N/A'))
    print("Tamaño: ", torrent.get('size', 'N/A'))
    print("Enlace: ", torrent.get('link', 'N/A'))
    print("Descripción: ", torrent.get('desc_link', 'N/A'))
    print("Motor: ", torrent.get('engine_url', 'N/A'))
    print("-" * 40)
