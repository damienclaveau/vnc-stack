#!/usr/bin/env python
from resource_management.libraries.functions.version import format_hdp_stack_version, compare_versions
from resource_management import *

# server configurations
config = Script.get_config()

install_eclipse = config['configurations']['vnc-config']['install.eclipse']
install_intellij = config['configurations']['vnc-config']['install.intellij']
install_spark = config['configurations']['vnc-config']['install.spark']
install_mvn = config['configurations']['vnc-config']['install.mvn']

vnc_password = config['configurations']['vnc-config']['vnc.password']
vnc_geometry = config['configurations']['vnc-config']['vnc.geometry']

eclipse_location = config['configurations']['vnc-config']['eclipse.location']
intellij_location = config['configurations']['vnc-config']['intellij.location']
mvn_location = config['configurations']['vnc-config']['mvn.location']
spark_location = config['configurations']['vnc-config']['spark.location']

log_location = config['configurations']['vnc-config']['log.file'] 