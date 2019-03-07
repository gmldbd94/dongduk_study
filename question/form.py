from django import forms
from . import models
#
# class BlogForm(forms.ModelForm):
#     title = forms.CharField(label="제목", widget=forms.TextInput(attrs={"placeholder": "제목을 입력하시오"}))
#     context = forms.CharField(required=True, label="내용", widget=forms.Textarea(attrs={"placeholder": "내용을 입력하시오"}))
#     class Meta:
#         model = Blog
#         fields = [
#             'title',
#             'context',
#         ]
#
#     def clean_context(self):
#         context = self.cleaned_data.get("context")
#         if context == None:
#             raise forms.ValidationError("내용울 입력하시오")
#         return context

class CommentForm(forms.ModelForm):
    message = forms.CharField(label="댓글내용", widget=forms.Textarea())

    class Meta:
        model = models.Comment
        fields = [
            'message',
        ]

