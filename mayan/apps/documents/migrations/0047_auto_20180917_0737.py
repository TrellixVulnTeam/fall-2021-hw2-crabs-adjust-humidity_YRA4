from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0046_auto_20180917_0713'),
    ]

    operations = [
        migrations.AddField(
            field=models.DateTimeField(
                auto_now_add=True, db_index=True,
                default=django.utils.timezone.now, verbose_name='Date time'
            ), model_name='documentpagecachedimage', name='datetime',
            preserve_default=False,
        ),
        migrations.AddField(
            field=models.PositiveIntegerField(
                db_index=True, default=0, verbose_name='File size'
            ), model_name='documentpagecachedimage', name='file_size',
        ),
    ]