def validate_material(material):
    """Validate basic concrete and prestressing-steel properties."""

    if material.fc <= 0.0:
        raise ValueError("fc harus > 0.")

    if material.fpu <= 0.0:
        raise ValueError("fpu harus > 0.")

    if material.Ep <= 0.0:
        raise ValueError("Ep harus > 0.")

    if material.Ec <= 0.0:
        raise ValueError("Ec harus > 0.")

    if material.density_concrete <= 0.0:
        raise ValueError("density_concrete harus > 0.")

    return True