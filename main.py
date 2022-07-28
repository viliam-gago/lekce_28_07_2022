# zadana_cisla = []
# while True:
#     vstup = input("Zadej cislo: ")
#
#     if vstup.isdigit():
#         zadana_cisla.append(int(vstup))
#         print('Zadana cisla:')
#         print(zadana_cisla)
#
#         prumer = sum(zadana_cisla) / len(zadana_cisla)
#         print(f"Prumer je {prumer}", end='\n')
#
#     elif vstup == "q":
#         break


# ceny = {'banan': 8, "jabko": 6, "boruvky": 30, "chleba": 25, "rohlik": 3, "mineralka": 12, "pivo": 15, "syr": 20, "sunka": 25, "mouka": 20}
#
# transakce = {
#     "t1": ["banan", "banan", "banan", "chleba", "rohlik", "rohlik"],
#     "t2": ["mineralka", "syr", "banan", "boruvky", "rohlik", "sunka"],
#     "t3": ["mineralka", "syr", "banan", "boruvky", "rohlik", "sunka"],
#     "t4": ["jabko","jabko","jabko","jabko", "pivo", "syr"],
#     "t5": ["pivo"],
#     "t6": ["pivo", "pivo", "pivo", "pivo", "sunka"],
#     "t7": ["boruvky", "banan", "banan", "jabko"]
# }
#
#
# # celkova trzba
# hodnoty = []
# for t in transakce:
#
#     kosik = transakce[t]
#
#     for polozka in kosik:
#         hodnoty.append(ceny[polozka])
#
# print(sum(hodnoty))
#
# ## trzba pres transakce
# for t in transakce:
#     hodnoty = []
#     kosik = transakce[t]
#
#     for polozka in kosik:
#         hodnoty.append(ceny[polozka])
#
#     print(sum(hodnoty))

# a = 54161
# if a < 100:
#
# x = [1,2,3,45,6,5,49]
# for cislo in x:
#     if cislo < 6:
#         print(cislo)