import html


def avg(firs,*rest):
   return (firs + sum(rest)) / (1+len(rest))
print(avg(1,2))


def make_element(name, value, **attrs):
   keyvals = [' %s="%s"' % item for item in attrs.items()]
   attr_str = ''.join(keyvals)
   element = '<{name}{attrs}>{value}</{name}>'.format(
               name=name,
               attrs=attr_str,
               value=html.escape(value))
   return element
# Пример
# Создает '<item size="large" quantity="6">Albatross</item>'
print(make_element('item', 'Albatross', size='large', quantity=6))
print(make_element('p', '<spam>'))