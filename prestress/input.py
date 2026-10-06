from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass
class MaterialInput:
    fc: float
    fpu: float
    Ep: float
    Ec: float
    density_concrete: float = 24.0


@dataclass
class SectionInput:
    area: float
    inertia: float
    y_top: float
    y_bottom: float


@dataclass
class TendonInput:
    name: str
    area: float
    number: int
    f_jacking: float
    profile: List[Tuple[float, float]] = field(default_factory=list)
    bonded: bool = True


@dataclass
class LoadInput:
    dead_load: float = 0.0
    superimposed_dead_load: float = 0.0
    live_load: float = 0.0


@dataclass
class PrestressDesignInput:
    span: float
    material: MaterialInput
    section: SectionInput
    tendon: TendonInput
    loads: LoadInput
    name: str = "Prestress Design"