# Generated by Django 4.2.7 on 2023-11-22 14:00

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_bankaccount_id_alter_creditcard_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bank_account',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='credit_card',
        ),
        migrations.AlterField(
            model_name='bankaccount',
            name='id',
            field=models.UUIDField(default=uuid.UUID('77c9a5f9-7ab3-4cff-baab-c855f88fcb2f'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='id',
            field=models.UUIDField(default=uuid.UUID('468e5ac3-14d7-43cb-b99c-6c67f5596dc1'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.UUIDField(default=uuid.UUID('c59495a7-aa0f-4952-99c2-c68da5f4899f'), primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='UserBankRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.bankaccount')),
                ('credit_card', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.creditcard')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
    ]