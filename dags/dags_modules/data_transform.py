def transform_data(extracted_data):

    transformed_data = [item for item in extracted_data if item['price'] > 0]
    return transformed_data