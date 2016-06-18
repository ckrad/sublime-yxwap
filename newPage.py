import sublime, sublime_plugin
import os

jsTplStr = """var Module = require('extend/module');
var Layout = require('component/common/layout');

var {yx:module} = React.createClass({
    render:function(){
      return(
        <Layout>
          <div className="g-row">
          </div>
        </Layout>
      );
    }
});

var Page = Module.extend({
  init:function(options) {
    this.supr(options);
    ReactDOM.render(<{yx:module} {...window.jsonData} />, document.getElementById('j-bd'));
  }
});

new Page();
"""

ftlTplStr = """<#include "/tmpl/layout/layout.ftl">
<#macro script>
    <script>
      var jsonData=${JSONObject.fromObject(data)};
    </script>
    <script src="/js/dist/{yx:module}.js"></script>
</#macro>
<#macro style>
  <link rel="stylesheet" href="/style/css/page/{yx:module}.css">
</#macro>
<@Layout script=script style=style>
<div class="g-bd">
    <div id="j-bd"></div>
</div>
</@Layout>
"""

tddTplStr = """{
	"data": {}
}
"""

class newPageCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.PROJECT_NAME = 'yanxuan-wap'
		self.PROJECT_ROOT = self.getProjectRoot()
		self.JS_ROOT = self.PROJECT_ROOT + '/src/main/webapp/js/src'
		self.SASS_ROOT = self.PROJECT_ROOT + '/src/main/webapp/style/scss'
		self.FTL_ROOT = self.PROJECT_ROOT + '/src/main/webapp/WEB-INF'
		self.TDD_ROOT = self.PROJECT_ROOT + '/src/test/mock/tdd'

		self.view.window().show_input_panel('请输入页面名称 例如：item/list', '', self.handleIptDone, None, None)
	
	def handleIptDone(self, pageName):
		jsFileName = self.JS_ROOT + '/page/' + pageName + '.jsx'
		scssFileName = self.SASS_ROOT + '/page/' + pageName + '.scss'
		ftlFileName = self.FTL_ROOT + '/' + pageName + '.ftl'
		tddFileName = self.TDD_ROOT + '/' + pageName + '.tdd'

		jsFile = self.touch(jsFileName)
		if jsFile:			
			jsFile.write(jsTplStr.replace('{yx:module}', self.getModuleName(pageName).title()))
			jsFile.close()
			print(jsFileName, '创建成功')

		scssFile = self.touch(scssFileName)
		if scssFile:			
			print(scssFile, '创建成功')

		ftlFile = self.touch(ftlFileName)
		if ftlFile:			
			ftlFile.write(ftlTplStr.replace('{yx:module}', self.getModuleName(pageName)))
			ftlFile.close()
			print(ftlFileName, '创建成功')

		tddFile = self.touch(tddFileName)
		if tddFile:			
			tddFile.write(tddTplStr)
			tddFile.close()
			print(tddFile, '创建成功')
			
	def handleIptCancel(self): 
		pass

	def touch(self, fileName):
		fileName = self.fixSlashIfInWin(fileName)

		if os.path.exists(fileName):
			print(fileName, '已存在')
			return -1

		baseDir = os.path.dirname(fileName)
		if not os.path.exists(baseDir):
			os.makedirs(baseDir)

		file = open(fileName, 'w+')
		return file

	def getProjectRoot(self):
		fileName = os.getcwd()
		index = fileName.find(self.PROJECT_NAME)

		if index > -1:
			return fileName[0:index] + self.PROJECT_NAME

		return false

	def getModuleName(self, pageName):
		str = ''
		for i, name in enumerate(pageName.split('/')):
			if i != 0:
				name = name.title()

			str += name

		return str

	def fixSlashIfInWin(self, str):
		if sublime.platform():
			return str.replace('/', '\\')

		return str



