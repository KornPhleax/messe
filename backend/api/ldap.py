#!/usr/bin/env python
# encoding: utf-8
from ldap3 import Server, Connection, Tls, ALL, SUBTREE
from ldap3.core.exceptions import LDAPException, LDAPBindError
import ssl

class LDAP:
    def __init__(self, server_addr, root_dn, bind_user="admin", pw="admin"):
        self.root_dn = root_dn
        self.bind_user = bind_user
        self.bind_user_pw = pw
        self.server = Server(server_addr, get_info=ALL, use_ssl = False)

    def health(self):
        return self.authenticate(f"cn={self.bind_user}", self.bind_user_pw)

    def authenticate(self, object, password):
        try:
            return True, Connection(
                self.server,
                user=f"{object},{self.root_dn}",
                password=password,
                auto_bind=True,
            )
        except (LDAPBindError) as e:
            return False, e

    def authenticate_user(self, uid, password):
        cn = self.__get_dn_from_uid(uid)
        if cn:
            ldap_object = f"cn={cn},ou=users"
            return self.authenticate(ldap_object, password)
        return False,"user not found"

    def __get_dn_from_uid(self, uid):
        c = Connection(
                self.server,
                user=f"cn={self.bind_user},{self.root_dn}",
                password=self.bind_user_pw,
                auto_bind=True,
            )
        c.search(f'ou=users,{self.root_dn}', f'(&(objectclass=posixAccount)(uid={uid}))', attributes=['cn', 'uid'])
        if len(c.entries) > 0:
            return c.entries[0].cn
        return False