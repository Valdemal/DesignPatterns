import typing


class Animation:
    """
    Легковес. Содержит состояние, которое повторяется во множестве объектов.
    Не имеет методов для изменения состояния.

    Множество однотипных сущностей(пули, частицы и т.д.) имеют одну и ту же
    анимацию для всех объектов класса.
    """
    pass


class AnimationFactory:
    """Управляет созданием и повторным использованием легковесов"""

    __cache: typing.Dict[str, Animation]

    @staticmethod
    def get_animation() -> Animation:
        pass


class AnimationManager:
    """Переключает анимации-легковесы в зависимости от состояния сущности"""
    pass

if __name__ == '__main__':
    pass
