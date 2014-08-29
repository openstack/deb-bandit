# -*- coding:utf-8 -*-
#
# Copyright 2014 Hewlett-Packard Development Company, L.P.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""Defines a set of tests targeting Import and ImportFrom nodes in the AST."""

import bandit
import bandit.context as b_context

def import_name_match(cur_context):
    context = b_context.Context(cur_context)
    info_on_import = ['pickle', 'subprocess', 'Crypto']
    for module in info_on_import:
        if context.is_module_imported(module):
            return(bandit.INFO,
                   "Consider possible security implications"
                   " associated with '%s' module" % module)


def import_name_telnetlib(cur_context):
    context = b_context.Context(cur_context)
    if context.is_module_imported('telnetlib'):
        return(bandit.ERROR, "Telnet is considered insecure. Use SSH or some"
               " other encrypted protocol.")
