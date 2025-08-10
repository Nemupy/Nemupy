<img src="https://capsule-render.vercel.app/api?type=waving&color=0:e96443,100:904e95&height=200&text=%F0%9F%91%80%20%EF%BC%9C%20Hi!%20I%27m%20%E8%8D%89%E3%81%96%E3%81%93%20Programmer!&fontSize=24&fontAlignY=40&fontColor=FFFFFF" alt="header" width="100%">

<div align="center">
  <a href="https://github.com/Nemupy">
    <img height="20" src="https://img.shields.io/badge/Github-Nemupy-Nemupy?logo=github&style=flat&color=171515">
  </a>
  <a href="https://discordapp.com/users/798439010594717737">
    <img height="20" src="https://img.shields.io/badge/Discord-Nemupy-Nemupy?logo=discord&style=flat&color=7289DA">
  </a>
</div>

<br>

<a href="https://discord.gg/5fHDJwVhWb">
  <img align="right" src="https://discordapp.com/api/guilds/902525668615663636/widget.png?style=banner4">
</a>

```py
import random

class MyProfile:
    def __init__(self):
        self.name = "Nemupy"
        self.loves = ["Python", "MYUKKE.", "KAWAII LAB."]
        self.repos = ["CuBot", "Janken", "Hello-World"]
        
    def hello(self):
        love = random.choice(self.loves)
        repo = random.choice(self.repos)
        print(f"Hello! I'm {self.name}.")
        print(f"I love {love}, and more!")
        print(f"Please check https://github.com/Nemupy/{repo}.")

nemupy = MyProfile()
nemupy.hello()
```
