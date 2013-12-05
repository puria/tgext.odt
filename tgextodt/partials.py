from tg import expose

@expose('tgextodt.templates.little_partial')
def something(name):
    return dict(name=name)