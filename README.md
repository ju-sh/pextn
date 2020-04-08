# pextn

A simple, lazy utility to display information about a file extension.

Can be used as command or a module.

<h2>Installation</h2>

Can be installed with pip using

    pip install pextn

<h2>Command line usage</h2>

    python3 -m pextn rst

would give

    Extension: rst
    --------------
    reStructuredText
    Used by: Docutils

<h2>Usage as module</h2>

The `pextn()` function can be used. It accepts the extension name as string.

Return value would be a list of lists.

Each sub-list corresponds to an entry related to that extension.

It consists of two elements:
 - The type of file which use the extension
 - The kind of software capable of manipulating such a file

For example,

    from pextn import pextn
    info = pextn("py")
    print(info)

would give

    [['Python script file', 'Python interpreter']]

and

    pextn("c")

returns

[['C source file', 'C compilers'], ['Unix file archive', 'COMPACT']]

<h2>Data source</h2>

The data used is almost entirely from [Wikipedia](https://en.wikipedia.org/wiki/List_of_filename_extensions).
