OBS_PROJECT := EA4
OBS_PACKAGE := ea-php72-php-memcached
DISABLE_BUILD += repository=CentOS_9
include $(EATOOLS_BUILD_DIR)obs.mk
