from five import grok
from Acquisition import aq_inner
from plone.directives import dexterity, form
from Products.CMFCore.utils import getToolByName
from plone.namedfile.interfaces import IImageScaleTraversable

from plone.app.contentlisting.interfaces import IContentListing

from steinacher.sitecontent.contentpage import IContentPage


class IPreviewFolder(form.Schema, IImageScaleTraversable):
    """
    A folder with extended listing view
    """


class PreviewFolder(dexterity.Container):
    grok.implements(IPreviewFolder)


class View(grok.View):
    grok.context(IPreviewFolder)
    grok.require('zope2.View')
    grok.name('view')

    def update(self):
        self.has_pages = len(self.content_pages()) > 0

    def content_pages(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        results = catalog(object_provides=IContentPage.__identifier__,
                          path=dict(query='/'.join(context.getPhysicalPath()),
                                    depth=1),
                          sort_on='getObjPositionInParent',
                          review_state='published')
        resultlist = IContentListing(results)
        return resultlist
