##############################################################################
#  Copyright (c) 2016 Intel Corporation
# 
# Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
# 
#      http://www.apache.org/licenses/LICENSE-2.0
# 
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
##############################################################################
#    File Abstract: 
#       Various helper utilities
##############################################################################
import traceback
import os
from Helpers import Alias

def IsNumeric(value):
    try:
        val = float(value)
        return True
    except ValueError:
        return False

def getCallStack(DoNotShowSystemStuff=True):
    curr_dir_path = Alias.AliasMgr.GetAlias("WORKING_DIR") +"\\"
    strReturn=" -- Stack Dump Start ---\n"
    for line in traceback.format_stack()[:-2]:
        if True == DoNotShowSystemStuff and not curr_dir_path in line: # trim off OS components, only care about my code
            continue
        line = line.replace(curr_dir_path,"")
        strReturn += line.strip() +"\n"

    strReturn+=" -- Stack Dump End ---"
    return strReturn