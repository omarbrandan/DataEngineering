def transform_data(extracted_data):
    transformed_data = [item for item in extracted_data if item.get('current_price', 0) > 0]
    return transformed_data