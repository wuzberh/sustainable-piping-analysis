# Sustainable Piping Analysis Tool

A tool for comparing the sustainability metrics of common piping materials, including PVC, copper, and HDPE.

## Overview

This project provides a simple framework to evaluate the environmental impact of different piping materials used in construction and manufacturing. It calculates a "Sustainability Score" based on key parameters such as renewable content, production energy, carbon footprint, lifespan, and recyclability.

## Data

Material data is stored in `data/material_data.csv` with the following columns:

- `Material_Name`: Name of the piping material (e.g., PVC, Copper, PEX)
- `Primary_Raw_Material`: Primary raw material source (e.g., "Salt & Oil", "Copper Ore")
- `Renewable_Content_Percent`: Percentage of renewable content in the material (0‑100)
- `Estimated_Production_Energy_MJ_per_kg`: Estimated energy required to produce 1 kg of material (MJ)
- `Estimated_Carbon_Footprint_kg_CO2e_per_kg`: Estimated carbon footprint per kg of material (kg CO2‑equivalent)
- `Average_Lifespan_years`: Expected service life in years
- `Recyclability_Percent`: Percentage of material that can be recycled at end‑of‑life (0‑100)

The CSV currently contains illustrative data for PVC, Copper, and PEX. The numbers are approximate and intended for demonstration purposes.

## Methodology

The Sustainability Score is computed by a weighted linear combination of the five numeric parameters. Positive factors (renewable content, lifespan, recyclability) increase the score, while negative factors (production energy, carbon footprint) decrease it.

The current weighting scheme is:

- Renewable content: **+0.20** per percentage point
- Lifespan: **+0.03** per year
- Recyclability: **+0.30** per percentage point
- Production energy: **‑0.01** per MJ/kg
- Carbon footprint: **‑0.20** per kg CO2e/kg

Thus, the score is calculated as:

```
Score = (Renewable_Content_Percent × 0.20)
      + (Average_Lifespan_years × 0.03)
      + (Recyclability_Percent × 0.30)
      - (Estimated_Production_Energy_MJ_per_kg × 0.01)
      - (Estimated_Carbon_Footprint_kg_CO2e_per_kg × 0.20)
```

These weights are arbitrary but chosen to produce a plausible ranking that reflects typical sustainability priorities (e.g., recyclability and renewable content are emphasized, while carbon footprint is penalized heavily). The weights can be easily adjusted in the script `analysis/compare.py`.

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/wuzberh/sustainable-piping-analysis.git
   cd sustainable-piping-analysis
   ```

2. Ensure you have Python 3 installed (no additional packages are required).

3. Run the comparison script:

   ```bash
   python analysis/compare.py
   ```

   The script will read the CSV file, compute scores for each material, and print a ranked list from most sustainable to least sustainable.

## Example Output

```
Sustainability Ranking of Piping Materials
==================================================
1. Copper: 27.60
2. PVC: 6.20
3. PEX: 5.10
(Note: Higher score indicates better sustainability based on weighted factors)
```

## Project Structure

- `data/material_data.csv` – dataset of material properties
- `analysis/compare.py` – Python script that performs the analysis
- `README.md` – this documentation

## Future Enhancements

Potential improvements include:

- Adding more materials (e.g., galvanized steel, cast iron, ABS)
- Incorporating performance metrics (pressure rating, temperature resistance)
- Using more sophisticated scoring methods (multi‑criteria decision analysis)
- Validating data with reliable sources
- Creating visualizations (bar charts, radar plots)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with proposed changes.

## License

This project is licensed under the MIT License – see the LICENSE file (if present) for details.