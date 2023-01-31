# JewelryCatalog
### Yet-to-do: Permissions, authentications, get_or_create, using admin panel for login/logout, sessions, secrity, FRONTEND, Deployment
## Required Packages
> django, djangorestframework, pillow, psycopg2-binary
## Postgresql Database setup
> In settings (-> "Engine":"django.db.backends.postgresql_psycopg2"), Name, User, Password, Port, Host )
## Media Setup
> MEDIA_URL, MEDIA_ROOT - path setup for media files access(-> models.ImageField(upload_to = 'media/') )
> static(settings.MEDIA_URL, document_root=setting.MEDIA_ROOT), add this to urlpatterns in project level urls.py file
## Code Style
settings.py > models.py > serializers.py > views.py > urls.py > test
## Models/Entites involved
Users, Category, Products, GoldPrice, Price, Orders, OrderItem
## Entity Relationships
**One** user can have **Many** orders<br>
> Users - Orders (one-to-many relationship ) (models.ForienKey(Users, related_name = 'orders', on_delete = models.CASCADE)<br>
**One** category can have **Many** products<br>
> Category - Products ( one-to-many relationship ) (model.ForiegnKey(Category, related_name = 'products', on_delete = models.CASCADE)<br>
**One** order can have **Many** orderitems<br>
> Orders - OrderItem ( one-to-many relationship ) (models.ForiegnKey(Orders, related_name = 'orderitem', on_delete = models.CASCADE)<br>
**One** product can be included in **Many** orderitems<br>
> Products - OrderItem ( one-to-many relationship ) (models.ForiegnKey(Products, related_name = 'orderitem', on_delete = models.CASCADE)<br>
**One** product can be included in **One** Price ( contains product with price )<br>
> Product - Price (one-to-one relationship ) ( models.OneToOneField(Products, related_name = 'price', on_delete = models.CASCADE)<br>
**One** GoldPrice can be included in **Many** Price<br>
> GoldPrice - Price (ont-to-many relationship ) ( models.ForiegnKey(GoldPrice, related_name = 'Price', on_delete = models.CASCADE)<br>
### @property - decorator help to create user-defined field using functions. ex. to get total_cost for all items in the cart<br>
### class Meta in a model class contains attributes verbose_name_plural to remove 's' in admin panel and default_related_name to set default related name to all ForiegnKey, OneToOneField... attributes<br>
### related_name is very important it can be showed with an example ( in orders - orderitem, Orders can use related_name of OrderItem ('orderitem') to access all orderitem's objects )<br>
### If issues occur when migrating then use "python manage.py migrate --fake", it fakes the migration<br>
### def save(self, *args, **kwargs) method in models to update a column value right while saving to the database<br>
### CharField - choices; imageField - upload_to; DateTimeField - auto_now_add; DecimaField - max-digits; <br>
### from django.db.models import F --> F() can be Used to updating a column value by adding, multiplying, dividing.. a scalar to it.<br>
==> https://betterprogramming.pub/django-select-related-and-prefetch-related-f23043fd635d for detailed info about select_related() and prefetch_related().
### select_related()<br>
--> “follows” foreign-key relationships, selecting additional related-object data when it executes its query.<br>
--> We use select_related when the object that you're going to select is a single object, which means forward ForeignKey, OneToOne and backward OneToOne.
--> select_related works by creating an SQL join and including the fields of the related object in the SELECT statement. For this reason, select_related gets the related objects in the same database query.
### prefetch_related() 
--> it does a separate lookup for each relationship and does the “joining” in Python.
--> We use prefetch_related when we’re going to get a set of things.
--> That means forward ManyToMany and backward ManyToMany, ForeignKey. prefetch_related does a separate lookup for each relationship, and performs the “joining” in Python.
