# Generated by Django 4.1.1 on 2022-09-17 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0004_alter_variacao_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='descricao_curta',
            field=models.TextField(max_length=255, verbose_name='Descrição curta'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='descricao_longa',
            field=models.TextField(verbose_name='Descrição longa'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco_marketing',
            field=models.FloatField(verbose_name='Preço Marketing'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco_marketing_promocional',
            field=models.FloatField(default=0, verbose_name='Preço Marketing promocional'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='tipo',
            field=models.CharField(choices=[('V', 'Variável'), ('S', 'Simples')], default='V', max_length=1),
        ),
    ]