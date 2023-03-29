"""
TroyMartian, who has at least 3 antenna and at most 4 eyes;
VladSaturnian, who has at most 6 antenna and at least 2 eyes;
GraemeMercurian, who has at most 2 antenna and at most 3 eyes.
"""

an = int(input())
eye = int(input())

if an>=3 and eye<=4:
    print('TroyMartian')
if an<=6 and eye>=2:
    print('VladSaturnian')
if an<=2 and eye<=3:
    print('GraemeMercurian')
