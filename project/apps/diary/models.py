from django.db import models
from django.conf import settings
from datetime import datetime
import logging

from lxml import etree
from lxml.etree import XMLSyntaxError
# Create your models here.

class Diary(models.Model):
    """Model for table Diary"""
    
    TRAVEL = 'travel'
    RECIPE = 'recipe'
    LIGHT = 'light'
    TECH = 'tech'
    CATEGORY_CHOICE = ((TRAVEL, "Travel"), 
                    (RECIPE, "Recipe"), 
                    (LIGHT, "Light"), 
                    (TECH, "Tech"))

    title = models.CharField(db_column="title", max_length=255)
    creation_time = models.DateTimeField(db_column="creation_time", default=datetime.now())
    last_update = models.DateTimeField(db_column="last_update", auto_now=True)

    xml_path = models.CharField(db_column="xml_path", max_length=255)
    category = models.CharField(db_column="category", max_length=20, choices=CATEGORY_CHOICE,
                                default=TRAVEL)
    #tags = models.CharField(db_column="tags", max_length=255)

    class Meta:
        db_table = "diary"
        app_label = "diary"
        managed = True
    
    def __unicode__(self):
        """Outputs some useful information for this instance"""
        
        return u"%s in %s at %s" % (self.title, self.category, self.creation_time)

    def readFromXML(self):
        """parses xml file"""
        
        root = etree.parse(settings.XML_PATH + self.xml_path)
        return etree.tostring(root.find('section'))

    def writeToXML(self, context):
        """ Write context to xml file, save it, and return the file path. """
        
        root = etree.Element("diary")
        title = etree.SubElement(root, "title")
        title.text = self.title

        category = etree.SubElement(root, "category")
        category.text = self.category

        date_time = etree.SubElement(root, "date-time")
        date = etree.SubElement(date_time, "date")
        date.text = self.creation_time.strftime("%d-%m-%Y")
        time = etree.SubElement(date_time, "time")
        time.text = self.creation_time.strftime("%H:%M:%S")
        
        context = context.replace("\n", "") #remove all '\n' if any
        context = context.replace("&nbsp;", "")
        context = context.replace("<p></p>", "") #remove empty paragraph
        try:
            section = etree.XML("<section>%s</section>"%context)
            root.append(section)
        except XMLSyntaxError, e:
            logging.warning(context)
            logging.error("%s"%e) #logout
            return False

        tree = etree.ElementTree(root)
        file_path = "%s/[%s]%s.xml" % (self.category, 
        	self.creation_time.strftime("%Y-%m-%dZ%H:%M:%S"), self.title)

        tree.write(settings.XML_PATH + file_path)
        logging.debug("diary saved.")
        return file_path
        
    def setXMLPath(self, path):
       """ Set xml path """
       self.xml_path = path


    def  get_absolute_url(self):
       
       return ("diary-detail", (), {"id":self.pk})
    get_absolute_url = models.permalink(get_absolute_url)