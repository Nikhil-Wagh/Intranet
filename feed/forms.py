from django import forms


class ProjectForm(forms.Form):
    name = forms.CharField(label='Name', max_length=250)
    manager_id = forms.CharField(label='Manager Id', max_length=10)
    description = forms.CharField(widget=forms.Textarea)


class ModuleForm(forms.Form):
    name = forms.CharField(label='Name', max_length=250)
    description = forms.CharField(widget=forms.Textarea)


class CommitForm(forms.Form):
    name = forms.CharField(label='Name', max_length=250)
    description = forms.CharField(widget=forms.Textarea)
    user_id = forms.IntegerField(label='User Id')
    file = forms.FileField(label='Upload File')


class CommentForm(forms.Form):
    name = forms.CharField(label='Name', max_length=250)
    user_id = forms.IntegerField(label='User Id')
    description = forms.CharField(widget=forms.Textarea)
    file = forms.FileField(label='Upload File')
