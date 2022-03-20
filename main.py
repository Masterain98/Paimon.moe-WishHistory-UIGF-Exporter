import pandas as pd
import json
from datetime import datetime
from uigfTools import uigfGachaTypeGenerator


def type_translate(x):
    if x == "Weapon":
        return "武器"
    elif x == "Character":
        return "角色"
    else:
        return ""


def UIGF_Converter(fileName, UID):
    debug = False

    print("正在转换文件： " + fileName)
    if fileName[0] == "\"":
        fileName = fileName.replace("\"", "")
        if debug:
            print("New file name: " + fileName)

    # 加载Paimon.moe的祈愿导出Excel文件
    df1 = pd.read_excel(fileName, sheet_name="Character Event")
    df2 = pd.read_excel(fileName, sheet_name="Weapon Event")
    df3 = pd.read_excel(fileName, sheet_name="Standard")
    df4 = pd.read_excel(fileName, sheet_name="Beginners' Wish")

    with open("zh.json", 'r') as load_f:
        zh_dict = json.load(load_f)

    # 角色活动祈愿
    # 翻译名称
    df1["name"] = df1.Name.apply(lambda x: zh_dict[x])
    df1.drop(columns=['Name'], inplace=True)
    # 翻译种类
    df1["item_type"] = df1.Type.apply(lambda x: type_translate(x))
    df1.drop(columns=['Type'], inplace=True)
    # 创建稀有度列
    df1["rank_type"] = df1["⭐"]
    df1.drop(columns=['⭐'], inplace=True)
    # 通过卡池信息判定gacha_type
    df1["gacha_type"] = df1.apply(lambda x: uigfGachaTypeGenerator(x), axis=1)
    df1.drop(columns=['Banner'], inplace=True)
    # 增加uigf_gacha_type列
    df1["uigf_gacha_type"] = str(301)

    # 武器活动祈愿
    # 翻译名称
    df2["name"] = df2.Name.apply(lambda x: zh_dict[x])
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
    df3["name"] = df3.Name.apply(lambda x: zh_dict[x])
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
    df4["name"] = df4.Name.apply(lambda x: zh_dict[x])
    df4.drop(columns=['Name'], inplace=True)
    # 翻译种类
    df4["item_type"] = df4.Type.apply(lambda x: type_translate(x))
    df4.drop(columns=['Type'], inplace=True)
    # 创建稀有度列
    df4["rank_type"] = df4["⭐"]
    df4.drop(columns=['⭐'], inplace=True)
    # 创建gacha_type列
    df4["gacha_type"] = str(200)
    df4["uigf_gacha_type"] = str(200)
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
    MergedDF["lang"] = ""
    MergedDF["item_id"] = ""
    MergedDF["count"] = ""
    MergedDF["id"] = ""
    # 创建id
    firstID = 1612303200000000000 - MergedDF.shape[0]
    MergedDF['id'] = firstID + MergedDF.index
    # 重置数据类型
    MergedDF['count'] = MergedDF['count'].astype(str)
    MergedDF['gacha_type'] = MergedDF['gacha_type'].astype(str)
    MergedDF['id'] = MergedDF['id'].astype(str)
    MergedDF['lang'] = MergedDF['lang'].astype(str)
    MergedDF['name'] = MergedDF['name'].astype(str)
    MergedDF['rank_type'] = MergedDF['rank_type'].astype(str)
    MergedDF['time'] = MergedDF['time'].astype(str)
    MergedDF['uid'] = MergedDF['uid'].astype(str)
    MergedDF['uigf_gacha_type'] = MergedDF['uigf_gacha_type'].astype(str)
    # 修改列顺序
    MergedDF = MergedDF[["count", "gacha_type", "id", "item_id", "item_type", "lang", "name",
               "rank_type", "time", "uid", "uigf_gacha_type"]]

    # 创建 UIGF Excel
    new_file_name = "uigf_" + str(UID) + ".xlsx"
    MergedDF.to_excel(new_file_name, sheet_name='原始数据', index=False)


if __name__ == "__main__":
    UIGF_Converter("paimonmoe_wish_history.xlsx", "107847862")