from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, forms

from reports.models import Post
from users.models import SiteUser


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'image_link', 'release_date']
        labels = {
            'title': 'Post Title',
            'description': 'Description',
            'image_link': 'Image URL',
            'release_date': 'Post Release Date',
        }
        help_texts = {
            'image_link': 'This must be a link directly to the image file, not the page the image is on.',
        }