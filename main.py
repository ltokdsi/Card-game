from game_logic import DrunkedGame


def validate_deck_string(user_input,forbidden_cards):
    """Чистая валидация данных"""
    if not user_input:
        print('Строка пустая')
        return None
    raw_cards = user_input.split()
    for card_str in raw_cards:
        if not card_str.isdigit():
            print('Вводите целые положительные числа!')
            return None
    if len(raw_cards) != 5:
        print(f"Нужно ввести ровно 5 карт. Получено: "
              f"{len(raw_cards)}")
        return None
    valid_numbers = []
    for card_str in raw_cards:
        card_num = int(card_str)
        if card_num < 0 or card_num > 9:
            print(f"Карта {card_num} выходит за диапазон 0-9")
            return None
        if card_num in valid_numbers:
            print(f"Карта {card_num} дублируется в вашей колоде!")
            return None
        if card_num in forbidden_cards:
            print(f"Карта {card_num} уже занята другим игроком")
            return None
        valid_numbers.append(card_num)
    return valid_numbers

def get_valid_deck(player_label, forbidden_cards = None):
    """Интерфейсная функция, отвечает за ввод-вывод и общение с
    пользователем"""
    if forbidden_cards is None:
        forbidden_cards = []
    while True:
        print(f"Введите 5 уникальных карт для {player_label} "
              f"(от 0 до 9 через пробел).")
        print('Для возврата в главное меню введите: назад')
        user_input = input('Вводите: ').strip().lower()
        if user_input == 'назад':
            return None
        valid_deck = validate_deck_string(user_input,forbidden_cards)
        if valid_deck is None:
            continue
        return valid_deck

def start_game():
    """Функция сценария запуска игры"""
    player1_cards = get_valid_deck('первого игрока')
    if player1_cards is None:
        print('Возврат в главное меню')
        return False
    print()
    player2_cards = get_valid_deck('второго игрока',
                                   forbidden_cards = player1_cards)
    if player2_cards is None:
        print('Возврат в главное меню')
        return False
    print('Начало игры')
    game = DrunkedGame(player1_cards, player2_cards)
    result,moves = game.play()
    print('Результат:')
    if result == 'botva':
        print('botva')
    else:
        print(result,moves)
    print('Игра завершена!')
    return True

def show_rules():
    """Функция вывода приветствия и правил игры при старте"""
    print('Добро пожаловать в карточную игру "Пьяница"!')
    print('Правила игры:')
    print('-Каждый игрок получает по 5 уникальных карт;')
    print('-Карты открываются сверху колоды;')
    print('-Тот, чья карта оказывается старше, \n забирает обе '
          'вскрытые карты и кладет их \n под низ своей колоды (сначала'
          ' карту первого игрока,затем второго игрока);')
    print('-Большая карта бьет меньшую. Исключение: 0 побеждает 9;')
    print('-Проигрывает тот, кто остается без карт;')
    print('-Если за 1.000.000 ходов победитель не найден,'
          ' объявляется "botva".')

def main():
    """Основная управляющая функция программы"""
    show_rules()
    while True:
        print('Главное меню:')
        print('1. Начать игру')
        print('2. Выйти из программы')
        choice = input('Выберите пункт меню (1-2): ').strip()
        if choice == '1':
            while True:
                game_played = start_game()
                if not game_played:
                    break
                while True:
                    print('Хотите сыграть еще раз?')
                    print('1. Да (перейти к вводу новых карт)')
                    print('2. Нет (выход в главное меню)')
                    repeat_choice = input('Ваш выбор: ').strip()
                    print()

                    if repeat_choice == '1' or repeat_choice == '2':
                        break
                    else:
                        print('Пожалуйста, введите 1 или 2')
                if repeat_choice == '2':
                    print('Возврат в меню')
                    print()
                    break
        elif choice == '2':
            print('Программа завершена!')
            break
        else:
            print('Пожалуйста, введите 1 или 2')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nПрограмма принудительно завершена')