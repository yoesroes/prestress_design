# prestress_design

Standalone Python library for analysis and design of prestressed concrete bridge girders.

## Scope

The project focuses on the local analysis and design of prestressed concrete girders:

- Section properties
- Concrete and prestressing steel materials
- Tendon geometry
- Prestressing force
- Prestress losses
- Transfer condition
- Serviceability
- Camber and deflection
- Flexural strength
- Shear strength
- Multiple tendon groups
- Design checks based on applicable standards

## Out of Scope

The following are intentionally outside this repository:

- Global bridge analysis
- Grillage modelling
- Moving-load distribution
- Piers and abutments
- Foundations and piles
- Scaffolding and temporary works
- Reinforcement detailing
- CAD/drawing generation

## Development Phases

1. Project foundation
2. Section properties
3. Tendon geometry and prestress force
4. Prestress losses
5. Transfer and service checks
6. Camber and deflection
7. Flexural strength
8. Shear strength
9. Multiple tendon groups
10. Integration with global bridge analysis

## Current Status

Early development — foundational section, tendon, and prestress calculations are being implemented.

## Project Structure

```text
prestress_design/
├── prestress/
├── tests/
├── examples/
├── docs/
├── README.md
├── requirements.txt
└── .gitignore
