from django.forms import ModelForm

from reports.models import Post


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image_link'].required = False
