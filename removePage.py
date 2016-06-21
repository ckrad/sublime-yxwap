import sublime_plugin
from .commandBase import commandBase

class removePageCommand(sublime_plugin.TextCommand, commandBase):
	def run(self, edit):
		self.config()
		self.view.window().show_input_panel('请输入要移除的页面名称 例如：item/list', '', self.handleIptDone, None, None)
	
	def handleIptDone(self, pageName):
		jsFileName = self.JS_ROOT + '/page/' + pageName + '.jsx'
		scssFileName = self.SASS_ROOT + '/page/' + pageName + '.scss'
		ftlFileName = self.FTL_ROOT + '/' + pageName + '.ftl'
		tddFileName = self.TDD_ROOT + '/' + pageName + '.tdd'

		fileList = [jsFileName, scssFileName, ftlFileName, tddFileName]

		for fileName in fileList:
			self.rm(fileName)