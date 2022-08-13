import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

class NetworkView(plugins.SingletonPlugin):

    plugins.implements(plugins.IConfigurer, inherit=True)
    plugins.implements(plugins.IResourceView, inherit=True)
    plugins.implements(plugins.ITemplateHelpers)

    def update_config(self, config):
        toolkit.add_template_directory(config, 'theme/templates')
        toolkit.add_public_directory(config, 'public')
        toolkit.add_resource('fanstatic', 'dreddx_networkview')

    def view_template(self):
        return 'networkview_base.html'
