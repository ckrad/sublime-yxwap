jsTplStr = """
var Module = require('extend/module');
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
    ReactDOM.render(<{yx:module} {...window.jsonData} cateList={window.cateList}/>, document.getElementById('j-bd'));
  }
});

new Page();
"""