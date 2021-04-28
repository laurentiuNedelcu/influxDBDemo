"""
This file will contain all functions required in order to perform influxDB's CRUD operations.
"""
import colorama
from colorama import Fore
from commands import utils

# Once is enough
colorama.init(autoreset=True)


def menu():
    """
    Print the title
    :return:
    """
    print(Fore.CYAN + "\n##### WELCOME TO INFLUXDB CLIENT DEMO #####\n")


def exit_text():
    """
    Print the farewell
    :return:
    """
    print("\nGOODBYE! See you next time ;)")


def show_commands():
    """
    Print the commands that can be used in this demo
    :return:
    """
    print("\n###### COMMANDS ######")
    print("* exit, close, quit")
    print("* create database " + Fore.CYAN + "database_name")
    print("* show databases")
    print("* show measurements")
    print("* select database " + Fore.CYAN + "database_name")
    print("* select " + Fore.CYAN + "stuff" + Fore.WHITE + " from " + Fore.CYAN + "measurement_name")
    print("* insert " + Fore.CYAN + "measurement_name key=value")
    print("* insert default json")
    print("* update " + Fore.CYAN + "measurement_name key=value time")
    print("* delete database " + Fore.CYAN + "database_name")
    print("* delete measurement " + Fore.CYAN + "measurement_name")
    print()


def show_error_command(command):
    """
    Print in red color a message error
    :param command: the command that produced the error
    :return:
    """
    print(Fore.RED + "Error! Command [" + command + "] does not exist or is not implemented yet.")


def check_format(command, n):
    """
    Check if we have the minimal number of parameters necessary before processing the command. This will make sure
    that the command is what we expected (at least the number of parameters) and will solve some problems of out of range.
    :param command: the command which we have to check the number of parameters it has
    :param n: the MINIMAL number of parameters we expected the command to has
    :return: boolean
    """
    cmd_list = command.split()

    # if we have more than n we do not care
    if len(cmd_list) < n:
        print(Fore.RED + "Error! Incorrect format.")
        return False
    return True


def create_database(command, client):
    """
    Create a new database in InfluxDB
    :param command: the command that contains the name of the database
    :param client: the client that connects with InfluxDB
    :return:
    """
    if check_format(command, 3):
        try:
            cmd_list = command.split()
            client.create_database(cmd_list[2])
            print("Database created!")
        except Exception as e:
            print(Fore.RED + "[Could not create database] More info: " + str(e))


def show_databases(command, client):
    """
    Show all databases which we have in InfluxDB
    :param command: just to check the command format. No extra use.
    :param client: the client that connects with InfluxDB
    :return:
    """
    if check_format(command, 2):
        try:
            print(client.get_list_database())
        except Exception as e:
            print(Fore.RED + "[Could not show databases] More info: " + str(e))


def show_measurements(command, client):
    """
    Show all measurements of a specific database
    :param command: just to check the command format. No extra use.
    :param client: the client that connects with InfluxDB
    :return:
    """
    if check_format(command, 2):
        try:
            print("Result: {0}".format(client.get_list_measurements()))
        except Exception as e:
            print(Fore.RED + "[Could not get measurements] More info: " + str(e))


def select_database(command, client):
    """
    Select the database with which we will work
    :param command: contains the name of the database
    :param client: the client that connects with InfluxDB
    :return:
    """
    if check_format(command, 3):
        try:
            cmd_list = command.split()
            client.switch_database(cmd_list[2])
            print("Database " + cmd_list[2] + " selected")
            utils.DATABASE_SELECTED = cmd_list[2]
        except Exception as e:
            print(Fore.RED + "[Could not select the database] More info: " + str(e))


def insert_node(command, client):
    """
    Write to the selected database a point or a set of points.
    TODO make able to insert time as an optional field

    :param command: contains the measurement on which we will insert the point and the points to be inserted
    :param client: the client that connects with InfluxDB
    :return:
    """
    if check_format(command, 3):
        try:
            cmd_list = command.split()

            # We have 2 ways to insert points, by lines or by json. We chose to do it with json.
            new_json_body = [
                {
                    "measurement": cmd_list[1],
                    "tags": {},  # For now we won't insert metadata
                    "fields": {v.split("=")[0]: v.split("=")[1] for v in cmd_list[2:]}
                }
            ]

            client.write_points(new_json_body, protocol="json")
            print("Inserted!")

        except Exception as e:
            print(Fore.RED + "[Could not insert data] More info: " + str(e))


def insert_default_json(client):
    """
    Insert the default JSON that it is located in utils.py

    :param client: the client that connects with InfluxDB
    :return:
    """
    try:
        # Should return True
        client.write_points(utils.json_body)
        print("JSON inserted successfully")
    except Exception as e:
        print(Fore.RED + "[Could not inserted json] More info: " + str(e))


def update_node(command, client):
    """
    Update the value of a specific node from a specific measurement
    :param command: contains the measurement name, the key, the new value to be applied and the time
    :param client: the client that connects with InfluxDB
    :return:
    """
    if check_format(command, 3):
        try:
            cmd_list = command.split()

            new_json_body = [
                {
                    "measurement": cmd_list[1],
                    "tags": {},
                    "time": cmd_list[3],
                    "fields": {
                        cmd_list[2].split("=")[0]: cmd_list[2].split("=")[1]  # There might be a better form to do this, but it is a demo...
                    }
                }
            ]
            client.write_points(new_json_body, protocol="json")
            print("Value updated")
        except Exception as e:
            print(Fore.RED + "[Could not update data] More info: " + str(e))


def drop_database(command, client):
    """
    Delete a specific database from InfluxDB
    :param command: contains the name of the database to be dropped
    :param client: the client that connects with InfluxDB
    :return:
    """
    if check_format(command, 3):
        try:
            cmd_list = command.split()
            client.drop_database(cmd_list[2])
            print("Database " + cmd_list[2] + " dropped")
            utils.DATABASE_SELECTED = ""
        except Exception as e:
            print(Fore.RED + "[Could not deleted database] More info: " + str(e))


def drop_measurement(command, client):
    """
    Delete the measurement of a specific database
    :param command: contains the name of the measurement to be dropped
    :param client: the client that connects with InfluxDB
    :return:
    """
    if check_format(command, 3):
        try:
            cmd_list = command.split()
            client.drop_measurement(cmd_list[2])
            print("Measurement " + cmd_list[2] + " dropped")
        except Exception as e:
            print(Fore.RED + "[Could not deleted measurement] More info: " + str(e))


def process_query(command, client):
    """
    Make a query selection and get a response from the request
    :param command: the statement to process by the query
    :param client: the client that connects with InfluxDB
    :return:
    """
    if check_format(command, 4):
        try:
            print("Result: {0}".format(client.query(command)))
            # print("Result: {0}".format(client.query(command).raw))
        except Exception as e:
            print(Fore.RED + "[Could not get query] More info: " + str(e))
