"""
Модуль для запуска майнинга.
"""
import time

import requests

from config import REQUEST_TIMEOUT, HEADERS, CLICK_TIMEOUT


def get_available_taps() -> int:
    """
    Проверяет количество доступных тапов.
    
    :return: Кол-во доступных кликов.
    """
    url = 'https://api.hamsterkombatgame.io/clicker/sync'
    headers = HEADERS
    response = requests.post(url, headers=headers, timeout=REQUEST_TIMEOUT)
    print(response.status_code)
    return response.json().get('clickerUser').get('availableTaps')


def click(count: int) -> None:
    """
    Производит клики.
    
    :param count: Количество кликов.
    """
    unix_timestamp = int(time.time())
    url = 'https://api.hamsterkombatgame.io/clicker/tap'

    headers = HEADERS

    body = {
        'count': count,
        'availableTaps': 0,
        'timestamp': unix_timestamp
        }

    response = requests.post(url, headers=headers, json=body, timeout=REQUEST_TIMEOUT)
    print(response.status_code)


if __name__ == '__main__':
    try:
        while True:
            available_taps = get_available_taps()
            click(available_taps)
            time.sleep(CLICK_TIMEOUT)
    except KeyboardInterrupt:
        print('exit')
