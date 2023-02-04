#!/usr/bin/python3
import requests
import argparse
import time
import os
import sys
import re
from dotenv import load_dotenv

extention = ['cpp', 'go']
leetcode_lang_dict = {'cpp' : 'C++', 'go' : 'Go'}
load_dotenv()

def createFloder(path: str) -> bool:
    if (os.path.exists(path) and os.path.isdir(path)):
        print(f'[x] The problem "{path}" exists')
        sys.exit()
    os.makedirs(path, exist_ok=True)
    print(f"[*] Created path: {path}")
    # for i in extention:
    #     print(f"[*] Creating file: {path}/sol.{i}")
    #     with open(f"{path}/sol.{i}", 'w') as fp:
    #         pass

def getLeetCodeSubmissions(name: str):
    print(f'[*] Getting "{name}" LeetCode Submissions')
    # get the dash_problem_name to compare with the title_slug in the response
    problem_name = re.sub(r"^\d+\. ", "", name)
    dash_problem_name = re.sub(r'\s+', '-', problem_name.lower())

    # get the submissions
    cookies = {'LEETCODE_SESSION': os.getenv('LEETCODE_SESSION')}
    headers = {'Accept': 'application/json'}
    link = 'https://leetcode.com/api/submissions/?offset=0&limit=15' 
    try:
        r = requests.get(link, cookies=cookies, headers=headers)
    except: 
        print(f'[x] Failed to get the submissions')
        print(f'[*] Retrying in 5 seconds')
        time.sleep(5)

    # find the submission with the same problem name and the same language
    sub_arr = r.json()['submissions_dump']
    for e in extention:
        for sub in sub_arr:
            if sub['status_display'] != 'Accepted':
                continue
            if sub['lang_name'] != leetcode_lang_dict[e]:
                continue
            if sub['title_slug'] != dash_problem_name:
                continue
            
            with open(f'{name}/sol.{e}', 'w') as f:
                f.write(sub['code'])
            
            # each extention just need one submission
            break
        print(f'[*] Created the "sol.{e}" successfull')

def genMarkDown(name: str) -> str:
    problem_name = re.sub(r"^\d+\. ", "", name)
    dash_problem_name = re.sub(r'\s+', '-', problem_name.lower())
    solution_name = name.replace(" ", "%20")

    return f"| [{problem_name}](https://leetcode.com/problems/{dash_problem_name})| [Solution]({os.getenv('GITHUB_REPO_LINK')}{solution_name})|"

def findLineIndex(level: str, p_type: str, lines) -> int:
    idx = 0
    while not (lines[idx].startswith("##") and level in lines[idx]):
        idx += 1

    while not (lines[idx].startswith("###") and p_type in lines[idx]):
        idx += 1

    idx += 1
    while (lines[idx].startswith("|")):
        idx += 1
    return idx

def changeReadMeFile(level: int, p_type: str, new_line: str):
    with open("README.md", "r") as file:
        lines = file.readlines()
        if level == 1:
            idx = findLineIndex("Easy", p_type, lines)
        if level == 2:
            idx = findLineIndex("Medium", p_type, lines)
        if level == 3:
            idx = findLineIndex("Hard", p_type, lines)
    lines.insert(idx, new_line + '\n')

    with open("README.md", "w") as file:
        file.writelines(lines)
           

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A script with a help argument')
    parser.add_argument('-n', type=str, help='The Problem Name')
    parser.add_argument('-t', type=str, help='The Problem Type')
    parser.add_argument('-l', type=int, help='The Problem Level')
    parser.add_argument('-c', action='store_true', help='Need to create the files')
    args = parser.parse_args()

    if args.n == None or args.t == None or args.l == None:
        parser.print_help()
        sys.exit()

    if args.c == True:
        createFloder(args.n)
        getLeetCodeSubmissions(args.n)

    line = genMarkDown(args.n)
    changeReadMeFile(args.l, args.t, line)
    print(f'[*] Add "{args.n}" In README.md Finished')
    
    
    