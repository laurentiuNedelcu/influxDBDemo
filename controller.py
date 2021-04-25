"""
This file contains the logic of the program which will call all functions we have created.
"""
import commands.resources as res
from commands import utils


def run(client):
    """
    The user will be asked to enter a command and depending on it, one procedure or another will be completed.
    :param client:
    :return:
    """

    exit_program = False
    while not exit_program:

        if utils.DATABASE_SELECTED == "":
            command = input("\n>>").strip()
        else:
            command = input("\n[" + utils.DATABASE_SELECTED + "]>>").strip()

        if command in ("close", "quit", "exit"):
            exit_program = True

        elif "create database" in command.lower():
            res.create_database(command, client)

        elif "show measurements" in command.lower():
            res.show_measurements(command, client)

        elif "show databases" in command.lower():
            res.show_databases(command, client)

        elif "select database" in command.lower():
            res.select_database(command, client)

        elif "insert default json" in command.lower():
            res.insert_default_json(client)

        elif "insert" in command.lower():
            res.insert_node(command, client)

        elif "update" in command.lower():
            res.update_node(command, client)

        elif "delete database" in command.lower() or "drop database" in command.lower():
            res.drop_database(command, client)

        elif "delete measurement" in command.lower() or "drop measurement" in command.lower():
            res.drop_measurement(command, client)

        elif "select" in command.lower():
            res.process_query(command, client)

        elif command.lower() in ("h", "help", "-h", "-help", "--h", "--help"):
            res.show_commands()

        else:
            res.show_error_command(command)
