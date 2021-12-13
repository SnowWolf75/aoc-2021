#!/usr/bin/env python3
# Advent of code working directories creator
# IMPORTANT Remember to edit the USER_SESSION_ID & author values with yours
# uses requests module. If not present use pip install requests
# Author = Alexe Simon
# Date = 06/12/2018
# From https://github.com/AlexeSimon/adventofcode

# USER SPECIFIC PARAMETERS
base_pos = "/Users/charles.wheeler/mygit/aoc-2021/"            # Folders will be created here. If you want to make a parent folder, change this to ex "./adventofcode/"
USER_SESSION_ID = "53616c7465645f5f3994efd05285873007778376dfa504c649ef8eaad59ab3879a3e3c691ee826546b02781784b534ee"       # Get your session by inspecting the session cookie content in your web browser while connected to adventofcode and paste it here as plain text in between the ". Leave at is to not download inputs.
DOWNLOAD_STATEMENTS = False # Set to false to not download statements. Note that only part one is downloaded (since you need to complete it to access part two)
DOWNLOAD_INPUTS = True     # Set to false to not download inputs. Note that if the USER_SESSION_ID is wrong or left empty, inputs will not be downloaded.
MAKE_CODE_TEMPLATE = True  # Set to false to not make code templates. Note that even if OVERWRITE is set to True, it will never overwrite codes.
MAKE_URL = False            # Set to false to not create a direct url link in the folder.
MAKE_SAMPLE = True         # Create an empty file for adding sample data
ADD_GIT = True             # Add the directory to the git repo
ADD_SVN = False            # Add the directory to the svn repo
author = "Snow Wolf"       # Name automatically put in the code templates.
OVERWRITE = False          # If you really need to download the whole thing again, set this to true. As the creator said, AoC is fragile; please be gentle. Statements and Inputs do not change. This will not overwrite codes.

# DATE SPECIFIC PARAMETERS
date = "December 2021"              # Date automatically put in the code templates.
starting_advent_of_code_year = 2021 # You can go as early as 2015.
last_advent_of_code_year = 2021     # The setup will download all advent of code data up until that date included
last_advent_of_code_day = 12         # If the year isn't finished, the setup will download days up until that day included for the last year
# Imports
import os
import datetime
try:
    import requests
except ImportError:
    sys.exit("You need requests module. Install it by running \"pip install requests\".")

if ADD_SVN:
    try:
        import svn
    except ImportError:
        sys.exit("You need SVN module. Install it by running \"pip install svn\".")
if ADD_GIT:
    try:
        from git import Repo
    except ImportError:
        sys.exit("You need GIT module. Install it by running \"pip install gitpython\".")

# Code
MAX_RECONNECT_ATTEMPT = 2
years = range(starting_advent_of_code_year, last_advent_of_code_year+1)
days = range(1,26)
link = "https://adventofcode.com/" # ex use : https://adventofcode.com/2017/day/19/input
USER_AGENT = "adventofcode_working_directories_creator"

def template(_year, _day, _author, _date):
    my_template = """#!/usr/bin/env python3
import argparse
# Advent of code Year {y} Day {da} solution
# Author = {a}
# Date = {dt}

parser = argparse.ArgumentParser(description='Add branching arguments for code.')
parser.add_argument('-s', '--sample', action="store_true", help="Use sample input")
parser.add_argument('-1', '--one', action="store_true", help="Execute first part")
parser.add_argument('-2', '--two', action="store_true", help="Execute second part")
args = parser.parse_args()

if not (args.one | args.two):
    args.one = True
    args.two = True
    
if args.sample:
    input_source = __file__.rstrip("code.py")+"sample.txt"
else:
    input_source = __file__.rstrip("code.py")+"input.txt"

with open(input_source, 'r') as input_file:
    input = input_file.read()

def part1(lines):
    return ""


def part2(lines):
    return ""


if args.one:
    one_ret = part1(input.splitlines())
    print("%sPart One : %s" % ("SAMPLE! " if args.sample else "", str(one_ret)))

if args.two:
    two_ret = part2(input.splitlines())
    print("%sPart Two : %s" % ("SAMPLE! " if args.sample else "", str(two_ret)))
    """
    return my_template.format(a=_author, da=_day, dt=_date, y=_year)


print("Setup will download data and create working directories and files for adventofcode.")
if not os.path.exists(base_pos):
    os.mkdir(base_pos)
for y in years:
    print("Year "+str(y))
    if not os.path.exists(base_pos+str(y)):
        os.mkdir(base_pos+str(y))
    year_pos = base_pos + str(y)
    for d in (d for d in days if (y < last_advent_of_code_year or d <= last_advent_of_code_day)):
        print("    Day "+str(d));
        if not os.path.exists(year_pos+"/"+str(d)):
            os.mkdir(year_pos+"/"+str(d))
        day_pos = year_pos+"/"+str(d)
        if MAKE_CODE_TEMPLATE and not os.path.exists(day_pos+"/code.py"):
            code = open(day_pos+"/code.py", "w+")
            code.write(template(year_pos, day_pos, author, date))
            code.close()
            os.chmod(path=day_pos+"/code.py", mode=0o775)
        if DOWNLOAD_INPUTS and (not os.path.exists(day_pos+"/input.txt") or OVERWRITE)and USER_SESSION_ID != "":
            done = False
            error_count = 0
            while not done:
                try:
                    with requests.get(url=link+str(y)+"/day/"+str(d)+"/input", cookies={"session": USER_SESSION_ID}, headers={"User-Agent": USER_AGENT}) as response:
                        if response.ok:
                            data = response.text
                            input = open(day_pos+"/input.txt", "w+")
                            input.write(data.rstrip("\n"))
                            input.close()
                        else:
                            print("        Server response for input is not valid.")
                    done = True
                except requests.exceptions.RequestException:
                    error_count += 1
                    if error_count > MAX_RECONNECT_ATTEMPT:
                        print("        Giving up.")
                        done = True
                    elif error_count == 0:
                        print("        Error while requesting input from server. Request probably timed out. Trying again.")
                    else:
                        print("        Trying again.")
                except Exception as e:
                    print("        Non handled error while requesting input from server. " + str(e))
                    done = True
        if DOWNLOAD_STATEMENTS and (not os.path.exists(day_pos+"/statement.html") or OVERWRITE):
            done = False
            error_count = 0
            while(not done):
                try:
                    with requests.get(url=link+str(y)+"/day/"+str(d), cookies={"session": USER_SESSION_ID}, headers={"User-Agent": USER_AGENT}) as response:
                        if response.ok:
                            html = response.text
                            start = html.find("<article")
                            end = html.rfind("</article>")+len("</article>")
                            end_success = html.rfind("</code>")+len("</code>")
                            statement = open(day_pos+"/statement.html", "w+")
                            statement.write(html[start:max(end, end_success)])
                            statement.close()
                        done = True
                except requests.exceptions.RequestException:
                    error_count += 1
                    if error_count > MAX_RECONNECT_ATTEMPT:
                        print("        Error while requesting statement from server. Request probably timed out. Giving up.")
                        done = True
                    else:
                        print("        Error while requesting statement from server. Request probably timed out. Trying again.")
                except Exception as e:
                    print("        Non handled error while requesting statement from server. " + str(e))
                    done = True

        if MAKE_SAMPLE:
            print("        Making empty sample.txt, for the sample input.")
            with open(day_pos+"/sample.txt", 'a'):
                os.utime(day_pos+"/sample.txt", None)

        if MAKE_URL and (not os.path.exists(day_pos+"/link.url") or OVERWRITE):
            url = open(day_pos+"/link.url", "w+")
            url.write("[InternetShortcut]\nURL="+link+str(y)+"/day/"+str(d)+"\n")
            url.close()

        if ADD_GIT:
            print("        Adding directory to GIT")
            repo = Repo(base_pos)
            repo.git.add([day_pos])

print("Setup complete : adventofcode working directories and files initialized with success.")

