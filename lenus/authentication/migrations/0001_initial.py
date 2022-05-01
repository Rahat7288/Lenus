# Generated by Django 3.2 on 2021-05-02 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='users', serialize=False, to='auth.user')),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('profession', models.CharField(choices=[('DOC', 'Doctor'), ('FRS', 'Fire Service'), ('POL', 'Police'), ('VTR', 'Volunteer'), ('PHY', 'Physiotherapist')], default='VTR', max_length=15, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pics')),
                ('location', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('phone', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]
