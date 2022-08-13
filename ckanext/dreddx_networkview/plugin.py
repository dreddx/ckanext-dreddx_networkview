import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

class NetworkView(plugins.SingletonPlugin):

    plugins.implements(plugins.IConfigurer, inherit=True)
    plugins.implements(plugins.IResourceView, inherit=True)
    plugins.implements(plugins.ITemplateHelpers)

    def get_helpers(self):
        return {}

    def update_config(self, config):
        toolkit.add_template_directory(config, 'theme/templates')
        toolkit.add_public_directory(config, 'public')
        toolkit.add_resource('fanstatic', 'dreddx_networkview')

    def info(self):
        return {
            'name': 'networkview',
            'title': 'Network',
            'icon': 'connectdevelop',
            'iframed': False,
            'filterable': False,
            'schema': {},
        }

    def can_view(self):
        return True

    def view_template(self):
        return 'networkview_base.html'
