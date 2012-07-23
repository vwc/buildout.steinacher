from five import grok
from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedBlobImage
from plone.app.textfield import RichText

from plone.directives import form

from sa.overview import _


class IOvContent(form.Schema, IImageScaleTraversable):
    """
    Description of the Example Type
    """
    preview = RichText(
        title=_(u"Preview List Items"),
        description=_(u"Please enter the items you wish to display as a "
                      U"preview in listings optionally formatted as a list."),
        required=False,
    )
    image = NamedBlobImage(
        title=_(u"Image"),
        required=True,
    )
    maintext = RichText(
        title=_(u"Haupttext"),
        required=False,
    )
