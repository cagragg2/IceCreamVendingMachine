# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'IceCream'
        db.create_table(u'IceCreamVendingMachine_icecream', (
            ('iceCreamID', self.gf('django.db.models.fields.IntegerField')(default=0, primary_key=True)),
            ('flavor', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('scoopable', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'IceCreamVendingMachine', ['IceCream'])

        # Adding model 'Stores'
        db.create_table(u'IceCreamVendingMachine_stores', (
            ('storeID', self.gf('django.db.models.fields.IntegerField')(default=0, primary_key=True)),
            ('storeName', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal(u'IceCreamVendingMachine', ['Stores'])

        # Adding model 'WhereOffered'
        db.create_table(u'IceCreamVendingMachine_whereoffered', (
            ('storeID', self.gf('django.db.models.fields.IntegerField')(default=0, primary_key=True)),
            ('iceCreamID', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'IceCreamVendingMachine', ['WhereOffered'])

        # Adding unique constraint on 'WhereOffered', fields ['storeID', 'iceCreamID']
        db.create_unique(u'IceCreamVendingMachine_whereoffered', ['storeID', 'iceCreamID'])

        # Adding model 'Cart'
        db.create_table(u'IceCreamVendingMachine_cart', (
            ('iceCreamID', self.gf('django.db.models.fields.IntegerField')(default=0, primary_key=True)),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'IceCreamVendingMachine', ['Cart'])


    def backwards(self, orm):
        # Removing unique constraint on 'WhereOffered', fields ['storeID', 'iceCreamID']
        db.delete_unique(u'IceCreamVendingMachine_whereoffered', ['storeID', 'iceCreamID'])

        # Deleting model 'IceCream'
        db.delete_table(u'IceCreamVendingMachine_icecream')

        # Deleting model 'Stores'
        db.delete_table(u'IceCreamVendingMachine_stores')

        # Deleting model 'WhereOffered'
        db.delete_table(u'IceCreamVendingMachine_whereoffered')

        # Deleting model 'Cart'
        db.delete_table(u'IceCreamVendingMachine_cart')


    models = {
        u'IceCreamVendingMachine.cart': {
            'Meta': {'object_name': 'Cart'},
            'iceCreamID': ('django.db.models.fields.IntegerField', [], {'default': '0', 'primary_key': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'IceCreamVendingMachine.icecream': {
            'Meta': {'object_name': 'IceCream'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'flavor': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'iceCreamID': ('django.db.models.fields.IntegerField', [], {'default': '0', 'primary_key': 'True'}),
            'scoopable': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        u'IceCreamVendingMachine.stores': {
            'Meta': {'object_name': 'Stores'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'storeID': ('django.db.models.fields.IntegerField', [], {'default': '0', 'primary_key': 'True'}),
            'storeName': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'IceCreamVendingMachine.whereoffered': {
            'Meta': {'unique_together': "(('storeID', 'iceCreamID'),)", 'object_name': 'WhereOffered'},
            'iceCreamID': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'storeID': ('django.db.models.fields.IntegerField', [], {'default': '0', 'primary_key': 'True'})
        }
    }

    complete_apps = ['IceCreamVendingMachine']