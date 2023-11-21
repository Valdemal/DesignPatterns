from abc import ABC, abstractmethod
from playsound import playsound
import datetime
import time


class Implementation(ABC):
    """Класс отвечающий за реализацию подсистемы (Интерфейс реализации)"""

    @abstractmethod
    def ring(self):
        pass

    @abstractmethod
    def notify(self):
        pass


class AlarmClock(ABC):
    """Класс реализующий интерфейс подсистемы (Итерфейс абстракции)"""

    def __init__(self, bridge: Implementation):
        self._bridge = bridge

    @abstractmethod
    def _to_wake(self):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class LockupAlarmClock(AlarmClock):
    """Зависающий будильник"""

    def __init__(self, imp: Implementation, time: datetime.datetime):
        super().__init__(imp)
        self.__time_of_wake = time
        self.__wait_for_wake = False

    def _to_wake(self):
        self._bridge.notify()
        self._bridge.ring()

    def start(self):
        self.__wait_for_wake = True

        while self.__wait_for_wake:
            t = datetime.datetime.now()

            if t.time().hour == self.__time_of_wake.hour and t.time().minute == self.__time_of_wake.minute:
                self.__wait_for_wake = False

            time.sleep(0.1)

        self._to_wake()

    def stop(self):
        self.__wait_for_wake = False


class MP3Imp(Implementation):

    def __init__(self, sound_file_name: str):
        self.__sound_file_name = sound_file_name

    def notify(self):
        print("ALARMING!!!")

    def ring(self):
        playsound(self.__sound_file_name)


if __name__ == '__main__':
    alarm_time = datetime.datetime(2022, 6, 28, 18, 48)
    alarm_clock = LockupAlarmClock(MP3Imp("sound.wav"), alarm_time)

    alarm_clock.start()
