from notify import notify_hot_match
from factory import MatchMock

match_mock = MatchMock()


def test_attacks_notification ():
    assert notify_hot_match(match_mock.create("by attacks")), "Deberia de alertar, ya que el numero de ataques es superior a los minutos transcurridos"
    assert notify_hot_match(match_mock.create("by shots")), "Deberia notificar"
    

