#!/bin/sh
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#

# tools/migration2git.sh ${1}
# ${1} Site folder to migrate

if test "$#" != 0; then
  echo "USAGE: $0"
  exit 1
fi

cd ${SVNPATH2}
echo Migrating ${SVNPATH2}/. to ${GITPATH2}
echo
# 1 - Tree structure
echo 'copy directory structure to assets and content trees'
find . -type d ! -empty -exec mkdir -p ${GITPATH2}/assets/{} \; -exec mkdir -p ${GITPATH2}/content/{} \;
# git does not commit empty directories
echo
# 2 - Assets
echo 'copy assets not (html and mdtext) to assets tree'
find . -type f ! -name "*.mdtext" -exec cp -p {} ${GITPATH2}/assets/{} \;
echo
# 3 - Markdown
echo 'Convert markdown pages'
find . -name "*.mdtext" -type f -exec ${GITPATH2}/tools/convert2md.sh page {} \;
echo
