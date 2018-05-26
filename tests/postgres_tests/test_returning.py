import datetime

from django.db import router
from django.db.models.sql import InsertQuery
from django.test import modify_settings

from . import PostgreSQLTestCase
from .models import JSONModel, ReturningModel


@modify_settings(INSTALLED_APPS={'append': 'django.contrib.postgres'})
class ReturningValuesTestCase(PostgreSQLTestCase):
    def test_pk_only(self):
        db = router.db_for_write(JSONModel)
        query = InsertQuery(JSONModel)
        query.insert_values(JSONModel._meta.fields, [], raw=False)
        # this line will PostgreSQLModel an AttributeError without the accompanying fix
        compiler = query.get_compiler(using=db)
        compiler.return_id = True
        sql = compiler.as_sql()[0][0]
        self.assertIn('RETURNING "postgres_tests_jsonmodel"."id"', sql)

    def test_multiple_fields(self):
        db = router.db_for_write(ReturningModel)
        query = InsertQuery(ReturningModel)
        query.insert_values(ReturningModel._meta.fields, [], raw=False)
        # this line will PostgreSQLModel an AttributeError without the accompanying fix
        compiler = query.get_compiler(using=db)
        compiler.return_id = True
        sql = compiler.as_sql()[0][0]
        self.assertIn('RETURNING "postgres_tests_returningmodel"."id"'
                      ', "postgres_tests_returningmodel"."created"', sql)

    def test_returning_value_on_obj(self):
        # ReturningModel uses database functions not python defaults
        obj = ReturningModel()
        obj.save()
        self.assertEquals(obj.pk, 1)
        self.assertIsInstance(obj.created, datetime.datetime)
