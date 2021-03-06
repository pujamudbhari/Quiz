# Generated by Django 3.1.1 on 2020-09-14 11:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quizzes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizTaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('completed', models.BooleanField(default=False)),
                ('date_finished', models.DateTimeField(null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UsersAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='response',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='response',
            name='question',
        ),
        migrations.RemoveField(
            model_name='response',
            name='quiztaker',
        ),
        migrations.AlterModelOptions(
            name='quiz',
            options={'ordering': ['timestamp'], 'verbose_name_plural': 'Quizzes'},
        ),
        migrations.RemoveField(
            model_name='answer',
            name='text',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='created',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='questions_count',
        ),
        migrations.AddField(
            model_name='answer',
            name='label',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='quiz',
            name='image',
            field=models.ImageField(default=0, upload_to=''),
        ),
        migrations.AddField(
            model_name='quiz',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='label',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.DeleteModel(
            name='QuizTakers',
        ),
        migrations.DeleteModel(
            name='Response',
        ),
        migrations.AddField(
            model_name='usersanswer',
            name='answer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quizzes.answer'),
        ),
        migrations.AddField(
            model_name='usersanswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzes.question'),
        ),
        migrations.AddField(
            model_name='usersanswer',
            name='quiz_taker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzes.quiztaker'),
        ),
        migrations.AddField(
            model_name='quiztaker',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzes.quiz'),
        ),
        migrations.AddField(
            model_name='quiztaker',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
