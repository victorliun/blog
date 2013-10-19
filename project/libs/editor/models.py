from django.db import models
from django.utils import timezone
# Create your models here.

class Article(models.Model):
    """Model for table article"""
    
    TRAVEL = 'tl'
    RECIPE = 'rp'
    LIGHT = 'lt'
    TECH = 'th'
    CATEGORY_CHOICE = ((TRAVEL, "Travel"), 
                    (RECIPE, "Recipe"), 
                    (LIGHT, "Light"), 
                    (TECH, "Tech"))

    title = models.CharField(db_column="title", max_length=255)
    creation_time = models.DateTimeField(db_column="creation_time", default=timezone.now)
    last_update = models.DateTimeField(db_column="last_update", default=timezone.now)

#    author = models.ForeignKey("auth.user")
    xml_path = models.CharField(db_column="xml_path", max_length=255)
    category = models.CharField(db_column="category", max_length=2, choices=CATEGORY_CHOICE,
                                default=TRAVEL)

    class Meta:
        db_table = "article"
        app_label = "editor"
        managed = True
    
    def __unicode__(self):
        """Outputs some useful information for this instance"""
        
        return u"%s in %s in %s" % (self.title, self.category, self.creation_time)