
    # --- Operaciones básicas (ejemplos) ---

    # Acceder a una colección
    mycollection = db.mycollection # Reemplaza 'mycollection' con el nombre de tu colección

    # Insertar un documento
    print("\nInsertando un documento...")
    document = {"name": "Alice", "age": 30, "city": "New York"}
    result = mycollection.insert_one(document)
    print(f"Documento insertado con _id: {result.inserted_id}")

    # Insertar varios documentos
    print("\nInsertando varios documentos...")
    documents = [
        {"name": "Bob", "age": 25, "city": "London"},
        {"name": "Charlie", "age": 35, "city": "Paris"}
    ]
    results = mycollection.insert_many(documents)
    print(f"Documentos insertados con _ids: {results.inserted_ids}")

    # Buscar un documento
    print("\nBuscando un documento (Alice)...")
    found_document = mycollection.find_one({"name": "Alice"})
    if found_document:
        print(f"Documento encontrado: {found_document}")
    else:
        print("Documento no encontrado.")

    # Buscar varios documentos
    print("\nBuscando todos los documentos...")
    for doc in mycollection.find():
        print(doc)

    # Actualizar un documento
    print("\nActualizando el documento de Alice...")
    mycollection.update_one({"name": "Alice"}, {"$set": {"age": 31}})
    updated_document = mycollection.find_one({"name": "Alice"})
    print(f"Documento actualizado: {updated_document}")

    # Eliminar un documento
    print("\nEliminando el documento de Bob...")
    mycollection.delete_one({"name": "Bob"})
    remaining_documents = mycollection.find()
    print("Documentos restantes después de la eliminación:")
    for doc in remaining_documents:
        print(doc)