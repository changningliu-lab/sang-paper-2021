#输入：plant_ortholog_genefamily_rm_redundancy.txt
#输出：plant_branch_point_ortholog_genefamily_num_statistics_methods1.txt
import sys
from collections import defaultdict 
list_2_1 = ['list_2_1', 'Arabidopsis_thaliana_lncrnas', 'Arabidopsis_lyrata_lncrnas']
list_2_2 = ['list_2_2', 'Brassica_rapa_lncrnas', 'Brassica_napus_lncrnas']
list_2_3 = ['list_2_3', 'Gossypium_raimondii_lncrnas', 'Theobroma_cacao_lncrnas']
list_2_4 = ['list_2_4', 'Malus_domestica_lncrnas', 'Prunus_persica_lncrnas']
list_2_5 = ['list_2_5', 'Glycine_max_lncrnas', 'Medicago_truncatula_lncrnas']
list_2_6 = ['list_2_6', 'Manihot_esculenta_lncrnas', 'Populus_trichocarpa_lncrnas']
list_2_7 = ['list_2_7', 'Solanum_lycopersicum_lncrnas', 'Solanum_tuberosum_lncrnas']
list_2_8 = ['list_2_8', 'Oryza_sativa_lncrnas', 'Oryza_brachyantha_lncrnas']
list_2_9 = ['list_2_9', 'Sorghum_bicolor_lncrnas', 'Zea_mays_lncrnas']
list_3 = ['list_3', 'Malus_domestica_lncrnas', 'Prunus_persica_lncrnas', 'Fragaria_vesca_lncrnas']
list_4 = ['list_4', 'Arabidopsis_thaliana_lncrnas', 'Arabidopsis_lyrata_lncrnas', 'Brassica_rapa_lncrnas', 'Brassica_napus_lncrnas']
list_5 = ['list_5', 'Oryza_sativa_lncrnas', 'Oryza_brachyantha_lncrnas', 'Sorghum_bicolor_lncrnas', 'Zea_mays_lncrnas', 'Brachypodium_distachyon_lncrnas']
list_6_1 = ['list_6_1', 'Arabidopsis_thaliana_lncrnas', 'Arabidopsis_lyrata_lncrnas', 'Brassica_rapa_lncrnas', 'Brassica_napus_lncrnas', 'Gossypium_raimondii_lncrnas', 'Theobroma_cacao_lncrnas']
list_6_2 = ['list_6_2', 'Oryza_sativa_lncrnas', 'Oryza_brachyantha_lncrnas', 'Sorghum_bicolor_lncrnas', 'Zea_mays_lncrnas', 'Brachypodium_distachyon_lncrnas', 'Musa_acuminata_lncrnas']
list_7 = ['list_7', 'Arabidopsis_thaliana_lncrnas', 'Arabidopsis_lyrata_lncrnas', 'Brassica_rapa_lncrnas', 'Brassica_napus_lncrnas', 'Gossypium_raimondii_lncrnas', 'Theobroma_cacao_lncrnas', 'Citrus_sinensis_lncrnas']
list_15 = ['list_15', 'Arabidopsis_thaliana_lncrnas', 'Arabidopsis_lyrata_lncrnas', 'Brassica_rapa_lncrnas', 'Brassica_napus_lncrnas', 'Gossypium_raimondii_lncrnas', 'Theobroma_cacao_lncrnas', 'Citrus_sinensis_lncrnas', 'Cucumis_sativus_lncrnas', 'Malus_domestica_lncrnas', 'Prunus_persica_lncrnas', 'Fragaria_vesca_lncrnas', 'Glycine_max_lncrnas', 'Medicago_truncatula_lncrnas', 'Manihot_esculenta_lncrnas', 'Populus_trichocarpa_lncrnas']
list_16 = ['list_16', 'Arabidopsis_thaliana_lncrnas', 'Arabidopsis_lyrata_lncrnas', 'Brassica_rapa_lncrnas', 'Brassica_napus_lncrnas', 'Gossypium_raimondii_lncrnas', 'Theobroma_cacao_lncrnas', 'Citrus_sinensis_lncrnas', 'Cucumis_sativus_lncrnas', 'Malus_domestica_lncrnas', 'Prunus_persica_lncrnas', 'Fragaria_vesca_lncrnas', 'Glycine_max_lncrnas', 'Medicago_truncatula_lncrnas', 'Manihot_esculenta_lncrnas', 'Populus_trichocarpa_lncrnas', 'Vitis_vinifera_lncrnas']
list_18 = ['list_18', 'Arabidopsis_thaliana_lncrnas', 'Arabidopsis_lyrata_lncrnas', 'Brassica_rapa_lncrnas', 'Brassica_napus_lncrnas', 'Gossypium_raimondii_lncrnas', 'Theobroma_cacao_lncrnas', 'Citrus_sinensis_lncrnas', 'Cucumis_sativus_lncrnas', 'Malus_domestica_lncrnas', 'Prunus_persica_lncrnas', 'Fragaria_vesca_lncrnas', 'Glycine_max_lncrnas', 'Medicago_truncatula_lncrnas', 'Manihot_esculenta_lncrnas', 'Populus_trichocarpa_lncrnas', 'Vitis_vinifera_lncrnas', 'Solanum_lycopersicum_lncrnas', 'Solanum_tuberosum_lncrnas']
list_24 = ['list_24', 'Arabidopsis_thaliana_lncrnas', 'Arabidopsis_lyrata_lncrnas', 'Brassica_rapa_lncrnas', 'Brassica_napus_lncrnas', 'Gossypium_raimondii_lncrnas', 'Theobroma_cacao_lncrnas', 'Citrus_sinensis_lncrnas', 'Cucumis_sativus_lncrnas', 'Malus_domestica_lncrnas', 'Prunus_persica_lncrnas', 'Fragaria_vesca_lncrnas', 'Glycine_max_lncrnas', 'Medicago_truncatula_lncrnas', 'Manihot_esculenta_lncrnas', 'Populus_trichocarpa_lncrnas', 'Vitis_vinifera_lncrnas', 'Solanum_lycopersicum_lncrnas', 'Solanum_tuberosum_lncrnas', 'Oryza_sativa_lncrnas', 'Oryza_brachyantha_lncrnas', 'Sorghum_bicolor_lncrnas', 'Zea_mays_lncrnas', 'Brachypodium_distachyon_lncrnas', 'Musa_acuminata_lncrnas']
list_25 = ['list_25', 'Theobroma_cacao_lncrnas', 'Zea_mays_lncrnas', 'Gossypium_raimondii_lncrnas', 'Malus_domestica_lncrnas', 'Amborella_trichopoda_lncrnas', 'Sorghum_bicolor_lncrnas', 'Arabidopsis_thaliana_lncrnas', 'Musa_acuminata_lncrnas', 'Glycine_max_lncrnas', 'Prunus_persica_lncrnas', 'Manihot_esculenta_lncrnas', 'Solanum_tuberosum_lncrnas', 'Solanum_lycopersicum_lncrnas', 'Brachypodium_distachyon_lncrnas', 'Medicago_truncatula_lncrnas', 'Brassica_rapa_lncrnas', 'Brassica_napus_lncrnas', 'Populus_trichocarpa_lncrnas', 'Citrus_sinensis_lncrnas', 'Cucumis_sativus_lncrnas', 'Vitis_vinifera_lncrnas', 'Arabidopsis_lyrata_lncrnas', 'Fragaria_vesca_lncrnas', 'Oryza_sativa_lncrnas', 'Oryza_brachyantha_lncrnas']
list_all = [list_2_1, list_2_2, list_2_3, list_2_4, list_2_5, list_2_6, list_2_7, list_2_8, list_2_9, list_3, list_4, list_5, list_6_1, list_6_2, list_7, list_15, list_16, list_18, list_24, list_25]

file_in = open('plant_ortholog_genefamily_rm_redundancy.txt', 'r')
file_out = open('plant_branch_point_ortholog_genefamily_num_statistics_methods1.txt', 'w')
Branch_point_num = {}
for line in file_in:
    item = line.strip().split(';')
    list_rm_first = item[1:]
    for list_num in list_all:
        list_tem = []      
        list_num_length = len(list_num)
        for species in list_num:
            if species in list_rm_first:
                list_tem.append(species)
        list_tem_length = len(list_tem)
        if list_num_length - list_tem_length == 1:
            if list_num[0] in Branch_point_num:
                Branch_point_num[list_num[0]] = Branch_point_num[list_num[0]] + 1
            else:
                Branch_point_num[list_num[0]] = 1

for key,value in Branch_point_num.items():
    file_out.write('\t'.join([key, str(value)]))
    file_out.write('\n')

file_in.close()
file_out.close()