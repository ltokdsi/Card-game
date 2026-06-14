from structures import CardQueue


class DrunkedGame:
    """Класс карточной игры. Управление колодами игроков и реализация
    правил ходов"""
    def __init__(self,player1_cards,player2_cards):
        self.first_player = CardQueue()
        self.second_player = CardQueue()
        self.limit = 10 ** 6
        for card in player1_cards:
            self.first_player.append(card)
        for card in player2_cards:
            self.second_player.append(card)

    def play(self):
        """Симуляция игры. Возвращение результата и количества
        ходов"""
        moves = 0
        while (not self.first_player.is_empty() and not
        self.second_player.is_empty() and moves < self.limit):
            moves += 1
            card1 = self.first_player.pop_left()
            card2 = self.second_player.pop_left()
            if card1 == 0 and card2 == 9:
                player1_wins = True
            elif card1 == 9 and card2 == 0:
                player1_wins = False
            else:
                player1_wins = card1 > card2
            if player1_wins:
                self.first_player.append(card1)
                self.first_player.append(card2)
            else:
                self.second_player.append(card1)
                self.second_player.append(card2)
        if moves >= self.limit:
            return "botva",moves
        elif self.first_player.is_empty():
            return "second",moves
        else:
            return "first",moves
