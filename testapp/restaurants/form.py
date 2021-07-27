from django import forms

class CommentForm(forms.Form):
    visitor = forms.CharField(max_length = 20)
    email = forms.EmailField(max_length=30, required=False, label='E-mail')
    content = forms.CharField(max_length=200, widget=forms.Textarea())

    #自訂 Content查驗 ，透過clean_字詞
    def clean_content(self):
        content = self.cleaned_data['content']
        if len(content)<5:
            raise forms.ValidationError('字數不足')
        return content