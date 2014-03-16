#completions.py
import sublime
import sublime_plugin
import re

class LoveCompletions(sublime_plugin.EventListener):
    ST = 3000 if sublime.version() == '' else int(sublime.version())

    def __init__(self):
        old_seps = None

    def on_query_completions(self, view, prefix, locations):
        if ST < 3000 and ("moonscript" in view.scope_name(locations[0])):
            seps = view.settings().get("word_separators")
            if not old_seps:
                old_seps = seps
            seps = seps.replace('.', '')
            view.settings().set("word_separators", seps)
