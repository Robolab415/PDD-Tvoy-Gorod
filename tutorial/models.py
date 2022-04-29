from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .files import image_upload, thumb_upload, create_thumbnail

class Ticket(models.Model):
    number = models.IntegerField(_("Номер билета"), unique=True, primary_key=True)
    question = models.TextField(_("Вопрос"), max_length=2000, help_text="Вопрос")
    choice1 = models.CharField(_("Вариант #1"), max_length=240, help_text="Вариант ответа")
    choice2 = models.CharField(_("Вариант #2"), max_length=240, help_text="Вариант ответа")
    choice3 = models.CharField(_("Вариант #3"), max_length=240, help_text="Вариант ответа")
    answer  = models.IntegerField(_("Номер правильного ответа"))
    image = models.ImageField(_("Изображение"), upload_to=image_upload, null=True, blank=True)
    thumbnail = models.ImageField(_("Превью"), upload_to=thumb_upload, null=True, blank=True)


    class Meta:
        ordering = ['number']

    def save(self, *args, **kwargs):
        adding = self._state.adding
        if adding:
            self.thumbnail = create_thumbnail(self.image)

        super().save(*args, **kwargs)

    def delete(self):
        for f in (self.image, self.thumbnail):
            f.delete(False)
        super().delete()

    def get_absolute_url(self):
        return reverse('ticket', args=[str(self.number)])

    def __str__(self):
        return 'Билет №'+str(self.number)


class Photo(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name="photos")
    photo = models.ImageField(_("Фотография"), upload_to=image_upload)
    thumbnail = models.ImageField(_("Превью"), upload_to=thumb_upload, null=True, blank=True)

    def save(self, *args, **kwargs):
        adding = self._state.adding
        if adding:
            self.thumbnail = create_thumbnail(self.photo)

        super().save(*args, **kwargs)

    def delete(self):
        for f in (self.photo, self.thumbnail):
            f.delete(False)
        super().delete()

    def get_absolute_url(self):
        return reverse('ticket', args=[str(self.ticket)])

    def __str__(self):
        return str(self.photo)
