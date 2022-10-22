import requests
import json

AvatarExcelConfigData = json.loads(requests.get("https://github.com/Dimbreath/GenshinData/raw/master" \
                                                "/ExcelBinOutput/AvatarExcelConfigData.json").text)
WeaponExcelConfigData = json.loads(requests.get("https://github.com/Dimbreath/GenshinData/raw/master" \
                                                "/ExcelBinOutput/WeaponExcelConfigData.json").text)
chs_dict = json.loads(
    requests.get("https://github.com/Dimbreath/GenshinData/raw/master/TextMap/TextMapCHS.json").text)
en_dict = json.loads(
    requests.get("https://github.com/Dimbreath/GenshinData/raw/master/TextMap/TextMapEN.json").text)

output_dict = {}
item_list = [AvatarExcelConfigData, WeaponExcelConfigData]
for this_list in item_list:
    for item in this_list:
        this_name_hash_id = item["nameTextMapHash"]
        try:
            eng_name = en_dict[str(this_name_hash_id)]
            chs_name = chs_dict[str(this_name_hash_id)]
            output_dict[eng_name] = chs_name
        except KeyError:
            continue

with open("EngToChs.json", "w", encoding="utf-8") as f:
    json.dump(output_dict, f, ensure_ascii=False, indent=4)
