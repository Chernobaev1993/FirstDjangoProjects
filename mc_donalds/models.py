from django.db import models


class Order(models.Model):
    # CREATE TABLE ORDERS (
    #     order_id INT AUTO_INCREMENT NOT NULL,
    #     time_in DATETIME NOT NULL,
    #     time_out DATETIME,
    #     cost FLOAT NOT NULL,
    #     pickup INT NOT NULL,
    #     staff INT NOT NULL,
    #
    #     PRIMARY KEY (order_id),
    #     FOREIGN KEY (staff) REFERENCES STAFF (staff_id)
    # );

    time_in = models.DateTimeField(auto_now_add=True)
    time_out = models.DateTimeField(null=True)
    cost = models.FloatField(default=0.0)
    pickup = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)

    staff = models.ForeignKey('Staff', on_delete=models.CASCADE)
    # staff — models.ForeignKey('Staff', on_delete=models.CASCADE)


class Product(models.Model):
    # CREATE TABLE PRODUCTS (
    #     product_id INT AUTO_INCREMENT NOT NULL,
    #     name CHAR(255) NOT NULL,
    #     price FLOAT NOT NULL,
    #     PRIMARY KEY (product_id)
    # );

    name = models.CharField(max_length=255)
    price = models.FloatField(default=0.0)


director = 'DI'
admin = 'AD'
cook = 'CO'
cashier = 'CA'
cleaner = 'CL'

POSITIONS = [
    (director, 'Директор'),
    (admin, 'Администратор'),
    (cook, 'Повар'),
    (cashier, 'Кассир'),
    (cleaner, 'Уборщик')
]


class Staff(models.Model):
    # CREATE TABLE STAFF (
    #     staff_id INT AUTO_INCREMENT NOT NULL,
    #     full_name CHAR(255) NOT NULL,
    #     position CHAR(255) NOT NULL,
    #     labor_contract INT NOT NULL,
    #
    #     PRIMARY KEY (staff_id)
    # );

    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=2, choices=POSITIONS, default=cashier)
    labor_contract = models.IntegerField()


class ProductOrder(models.Model):
    pass
