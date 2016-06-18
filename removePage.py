import sublime, sublime_plugin
import os

class removePageCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.PROJECT_NAME = 'yanxuan-wap'
		self.PROJECT_ROOT = self.getProjectRoot()
		self.JS_ROOT = self.PROJECT_ROOT + '/src/main/webapp/js/src'
		self.SASS_ROOT = self.PROJECT_ROOT + '/src/main/webapp/style/scss'
		self.FTL_ROOT = self.PROJECT_ROOT + '/src/main/webapp/WEB-INF'
		self.TDD_ROOT = self.PROJECT_ROOT + '/src/test/mock/tdd'

		self.view.window().show_input_panel('请输入要移除的页面名称 例如：item/list', '', self.handleIptDone, None, None)
	
	def handleIptDone(self, pageName):
		jsFileName = self.JS_ROOT + '/page/' + pageName + '.jsx'
		scssFileName = self.SASS_ROOT + '/page/' + pageName + '.scss'
		ftlFileName = self.FTL_ROOT + '/' + pageName + '.ftl'
		tddFileName = self.TDD_ROOT + '/' + pageName + '.tdd'

		fileList = [jsFileName, scssFileName, ftlFileName, tddFileName]

		for fileName in fileList:
			if os.path.exists(fileName):
				os.remove(fileName)
				print(fileName, '移除成功')
			else:
				print(fileName, '不存在')


	def getProjectRoot(self):
		fileName = os.getcwd()
		index = fileName.find(self.PROJECT_NAME)

		if index > -1:
			return fileName[0:index] + self.PROJECT_NAME

		return false

	def fixSlashIfInWin(self, str):
		if sublime.platform():
			return str.replace('/', '\\')

		return str



