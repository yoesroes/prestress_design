def calculate_prestress_force(tendon, section):
    """Calculate basic jacking force and tendon eccentricity."""

    if tendon.area <= 0.0:
        raise ValueError("Luas tendon harus > 0.")

    if tendon.number <= 0:
        raise ValueError("Jumlah tendon harus > 0.")

    if tendon.f_jacking <= 0.0:
        raise ValueError("f_jacking harus > 0.")

    Ap_total = tendon.area * tendon.number

    Pjack_N = tendon.f_jacking * Ap_total
    Pjack_kN = Pjack_N / 1000.0

    profile = tendon.profile

    if not profile:
        eccentricity = 0.0
    else:
        x_mid = profile[-1][0] / 2.0

        eccentricity = min(
            profile,
            key=lambda point: abs(point[0] - x_mid)
        )[1]

    return {
        "Ap_total": Ap_total,
        "Pjack_N": Pjack_N,
        "Pjack_kN": Pjack_kN,
        "eccentricity": eccentricity,
    }


def calculate_concrete_stress(
    prestress_force,
    eccentricity,
    section_properties,
):
    """Calculate concrete stress from prestress.

    Compression is returned as positive.
    """

    P = prestress_force["Pjack_N"]
    A = section_properties["A"] * 1.0e6
    Z_top = section_properties["Z_top"] * 1.0e9
    Z_bottom = section_properties["Z_bottom"] * 1.0e9

    e = eccentricity * 1000.0

    sigma_P = P / A

    sigma_top = sigma_P + (P * e / Z_top)
    sigma_bottom = sigma_P - (P * e / Z_bottom)

    return {
        "sigma_P": sigma_P,
        "sigma_top": sigma_top,
        "sigma_bottom": sigma_bottom,
    }