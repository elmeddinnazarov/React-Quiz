# Generated by Django 4.2 on 2023-05-13 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizApp', '0005_alter_question_quiz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='quiz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quiz_reports', to='quizApp.quiz'),
        ),
    ]
