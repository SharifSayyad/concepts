from django import forms



class StudentForm(forms.Form):
    name = forms.CharField()
    mark = forms.IntegerField()


    def clean_name(self):
        inputname = self.cleaned_data['name']
        if inputname == 'sharif':
            raise forms.ValidationError('User alrady avalable')
        return inputname