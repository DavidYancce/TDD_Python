from notify import notify_hot_match
from factory import MatchMock

match_mock = MatchMock()
mock_shots = match_mock.create("by shots")
mock_attacks = match_mock.create("by atttacks")

def test_attacks_notification ():
    assert notify_hot_match(mock_shots), "Deberia de alertar, ya que el numero de ataques es superior a los minutos transcurridos"
    assert notify_hot_match(mock_shots), "Deberia notificar"

    

