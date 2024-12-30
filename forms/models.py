from django.db import models

class Form(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    QUESTION_TYPES = [
        ('text', 'Text'),
        ('dropdown', 'Dropdown'),
        ('checkbox', 'Checkbox'),
    ]
    form = models.ForeignKey(Form, related_name='questions', on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES)
    order = models.IntegerField()

    def __str__(self):
        return f"{self.order}. {self.text}"

    def save(self, *args, **kwargs):
        if not self.order:
            last_order = Question.objects.filter(form=self.form).aggregate(models.Max('order'))['order__max'] or 0
            self.order = last_order + 1
        super().save(*args, **kwargs)

class Option(models.Model):
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class Response(models.Model):
    form = models.ForeignKey(Form, related_name='responses', on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Response to {self.form.title} at {self.submitted_at}"

class Answer(models.Model):
    response = models.ForeignKey(Response, related_name='answers', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

   
    text = models.TextField(blank=True, null=True)

    # For single choice -> dropdown
    selected_option = models.ForeignKey(Option, related_name='selected_answers', on_delete=models.SET_NULL, blank=True, null=True)

    # For multiple choices -> checkbox
    selected_options = models.ManyToManyField(Option, related_name='multi_selected_answers', blank=True)

    def __str__(self):
        return f"Answer to {self.question.text}"
