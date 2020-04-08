# pextn

A simple, lazy utility to display information about a file extension.

Can be used as command or a module.

##Command line usage

    python3 -m pextn rst

would give

    rst: reStructuredText

    Used by: Docutils

##Usage as module

    from pextn import pextn
    info = pextn("py")
    print(info)

would give


