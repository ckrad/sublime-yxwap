import sublime
import os
import shutil

class commandBase:
	def config(self):
		self.PROJECT_ROOT = self.getProjectRoot()
		self.JS_ROOT = self.PROJECT_ROOT + '/src/main/webapp/js/src'
		self.SASS_ROOT = self.PROJECT_ROOT + '/src/main/webapp/style/scss'
		self.FTL_ROOT = self.PROJECT_ROOT + '/src/main/webapp/WEB-INF'
		self.TDD_ROOT = self.PROJECT_ROOT + '/src/test/mock/tdd'
		self.XHR_ROOT = self.PROJECT_ROOT + '/src/test/mock/xhr'

	def getProjectRoot(self):
		return sublime.active_window().folders()[0]

	def fixSlashIfInWin(self, str):
		if sublime.platform():
			return str.replace('/', '\\')

		return str

	def touch(self, options):
		fileName = self.fixSlashIfInWin(options['fileName'])

		if os.path.exists(fileName):
			print(fileName, '已存在')
			return -1

		baseDir = os.path.dirname(fileName)
		if not os.path.exists(baseDir):
			os.makedirs(baseDir)

		file = open(fileName, 'w+')
		if 'content' in options.keys():
			file.write(options['content'])
		file.close()

		print(fileName, '创建成功')

	def rm(self, path):
		if os.path.exists(path):
			if os.path.isdir(path):
				shutil.rmtree(path)
			else:
				os.remove(path)
			print(path, '移除成功')
		else:
			print(path, '不存在')

	def open(self, fileName):
		if os.path.exists(fileName):
			self.view.window().open_file(fileName)

	def pathToModuleName(self, path, allTitle=False):
		str = ''

		if path[0] == '/':
			path = path[1:len(path)]
		
		for i, name in enumerate(path.split('/')):
			if i != 0 or allTitle == True:
				name = name.title()

			str += name

		return str
			
	def getServiceFileName(self, serviceLinkPre):
		return self.JS_ROOT + '/service/' + self.getServiceName(serviceLinkPre) + '.js'

	def getServiceName(self, serviceLinkPre):
		return self.pathToModuleName(serviceLinkPre.replace('/xhr', '')) + 'Service'

	def addQuoteToStr(self, str):
		return '\'' + str + '\''

	def getXhrFileName(self, serviceLinkPre, method):
		return self.getXhrDir(serviceLinkPre) + '/' +  method + '.json'

	def getXhrDir(self, serviceLinkPre):
		return self.XHR_ROOT + '/' + serviceLinkPre.replace('/xhr', '')

	def splitWordsByComma(self, str):
		words = str.split(',')

		return [word.strip() for word in words]
