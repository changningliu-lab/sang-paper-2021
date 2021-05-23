#输入：plant_ortholog_genefamily_redundancy_add_linenumber.txt
#输出：>>statistic_conserved_lnc_ratio_of_each_plant.txt
import sys
from collections import defaultdict
file_in = open('plant_ortholog_genefamily_redundancy_add_linenumber.txt', 'r')

all_lnc_num_dict = {'Theobroma_cacao_lncrnas':7459, 'Zea_mays_lncrnas':23512, 'Gossypium_raimondii_lncrnas':6422, 'Malus_domestica_lncrnas':9228, 'Amborella_trichopoda_lncrnas':7074, 'Sorghum_bicolor_lncrnas':6326, 'Arabidopsis_thaliana_lncrnas':5539, 'Musa_acuminata_lncrnas':5121, 'Glycine_max_lncrnas':8817, 'Prunus_persica_lncrnas':4183, 'Manihot_esculenta_lncrnas':7660, 'Solanum_tuberosum_lncrnas':7797, 'Solanum_lycopersicum_lncrnas':6807, 'Brachypodium_distachyon_lncrnas':6783, 'Medicago_truncatula_lncrnas':10904, 'Brassica_rapa_lncrnas':10797, 'Brassica_napus_lncrnas':16597, 'Populus_trichocarpa_lncrnas':8334, 'Citrus_sinensis_lncrnas':3430, 'Cucumis_sativus_lncrnas':5466, 'Vitis_vinifera_lncrnas':6151, 'Arabidopsis_lyrata_lncrnas':9363, 'Fragaria_vesca_lncrnas':3889, 'Oryza_sativa_lncrnas':7211, 'Oryza_brachyantha_lncrnas':4926}

conserved_lnc_num_dict = defaultdict(list)
for line in file_in:
    item = line.strip().split(';')
    lnc_list = item[1:-1]
    for lnc in lnc_list:
        item2 = lnc.split('#')
        species = item2[0]
        lncname = item2[1]
        conserved_lnc_num_dict[species].append(lncname)
#print(conserved_lnc_num_dict['Fragaria_vesca_lncrnas'])
#sys.exit()
for all_species,all_lnc_num in all_lnc_num_dict.items():
    ratio = int(len(conserved_lnc_num_dict[all_species]))/int(all_lnc_num)
    print(all_species+' : '+'%.4f'%ratio)
