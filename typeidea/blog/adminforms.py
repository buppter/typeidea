"""
author: buppter
datetime: 2019/12/5 19:40
"""
from django import forms


class PostAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea, label="摘要", required=False)
