import time

def loading_indicator():
    while True:
        for symbol in "|/-\\":
            print(f"\rLoading {symbol}", end="", flush=True)
            time.sleep(0.2)
