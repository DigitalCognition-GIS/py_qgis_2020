#------------------------------------------------------------------------------
# CPACK controls
#------------------------------------------------------------------------------

SET(CPACK_PACKAGE_VERSION_MAJOR ${LASZIP_API_VERSION_MAJOR})
SET(CPACK_PACKAGE_VERSION_MINOR ${LASZIP_API_VERSION_MINOR})
SET(CPACK_PACKAGE_VERSION_PATCH ${LASZIP_API_VERSION_PATCH})
SET(CPACK_PACKAGE_NAME "LASzip")

SET(CPACK_SOURCE_GENERATOR "TBZ2;TGZ")
SET(CPACK_PACKAGE_VENDOR "LASzip Development Team")
SET(CPACK_RESOURCE_FILE_LICENSE    "${PROJECT_SOURCE_DIR}/COPYING.txt")

set(CPACK_SOURCE_PACKAGE_FILE_NAME
    "laszip-src-${LASZIP_API_VERSION_STRING}")

set(CPACK_SOURCE_IGNORE_FILES
"/\\\\.gitattributes;/\\\\.vagrant;/\\\\.DS_Store;/CVS/;/\\\\.git/;\\\\.swp$;~$;\\\\.\\\\#;/\\\\#")

list(APPEND CPACK_SOURCE_IGNORE_FILES "CMakeScripts/")
list(APPEND CPACK_SOURCE_IGNORE_FILES "CMakeCache.txt")
list(APPEND CPACK_SOURCE_IGNORE_FILES ".xcodeproj")
list(APPEND CPACK_SOURCE_IGNORE_FILES "build.make")
list(APPEND CPACK_SOURCE_IGNORE_FILES "_CPack_Packages")
list(APPEND CPACK_SOURCE_IGNORE_FILES "CPackSourceConfig.cmake")
list(APPEND CPACK_SOURCE_IGNORE_FILES "CPackConfig.cmake")
list(APPEND CPACK_SOURCE_IGNORE_FILES "cmake_install.cmake")
list(APPEND CPACK_SOURCE_IGNORE_FILES "Testing")
list(APPEND CPACK_SOURCE_IGNORE_FILES "bin/")
list(APPEND CPACK_SOURCE_IGNORE_FILES "data/")
list(APPEND CPACK_SOURCE_IGNORE_FILES "scripts/")
list(APPEND CPACK_SOURCE_IGNORE_FILES "lib/")
list(APPEND CPACK_SOURCE_IGNORE_FILES "/build/")
list(APPEND CPACK_SOURCE_IGNORE_FILES "Makefile")
list(APPEND CPACK_SOURCE_IGNORE_FILES ".gz")
list(APPEND CPACK_SOURCE_IGNORE_FILES ".bz2")
list(APPEND CPACK_SOURCE_IGNORE_FILES "unused/")
list(APPEND CPACK_SOURCE_IGNORE_FILES "CMakeFiles")
list(APPEND CPACK_SOURCE_IGNORE_FILES "CTestTestfile.cmake")
list(APPEND CPACK_SOURCE_IGNORE_FILES "/test/data/local/")
list(APPEND CPACK_SOURCE_IGNORE_FILES "/docs")
list(APPEND CPACK_SOURCE_IGNORE_FILES "/dll/laszip_api_version.h")

include(CPack)
