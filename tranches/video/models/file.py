from django.db import models


class File(models.Model):
    '''
    **Fields:**
    - name: CharField to store the name of the file.
    - url: URLField to store the URL where the file is located.
    - created_at: DateTimeField to store when the file was created.
    '''

    name = models.CharField(max_length=255)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Font(models.Model):
    '''
    **Fields:**
    - name: CharField to store the name of the font.
    - file: ForeignKey to the `File` model, representing the actual font file.
    - created_at: DateTimeField to store when the font was created.
    '''

    name = models.CharField(max_length=255)
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class AeVersion(models.Model):
    '''
    **Fields:**
    - name: CharField to store the name of the After Effects version.
    - created_at: DateTimeField to store when the version entry was created.
    '''
    
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
