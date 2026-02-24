import time
from plyer import notification


while True:
    print("Drink some water!")
    notification.notify(title="Drink some water!", message="sip some water! Stay hydrated")
    time.sleep(60*60)
