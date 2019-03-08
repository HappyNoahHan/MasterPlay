import battle.skill
import random
#old verson skill setting
#技能列表与代号
#当实例里面有参数有使用次数 用同一个类实例会出现问题
#2.0 pp value 内部固定

skill_dict = {
    'A001': battle.skill.fireBall,
    'A002': battle.skill.FireFang,#火焰牙
    'A004': battle.skill.fireSpin,
    'A005': battle.skill.JetFlame,
    'A009': battle.skill.flameAffinity,
    'F001': battle.skill.Gust, #起风
    'F002': battle.skill.WingAttack, #翅膀攻击
    'F003': battle.skill.AirSlash, #空气斩
    'F004': battle.skill.AirCutter, #空气利刃
    'F005': battle.skill.FeatherDance,#羽毛舞
    'F006': battle.skill.Roost,#羽栖
    'F007': battle.skill.Tailwind,#顺风
    'F008': battle.skill.MirrorMove,#鹦鹉学舌
    'F009': battle.skill.Hurricane,#暴风
    'F010': battle.skill.Peck,#啄
    'F011': battle.skill.AerialAce,#燕返
    'F012': battle.skill.DrillPeck,#啄钻
    'F013': battle.skill.Pluck,#啄食
    'N001': battle.skill.Tackle,#撞击
    'N002': battle.skill.Grab,#抓
    'N003': battle.skill.Supersonic, #超音波
    'N004': battle.skill.Swift, #高速星星
    'N005': battle.skill.MeanLook, #黑色目光
    'N006': battle.skill.Screech,#刺耳声
    'N007': battle.skill.Wrap,#紧束
    'N008': battle.skill.Leer,#瞪眼
    'N009': battle.skill.Glare,#大蛇瞪眼
    'N010': battle.skill.Stockpile,#蓄力
    'N011': battle.skill.Swallow,#吞下
    'N012': battle.skill.SpitUp,#喷出
    'N013': battle.skill.QuickAttack,#电光一闪
    'N014': battle.skill.Whirlwind,#吹飞
    'N015': battle.skill.Growl,#叫声
    'N016': battle.skill.FuryAttack,#乱击
    'N017': battle.skill.FocusEnergy,#聚气
    'N018': battle.skill.Growth,#生长
    'N019': battle.skill.SweetScent,#甜甜香气
    'N020': battle.skill.LuckyChant,#幸运咒语
    'N021': battle.skill.NaturalGift,#自然之恩
    'N022': battle.skill.Slam,#摔打
    'N023': battle.skill.WringOut,#绞紧
    'N024': battle.skill.Constrict,#缠绕
    'N025': battle.skill.ReflectType,#镜面属性
    'N026': battle.skill.Smokescreen,#烟幕
    'N027': battle.skill.TailWhip,#摇尾巴
    'N028': battle.skill.HornAttack,#角撞
    'N029': battle.skill.Flail,#抓狂
    'N030': battle.skill.HornDrill,#角钻
    'N031': battle.skill.Harden,#变硬
    'N032': battle.skill.RapidSpin,#高速旋转
    'N033': battle.skill.Recover,#自我再生
    'N034': battle.skill.Camouflage,#保护色
    'N035': battle.skill.Minimize,#变小
    'B001': battle.skill.StunSpore,#麻痹粉
    'B002': battle.skill.azorLeaf,#飞叶快刀
    'B003': battle.skill.lifeRecovery,
    'B004': battle.skill.lifeChains,
    'B005': battle.skill.vinesTied,
    'B006': battle.skill.Absorb, #吸取
    'B007': battle.skill.SleepPowder,  # 催眠粉
    'B008': battle.skill.MegaDrain,#超级吸取
    'B009': battle.skill.GigaDrain,#终极吸取
    'B010': battle.skill.GrassyTerrain,#青草场地
    'B011': battle.skill.PetalDance,#花瓣舞
    'B012': battle.skill.PetalBlizzard,#落英缤纷
    'B013': battle.skill.Aromatherapy,#芳香治疗
    'B014': battle.skill.SolarBeam,#日光束
    'B015': battle.skill.VineWhip,#藤鞭
    'B016': battle.skill.LeafTornado,#青草搅拌器
    'B017': battle.skill.LeafStorm,#飞叶风暴
    'B018': battle.skill.LeafBlade,#叶刃
    'S001': battle.skill.illuminatiom,
    'S002': battle.skill.Agility,#高速移动
    'S003': battle.skill.Barrier,#屏障
    'S004': battle.skill.Psywave,#精神波
    'S005': battle.skill.Psychic,#精神强念
    'S006': battle.skill.LightScreen,#光墙
    'S007': battle.skill.CosmicPower,#宇宙力量
    'I001': battle.skill.Haze, #黑雾
    'I002': battle.skill.IceFang,#冰冻牙
    'T001': battle.skill.disperse,
    'T002': battle.skill.threaten,
    'T003': battle.skill.Bite, #咬住
    'T004': battle.skill.Crunch,#咬碎
    'T005': battle.skill.Pursuit,#追打
    'T006': battle.skill.Assurance,#恶意追击
    'T007': battle.skill.KnockOff,#拍落
    'C001': battle.skill.Megahorn,#超级角击
    'C003': battle.skill.LeechLife, #吸血
    'D001': battle.skill.WaterJump,
    'D002': battle.skill.Bubble,#泡沫
    'D003': battle.skill.HydroPump,#水炮
    'D004': battle.skill.WaterPulse,#水之波动
    'D005': battle.skill.BubbleBeam,#泡沫光线
    'D006': battle.skill.Brine,#盐水
    'D007': battle.skill.WaterGun,#水枪
    'D008': battle.skill.WaterSport,#玩水
    'D009': battle.skill.AquaRing,#水流环
    'D010': battle.skill.Waterfall,#攀瀑
    'D011': battle.skill.Soak,#浸水
    'R001': battle.skill.DownRock,
    'R002': battle.skill.RockFall,
    'R003': battle.skill.PowerGem,#力量宝石
    'E001': battle.skill.Earthquake,#地震
    'E002': battle.skill.MudBomb,#泥巴炸弹
    'E003': battle.skill.SandAttack,#泼沙
    'E004': battle.skill.DrillRun,#直冲钻
    'Q001': battle.skill.ConfuseRay, #奇异之光
    'Q002': battle.skill.Astonish, #惊吓
    'Q003': battle.skill.Hex,#祸不单行
    'P001': battle.skill.Toxic, #剧毒
    'P002': battle.skill.PoisonFang, #剧毒牙
    'P003': battle.skill.Venoshock, #毒液冲击
    'P004': battle.skill.PoisonSting, #毒针
    'P005': battle.skill.Acid, #溶解液
    'P006': battle.skill.AcidSpray,#酸液炸弹
    'P007': battle.skill.GastroAcid,#胃液
    'P008': battle.skill.Belch,#打嗝
    'P009': battle.skill.Coil,#盘蜷
    'P010': battle.skill.GunkShot,#垃圾射击
    'P011': battle.skill.PoisonPowder,#毒粉
    'P012': battle.skill.PoisonJab,#毒击
    'P013': battle.skill.ToxicSpikes,#毒菱
    'P014': battle.skill.SludgeWave,#污泥波
    'H001': battle.skill.ThunderFang,#雷电牙
    'G001': battle.skill.Twister,#龙卷风
    'G002': battle.skill.DragonPulse,#龙之波动
    'G003': battle.skill.DragonDance,#龙之舞
    'Y001': battle.skill.Moonlight,#月光
    'Y002': battle.skill.Moonblast,#月亮之力
    'X001': battle.skill.GyroBall,#陀螺球

}

#背包概念 名称 数量
skill_bag_dict={
    1:[skill_dict['A001'],99],
    2:[skill_dict['B001'],99],
}

#得到技能道具
def getSkill(skill_code,number = 1):
    print("获得了 %s X %d !" % (skill_dict[skill_code].show_name,number))
    for key,value in skill_bag_dict.items():
        if value[0] == skill_dict[skill_code]:
            value[1] += number
            return True

    for key in range(1,101):
        if key not in skill_bag_dict:
            skill_bag_dict[key] = [skill_dict[skill_code],number]
            return True

    return False
