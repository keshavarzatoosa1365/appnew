from django.db import models
diff_choice=(
    ("easy","آسان"),
    ("medium","متوسط"),
    ("hard","سخت"),
)
class Mdl_Quize(models.Model):
    topic=models.CharField(max_length=50)
    difficulty=models.CharField(max_length=30,verbose_name="سطح سوال",choices=diff_choice)
    def __str__(self):
        return self.topic;
    def get_Mdl_Question(self):
        return self.mdl_Question_set.all();

class Mdl_Question(models.Model):
    quiz=models.ForeignKey(Mdl_Quize,on_delete=models.CASCADE,null=True,blank=True)
    question_text=models.CharField(max_length=2000,verbose_name="متن سوال")
    pub_date=models.DateField(verbose_name='تاریخ انتشار',auto_now_add=True,null=True,blank=True)
    class Meta:
        verbose_name=u"سوالات"
    def __str__(self):
        return self.question_text;
    def get_Mdl_Answers(self):
        return self.mdl_Answer_set.all()   

class Mdl_Answers(models.Model):
    question=models.ForeignKey(Mdl_Question,on_delete=models.CASCADE,null=True,blank=True)
    Answer_text=models.CharField(max_length=200,verbose_name="پاسخ")
    correct=models.BooleanField(default=False)
    class Meta:
        verbose_name=u"پاسخ "
    def __str__(self):
        return self.Answer_text; 


class Mdl_Result(models.Model):
    quiz=models.ForeignKey(Mdl_Quize,on_delete=models.CASCADE)
    score=models.IntegerField(default=0)
    def __str__(self):
        return self.score             




