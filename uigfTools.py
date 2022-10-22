from datetime import datetime


def uigf_gacha_type_generator(row):
    gacha_time = datetime.strptime(row["Time"], "%Y-%m-%d %H:%M:%S")
    banner_name = row["Banner"]
    gacha_type = 0
    if banner_name == "Ballad in Goblets":
        # 温迪
        gacha_type = 1
        if datetime(2020, 9, 28, 0, 0, 0) < gacha_time < datetime(2020, 10, 18, 18, 0, 0):
            gacha_type = 301
        elif datetime(2021, 3, 17, 6, 0, 0) < gacha_time < datetime(2021, 4, 6, 16, 0, 0):
            gacha_type = 301
        elif datetime(2022, 3, 30, 6, 0, 0) < gacha_time < datetime(2022, 4, 19, 17, 59, 59):
            gacha_type = 400
        elif datetime(2022, 9, 28, 6, 0, 0) < gacha_time < datetime(2022, 10, 14, 17, 59, 59):
            gacha_type = 400
    elif banner_name == "Sparkling Steps":
        # 可莉
        gacha_type = 1
        if datetime(2020, 10, 20, 18, 0, 0) < gacha_time < datetime(2020, 11, 10, 16, 0, 0):
            gacha_type = 301
        elif datetime(2021, 6, 9, 6, 0, 0) < gacha_time < datetime(2021, 6, 29, 17, 59, 59):
            gacha_type = 301
        elif datetime(2022, 7, 13, 6, 0, 0) < gacha_time < datetime(2022, 8, 2, 17, 59, 59):
            gacha_type = 400
    elif banner_name == "Farewell of Snezhnaya":
        # 公子
        gacha_type = 1
        if datetime(2020, 11, 11, 6, 0, 0) < gacha_time < datetime(2020, 12, 1, 16, 0, 0):
            gacha_type = 301
        elif datetime(2021, 4, 6, 18, 0, 0) < gacha_time < datetime(2021, 4, 27, 15, 0, 0):
            gacha_type = 301
        elif datetime(2021, 10, 13, 6, 0, 0) < gacha_time < datetime(2021, 11, 2, 17, 59, 59):
            gacha_type = 301
    elif banner_name == "Gentry of Hermitage":
        # 钟离
        gacha_type = 1
        if datetime(2020, 12, 1, 18, 0, 0) < gacha_time < datetime(2020, 12, 22, 15, 0, 0):
            gacha_type = 301
        elif datetime(2021, 4, 28, 6, 0, 0) < gacha_time < datetime(2021, 5, 18, 17, 59, 59):
            gacha_type = 301
        elif datetime(2022, 1, 25, 18, 0, 0) < gacha_time < datetime(2022, 2, 15, 14, 59, 59):
            gacha_type = 301
        if datetime(2022, 8, 24, 6, 0, 0) < gacha_time < datetime(2022, 9, 9, 17, 59, 59):
            gacha_type = 400
    elif banner_name == "Secretum Secretorum":
        # 阿贝多
        gacha_type = 1
        if datetime(2020, 12, 23, 6, 0, 0) < gacha_time < datetime(2021, 1, 12, 16, 0, 0):
            gacha_type = 301
        elif datetime(2021, 11, 24, 6, 0, 0) < gacha_time < datetime(2021, 12, 14, 17, 59, 59):
            gacha_type = 301
        elif datetime(2022, 10, 14, 18, 0, 0) < gacha_time < datetime(2022, 11, 1, 14, 59, 59):
            gacha_type = 400
    elif banner_name == "Adrift in the Harbor":
        # 甘雨
        gacha_type = 1
        if datetime(2021, 1, 12, 18, 0, 0) < gacha_time < datetime(2021, 2, 2, 15, 0, 0):
            gacha_type = 301
        elif datetime(2022, 1, 25, 18, 0, 0) < gacha_time < datetime(2022, 2, 15, 14, 59, 59):
            gacha_type = 400
        elif datetime(2022, 9, 9, 18, 0, 0) < gacha_time < datetime(2022, 9, 27, 14, 59, 59):
            gacha_type = 301
    elif banner_name == "Invitation to Mundane Life":
        # 魈
        gacha_type = 1
        if datetime(2021, 2, 3, 6, 0, 0) < gacha_time < datetime(2021, 2, 17, 16, 0, 0):
            gacha_type = 301
        elif datetime(2022, 1, 5, 6, 0, 0) < gacha_time < datetime(2022, 1, 25, 17, 59, 59):
            gacha_type = 400
        elif datetime(2022, 5, 31, 9, 0, 0) < gacha_time < datetime(2022, 6, 21, 17, 59, 59):
            gacha_type = 400
    elif banner_name == "Dance of Lanterns":
        # 刻晴
        gacha_type = 1
        if datetime(2021, 2, 17, 18, 0, 0) < gacha_time < datetime(2021, 3, 2, 16, 0, 0):
            gacha_type = 301
    elif banner_name == "Moment of Bloom":
        # 胡桃
        gacha_type = 1
        if datetime(2021, 3, 2, 18, 0, 0) < gacha_time < datetime(2021, 3, 16, 15, 0, 0):
            gacha_type = 301
        elif datetime(2021, 11, 2, 18, 0, 0) < gacha_time < datetime(2021, 11, 23, 14, 59, 59):
            gacha_type = 301
    elif banner_name == "Born of Ocean Swell":
        # 优菈
        gacha_type = 1
        if datetime(2021, 5, 18, 18, 0, 0) < gacha_time < datetime(2021, 6, 8, 15, 0, 0):
            gacha_type = 301
        elif datetime(2021, 11, 24, 6, 0, 0) < gacha_time < datetime(2021, 12, 14, 17, 59, 59):
            gacha_type = 400
    elif banner_name == "Leaves in the Wind":
        # 万叶
        gacha_type = 1
        if datetime(2021, 6, 29, 18, 0, 0) < gacha_time < datetime(2021, 7, 20, 14, 59, 59):
            gacha_type = 301
        elif datetime(2022, 7, 13, 6, 0, 0) < gacha_time < datetime(2022, 8, 2, 17, 59, 59):
            gacha_type = 301
    elif banner_name == "The Herons Court":
        # 神里绫华
        gacha_type = 1
        if datetime(2021, 7, 21, 6, 0, 0) < gacha_time < datetime(2021, 8, 10, 17, 59, 59):
            gacha_type = 301
        elif datetime(2022, 4, 19, 18, 0, 0) < gacha_time < datetime(2022, 5, 31, 5, 59, 59):
            gacha_type = 301
    elif banner_name == "Tapestry of Golden Flames":
        # 宵宫
        gacha_type = 1
        if datetime(2021, 8, 10, 18, 0, 0) < gacha_time < datetime(2021, 8, 31, 14, 59, 59):
            gacha_type = 301
        elif datetime(2022, 8, 2, 18, 0, 0) < gacha_time < datetime(2022, 8, 23, 14, 59, 59):
            gacha_type = 301
    elif banner_name == "Reign of Serenity":
        # 雷电将军
        gacha_type = 1
        if datetime(2021, 9, 1, 6, 0, 0) < gacha_time < datetime(2021, 9, 21, 17, 59, 59):
            gacha_type = 301
        elif datetime(2022, 3, 8, 18, 0, 0) < gacha_time < datetime(2022, 3, 29, 14, 59, 59):
            gacha_type = 301
    elif banner_name == "Drifting Luminescence":
        # 珊瑚宫心海
        gacha_type = 1
        if datetime(2021, 9, 21, 18, 0, 0) < gacha_time < datetime(2021, 10, 12, 14, 59, 59):
            gacha_type = 301
        elif datetime(2022, 3, 8, 18, 0, 0) < gacha_time < datetime(2022, 3, 29, 14, 59, 59):
            gacha_type = 400
        elif datetime(2022, 9, 9, 18, 0, 0) < gacha_time < datetime(2022, 9, 27, 14, 59, 59):
            gacha_type = 400
    elif banner_name == "Oni's Royale":
        # 荒泷一斗
        gacha_type = 1
        if datetime(2021, 12, 14, 18, 0, 0) < gacha_time < datetime(2022, 1, 4, 17, 59, 59):
            gacha_type = 301
        elif datetime(2022, 6, 21, 18, 0, 0) < gacha_time < datetime(2022, 7, 12, 14, 59, 59):
            gacha_type = 301
    elif banner_name == "The Transcendent One Returns":
        # 申鹤
        gacha_type = 1
        if datetime(2022, 1, 5, 6, 0, 0) < gacha_time < datetime(2022, 1, 25, 17, 59, 59):
            gacha_type = 301
    elif banner_name == "Everbloom Violet":
        # 八重神子
        gacha_type = 1
        if datetime(2022, 2, 16, 6, 0, 0) < gacha_time < datetime(2022, 3, 8, 17, 59, 59):
            gacha_type = 301
    elif banner_name == "Azure Excursion":
        # 神里绫人
        gacha_type = 1
        if datetime(2022, 3, 30, 6, 0, 0) < gacha_time < datetime(2022, 4, 19, 18, 0, 0):
            gacha_type = 301
    elif banner_name == "Discerner of Enigmas":
        # 夜兰
        gacha_type = 1
        if datetime(2022, 5, 31, 9, 0, 0) < gacha_time < datetime(2022, 6, 21, 17, 59, 59):
            gacha_type = 301
    elif banner_name == "Viridescent Vigil":
        # 提纳里
        gacha_type = 1
        if datetime(2022, 8, 24, 6, 0, 0) < gacha_time < datetime(2022, 9, 9, 17, 59, 59):
            gacha_type = 301
    elif banner_name == "Twilight Arbiter":
        # 赛诺
        gacha_type = 1
        if datetime(2022, 9, 28, 6, 0, 0) < gacha_time < datetime(2022, 10, 14, 17, 59, 59):
            gacha_type = 301
    elif banner_name == "Twirling Lotus":
        # 妮露
        gacha_type = 1
        if datetime(2022, 10, 14, 18, 0, 0) < gacha_time < datetime(2022, 11, 1, 14, 59, 59):
            gacha_type = 301
    return gacha_type
