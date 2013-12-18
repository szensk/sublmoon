Description
===========

Moonscripty is a package for [Sublime Text 2/3](http://www.sublimetext.com) for MoonScript developers. It adds a live parser based on [LuaSublime](https://github.com/rorydriscoll/LuaSublime) and [Love](https://love2d.org) completions to [moonscript-tmbundle](https://github.com/leafo/moonscript-tmbundle).

Installation
============

You can install this package through [Package Control](https://sublime.wbond.net/installation), simply use Command Palette: Package Control Install Package -> Moonscripty.

Alternatively, you can install this package by running the following command in your Packages directory:

    git clone git://github.com/szensk/sublmoon.git

Error checking
--------------
By default any moon file will be run through moonc -p and the first encountered error is outlined.

To disable or change this behavior

```json
{
   	"live_parser": true,
   	"live_parser_style": "{dot|circle|outline}",
   	"live_parser_persistent:" false,
   	"moonc_path": "moonc"
}
```

in Moonscript > User Settings.

Syntax highlighting
-------------------
![alt text](https://i.imgur.com/eAn0ZlG.png "syntax hightlighting")

Command Palette: Set Syntax: Moonscript

Completions
-----------
LuaDoc tags are available in comments. For example. "@param" expands to "-- @param type name desc". Love2D functions are available by default. To disable them, simply delete the Love.sublime-completions file.

Build Modes
-----------
* Ctrl + B: Run script with moon

* Ctrl + Shift + B: Compile file with moonc

* Command Palette: "moonc: show Lua" will output to the build panel.

* Command Palette: "ldoc" commands generate documentation using [LDoc](https://github.com/stevedonovan/LDoc).

* Command Palette: "love" commands execute the current file (or project directory) with [Love](https://love2d.org).
