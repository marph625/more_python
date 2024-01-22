# Import der Klasse Musikinstrument
from musikinstrument import Musikinstrument

# Instanziierung, anlegen eines Objektes

instrument = Musikinstrument("PRS Custom 24 BW", "PRS")

def main():
    instrument.set_preis(3997.0)
    print(instrument.get_daten())

# Aufruf
main()