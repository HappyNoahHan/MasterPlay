import battle.skill
import random
#old verson skill setting
#技能列表与代号
#当实例里面有参数有使用次数 用同一个类实例会出现问题
#2.0 pp value 内部固定

skill_dict = {
    'A001': battle.skill.Ember,#火花
    'A002': battle.skill.FireFang,#火焰牙
    'A003': battle.skill.FlameBurst,#火焰溅射
    'A004': battle.skill.fireSpin,#火焰漩涡
    'A005': battle.skill.Flamethrower,#喷射火焰
    'A006': battle.skill.Inferno,#炼狱
    'A007': battle.skill.FlareBlitz,#闪焰冲锋
    'A008': battle.skill.HeatWave,#热风
    'A099': battle.skill.flameAffinity,
    'A009': battle.skill.WillOWisp,#鬼火
    'A010': battle.skill.FireBlast,#大字爆炎
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
    'N036': battle.skill.Pound,#拍击
    'N037': battle.skill.Disable,#定身法
    'N038': battle.skill.SonicBoom,#音爆
    'N039': battle.skill.Lockon,#锁定
    'N040': battle.skill.TriAttack,#三重攻击
    'N041': battle.skill.SelfDestruct,#自爆
    'N042': battle.skill.DoubleEdge,#舍身冲撞
    'N043': battle.skill.Explosion,#大爆炸
    'N044': battle.skill.DefenseCurl,#变圆
    'N045': battle.skill.ScaryFace,#鬼面
    'N046': battle.skill.Slash,#劈开
    'N047': battle.skill.TakeDown,#猛撞
    'N048': battle.skill.Protect,#守住
    'N049': battle.skill.SkullBash,#火箭头锤
    'N050': battle.skill.FakeOut,#击掌奇袭
    'N051': battle.skill.Safeguard,#神秘守护
    'N052': battle.skill.Captivate,#诱惑
    'N053': battle.skill.Endeavor,#蛮干
    'N054': battle.skill.Rage,#愤怒  后续先这样
    'N055': battle.skill.HyperFang,#必杀门牙
    'N056': battle.skill.SuckerPunch,#突袭
    'N057': battle.skill.SuperFang,#愤怒门牙
    'N058': battle.skill.SwordsDance,#剑舞
    'N059': battle.skill.PlayNice,#和睦相处
    'N060': battle.skill.Feint,#佯攻
    'N061': battle.skill.DoubleTeam,#影子分身
    'N062': battle.skill.FurySwipes,#乱抓
    'N063': battle.skill.CrushClaw,#撕裂爪
    'N064': battle.skill.ChipAway,#逐步击破
    'N065': battle.skill.BodySlam,#泰山压顶
    'N066': battle.skill.Thrash,#大闹一番
    'N067': battle.skill.DoubleSlap,#连环巴掌
    'N068': battle.skill.Sing,#唱歌
    'N069': battle.skill.Roar,#吼叫
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
    'B019': battle.skill.LeechSeed,#寄生种子
    'B020': battle.skill.WorrySeed,#烦恼种子
    'B021': battle.skill.Synthesis,#光合作用
    'B022': battle.skill.SeedBomb,#种子炸弹
    'S001': battle.skill.illuminatiom,
    'S002': battle.skill.Agility,#高速移动
    'S003': battle.skill.Barrier,#屏障
    'S004': battle.skill.Psywave,#精神波
    'S005': battle.skill.Psychic,#精神强念
    'S006': battle.skill.LightScreen,#光墙
    'S007': battle.skill.CosmicPower,#宇宙力量
    'S008': battle.skill.Confusion,#念力
    'S009': battle.skill.Psybeam,#幻象光线
    'S010': battle.skill.StoredPower,#辅助力量
    'S011': battle.skill.Extrasensory,#神通力
    'S012': battle.skill.Imprison,#封印
    'I001': battle.skill.Haze, #黑雾
    'I002': battle.skill.IceFang,#冰冻牙
    'T001': battle.skill.disperse,
    'T002': battle.skill.threaten,
    'T003': battle.skill.Bite, #咬住
    'T004': battle.skill.Crunch,#咬碎
    'T005': battle.skill.Pursuit,#追打
    'T006': battle.skill.Assurance,#恶意追击
    'T007': battle.skill.KnockOff,#拍落
    'T008': battle.skill.Fling,#投掷
    'T009': battle.skill.Memento,#临别礼物
    'T010': battle.skill.Flatter,#吹捧
    'T011': battle.skill.Payback,#以牙还牙
    'T012': battle.skill.FeintAttack,#出奇一击
    'T013': battle.skill.NastyPlot,#诡计
    'C001': battle.skill.Megahorn,#超级角击
    'C002': battle.skill.StringShot,#吐丝
    'C003': battle.skill.LeechLife, #吸血
    'C004': battle.skill.Steamroller,#疯狂滚压
    'C005': battle.skill.BugBite,#虫咬
    'C006': battle.skill.SilverWind,#银色旋风
    'C007': battle.skill.BugBuzz,#虫鸣
    'C008': battle.skill.QuiverDance,#蝶舞
    'C009': battle.skill.Twineedle,#双针
    'C010': battle.skill.PinMissile,#飞弹针
    'C011': battle.skill.FellStinger,#致命针刺
    'C012': battle.skill.FuryCutter,#连斩
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
    'D012': battle.skill.Withdraw,#缩入壳中
    'D013': battle.skill.AquaTail,#水流尾
    'D014': battle.skill.RainDance,#求雨
    'D015': battle.skill.AquaJet,#水流喷射
    'R001': battle.skill.RockThrow,#落石
    'R002': battle.skill.RockSlide,#岩崩
    'R003': battle.skill.PowerGem,#力量宝石
    'R004': battle.skill.RockPolish,#岩石打磨
    'R005': battle.skill.Rollout,  # 滚动
    'R006': battle.skill.SmackDown,#击落
    'R007': battle.skill.StoneEdge,#尖石攻击
    'R008': battle.skill.RockBlast,#岩石爆击
    'R009': battle.skill.StealthRock,#隐形岩   交换类节能改为容易受伤
    'R010': battle.skill.Sandstorm,#沙暴
    'E001': battle.skill.Earthquake,#地震
    'E002': battle.skill.MudBomb,#泥巴炸弹
    'E003': battle.skill.SandAttack,#泼沙
    'E004': battle.skill.DrillRun,#直冲钻
    'E005': battle.skill.MudSlap,#掷泥
    'E006': battle.skill.MudSport,#玩泥巴
    'E007': battle.skill.Magnitude,#震级
    'E008': battle.skill.Bulldoze,#重踏
    'E009': battle.skill.SandTomb,#流沙地狱
    'E010': battle.skill.Dig,#挖洞
    'E011': battle.skill.EarthPower,#大地之力
    'Q001': battle.skill.ConfuseRay, #奇异之光
    'Q002': battle.skill.Astonish, #惊吓
    'Q003': battle.skill.Hex,#祸不单行
    'Q004': battle.skill.ShadowClaw,#暗影爪
    'Q005': battle.skill.Grudge,#怨念
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
    'P015': battle.skill.PoisonGas,#毒瓦斯
    'P016': battle.skill.Sludge,#污泥攻击
    'P017': battle.skill.SludgeBomb,#污泥炸弹
    'P018': battle.skill.AcidArmor,#溶化
    'P019': battle.skill.VenomDrench,#毒液陷阱
    'H001': battle.skill.ThunderFang,#雷电牙
    'H002': battle.skill.ThunderShock,#电击
    'H003': battle.skill.ThunderWave,#电磁波
    'H004': battle.skill.Spark,#电光
    'H005': battle.skill.ElectroBall,#电球
    'H006': battle.skill.Discharge,#放电
    'H007': battle.skill.MagnetRise,#电磁飘浮
    'H008': battle.skill.ZapCannon,#电磁炮
    'H009': battle.skill.ElectricTerrain,#电气场地
    'H010': battle.skill.Nuzzle,#蹭蹭脸颊
    'H011': battle.skill.Thunderbolt,#十万伏特
    'H012': battle.skill.WildCharge,#疯狂伏特
    'H013': battle.skill.Thunder,#打雷
    'G001': battle.skill.Twister,#龙卷风
    'G002': battle.skill.DragonPulse,#龙之波动
    'G003': battle.skill.DragonDance,#龙之舞
    'G004': battle.skill.DragonRage,#龙之怒
    'G005': battle.skill.DragonClaw,#龙爪
    'Y001': battle.skill.Moonlight,#月光
    'Y002': battle.skill.Moonblast,#月亮之力
    'Y003': battle.skill.DisarmingVoice,#魅惑之声
    'Y004': battle.skill.BabyDollEyes,#圆瞳
    'X001': battle.skill.GyroBall,#陀螺球
    'X002': battle.skill.MagnetBomb,#磁铁炸弹
    'X003': battle.skill.MirrorShot,#镜光射击
    'X004': battle.skill.MetalSound,#金属音
    'X005': battle.skill.FlashCannon,#加农光炮
    'X006': battle.skill.IronDefense,#铁壁
    'X007': battle.skill.MeteorMash,#彗星拳
    'Z001': battle.skill.DoubleKick,#二连踢
    'Z002': battle.skill.Superpower,#蛮力
    'Z003': battle.skill.WakeUpSlap,#唤醒巴掌

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
