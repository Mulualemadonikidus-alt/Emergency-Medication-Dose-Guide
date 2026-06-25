def calculate_dosage(drug, weight):
    """
    Handles clinical math to determine final dosage.
    """
    if drug['type'] == 'weight_based':
        dose = round(drug['factor'] * weight, 2)
    else:
        dose = drug['dose']
    
    # Simple bounds check logic
    is_alert = dose > drug['max_dose']
    return dose, is_alert