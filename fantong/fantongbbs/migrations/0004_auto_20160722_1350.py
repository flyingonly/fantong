# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-22 05:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fantongbbs', '0003_auto_20160722_0115'),
    ]

    operations = [
        migrations.CreateModel(
            name='BBSUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UAccount', models.EmailField(max_length=254)),
                ('UName', models.CharField(max_length=50)),
                ('UPassword', models.CharField(max_length=50)),
                ('UImage', models.ImageField(upload_to='')),
                ('UAdmin', models.BooleanField()),
                ('UFollowUserNum', models.IntegerField()),
                ('UFollowPostNum', models.IntegerField()),
                ('UPostNum', models.IntegerField()),
                ('UForbidden', models.BooleanField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Post',
            new_name='BBSPost',
        ),
        migrations.AlterField(
            model_name='bbspost',
            name='PUserID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fantongbbs.BBSUser'),
        ),
        migrations.AlterField(
            model_name='followuser',
            name='User1ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='followuser',
            name='User2ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followee', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userfollowpost',
            name='UserID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userlikepost',
            name='UserID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userreportpost',
            name='UserID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='bbsuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
