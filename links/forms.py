from django import forms
from .models import UserProfile, Link
from .models import Vote

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        exclude = ("submitter", "rank_score")

class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
