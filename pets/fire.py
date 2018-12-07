import pets.propets

class FireFox(pets.propets.Fire):
    name = '火狐狸'
    talent = 'a' #天赋 eg：火属性技能伤害+10% 后续nnn版本 做一张map 天赋技能树 各种类型

    def __str__(self):
        return super().__str__() + ':' + self.name
