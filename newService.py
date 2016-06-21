import sublime_plugin
from .commandBase import commandBase

serviceTplStr = """
var createService = require('service/createService');

var {yx:serviceName} = createService('{yx:serviceLinkPre}', [{yx:serviceMethods}]);

module.exports = {yx:serviceName};
"""

xhrTplStr = """
{"code": 200, "data": []}
"""

class newServiceCommand(sublime_plugin.TextCommand, commandBase):
	def run(self, edit):
		self.config()
		self.view.window().show_input_panel('请输入服务链接前缀 例如：/xhr/u/login', '', self.handleEnterServiceLinkPre, None, None)
	
	def handleEnterServiceLinkPre(self, serviceLinkPre):
		self.serviceLinkPre = serviceLinkPre

		self.view.window().show_input_panel('请输入需要生成的方法, 多个方法用逗号分隔 例如：add, list...', '', self.handleEnterServiceMethods, None, None)

	def handleEnterServiceMethods(self, serviceMethodsStr):
		self.serviceMethods = self.splitWordsByComma(serviceMethodsStr)
		self.createService()

	def createService(self):
		jsFileName = self.getServiceFileName(self.serviceLinkPre) 
		self.touch({
			'fileName': jsFileName,
			'content': serviceTplStr
						.replace('{yx:serviceName}', self.getServiceName(self.serviceLinkPre))
						.replace('{yx:serviceLinkPre}', self.serviceLinkPre)
						.replace('{yx:serviceMethods}', ', '.join(map(self.addQuoteToStr, self.serviceMethods)))
		})
		self.open(jsFileName)

		for method in self.serviceMethods:
			jsonFile = self.getXhrFileName(self.serviceLinkPre, method)
			self.touch({
				'fileName': jsonFile,
				'content': xhrTplStr
			})
			self.open(jsonFile)