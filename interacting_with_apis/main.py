from libs.openexchange import OpenExchangeClient

APP_ID = "6232b3f75ff94f84a5cbcb054e215a58"


def run():
    client = OpenExchangeClient(APP_ID)
    usd_amount = 1000
    gbp_amount = client.convert(usd_amount, "USD", "GBP")
    print(f"USD {usd_amount:.2f} is GBP {gbp_amount:.2f}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()

