from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary import CloudinaryImage
from cloudinary.utils import cloudinary_url
from cloudinary.uploader import upload
from cloudinary.models import CloudinaryField
from PIL import Image
from django.urls import reverse
from django.utils import timezone
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

# Create your models here.



class User(AbstractUser):
    email = models.EmailField(unique=True)


# User profile model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='norm_user')
    profile_img = CloudinaryField('image', null=True, blank=True)
    phone_num = models.CharField(max_length=12, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    # for adding to cart after logging out and logging back in
    old_cart = models.CharField(max_length=1000, null=True, blank=True)
    # for adding to wishlist after logging out and logging back in
    old_wishlist = models.CharField(max_length=1000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    mute = models.BooleanField(default=False)

    @property
    def profile_pic(self):
        if self.profile_img:
            # Use Cloudinary's image transformation to resize the image
            return CloudinaryImage(str(self.profile_img)).build_url(width=500, height=500, crop='fill', format='jpg')
        else:
            return None


class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    category_logo = CloudinaryField('image', null=True, blank=True)

    class Meta:
        ordering = ['category_name']

    @property
    def category_pic(self):
        if self.category_logo:
            # Use Cloudinary's image transformation to resize the image
            return CloudinaryImage(str(self.category_logo)).build_url(width=500, height=500, crop='fill', format='jpg')
        else:
            return None

    def __str__(self):
        return self.category_name

    # def get_absolute_url(self):
    #     return reverse('ecommerce:school_detail', args=[self.id])



class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categorize')
    product_name = models.CharField(max_length=100)
    product_img = CloudinaryField('image', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True, default='')
    parts = models.CharField(max_length=100, null=True, blank=True)
    posted_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    # on sale?
    sale = models.BooleanField(default=True)

    class Meta:
        unique_together = ('product_name', 'category')

    def get_absolute_url(self):
        """this is used to get the detail url for order"""
        return reverse('ecommerce:product_detail',
                       args=[self.pk])

    @property
    def product_pic(self):
        if self.product_img:
            # Use Cloudinary's image transformation to resize the image
            return CloudinaryImage(str(self.product_img)).build_url(
                width=500,
                height=500,
                crop='fill',
                format='jpg'
            )
        return None

    def __str__(self):
        return self.product_name





@receiver(post_save, sender=User)
def create_token(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        instance.save()

