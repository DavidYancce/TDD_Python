from numpy import mat
from notify import Match
from notify import TeamStats

class MatchMock:
    def create (self, _type):
        if _type == "by attacks":
            home_stats = TeamStats(3, 6, 10)
            away_stats = TeamStats(1, 2, 3)
            match = Match(12, home_stats, away_stats)
            return match
        elif _type == "by shots":
            home_stats2 = TeamStats(3, 6, 10)
            away_stats2 = TeamStats(1, 2, 3)
            match2 = Match(12, home_stats2, away_stats2)
            return match2