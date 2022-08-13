import ckan.plugins as p

class NetworkView(p.SingletonPlugin):

    p.implements(p.IConfigurer, inherit=True)
    p.implements(p.IResourceView, inherit=True)
    p.implements(p.ITemplateHelpers)

    def view_template(self):
        return 'networkview_base.html'
