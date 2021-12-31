year := "2021"

_:
    @just -l -u --list-heading $'Welcome to {{year}} AoC 🎄\n'

# Python

start day:
    #!/usr/bin/env bash
    cd {{year}}
    # mkdir -p {{day}}
    # cd {{day}}
    # touch main.py
    # day=$((10#{{day}}))
    # # echo "session=53616c74..." > cookie.txt
    # url="https://adventofcode.com/{{year}}/day/${day}"
    # curl -b "$(cat {{justfile_directory()}}/cookie.txt)" "${url}/input" > input
    # echo $url
    # just sample "${url}" > sample
    touch {{day}}p1.py
    code -n -w input
    code -r {{day}}p1.py

run day:
    #!/usr/bin/env bash
    cd {{year}}
    python3.10 {{day}}.py < input

open day:
    #!/usr/bin/env bash
    cd {{year}}
    # mkdir -p {{day}}
    # cd {{day}}
    # touch main.py
    # day=$((10#{{day}}))
    # # echo "session=53616c74..." > cookie.txt
    # url="https://adventofcode.com/{{year}}/day/${day}"
    # curl -b "$(cat {{justfile_directory()}}/cookie.txt)" "${url}/input" > input
    # echo $url
    # just sample "${url}" > sample
    code -n -w input
    code -r {{day}}p1.py
    code -r {{day}}p2.py

edit:
    #!/usr/bin/env bash
    code justfile