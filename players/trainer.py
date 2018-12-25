from players import play
from pets import fly,wood
from battle import skill

trainer_in_grass_no_1 = {
    '迷途少女': play.Player(name='迷途少女',pet_list={'Master': fly.aiPidgey(level=5,skill_list={'1': skill.scream()})}),
}