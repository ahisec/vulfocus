# Generated by Django 2.2.10 on 2020-12-15 18:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('layout_image', '0003_auto_20201214_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='layout',
            name='is_release',
            field=models.BooleanField(default=False, verbose_name='是否发布，默认否'),
        ),
        migrations.AlterField(
            model_name='layout',
            name='layout_id',
            field=models.UUIDField(default=uuid.UUID('56de0b5b-0442-422b-8d37-57f8a6a8f89a'), editable=False, primary_key=True, serialize=False, verbose_name='编排UUID'),
        ),
        migrations.AlterField(
            model_name='layoutdata',
            name='layout_user_id',
            field=models.UUIDField(default=uuid.UUID('dcba0fb6-1411-4d61-80a1-4b327f587745'), editable=False, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='layoutservice',
            name='service_id',
            field=models.UUIDField(default=uuid.UUID('27b28489-316e-48b6-b6d9-0dfd8b64e3a7'), editable=False, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='layoutservicecontainer',
            name='service_container_id',
            field=models.UUIDField(default=uuid.UUID('a095269c-515a-4f4f-8cdc-285d4d504229'), editable=False, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='layoutservicenetwork',
            name='layout_service_network_id',
            field=models.UUIDField(default=uuid.UUID('a0723689-2d27-439e-a13e-53b58a675b59'), editable=False, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]