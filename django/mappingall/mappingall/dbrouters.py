
BACKUP_APP_LIST = ['manytomany','manytoone']
MYSQL_APP_LIST = ['onetoone','onetomany']

class MyDatabaseRouters(object):


    def db_for_read(self, model, **hints): #from which database you want read data
        if model._meta.app_label in MYSQL_APP_LIST:
            return 'backudb'
        elif model._meta.app_label in MYSQL_APP_LIST:
            return 'default'

    def db_for_write(self, model, **hints): # for which database you want write data
        if model._meta.app_label in BACKUP_APP_LIST:
            return 'backupdb'
        elif model._meta.app_label in MYSQL_APP_LIST:
            return 'default'

    def allow_relation(self, obj1, obj2, **hints):# relation allow or not
        if obj1._meta.app_label in ['onetoone','manytoone'] and \
                obj2._meta.app_label in ['onetoone','manytoone']:
            return True
        elif obj1._meta.app_label in ['onetomany','manytomany'] and \
                obj2._meta.app_label in ['onetomany','manytomany']:
            return True
        return None


    def allow_migrate(self, db, app_label, model_name=None, **hints):# to which migrate allowed
        pass

