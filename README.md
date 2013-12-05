Description
===========

Moonscript is a package for [Sublime Text 2/3](http://www.sublimetext.com). It adds a live parser based on [LuaSublime](https://github.com/rorydriscoll/LuaSublime) to [moonscript-tmbundle](https://github.com/leafo/moonscript-tmbundle).

Installation
============

You can install this package through [Package Control](https://sublime.wbond.net/installation), simply use Command Palette: Package Control Install Package -> Moonscript.

Alternatively, you can install this package by running the following command in your Packages directory:
    
    git clone git://github.com/szensk/sublmoon.git

Error checking
--------------
By default any Lua file will be run through luac -p and the fir`st encountered error is outlined. The error is displayed in the status bar.

To disable or change this behavior

```json
{
   	"live_parser": false,
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
--------
LuaDoc tags are available in comments. For example. "@param" expands to "-- @param type name desc".
