"""
author: buppter
datetime: 2019/12/9 14:34
"""
import mistune
from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    nickname = forms.CharField(
        label="昵称",
        max_length=50,
        widget=forms.widgets.Input(
            attrs={'class': 'form-control', 'style': 'width:60%;'}
        )
    )

    email = forms.CharField(
        label="Email",
        max_length=50,
        widget=forms.widgets.EmailInput(
            attrs={'class': 'form-control', 'style': "width:60%;"}
        )
    )

    website = forms.CharField(
        label="网站",
        max_length=100,
        widget=forms.widgets.URLInput(
            attrs={'class': 'form-control', 'style': 'width:60%;'}
        )
    )

    content = forms.CharField(
        label="内容",
        max_length=500,
        widget=forms.widgets.Textarea(
            attrs={'rows': 2, 'cols': 40, 'class': 'form-control'}
        )
    )

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) < 10:
            raise forms.ValidationError("内容长度怎么能这么短呢！")
        content = mistune.markdown(content)
        return content

    class Meta:
        model = Comment
        fields = ['nickname', 'email', 'website', 'content']
