from django.db import models
from django.conf import settings

from lxml import etree
# Create your models here.

class Article(models.Model):
    """Model for table article"""
    
    TRAVEL = 'travel'
    RECIPE = 'recipe'
    LIGHT = 'light'
    TECH = 'tech'
    CATEGORY_CHOICE = ((TRAVEL, "Travel"), 
                    (RECIPE, "Recipe"), 
                    (LIGHT, "Light"), 
                    (TECH, "Tech"))

    title = models.CharField(db_column="title", max_length=255)
    creation_time = models.DateTimeField(db_column="creation_time", auto_now_add=True)
    last_update = models.DateTimeField(db_column="last_update", auto_now=True)

#    author = models.ForeignKey("auth.user")
    xml_path = models.CharField(db_column="xml_path", max_length=255)
    category = models.CharField(db_column="category", max_length=20, choices=CATEGORY_CHOICE,
                                default=TRAVEL)

    class Meta:
        db_table = "article"
        app_label = "editor"
        managed = True
    
    def __unicode__(self):
        """Outputs some useful information for this instance"""
        
        return u"%s in %s in %s" % (self.title, self.category, self.creation_time)

    def parseXML(self):
        """parses xml file"""
        
        content = {}
        root = etree.parse(settings.XML_PATH + self.xml_path)
        content['paras'] = []
        for para in root.findall(".//p"):
            content['paras'].append(para.text)
        
        content['images'] = []
        for img in root.findall(".//img"):
            content['images'].append(etree.tostring(img))

        content['section'] = etree.tostring(root.find('section'))
        return content