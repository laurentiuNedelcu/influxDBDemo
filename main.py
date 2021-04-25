from influxdb import InfluxDBClient
import controller as contr
from commands import resources as res


def main():
    """
    Program starting and main logic
    :return:
    """
    # Create new client to connect with InfluxDB
    client = InfluxDBClient(host="localhost", port=8086)

    # Welcome!
    res.menu()

    # Start!
    contr.run(client)

    # Goodbye!
    res.exit_text()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

