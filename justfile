year := "2021"

_:
    @just -l -u --list-heading $'Welcome to {{year}} AoC 🎄\n'

# Python

start day:
    #!/usr/bin/env bash
    cd {{year}}
    touch {{day}}.py
    code -n -w input
    code -r {{day}}.py

run day:
    #!/usr/bin/env bash
    cd {{year}}
    python3.10 {{day}}.py < input

open day:
    #!/usr/bin/env bash
    cd {{year}}
    code -n -w input
    code -r {{day}}.py

edit:
    #!/usr/bin/env bash
    code justfile