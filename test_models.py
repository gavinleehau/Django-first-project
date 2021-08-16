import os
import django
import datetime

from django.utils.translation import activate
os.environ.setdefault("DJANGO_SETTINGS_MODule","myweb.settings")
django.setup()

from myapp.models import Place,  Restaurant, Reporter, Article,Publication,baiBao
# a=Python2104(ten="Le", tuoi = 20, diachi = "HCM")
# a.save()
# a=Python2104.objects.get(id=6)
# print(a.ten, a.id)
# a.delete()
# all_data = Python2104.objects.all()
# for item in all_data:
#     print(item.ten, item.tuoi)

# p1=Place(name="quan Ninh Kieu", address = "CT")
# p1.save()
# rest1 = Restaurant(place_id = 1, serves_hot_dogs = True, serves_pizza = False)
# rest1.save()

# rest1=Place.objects.get(id=3)
# print(rest1.id, rest1.name,rest1.address)
# rest1.delete()


# p2=Place(name="quan Cai Rang", address = "CT")
# p2.save()
# rest2 = Restaurant(place_id = 2, serves_hot_dogs = True, serves_pizza = False)
# rest2.save()

# p1 = Place.objects.get(name="quan Ninh Kieu")
# print(p1)
# print(p1.restaurant)

# all_rest = Restaurant.objects.all()
# for rest in all_rest:
#     print(rest.place.name) 
####### quan hệ 1-1: thong qua field: one-toone field
####### place 1-1 restaurant

# c1:
# reporter1 = Reporter.objects.create(first_name = "Le", last_name = "Hau", email = "Lehau@gmail.com")
# article1 = Article(headline="Hau béo",
# pub_date=datetime.datetime.now(), reporter_id = 1)
# article1.save()

# c2:
# reporter1 = Reporter.objects.get(id=1)
# reporter1.article_set.create(headline="Hau béo ú ù u",
# pub_date=datetime.datetime.now())

# lấy thông tin ra
# reportor1=Reporter.objects.get(pk=1)
# print(reportor1.first_name, reportor1.last_name)
# # print(reportor1.article_set.all())
# articles = Article.objects.filter(reporter_id=reportor1.id)
# for item in reportor1.article_set.all():
#     print(item.headline)

###### quan hệ 1-nhiều:


# Publication.objects.create(title ="title 1")
# Publication.objects.create(title ="title 2") 
# baiBao.objects.create(headline = "hd1")
# baiBao.objects.create(headline = "hd2")

pub1 = Publication.objects.get(title ="title 1")
pub2 = Publication.objects.create(title ="title 2")
b1 = baiBao.objects.get(headline = "hd1")
b2 = baiBao.objects.get(headline = "hd2")
# b1.publications.add(pub1,pub2)
pub1.baibao_set.add(b1,b2)