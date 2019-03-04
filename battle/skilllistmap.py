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
    'S001': battle.skill.illuminatiom,
    'S002': battle.skill.Agility,#高速移动
    'I001': battle.skill.Haze, #黑雾
    'I002': battle.skill.IceFang,#冰冻牙
    'T001': battle.skill.disperse,
    'T002': battle.skill.threaten,
    'T003': battle.skill.Bite, #咬住
    'T004': battle.skill.Crunch,#咬碎
    'T005': battle.skill.Pursuit,#追打
    'T006': battle.skill.Assurance,#恶意追击
    'T007': battle.skill.KnockOff,#拍落
    'C003': battle.skill.LeechLife, #吸血
    'D001': battle.skill.WaterJump,
    'D002': battle.skill.WaterBall,
    'D003': battle.skill.WaterCannon,
    'R001': battle.skill.DownRock,
    'R002': battle.skill.RockFall,
    'E001': battle.skill.Earthquake,#地震
    'E002': battle.skill.MudBomb,#泥巴炸弹
    'E003': battle.skill.SandAttack,#泼沙
    'E004': battle.skill.DrillRun,#直冲钻
    'Q001': battle.skill.ConfuseRay, #奇异之光
    'Q002': battle.skill.Astonish, #惊吓
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
    'H001': battle.skill.ThunderFang,#雷电牙
    'G001': battle.skill.Twister,#龙卷风
    'Y001': battle.skill.Moonlight,#月光
    'Y002': battle.skill.Moonblast,#月亮之力

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
