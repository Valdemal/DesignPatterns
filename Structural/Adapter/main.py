from Adapters import GeneralizedAdapter, AggregatedAdapter
from ClosedClass import Service
from Person import Person

p = Person("Vladimir", "Nekhaenko", 19)

aa = AggregatedAdapter(Service())
ga = GeneralizedAdapter()

aa.parse(p)
ga.parse(p)
