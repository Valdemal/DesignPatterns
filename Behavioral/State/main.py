from typing import List

from State.states import State, ReadyState


class Player:
    """Контекст"""

    def __init__(self):
        self._state: State = ReadyState(self)
        self.__playing = False
        self.__tracks: List[str] = ['enter sandman', 'lithium', 'duality']
        self.__current_track_index = 0

    # Геттеры и сеттеры
    def change_state(self, state: State):
        self._state = state

    @property
    def current_track(self) -> str:
        return self.__tracks[self.__current_track_index]

    @property
    def playing(self) -> bool:
        return self.__playing

    # Сервисные методы контекста, вызываемые состояниями
    def start_playback(self):
        self.__playing = True
        print(f"Начало песни {self.current_track}")

    def stop_playback(self):
        self.__playing = False
        print(f"Пауза песни {self.current_track}")

    def next_track(self):
        if self.__current_track_index < len(self.__tracks) - 1:
            self.__current_track_index += 1
            self.start_playback()

    def previous_track(self):
        if self.__current_track_index > 0:
            self.__current_track_index -= 1
            self.start_playback()

    # Методы, делегирующие работу активному состоянию
    def click_lock(self):
        self._state.click_lock()

    def click_play(self):
        self._state.click_play()

    def click_next(self):
        self._state.click_next()

    def click_previous(self):
        self.click_previous()


if __name__ == '__main__':
    player = Player()
    player.click_play()
    player.click_lock()
    player.click_play()
    player.click_next()
