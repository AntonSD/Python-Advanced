from project.hero import Hero
from project.elf import Elf
from project.wizard import Wizard
from project.knight import Knight
from project.museelf import MuseElf
from project.darkwizard import DarkWizard
from project.soulmaster import SoulMaster
from project.darkknight import DarkKnight
from project.bladeknight import BladeKnight

hero = Hero("H", 4)
print(hero.username)
print(hero.level)
print(str(hero))
elf = Elf("E", 4)
print(str(elf))
print(elf.__class__.__bases__[0].__name__)
print(elf.username)
print(elf.level)
