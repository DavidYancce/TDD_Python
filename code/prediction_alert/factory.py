from notify import Match, TeamStats

class MatchMock:
    def create (self, _type):
        if _type == "by attacks":
            home_stats = TeamStats(3, 6, 10)
            away_stats = TeamStats(1, 2, 3)
            match = Match(12, home_stats, away_stats)
            return match
        elif _type == "by shots":
            home_stats = TeamStats(3, 6, 10)
            away_stats = TeamStats(1, 2, 3)
            match = Match(10, home_stats, away_stats)
            return match