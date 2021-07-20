from django.forms import ModelForm
from appscore import models
class frm_Question(ModelForm):
    class Meta:
        model=models.Mdl_Question
        fields='__all__'

class frm_Answer(ModelForm):
    class Meta:
        model=models.Mdl_Answers
        exclude=['question']      