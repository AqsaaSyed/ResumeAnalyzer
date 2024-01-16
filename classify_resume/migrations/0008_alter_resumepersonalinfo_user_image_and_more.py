# Generated by Django 4.2.7 on 2023-12-11 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classify_resume', '0007_resumepersonalinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumepersonalinfo',
            name='user_image',
            field=models.ImageField(default='media/profile/default-info.jpg', upload_to='media/profile/'),
        ),
        migrations.CreateModel(
            name='ResumeEducationInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree_category', models.CharField(blank=True, max_length=256)),
                ('start_degree', models.DateField(blank=True, null=True)),
                ('end_degree', models.DateField(blank=True, null=True)),
                ('degree_image', models.ImageField(default='media/degree/default-degree.jpg', upload_to='media/degree/')),
                ('degree_description', models.TextField(blank=True, max_length=1000)),
                ('user_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_education_info', to='classify_resume.resumepersonalinfo')),
            ],
        ),
    ]
