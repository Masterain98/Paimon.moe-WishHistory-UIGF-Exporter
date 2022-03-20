from datetime import datetime


def uigfGachaTypeGenerator(row):
    gachaTime = datetime.strptime(row["Time"], "%Y-%m-%d %H:%M:%S")
    bannerName = row["Banner"]
    gachaType = 0
    if bannerName == "Ballad in Goblets":
        # 温迪
        gachaType = 1
        if gachaTime > datetime(2020,9,28,0,0,0) and gachaTime < datetime(2020,10,18,18,0,0):
            gachaType = 301
        elif gachaTime > datetime(2021,3,17,6,0,0) and gachaTime < datetime(2021,4,6,16,0,0):
            gachaType = 301
    elif bannerName == "Sparkling Steps":
        # 可莉
        gachaType = 1
        if gachaTime > datetime(2020,10,20,18,0,0) and gachaTime < datetime(2020,11,10,16,0,0):
            gachaType = 301
        elif gachaTime > datetime(2021,6,9,6,0,0) and gachaTime < datetime(2021,6,29,17,59,59):
            gachaType = 301
    elif bannerName == "Farewell of Snezhnaya":
        # 公子
        gachaType = 1
        if gachaTime > datetime(2020,11,11,6,0,0) and gachaTime < datetime(2020,12,1,16,0,0):
            gachaType = 301
        elif gachaTime > datetime(2021,4,6,18,0,0) and gachaTime < datetime(2021,4,27,15,0,0):
            gachaType = 301
        elif gachaTime > datetime(2021,10,13,6,0,0) and gachaTime < datetime(2021,11,2,17,59,59):
            gachaType = 301
    elif bannerName == "Gentry of Hermitage":
        # 钟离
        gachaType = 1
        if gachaTime > datetime(2020,12,1,18,0,0) and gachaTime < datetime(2020,12,22,15,0,0):
            gachaType = 301
        elif gachaTime > datetime(2021,4,28,6,0,0) and gachaTime < datetime(2021,5,18,17,59,59):
            gachaType = 301
        elif gachaTime > datetime(2022,1,25,18,0,0) and gachaTime < datetime(2022,2,15,14,59,59):
            gachaType = 301
    elif bannerName == "Secretum Secretorum":
        # 阿贝多
        gachaType = 1
        if gachaTime > datetime(2020,12,23,6,0,0) and gachaTime < datetime(2021,1,12,16,0,0):
            gachaType = 301
        elif gachaTime > datetime(2021,11,24,6,0,0) and gachaTime < datetime(2021,12,14,17,59,59):
            gachaType = 301
    elif bannerName == "Adrift in the Harbor":
        # 甘雨
        gachaType = 1
        if gachaTime > datetime(2021,1,12,18,0,0) and gachaTime < datetime(2021,2,2,15,0,0):
            gachaType = 301
        elif gachaTime > datetime(2022,1,25,18,0,0) and gachaTime < datetime(2022,2,15,14,59,59):
            gachaType = 400
    elif bannerName == "Invitation to Mundane Life":
        # 魈
        gachaType = 1
        if gachaTime > datetime(2021,2,3,6,0,0) and gachaTime < datetime(2021,2,17,16,0,0):
            gachaType = 301
        elif gachaTime > datetime(2022,1,5,6,0,0) and gachaTime < datetime(2022,1,25,17,59,59):
            gachaType = 400
    elif bannerName == "Dance of Lanterns":
        # 刻晴
        gachaType = 1
        if gachaTime > datetime(2021,2,17,18,0,0) and gachaTime < datetime(2021,3,2,16,0,0):
            gachaType = 301
    elif bannerName == "Moment of Bloom":
        # 胡桃
        gachaType = 1
        if gachaTime > datetime(2021,3,2,18,0,0) and gachaTime < datetime(2021,3,16,15,0,0):
            gachaType = 301
        elif gachaTime > datetime(2021,11,2,18,0,0) and gachaTime < datetime(2021,11,23,14,59,59):
            gachaType = 301
    elif bannerName == "Born of Ocean Swell":
        # 优菈
        gachaType = 1
        if gachaTime > datetime(2021,5,18,18,0,0) and gachaTime < datetime(2021,6,8,15,0,0):
            gachaType = 301
        elif gachaTime > datetime(2021,11,24,6,0,0) and gachaTime < datetime(2021,12,14,17,59,59):
            gachaType = 400
    elif bannerName == "Leaves in the Wind":
        # 万叶
        gachaType = 1
        if gachaTime > datetime(2021,6,29,18,0,0) and gachaTime < datetime(2021,7,20,14,59,59):
            gachaType = 301
    elif bannerName == "The Herons Court":
        # 神里绫华
        gachaType = 1
        if gachaTime > datetime(2021,7,21,6,0,0) and gachaTime < datetime(2021,8,10,17,59,59):
            gachaType = 301
    elif bannerName == "Tapestry of Golden Flames":
        # 宵宫
        gachaType = 1
        if gachaTime > datetime(2021,8,10,18,0,0) and gachaTime < datetime(2021,8,31,14,59,59):
            gachaType = 301
    elif bannerName == "Reign of Serenity":
        # 雷电将军
        gachaType = 1
        if gachaTime > datetime(2021,9,1,6,0,0) and gachaTime < datetime(2021,9,21,17,59,59):
            gachaType = 301
        elif gachaTime > datetime(2022,3,8,18,0,0) and gachaTime < datetime(2022,3,29,14,59,59):
            gachaType = 301
    elif bannerName == "Drifting Luminescence":
        # 珊瑚宫心海
        gachaType = 1
        if gachaTime > datetime(2021,9,21,18,0,0) and gachaTime < datetime(2021,10,12,14,59,59):
            gachaType = 301
        elif gachaTime > datetime(2022,3,8,18,0,0) and gachaTime < datetime(2022,3,29,14,59,59):
            gachaType = 400
    elif bannerName == "Oni's Royale":
        # 荒泷一斗
        gachaType = 1
        if gachaTime > datetime(2021,12,14,18,0,0) and gachaTime < datetime(2022,1,4,17,59,59):
            gachaType = 301
    elif bannerName == "The Transcendent One Returns":
        # 申鹤
        gachaType = 1
        if gachaTime > datetime(2022,1,5,6,0,0) and gachaTime < datetime(2022,1,25,17,59,59):
            gachaType = 301
    elif bannerName == "Everbloom Violet":
        # 八重神子
        gachaType = 1
        if gachaTime > datetime(2022,2,16,6,0,0) and gachaTime < datetime(2022,3,8,17,59,59):
            gachaType = 301
    return gachaType