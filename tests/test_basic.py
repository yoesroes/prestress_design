from prestress.input import (
    MaterialInput,
    SectionInput,
    TendonInput,
)

from prestress.materials import validate_material
from prestress.section import calculate_section_properties
from prestress.prestress import calculate_prestress_force


def test_material():
    material = MaterialInput(
        fc=40.0,
        fpu=1860.0,
        Ep=195000.0,
        Ec=30000.0,
    )

    assert validate_material(material) is True


def test_section():
    section = SectionInput(
        area=1.20,
        inertia=0.45,
        y_top=0.90,
        y_bottom=0.90,
    )

    props = calculate_section_properties(section)

    assert props["A"] == 1.20
    assert props["I"] == 0.45
    assert props["Z_top"] == 0.5
    assert props["Z_bottom"] == 0.5


def test_prestress_force():
    tendon = TendonInput(
        name="19T15.2",
        area=2850.0,
        number=4,
        f_jacking=1395.0,
        profile=[
            (0.0, 0.15),
            (15.0, 0.50),
            (30.0, 0.15),
        ],
    )

    result = calculate_prestress_force(tendon, None)

    assert result["Ap_total"] == 11400.0
    assert result["Pjack_kN"] == 15903.0
    assert result["eccentricity"] == 0.50

if __name__ == "__main__":
    test_material()
    test_section()
    test_prestress_force()
    print("ALL BASIC TESTS PASSED")