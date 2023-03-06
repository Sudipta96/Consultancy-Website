from .models import StudentFeedback
from django import forms


RATING_CHOICES = (
        ('1', "ONE STAR"),
        ('2', "TWO STAR"),
        ('3', "THREE STAR"),
        ('4', "FOUR STAR"),
        ("5", "FIVE STAR")
    )

class StudentFeedbackForm(forms.ModelForm):
    # rating = forms.ModelChoiceField()
    class Meta:
        model = StudentFeedback
        fields = ("rating", "review",)
    
    # def clean_review(self):
    #     review = self.cleaned_data['review']
    #     if review == "":
    #         raise forms.ValidationError(f'Review can not be empty. Please fill it.')
        