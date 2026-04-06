from Mailing import Mailing
from Address import address

to_address = address(124498, "Зеленоград", "Центральный проспект", "445", "252")
from_address = address(124498, "Зеленоград", "Центральный проспект", "445", "25")

mailing = Mailing(to_address, from_address, 810, 124498)

print(mailing)