# Generated by Django 2.0 on 2019-06-10 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=100)),
                ('store_introduction', models.TextField(default='')),
                ('store_image', models.ImageField(blank=True, height_field='store_image_height', null=True, upload_to='', width_field='store_image_width')),
                ('store_image_width', models.IntegerField(default=0)),
                ('store_image_height', models.IntegerField(default=0)),
                ('store_address', models.TextField(default='')),
                ('store_phone', models.CharField(max_length=13)),
                ('store_opening_time', models.TextField(default='')),
                ('introduction_createtime', models.DateTimeField(verbose_name='date published')),
            ],
            options={
                'ordering': ['-introduction_createtime'],
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=100)),
                ('user_account', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='store',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Users'),
        ),
    ]
