from django.db import models

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

# Create your models here.


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    # TODO: Define fields here
    owner = models.ForeignKey('auth.User',
                              related_name='snippets',
                              on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    highlighted = models.TextField()
    language = models.CharField(
        choices=LANGUAGE_CHOICES,
        default='python',
        max_length=100
    )
    style = models.CharField(
        choices=STYLE_CHOICES,
        default='friendly',
        max_length=100
    )

    class Meta:
        verbose_name = "Snippet"
        verbose_name_plural = "Snippets"
        ordering = ('created',)

    def __str__(self):
        return "%s" % self.pk

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a higlighted
        HTML representation of the code snippet
        """
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style,
                                  linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code,
                                     lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)

    # TODO: Define custom methods here
