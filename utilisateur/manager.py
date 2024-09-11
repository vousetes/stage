from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class utilisateurManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password=None, **extra_fields):

        if not email:
            raise ValueError("Le Email doit etre definie")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Un superuser doit avoir le champ is_staff a True")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Un superuser doit avoir le champ is_superuser a True")
        
        return self._create_user(email, password, **extra_fields)

    