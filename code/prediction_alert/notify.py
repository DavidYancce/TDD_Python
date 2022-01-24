
from copyreg import constructor
from numpy import true_divide


def notify_hot_match(match):
    return match.is_hot_match()

class Match:
    def __init__(self, game_time, home, away):
        self.game_time = game_time
        self.home = home
        self.away = away
    def is_hot_match(self):
        if self.get_match_attacks() >= self.game_time : 
            return True
        if self.game_time <= 10 and self.get_shots()>=4 :
            return True
        return False
    def get_match_attacks(self):
        return self.home.attacks + self.away.attacks
    def get_shots(self):
        return self.home.get_all_shots() + self.away.get_all_shots()
        
class TeamStats:
    on_target = 0
    off_target = 0
    attacks = 0
    def __init__(self, on_target, off_target, attacks) -> None:
        self.on_target = on_target
        self.off_target = off_target
        self.attacks = attacks
    def get_all_shots(self):
        return self.off_target + self.on_target


