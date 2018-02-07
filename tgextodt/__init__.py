# -*- coding: utf-8 -*-
"""The tgapp-odt package"""
from tempfile import NamedTemporaryFile
from py3o.template import Template
from tg.configuration import config
from tg.render import cached_template


class RenderOdt(object):
    """Singleton that can be called as the odt render function."""

    genshi_functions = {}

    def __call__(self, template_name, template_vars, **kwargs):

        # Gets document type from content type or from config options
        doctype = 'application/vnd.oasis.opendocument.text'
        method='odt'
        kwargs['doctype'] = doctype
        kwargs['method'] = method

        def render_template():
            finder = config['pylons.app_globals'].dotted_filename_finder
            odt_template_file = finder.get_dotted_filename(
                             template_name=template_name,
                             template_extension=".odt")
            output = NamedTemporaryFile()
            t = Template(odt_template_file, output.name)
            t.render(dict(document=template_vars))
            return output.read()

        return cached_template(
            template_name, render_template,
            **kwargs)


def setup_odt_renderer(self):
    self.render_functions.odt = RenderOdt()


def plugme(app_config, options):
    from types import MethodType
    app_config.setup_odt_renderer = MethodType(setup_odt_renderer, app_config)
    app_config.renderers.append('odt')
    return dict(appid='tgextodt', global_helpers=False)
