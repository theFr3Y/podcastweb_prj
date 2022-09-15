# Generated by Django 4.0.5 on 2022-09-11 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_podcastermodel_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lasttname', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('publish', models.BooleanField(default=False)),
                ('sendtime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-sendtime'],
            },
        ),
        migrations.AlterField(
            model_name='podcastmodel',
            name='category',
            field=models.ManyToManyField(related_name='podcastercat', to='mainapp.podcastermodel'),
        ),
    ]
