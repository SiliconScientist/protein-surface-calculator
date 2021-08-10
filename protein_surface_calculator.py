import os
import freesasa
import numpy as np

taxa = ['psychro', 'thermo']
num_taxa = len(taxa)

# Create empty arrays to contain the ratios or their averages
ratio = [[] for i in range(num_taxa)]
ratio_mean = []

# Loop for each taxa
for i in range(num_taxa):
    # Locate folder for use use
    path = f'/Users/averyhill/MyDocuments/schoeffler_research_summer_2021/pdbs/{taxa[i]}philes/{taxa[i]}_gyra_pdb_folder'
    file_array = os.listdir(path)
    
    # Calculate the surface area of each pdb model
    for pdb in file_array:
        structure = freesasa.Structure(f'{path}/{pdb}')
        result = freesasa.calc(structure)
        area_classes = freesasa.classifyResults(result, structure)
        
        # Calculate the polar to apolar ratio and put them in an array
        ratio[i].append(area_classes['Polar']/area_classes['Apolar'])
        
    # Average the items in each ratio array
    ratio_mean.append(np.mean(ratio[i]))

# Print out statistics
print('Mean ratio:')
print(f'Psychrophiles: {ratio_mean[0]}')
print(f'Thermophiles: {ratio_mean[1]}')
print()
print('Highest ratio:')
print(f'Psychrophiles: {np.max(ratio[0])}')
print(f'Thermophiles: {np.max(ratio[1])}')
print()
print('Lowest ratio:')
print(f'Psychrophiles {np.min(ratio[0])}')
print(f'Thermophiles {np.min(ratio[1])}')