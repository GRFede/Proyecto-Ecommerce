# Generated by Django 5.1.2 on 2024-11-03 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_remove_personas_foto_personas_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrearProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres_producto', models.CharField(max_length=20)),
                ('descripcion_breve_producto', models.CharField(max_length=200)),
                ('descripcion_extendida_producto', models.CharField(max_length=1000)),
                ('precio', models.IntegerField()),
                ('imagen_producto', models.ImageField(blank=True, null=True, upload_to='imagenes-productos')),
                ('categoria_producto', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='personas',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes-usuario'),
        ),
    ]
