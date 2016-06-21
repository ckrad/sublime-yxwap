import sublime_plugin
from .commandBase import commandBase

class removeServiceCommand(sublime_plugin.TextCommand, commandBase):
	def run(self, edit):
		self.config()
		self.view.window().show_input_panel('请输入移除的服务链接前缀 例如：/xhr/u/login', '', self.handleIptDone, None, None)
	
	def handleIptDone(self, serviceLinkPre):
		self.serviceLinkPre = serviceLinkPre

		self.rm(self.getServiceFileName(serviceLinkPre))
		self.rm(self.getXhrDir(serviceLinkPre))