ApkUpdate
=========

Simple solution for enterprise android application automatic updates. It is an alternative for <a href="http://www.auto-update-apk.com/">www.auto-update-apk.com</a> for those who is ready to handle server side aspect. The solution is compatible with client side of the Auto Update APK because basically the original <a href="https://code.google.com/p/auto-update-apk-client/">client source code</a> is used with minor modification.

Installation
-------

<h3>Client side</h3>
Put client/AutoUpdateApk.java into your android project. Uncomment API_URL constant and put your domain or IP there.
At this stage you can also tune other settings available in constants. Then you initialize the class like it was said in <a href="https://code.google.com/p/auto-update-apk-client/">original documentation</a>. VariantId string is passed via constructor (use empty string if you don't need variants)

<h3>Server side</h3>
It is not that powerful as Auto Update APK in first implementation. There is no check by md5 implemented, so it does not update anything without incrementing version code. However new feature is added: variants. It is a reflection of <a href="http://tools.android.com/tech-docs/new-build-system/user-guide#TOC-Build-Variants">Gradle build variants</a> which allow you distribute same packages for different customers or departaments separately. 

To use the tool in first turn you need to get a server available via Internet :). Although you may want to put it inside your company network and it can work too.

This repo offers deploy via docker images pushing to your registry. .env file should be created with REGISTRY and DOCKER_MACHINE vars for doing so. 

Main file which describes your packages is packages.py. Corresponding apk files should be put in same file structure as in example. Or you can change alias path for /download inside nginx.conf

<h2>Contribution and bugs</h2>
I implemented the thing very quickly with not paying attention to some details. Any help will be appreciated meaning both bug reports and pull requests.

License
-------

    Copyright 2014 Eugene
    
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
    
    http://www.apache.org/licenses/LICENSE-2.0
    
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

