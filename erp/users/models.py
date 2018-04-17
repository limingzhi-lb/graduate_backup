from django.contrib.auth.models import AbstractUser
from django.db import models
import json


class JSONField(models.TextField):
    __metaclass__ = models.SubfieldBase
    description = "Json"

    def to_python(self, value):
        v = models.TextField.to_python(self, value)
        try:
            return json.loads(v)['v']
        except:
            pass
        return v

    def get_prep_value(self, value):
        return json.dumps({'v': value})


class User(AbstractUser):
    __name__ = 'User'
    staff_id = models.IntegerField(primary_key=True, db_index=True)
    is_leader = models.BooleanField(default=False)
    dep_id = models.IntegerField(null=False, db_index=True)
    status = models.BooleanField(default=True)

    class Meta(AbstractUser.Meta):
        pass


class Role(models.Model):
    __name__ = 'Role'
    role_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=24, db_index=True, null=False)
    permission = JSONField()


class OrgRole(models.Model):
    __name__ = 'OrgRole'
    role_id = models.IntegerField(primary_key=True, db_index=True)
    dep_category = models.IntegerField(db_index=True, null=False)

    class Meta:
        unique_together = ('role_id', 'dep_category')


class UserPermission(models.Model):
    __name__ = 'UserPermission'
    staff_id = models.IntegerField(db_index=True)
    action = models.CharField(max_length=24)
    resource = models.CharField(max_length=24)

    class Meta:
        unique_together = ('staff_id', 'action', 'resource')


class RolePermission(models.Model):
    __name__ = 'RolePermission'
    role_id = models.IntegerField(primary_key=True,db_index=True)
    permission = JSONField()


class UserRole(models.Model):
    __name__ = 'UserRole'
    staff_id = models.IntegerField(db_index=True)
    org_id = models.IntegerField(db_index=True)
    role_id = models.IntegerField(db_index=True)


class Department(models.Model):
    __name__ = 'Department'
    name = models.CharField(max_length=12, primary_key=True)
    category = models.IntegerField()
