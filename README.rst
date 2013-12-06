About tgextodt
-------------------------

tgextodt is a Pluggable application for TurboGears2 that allows the rendering of .odt (openoffice/libreoffice) documents as an output templates.

Installing
-------------------------------

tgextodt can be installed both from pypi or from bitbucket::

    pip install tgextodt

should just work for most of the users

Plugging tgextodt
----------------------------

In your application *config/app_cfg.py* import **plug**, then at the *end of the file* call plug with tgextodt::

    from tgext.pluggable import plug
    plug(base_config, 'tgextodt')


Usage
--------------------

To use an odt template you have to declare the type in your controller as below::

    @expose('odt:example.templates.about', content_type='application/vnd.oasis.opendocument.text')
    def about(self):
        response.headerlist.append(('Content-Disposition', 'attachment;filename=filename.odt'))
        return dict(hello='Hello World')


obviously in your *example* application in the folder *example/templates* you should provide a templated named about.odt in wich you have defined the variable field *py3o.document.hello*.

To define a variable field in libreoffice you can dig more information on https://help.libreoffice.org/Writer/Variables basically from the menu Insert -> Fields -> Other -> Variables

For more complex features, like for loops and more detailed reporting stuff, you want to read the documentation of the py3o library itself http://py3otemplate.readthedocs.org/

Now you can directly download your output from  **/about** or **/about.odt**

