#!/usr/bin/env python3
import re

class UserInput:

    def __init__(self):
        self.frequency = ''
        self.unimportant_ports = ''

    def input_unimportant_ports(self):
        print("Please type below numbers according to services you DON'T WANT TO WATCH. Separate them with comma, eg. 21, 22, 23, 80")

        while True:
            unports = input("Enter port numbers: ").replace(" ", "").replace("  ", "")
            try:
                matched = re.match("\d{1,5}(,\d{1,5})*", unports).group(0)
            except Exception:
                print("Your input is invalid. Let's try again.")
                continue
            else:
                if(unports == matched):
                    self.unimportant_ports = unports
                    break
                else:
                    print("Your input is invalid. Let's try again.")



    def input_frequency(self):

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
                if(freq == matched):
                    self.frequency = freq
                    break
                else:
                    print("Your input is invalid. Let's try again.")



