#!/bin/bash

function create(){
    cd /Users/stone/Dev/ProjectInitCommand
    python create.py $1
    cd /Users/stone/Dev/$1
    git init
    git remote add origin git@github.com:stonechamp/$1.git
    touch README.md
    git add .
    git commit -m "Initial commit"
    git push -u origin master
    code .
}