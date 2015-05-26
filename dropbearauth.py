#!/usr/bin/env python

# Dropbear authentication, example of general custom authentication using return code 
# for keystone/openstack.
# 
# Pontus Freyhult, 2015
# Originally based on https://thestaticvoid.com/post/2013/06/04/customizing-the-openstack-keystone-authentication-backend/
#

from __future__ import absolute_import
import subprocess
import os
from . import sql

class Identity(sql.Identity):
    def _check_password(self, password, user_ref):
        username = user_ref.get('name')
        
        if (username in ['admin', 'nova', 'swift']):
            return super(Identity, self)._check_password(password, user_ref)

        os.putenv("DROPBEAR_PASSWORD",password)
        exit = subprocess.call(["dbclient", "-l",username,"tintin.uppmax.uu.se","true"])        

        if exit == 0: 
          return True

        # Be nice at first!
        return super(Identity, self)._check_password(password, user_ref)
        return False
