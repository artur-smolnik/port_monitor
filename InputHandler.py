#!/usr/bin/env python3
import re
import socket


class UserInput:

    def __init__(self):
        self.frequency = ''
        self.unimportant_ports = ''
        self.target_address = ''

    def input_unimportant_ports(self):
        print()
        print(
            "Please type below numbers according to services you DON'T WANT TO WATCH. Separate them with comma, eg. 21, 22, 23, 80")
        print("If you don't want to exclude ports, type \"n\".")

        while True:
            unports = input("Enter port numbers: ").replace(" ", "").replace("  ", "")
            if unports == 'n':
                self.unimportant_ports = -1
                break
            try:
                matched = re.match("\d{1,5}([,-]{1}\d{1,5})*", unports).group(0)

                tmp_ports = unports.split(',')
                for port_range in tmp_ports:
                    if port_range.__contains__('-'):
                        port_range = port_range.split('-')
                        if int(port_range[0]) > 65535 or int(port_range[0]) < 0 or int(
                                port_range[1]) > 65535 or int(port_range[1]) < 0 or int(port_range[0]) >= int(
                            port_range[1]):
                            raise Exception
                    else:
                        if int(port_range) > 65535 or int(port_range) < 0:
                            raise Exception

            except Exception:
                print("Your input is invalid. Let's try again.")
                continue
            else:

                if (unports == matched):
                    self.unimportant_ports = unports
                    break
                else:
                    print("Your input is invalid. Let's try again.")

    def input_target_address(self):
        print()
        print("Please input ip address of target. Remember that you have to have permission to scan machines.")

        while True:
            address = input("Enter ipv4 target address: ").replace(" ", "").replace("  ", "")

            if address == 'localhost':
                self.target_address = address
                break

            address = address.split('.')

            try:
                if len(address) != 4:
                    raise Exception
                elif int(address[0]) > 255 or int(address[1]) > 255 or int(address[2]) > 255 or int(
                        address[3]) > 255 or int(address[0]) < 0 or int(address[1]) < 0 or int(address[2]) < 0 or int(
                    address[3]) < 0:
                    raise Exception

                else:
                    self.target_address = str(address[0]) + '.' + str(address[1]) + '.' + str(address[2]) + '.' + str(
                        address[3])
                    break
            except Exception:
                print("Given ipv4 address is invalid. Try again.")
                continue

    def input_frequency(self):
        print()
        print("Let's set a scanning frequency.")
        print("If you want to scan every three hours, type h3, one scan per day - h24, or maybe every 17 minutes - m17")
        print("The minimal interval is 1 minute")

        while True:
            freq = input("Please type the frequency: ")

            try:
                matched = re.match("[hm]{1}\d{1,6}", freq).group(0)
            except Exception:
                print("Your input is invalid. Let's try again.")
                continue
            else:
                if (freq == matched):
                    self.frequency = freq
                    break
                else:
                    print("Your input is invalid. Let's try again.")
