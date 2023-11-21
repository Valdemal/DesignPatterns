from abc import ABC, abstractmethod


class State(ABC):
    """Интерфейс состояний"""

    def __init__(self, player: "Player"):
        self._player = player

    @abstractmethod
    def click_lock(self):
        pass

    @abstractmethod
    def click_play(self):
        pass

    @abstractmethod
    def click_next(self):
        pass

    @abstractmethod
    def click_previous(self):
        pass


class LockedState(State):
    def click_lock(self):
        if self._player.playing:
            self._player.change_state(PlayingState(self._player))
        else:
            self._player.change_state(ReadyState(self._player))

    def click_play(self):
        pass

    def click_next(self):
        pass

    def click_previous(self):
        pass


class ReadyState(State):
    def click_lock(self):
        self._player.change_state(LockedState(self._player))

    def click_play(self):
        self._player.start_playback()
        self._player.change_state(PlayingState(self._player))

    def click_next(self):
        self._player.next_track()

    def click_previous(self):
        self._player.previous_track()


class PlayingState(State):
    def click_lock(self):
        self._player.change_state(LockedState(self._player))

    def click_play(self):
        self._player.stop_playback()
        self._player.change_state(PlayingState(self._player))

    def click_next(self):
        self._player.next_track()

    def click_previous(self):
        self._player.previous_track()
