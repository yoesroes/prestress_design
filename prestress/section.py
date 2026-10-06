def calculate_section_properties(section):
    """Calculate basic gross-section properties."""

    if section.area <= 0.0:
        raise ValueError("Section area harus > 0.")

    if section.inertia <= 0.0:
        raise ValueError("Section inertia harus > 0.")

    if section.y_top <= 0.0 or section.y_bottom <= 0.0:
        raise ValueError("y_top dan y_bottom harus > 0.")

    Z_top = section.inertia / section.y_top
    Z_bottom = section.inertia / section.y_bottom

    return {
        "A": section.area,
        "I": section.inertia,
        "y_top": section.y_top,
        "y_bottom": section.y_bottom,
        "Z_top": Z_top,
        "Z_bottom": Z_bottom,
    }