from django.db import models
from tranches.utils import install_font, FontInstallationError


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
    name = models.CharField(max_length=255)
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        is_new = self._state.adding

        if is_new:
            if not self.file:
                raise ValueError('File is required')

            if not isinstance(self.file, File):
                raise TypeError('file must be an instance of File model')

            try:
                install_font(self.file.url)
            except FontInstallationError as e:
                raise FontInstallationError(f"Font installation failed: {str(e)}")

        super().save(*args, **kwargs)

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
