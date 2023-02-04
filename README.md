# LeetCode-Solution-Bot
Help organizing the solutions you have done in leetcode

## Prerequisites
```
# python3
pip install -r requirements.txt
```
## Add .env file
```
LEETCODE_SESSION=<YOUR_LEETCODE_SESSION>
GITHUB_REPO_LINK=https://github.com/<YOUR_GITHUB_REPO_LINK>
```
### You can get the LEETCODE_SESSION value here
### F12 -> Application -> Cookies -> LEETCODE_SESSION -> copy the value to .env
![Screenshot from 2023-02-04 21-18-18](https://user-images.githubusercontent.com/46760916/216769905-6b0249a8-92f0-4dc3-a2a8-df55c6a09f86.png)

## Add <YOUR_README.md> file like this
```
## Hard
### String
| Title |  Solution |
|-------|-----------|
|[TEST]()|[Solution]()|

### Array
| Title |  Solution |
|-------|-----------|
|[TEST]()|[Solution]()|

## Medium
### DFS
| Title |  Solution |
|-------|-----------|
|[TEST]()|[Solution]()|

## Easy
### Array
| Title |  Solution |
|-------|-----------|
|[TEST]()|[Solution]()|
```
## Usage
```
optional arguments:
  -h, --help  show this help message and exit
  -n N        The Problem Name
  -t T        The Problem Type
  -l L        The Problem Level(Easy:1, Medium:2, Hard:3)

./bot.py -n "72. Edit Distance" -t "String" -l 3
# or
python3 bot.py -n "72. Edit Distance" -t "String" -l 3
```
1. Run the bot.py
2. Create "72. Edit Distance" Path
3. Use leetcode api to get your solutions in leetcode 
4. Add the MarkDown text in [YOUR_README.md](https://github.com/fanhouin/LeetCode-Solution-Bot/blob/main/YOUR_README.md)


## Directory
```
├── 72. Edit Distance
│   ├── sol.cpp
│   └── sol.go
├── .env 
├── bot.py
├── requirements.txt
└── YOUR_README.md
```
