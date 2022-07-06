from FurnituerFactory import FurnitureFactory, ModernFactory, VictorianFactory


def create_factory(factory_type: str) -> FurnitureFactory:
    if factory_type == "modern":
        return ModernFactory()
    elif factory_type == "victorian":
        return VictorianFactory()
    else:
        raise ValueError()


if __name__ == "__main__":
    factory = create_factory("modern")

    chair = factory.create_chair()

    chair.sit_on()