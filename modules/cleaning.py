def remove_duplicates(data):
    """
    Elimina duplicados de una lista de diccionarios basándose en la clave 'id'.

    :param data: Lista de diccionarios con una clave 'id' para identificar duplicados.
    :return: Lista de diccionarios sin duplicados.
    """
    seen_ids = set()
    unique_data = []

    for item in data:
        item_id = item.get('id')
        if item_id not in seen_ids:
            seen_ids.add(item_id)
            unique_data.append(item)

    return unique_data