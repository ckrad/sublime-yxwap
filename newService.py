import sublime, sublime_plugin

class newServiceCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.window().show_input_panel('请输入服务参数(serviceName, method1, method2...) 例如：wap/item, add, del', '', self.handleIptDone, None, None)
	
	def handleIptDone(self, argsStr):
		args = args.strip(' ').split()