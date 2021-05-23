#输入1：plant_ortholog_genefamily_rm_redundancy_add_linenumber.txt
#输入2：plant_ortholog_genefamily_redundancy_add_linenumber.txt
#输出：以类似list_2_1命名的20个进化树枝点，文件包含该枝点的所有lncRNAs。
import sys
from collections import defaultdict

branch_point_dict = {('Arabidopsis_thaliana_lncrnas', 'Arabidopsis_lyrata_lncrnas'): 'list_2_1', ('Brassica_rapa_lncrnas', 'Brassica_napus_lncrnas'):'list_2_2', ('Gossypium_raimondii_lncrnas', 'Theobroma_cacao_lncrnas'):'list_2_3', ('Malus_domestica_lncrnas', 'Prunus_persica_lncrnas'):'list_2_4', ('Glycine_max_lncrnas', 'Medicago_truncatula_lncrnas'):'list_2_5', ('Manihot_esculenta_lncrnas', 'Populus_trichocarpa_lncrnas'):'list_2_6', ('Solanum_lycopersicum_lncrnas', 'Solanum_tuberosum_lncrnas'):'list_2_7', ('Oryza_sativa_lncrnas', 'Oryza_brachyantha_lncrnas'):'list_2_8', ('Sorghum_bicolor_lncrnas', 'Zea_mays_lncrnas'):'list_2_9', ('Malus_domestica_lncrnas', 'Prunus_persica_lncrnas', 'Fragaria_vesca_lncrnas'):'list_3', ('Arabidopsis_thaliana_lncrnas', 'Arabidopsis_lyrata_lncrnas', 'Brassica_rapa_lncrnas', 'Brassica_napus_lncrnas'):'list_4', ('Oryza_sativa_lncrnas', 'Oryza_brachyantha_lncrnas', 'Sorghum_bicolor_lncrnas', 'Zea_mays_lncrnas', 'Brachypodium_distachyon_lncrnas'):'list_5', ('Arabidopsis_thaliana_lncrnas', 'Arabidopsis_lyrata_lncrnas', 'Brassica_rapa_lncrnas', 'Brassica_napus_lncrnas', 'Gossypium_raimondii_lncrnas', 'Theobroma_cacao_lncrnas'):'list_6_1', ('Oryza_sativa_lncrnas', 'Oryza_brachyantha_lncrnas', 'Sorghum_bicolor_lncrnas', 'Zea_mays_lncrnas', 'Brachypodium_distachyon_lncrnas', 'Musa_acuminata_lncrnas'):'list_6_2', ('Arabidopsis_thaliana_lncrnas', 'Arabidopsis_lyrata_lncrnas', 'Brassica_rapa_lncrnas', 'Brassica_napus_lncrnas', 'Gossypium_raimondii_lncrnas', 'Theobroma_cacao_lncrnas', 'Citrus_sinensis_lncrnas'):'list_7', ('Arabidopsis_thaliana_lncrnas', 'Arabidopsis_lyrata_lncrnas', 'Brassica_rapa_lncrnas', 'Brassica_napus_lncrnas', 'Gossypium_raimondii_lncrnas', 'Theobroma_cacao_lncrnas', 'Citrus_sinensis_lncrnas', 'Cucumis_sativus_lncrnas', 'Malus_domestica_lncrnas', 'Prunus_persica_lncrnas', 'Fragaria_vesca_lncrnas', 'Glycine_max_lncrnas', 'Medicago_truncatula_lncrnas', 'Manihot_esculenta_lncrnas', 'Populus_trichocarpa_lncrnas'):'list_15', ('Arabidopsis_thaliana_lncrnas', 'Arabidopsis_lyrata_lncrnas', 'Brassica_rapa_lncrnas', 'Brassica_napus_lncrnas', 'Gossypium_raimondii_lncrnas', 'Theobroma_cacao_lncrnas', 'Citrus_sinensis_lncrnas', 'Cucumis_sativus_lncrnas', 'Malus_domestica_lncrnas', 'Prunus_persica_lncrnas', 'Fragaria_vesca_lncrnas', 'Glycine_max_lncrnas', 'Medicago_truncatula_lncrnas', 'Manihot_esculenta_lncrnas', 'Populus_trichocarpa_lncrnas', 'Vitis_vinifera_lncrnas'):'list_16', ('Arabidopsis_thaliana_lncrnas', 'Arabidopsis_lyrata_lncrnas', 'Brassica_rapa_lncrnas', 'Brassica_napus_lncrnas', 'Gossypium_raimondii_lncrnas', 'Theobroma_cacao_lncrnas', 'Citrus_sinensis_lncrnas', 'Cucumis_sativus_lncrnas', 'Malus_domestica_lncrnas', 'Prunus_persica_lncrnas', 'Fragaria_vesca_lncrnas', 'Glycine_max_lncrnas', 'Medicago_truncatula_lncrnas', 'Manihot_esculenta_lncrnas', 'Populus_trichocarpa_lncrnas', 'Vitis_vinifera_lncrnas', 'Solanum_lycopersicum_lncrnas', 'Solanum_tuberosum_lncrnas'):'list_18', ('Arabidopsis_thaliana_lncrnas', 'Arabidopsis_lyrata_lncrnas', 'Brassica_rapa_lncrnas', 'Brassica_napus_lncrnas', 'Gossypium_raimondii_lncrnas', 'Theobroma_cacao_lncrnas', 'Citrus_sinensis_lncrnas', 'Cucumis_sativus_lncrnas', 'Malus_domestica_lncrnas', 'Prunus_persica_lncrnas', 'Fragaria_vesca_lncrnas', 'Glycine_max_lncrnas', 'Medicago_truncatula_lncrnas', 'Manihot_esculenta_lncrnas', 'Populus_trichocarpa_lncrnas', 'Vitis_vinifera_lncrnas', 'Solanum_lycopersicum_lncrnas', 'Solanum_tuberosum_lncrnas', 'Oryza_sativa_lncrnas', 'Oryza_brachyantha_lncrnas', 'Sorghum_bicolor_lncrnas', 'Zea_mays_lncrnas', 'Brachypodium_distachyon_lncrnas', 'Musa_acuminata_lncrnas'):'list_24', ('Theobroma_cacao_lncrnas', 'Zea_mays_lncrnas', 'Gossypium_raimondii_lncrnas', 'Malus_domestica_lncrnas', 'Amborella_trichopoda_lncrnas', 'Sorghum_bicolor_lncrnas', 'Arabidopsis_thaliana_lncrnas', 'Musa_acuminata_lncrnas', 'Glycine_max_lncrnas', 'Prunus_persica_lncrnas', 'Manihot_esculenta_lncrnas', 'Solanum_tuberosum_lncrnas', 'Solanum_lycopersicum_lncrnas', 'Brachypodium_distachyon_lncrnas', 'Medicago_truncatula_lncrnas', 'Brassica_rapa_lncrnas', 'Brassica_napus_lncrnas', 'Populus_trichocarpa_lncrnas', 'Citrus_sinensis_lncrnas', 'Cucumis_sativus_lncrnas', 'Vitis_vinifera_lncrnas', 'Arabidopsis_lyrata_lncrnas', 'Fragaria_vesca_lncrnas', 'Oryza_sativa_lncrnas', 'Oryza_brachyantha_lncrnas'):'list_25'}


file_in = open('plant_ortholog_genefamily_rm_redundancy_add_linenumber.txt', 'r')
file_in2 = open('plant_ortholog_genefamily_redundancy_add_linenumber.txt', 'r')

family_lncRNAlist_dict = {}
for line in file_in2:
    item2 = line.strip().split(';')
    list_rm_first2 = item2[1:-1]
    ortholog_linenumber2 = item2[0].split()[0]
    family_lncRNAlist_dict[ortholog_linenumber2] = list_rm_first2

Branchpoint_families_dict = defaultdict(list)
for line in file_in:
    item = line.strip().split(';')
    list_rm_first = item[1:]
    ortholog_linenumber = item[0].split()[0]
    tem_length = 26
    for key,value in branch_point_dict.items():
        intersection_list = list(set(list_rm_first).intersection(set(key)))
        if len(intersection_list) == len(list_rm_first):
            key_length = len(key)
            if key_length < tem_length:
                tem_length = key_length
                final_tuple = key
    list_num = branch_point_dict[final_tuple]
    Branchpoint_families_dict[list_num].append(ortholog_linenumber)

for key,value in Branchpoint_families_dict.items():
    file_out = open(key + '_lncRNAs.txt', 'w')
    for linenum in value:
        file_out.write('\n'.join(family_lncRNAlist_dict[linenum]) + '\n')
    file_out.close()


file_in.close()
file_in2.close()