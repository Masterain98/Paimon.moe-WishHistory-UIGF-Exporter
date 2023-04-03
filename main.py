import time

import pandas as pd
import json
import requests
import os
from uigfTools import uigf_gacha_type_generator

# 打印提示
print("正在生成翻译表...")

# 读取角色和武器的ID对照表
item_dict = json.loads(requests.get("https://api.uigf.org/dict/en.json").text)

# 生成翻译表
AvatarExcelConfigData = json.loads(
    requests.get("https://genshin-data.uigf.org/d/latest/ExcelBinOutput/AvatarExcelConfigData.json").text)
WeaponExcelConfigData = json.loads(
    requests.get("https://genshin-data.uigf.org/d/latest/ExcelBinOutput/WeaponExcelConfigData.json").text)
chs_dict = json.loads(
    requests.get("https://genshin-data.uigf.org/d/latest/TextMap/TextMapCHS.json").text)
en_dict = json.loads(
    requests.get("https://genshin-data.uigf.org/d/latest/TextMap/TextMapEN.json").text)

eng_to_chs_dict = {}
item_list = [AvatarExcelConfigData, WeaponExcelConfigData]
for this_list in item_list:
    for item in this_list:
        this_name_hash_id = item["nameTextMapHash"]
        try:
            eng_name = en_dict[str(this_name_hash_id)]
            chs_name = chs_dict[str(this_name_hash_id)]
            eng_to_chs_dict[eng_name] = chs_name
        except KeyError:
            continue
print("翻译表生成完成")


def type_translate(x: str) -> str:
    if x == "Weapon":
        return "武器"
    elif x == "Character":
        return "角色"
    else:
        return ""


def item_id_converter(x: str) -> int:
    if x in item_dict.keys():
        return item_dict[x]
    print("转换物品 ID 错误： " + x)
    return 0


def UIGF_Converter(file_name, UID):
    debug = False

    print("正在转换文件： " + file_name)
    if file_name[0] == "\"":
        file_name = file_name.replace("\"", "")
        if debug:
            print("New file name: " + file_name)

    # 加载 Paimon.moe的祈愿导出Excel文件
    df1 = pd.read_excel(file_name, sheet_name="Character Event")
    df2 = pd.read_excel(file_name, sheet_name="Weapon Event")
    df3 = pd.read_excel(file_name, sheet_name="Standard")
    df4 = pd.read_excel(file_name, sheet_name="Beginners' Wish")

    # 角色活动祈愿
    # 翻译名称
    df1["item_id"] = df1.Name.apply(lambda x: item_dict[x])
    df1["name"] = df1.Name.apply(lambda x: eng_to_chs_dict[x])
    df1.drop(columns=['Name'], inplace=True)
    # 翻译种类
    df1["item_type"] = df1.Type.apply(lambda x: type_translate(x))
    df1.drop(columns=['Type'], inplace=True)
    # 创建稀有度列
    df1["rank_type"] = df1["⭐"]
    df1.drop(columns=['⭐'], inplace=True)
    # 通过卡池信息判定gacha_type
    df1["gacha_type"] = df1.apply(lambda x: uigf_gacha_type_generator(x), axis=1)
    df1.drop(columns=['Banner'], inplace=True)
    # 增加uigf_gacha_type列
    df1["uigf_gacha_type"] = str(301)

    # 武器活动祈愿
    # 翻译名称
    df2["item_id"] = df2.Name.apply(lambda x: item_id_converter(x))
    df2["name"] = df2.Name.apply(lambda x: eng_to_chs_dict[x])
    df2.drop(columns=['Name'], inplace=True)
    # 翻译种类
    df2["item_type"] = df2.Type.apply(lambda x: type_translate(x))
    df2.drop(columns=['Type'], inplace=True)
    # 创建稀有度列
    df2["rank_type"] = df2["⭐"]
    df2.drop(columns=['⭐'], inplace=True)
    # 创建gacha_type列
    df2["gacha_type"] = str(302)
    df2["uigf_gacha_type"] = str(302)
    df2.drop(columns=['Banner'], inplace=True)

    # 常驻祈愿
    # 翻译名称
    df3["item_id"] = df3.Name.apply(lambda x: item_id_converter(x))
    df3["name"] = df3.Name.apply(lambda x: eng_to_chs_dict[x])
    df3.drop(columns=['Name'], inplace=True)
    # 翻译种类
    df3["item_type"] = df3.Type.apply(lambda x: type_translate(x))
    df3.drop(columns=['Type'], inplace=True)
    # 创建稀有度列
    df3["rank_type"] = df3["⭐"]
    df3.drop(columns=['⭐'], inplace=True)
    # 创建gacha_type列
    df3["gacha_type"] = str(200)
    df3["uigf_gacha_type"] = str(200)
    df3.drop(columns=['Banner'], inplace=True)

    # 新手祈愿
    # 翻译名称
    df4["item_id"] = df4.Name.apply(lambda x: item_id_converter(x))
    df4["name"] = df4.Name.apply(lambda x: eng_to_chs_dict[x])
    df4.drop(columns=['Name'], inplace=True)
    # 翻译种类
    df4["item_type"] = df4.Type.apply(lambda x: type_translate(x))
    df4.drop(columns=['Type'], inplace=True)
    # 创建稀有度列
    df4["rank_type"] = df4["⭐"]
    df4.drop(columns=['⭐'], inplace=True)
    # 创建gacha_type列
    df4["gacha_type"] = str(100)
    df4["uigf_gacha_type"] = str(100)
    df4.drop(columns=['Banner'], inplace=True)

    # 连接DF
    MergedDF = [df1, df2, df3, df4]
    MergedDF = pd.concat(MergedDF)
    MergedDF.reset_index(inplace=True)
    MergedDF.drop(columns='index', inplace=True)
    # 删除无用列
    MergedDF["time"] = MergedDF["Time"]
    MergedDF.drop(columns=['Time'], inplace=True)
    MergedDF.sort_values(by=['time'], ascending=True, inplace=True)
    MergedDF.drop(columns=['Pity', '#Roll', 'Group'], inplace=True)
    # 添加杂项列
    MergedDF["uid"] = ""
    MergedDF["lang"] = "zh-cn"
    MergedDF["count"] = "1"
    MergedDF["id"] = ""
    # 创建id
    first_id = 1612303200000000000 - MergedDF.shape[0]
    MergedDF['id'] = first_id + MergedDF.index
    # 重置数据类型
    MergedDF['count'] = MergedDF['count'].astype(str)
    MergedDF['gacha_type'] = MergedDF['gacha_type'].astype(str)
    MergedDF['id'] = MergedDF['id'].astype(str)
    MergedDF['lang'] = MergedDF['lang'].astype(str)
    MergedDF['name'] = MergedDF['name'].astype(str)
    MergedDF['item_id'] = MergedDF['item_id'].astype(str)
    MergedDF['rank_type'] = MergedDF['rank_type'].astype(str)
    MergedDF['time'] = MergedDF['time'].astype(str)
    MergedDF['uid'] = MergedDF['uid'].astype(str)
    MergedDF['uigf_gacha_type'] = MergedDF['uigf_gacha_type'].astype(str)
    # 修改列顺序
    MergedDF = MergedDF[["count", "gacha_type", "id", "item_type", "lang", "item_id", "name",
                         "rank_type", "time", "uid", "uigf_gacha_type"]]

    # 创建 UIGF Excel
    new_file_name = "uigf_" + str(UID) + ".xlsx"
    MergedDF.to_excel(new_file_name, sheet_name='原始数据', index=False)

    # 创建 UIGF JSON
    json_output = {
        "info": {
            "uid": UID,
            "lang": "zh-cn",
            "export_timestamp": int(time.time()),
            "export_app": "Paimon.moe-WishHistory-UIGF-Exporter",
            "export_app_version": "1.0.0",
            "uigf_version": "v2.2"
        }
    }
    output_list = []
    for index, row in MergedDF.iterrows():
        this_row_data = {
            "uigf_gacha_type": row["uigf_gacha_type"],
            "gacha_type": row["gacha_type"],
            "name": row["name"],
            "item_id": row["item_id"],
            "count": row["count"],
            "time": row["time"],
            "rank_type": row["rank_type"],
            "id": row["id"],
            "item_type": row["item_type"]
        }
        output_list.append(this_row_data)
    json_output["list"] = output_list
    with open("uigf_" + str(UID) + ".json", "w", encoding="utf-8") as f:
        json.dump(json_output, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    print("=" * 20)
    print("Paimon.moe UIGF Converter")
    print("版本：1.0.0")
    print("发布于：https://github.com/Masterain98/Paimon.moe-WishHistory-UIGF-Exporter")
    print("=" * 20)
    print("本工具用于Paimon.moe导出的Excel格式祈愿记录向UIGF格式转化")
    print("UIGF-org: https://uigf.org/")
    print("=" * 20)
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    if "paimonmoe_wish_history.xlsx" in files:
        print("检测到 paimonmoe_wish_history.xlsx 文件")
        original_xlsx_name = "./paimonmoe_wish_history.xlsx"
    else:
        original_xlsx_name = input("请输入原始Excel文件路径：")
    user_uid_input = input("请输入UID：")
    print("=" * 20)
    try:
        UIGF_Converter(original_xlsx_name, user_uid_input)
        input("Excel转换已结束，按任意键退出...")
    except FileNotFoundError:
        input("文件名错误，请尝试将原始Excel修改为较为简单的名称...")
    except Exception as err:
        print("主程序发生意外错误，请联系开发者")
        input(err)
