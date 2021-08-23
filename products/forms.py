from django import forms
from .models import ProductReview

"""
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('product', 'name', 'body',)
        exclude = ('created_on',)

    def __init__(self, *args, **kwargs):
        
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        
        super().__init__(*args, **kwargs)
        placeholders = {
            'product': 'Book Title',
            'name': 'Your Name',
            'body': 'Your Review',
        }
"""
class ReviewForm(forms.ModelForm):

    class Meta:
        model = ProductReview
        exclude = ('product', 'user', 'date_added')
