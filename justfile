year := "2016"

_:
    @just -l -u --list-heading $'Welcome to {{year}} AoC 🎄\n'

run day:
    #!/usr/bin/env bash
    cd {{year}}
    if ! test -f ./{{day}}.py; then
        cp {{invocation_directory()}}/template.py {{day}}.py
        code -n -w input
        code -r {{day}}.py
    fi
    python {{day}}.py < input

open day:
    #!/usr/bin/env bash
    cd {{year}}
    code -n -w input
    code -r {{day}}.py

edit:
    #!/usr/bin/env bash
    code justfile