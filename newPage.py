import sublime_plugin
from .commandBase import commandBase

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

class newPageCommand(sublime_plugin.TextCommand, commandBase):
	def run(self, edit):
		self.config()
		self.view.window().show_input_panel('请输入页面名称 例如：item/list', '', self.handleIptDone, None, None)
	
	def handleIptDone(self, pageName):
		jsFileName = self.JS_ROOT + '/page/' + pageName + '.jsx'
		scssFileName = self.SASS_ROOT + '/page/' + pageName + '.scss'
		ftlFileName = self.FTL_ROOT + '/' + pageName + '.ftl'
		tddFileName = self.TDD_ROOT + '/' + pageName + '.tdd'
		moduleName = self.pathToModuleName(pageName)

		fileList = [
			{
				'fileName': tddFileName,
				'content': tddTplStr
			},
			{
				'fileName': ftlFileName,
				'content': ftlTplStr.replace('{yx:module}', moduleName)
			},
			{
				'fileName': scssFileName
			},
			{
				'fileName': jsFileName, 
				'content': jsTplStr.replace('{yx:module}', self.pathToModuleName(pageName, True))
			}
		]

		for file in fileList:
			self.touch(file)
			self.open(file['fileName'])
