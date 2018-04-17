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
    staff_id = models.IntegerField(primary_key=True,db_index=True)
    is_leader = models.BooleanField(default=False)
    dep_id = models.IntegerField(null=False,db_index=True)

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
