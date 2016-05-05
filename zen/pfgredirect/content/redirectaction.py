"""Definition of the RedirectAction content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata
from Products.PloneFormGen.interfaces import IPloneFormGenThanksPage

from zen.pfgredirect.interfaces import IRedirectAction
from zen.pfgredirect.config import PROJECTNAME

RedirectActionSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

  atapi.StringField('redirectURL',
            widget=atapi.StringWidget(label="Redirect URL"),
            ),

))

RedirectActionSchema['title'].storage = atapi.AnnotationStorage()
RedirectActionSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(RedirectActionSchema, moveDiscussion=False)


class RedirectAction(base.ATCTContent):
    """Redirect Action"""
    implements(IRedirectAction, IPloneFormGenThanksPage)

    meta_type = "RedirectAction"
    schema = RedirectActionSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

atapi.registerType(RedirectAction, PROJECTNAME)
