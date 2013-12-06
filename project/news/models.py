from django.db import models

class Reporter(models.Model):
    first_name = models.CharField(db_column="first_name", max_length=20)
    last_name = models.CharField(db_column="last_name", max_length=20)
    email_addr = models.CharField(db_column="email_address", max_length=70)

    def __unicode__(self):
        return u"%s %s" %(self.first_name, self.last_name)

    class Meta:
        app_label = "news"
        db_table = "reporter"
        managed = True

class Article(models.Model):
    pub_date = models.DateField(db_column="publish_date")
    headline = models.CharField(db_column="headline", max_length=200)
    content = models.TextField(db_column="content")
    reporter = models.ForeignKey(Reporter)

    def __unicode__(self):
        return u"%s - %s" %(self.headline, self.reporter)

    class Meta:
        app_label = "news"
        db_table = "articles"
        managed = True
