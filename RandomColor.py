import sublime, sublime_plugin
import random

class RandomColorCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for i in self.view.sel():
			x = random.randint(0, 16777215)
			if (i.begin()-i.end()) < 0:
				self.view.replace(edit, i, "#%06x" % x)
			else:
				self.view.insert(edit, i.begin(), "#%06x" % x)
		return self.view.sel()[0]