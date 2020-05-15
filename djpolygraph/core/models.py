from django.db import models


class Paper(models.Model):
    type_paper = models.CharField(max_length=40, verbose_name="Тип бумаги")
    density = models.IntegerField(verbose_name="Плотность бумаги", blank=True, null=True)

    class Meta:
        verbose_name = "Тип бумаги"
        verbose_name_plural = "Тип бумаг"

    def __str__(self):
        if self.density is not None:
            return self.type_paper + ' ' + str(self.density)
        return self.type_paper
        

class Production(models.Model):
    name_product = models.CharField(max_length=35, verbose_name="Название продукта")
    paper = models.ManyToManyField(Paper)

    class Meta:
        verbose_name = "Продукция"
        verbose_name_plural = "Продукции"

    def __str__(self):
        return self.name_product


class Circulation(models.Model):
    min_count = models.IntegerField(verbose_name="Минимальное кол-во")
    max_count = models.IntegerField(verbose_name="Максимальное кол-во")

    class Meta:
        verbose_name = "Тираж"
        verbose_name_plural = "Тираж"

    def __str__(self):
        return f'Тираж от {self.min_count} до {self.max_count}'
        
    
class Colorfulness(models.Model):
    colorfulness = models.CharField(max_length=15, verbose_name="Красочность")

    class Meta:
        verbose_name = "Красочность"
        verbose_name_plural = "Красочность"

    def __str__(self):
        return self.colorfulness


class TypePrint(models.Model):
    name_print = models.CharField(max_length=40, verbose_name="Тип печати")
    production = models.ManyToManyField(Production)
    colorfulness = models.ManyToManyField(Colorfulness)
    count = models.ForeignKey(Circulation, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Вид печати"
        verbose_name_plural = "Виды печати"

    def __str__(self):
        return self.name_print

    


    





