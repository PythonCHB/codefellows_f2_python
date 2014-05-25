#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.
class Element(object):
    ''' Describe the Html render class'''
    
    tag = ''
    indent = '    '
    #html_attributes dict?

    def __init__(self, content=None, **html_attributes):
        self.html_attributes = html_attributes
        if content is not None:
            self.content = [content]
        else:
            self.content = []

    def render(self, file_out, ind=''):
        html_attributes = ['%s="%s"' % (k, v) for k, v in self.html_attributes.items()]
        file_out.write('\n%s<%s %s>' % (ind, self.tag, ' '.join(html_attributes)))
        for item in self.content:
            try:
                item.render(file_out, ind + self.indent)
            except AttributeError:
                file_out.write('\n' + self.indent + ind + item)
        file_out.write('\n%s<%s/> ' % (ind, self.tag))

    def append(self, a_string):
        self.content.append(a_string)

class Html(Element):
    tag = u'html'


class Body(Element):
    tag = u'body'

class P(Element):
    tag = u'p'

class Head(Element):
    tag = u'head'


class OneLineTag(Element):
    ''' Renders a one line tage where appropriate from the Element class '''
    def render(self, file_out, ind=''):
        file_out.write('\n%s<%s >' % (ind, self.tag))
        for item in self.content:
            try:
                item.render(file_out, ind+self.indent)
            except AttributeError:
                file_out.write(item)
        file_out.write('<%s/> ' % (self.tag))

class Title(OneLineTag):
    tag = u'title'
        

class SelfClosingTag(Element):
    ''' Renders a one line tage where appropriate from the Element class '''
    def render(self, file_out, ind=''):
        file_out.write('\n%s<%s>' % (ind, self.tag))

class Hr(SelfClosingTag):
    tag = u'hr/'

class Br(SelfClosingTag):
    tag = u'br/'

class A(Element):
    """ link and content rendered as Element's html_attributes with explicit use of 'href' """
    def __init__(self, link, content, **kwargs): # kwargs allows for other attributes, if necessary
        super(A, self).__init__(content, href=link, **kwargs) 
                                                                            
class Ul(Element):
    tag = u'ul'

class Li(Element):
    tag = u'li'

class Header(Element):
    pass
