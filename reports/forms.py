from django.forms import ModelForm

from reports.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'image_link']
        labels = {
            'title': 'Post Title',
            'description': 'Description',
            'image_link': 'Image URL',
        }
        help_texts = {
            'image_link': 'This must be a link directly to the image file, not only the the image is on.',
        }
