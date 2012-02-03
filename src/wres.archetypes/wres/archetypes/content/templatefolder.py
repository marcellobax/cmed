#coding=utf-8

"""Definition of the TemplateFolder content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-

from wres.archetypes.interfaces import ITemplateFolder
from wres.archetypes.config import PROJECTNAME

TemplateFolderSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

))

schemata.finalizeATCTSchema(
    TemplateFolderSchema,
    folderish=True,
    moveDiscussion=False
)


class TemplateFolder(folder.ATFolder):
    """A folder for medical templates."""
    implements(ITemplateFolder)

    meta_type = "TemplateFolder"
    schema = TemplateFolderSchema

atapi.registerType(TemplateFolder, PROJECTNAME)
