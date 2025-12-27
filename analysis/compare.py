#!/usr/bin/env python3
"""
Compare sustainability of piping materials based on CSV data.
Calculates a Sustainability Score for each material and ranks them.
"""

import csv
import os
import sys

def calculate_sustainability_score(row):
    """Calculate a simple sustainability score based on material parameters."""
    # Convert values from CSV strings to appropriate types
    renewable = float(row['Renewable_Content_Percent'])
    lifespan = float(row['Average_Lifespan_years'])
    recyclability = float(row['Recyclability_Percent'])
    energy = float(row['Estimated_Production_Energy_MJ_per_kg'])
    carbon = float(row['Estimated_Carbon_Footprint_kg_CO2e_per_kg'])
    
    # Weighting factors (can be adjusted)
    w_renewable = 0.2
    w_lifespan = 0.03   # lifespan in years, scale factor to bring to similar magnitude
    w_recyclability = 0.3
    w_energy = -0.01    # negative because higher energy is worse
    w_carbon = -0.2     # negative because higher carbon footprint is worse
    
    score = (renewable * w_renewable +
             lifespan * w_lifespan +
             recyclability * w_recyclability +
             energy * w_energy +
             carbon * w_carbon)
    return score

def main():
    csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'material_data.csv')
    if not os.path.exists(csv_path):
        print(f"Error: CSV file not found at {csv_path}", file=sys.stderr)
        sys.exit(1)
    
    materials = []
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            score = calculate_sustainability_score(row)
            materials.append({
                'name': row['Material_Name'],
                'score': score,
                'raw': row
            })
    
    # Sort by score descending (higher score = more sustainable)
    materials_sorted = sorted(materials, key=lambda x: x['score'], reverse=True)
    
    print("Sustainability Ranking of Piping Materials")
    print("=" * 50)
    for i, mat in enumerate(materials_sorted, start=1):
        print(f"{i}. {mat['name']}: {mat['score']:.2f}")
        # Optionally show details
        # print(f"   Renewable: {mat['raw']['Renewable_Content_Percent']}%, Lifespan: {mat['raw']['Average_Lifespan_years']} yrs, Recyclability: {mat['raw']['Recyclability_Percent']}%")
        # print(f"   Production Energy: {mat['raw']['Estimated_Production_Energy_MJ_per_kg']} MJ/kg, Carbon: {mat['raw']['Estimated_Carbon_Footprint_kg_CO2e_per_kg']} kg CO2e/kg")
    print("\n(Note: Higher score indicates better sustainability based on weighted factors)")

if __name__ == '__main__':
    main()