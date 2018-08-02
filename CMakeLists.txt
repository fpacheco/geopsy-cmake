cmake_minimum_required(VERSION 2.6)

project(Geopsy_App)
 
set(CMAKE_BINARY_DIR ${CMAKE_SOURCE_DIR}/build)
 
set(EXECUTABLE_OUTPUT_PATH ${CMAKE_BINARY_DIR})
set(LIBRARY_OUTPUT_PATH ${CMAKE_BINARY_DIR})
 
set(PROJECT_INCLUDE_DIR ${PROJECT_SOURCE_DIR}/include)
 
include_directories("${PROJECT_INCLUDE_DIR}")
include_directories("${PROJECT_SOURCE_DIR}")

#lib/QGpCoreTools \
#lib/QGpGuiTools \
#lib/QGpCoreMath \
#lib/SciFigs \
#lib/QGpGuiMath \
#figue \
#lib/QGpCoreWave \
#lib/QGpGuiWave \
#lib/QGpCompatibility \
#geopsy/GeopsyCore \
#geopsy/GeopsyGui \
#geopsy/geopsyfigs \
#geopsy/GeopsySLink \
#geopsy/GeopsySLinkGui \
#dinver/DinverCore \
#dinver/DinverGui \
#dinver/DinverDCCore \
#dinver/DinverDCGui \
#lib/QGpCoreStat \
#geopsy/ArrayCore \
#geopsy/ArrayGui \
#geopsy/MonoStation \
#geopsy/geopsy-fk \
#geopsy/geopsy \
#geopsy/vslarray \
#dinver/dinver \
#waran/WaranCore \
#waran/TapePositioningSystem \
#waran/waran \
#waran/warangps \
#geopsy/tools/geopsyarray \
#geopsy/tools/geopsyhv \
#geopsy/tools/geopsydamping \
#geopsy/tools/geopsytfa \
#geopsy/tools/geopsynr \
#geopsy/tools/geopsyptmotion \
#geopsy/tools/geopsyrefra \
#geopsy/tools/hvtfa \
#geopsy/campbelltob3 \
#dinver/dinverdc \
#dinver/dinverext \
#spac2disp \
#max2curve \
#gptools/gppoisson \
#gptools/gpprofile \
#gptools/gpdc \
#gptools/gplivemodel \
#gptools/gpec8 \
#gptools/gpdcreport \
#gptools/gptarget \
#gptools/gpviewdcreport \
#gptools/gpdcmisfit \
#gptools/gpell \
#gptools/gpgroup2phase \
#gptools/gpmodel2param \
#gptools/gpparam2model \
#gptools/gpdepths \
#gptools/gpsort \
#gptools/gpcurve \
#gptools/gprandom \
#gptools/gpspac \
#gptools/gprefra \
#gptools/gpsignal \
#gptools/gphistogram \
#gptools/gpviewmax \
#gptools/gpdistance \
#gptools/gptime \
#gptools/gpcoord \
#gptools/gpreplace \
#gptools/gpsh \
#gptools/gpmt \
#gptools/gpgridsearch \
#gptools/gpfksimulator \
#gptools/gpmaplayer \
#lib/GpCoreTools \
#waran/warangpsd \
#waran/waranscreend \
#waran/waranecho \
#waran/warannetd \
#waran/warand \
#waran/dascubed \
#dinver/dinvermatlab \
#geopsy/matfiles \
#geopsypack/GeopsyPackCore \
#geopsypack/geopsypackinstall \
#geopsypack/geopsypackd \
#geopsypack/selfcompress \
#geopsypack/mkdmg \
#geopsypack/bugparser \

### Geopsy libs package 
# Without GUI
add_subdirectory(${CMAKE_SOURCE_DIR}/geopsy-libs/GpCoreTools)
add_subdirectory(${CMAKE_SOURCE_DIR}/geopsy-libs/QGpCoreTools)
add_subdirectory(${CMAKE_SOURCE_DIR}/geopsy-libs/QGpCoreMath)
add_subdirectory(${CMAKE_SOURCE_DIR}/geopsy-libs/QGpCoreWave)
# With GUI
add_subdirectory(${CMAKE_SOURCE_DIR}/geopsy-libs/QGpGuiMath)
add_subdirectory(${CMAKE_SOURCE_DIR}/geopsy-libs/QGpGuiTools)
add_subdirectory(${CMAKE_SOURCE_DIR}/geopsy-libs/QGpGuiWave)
### 

add_subdirectory(${CMAKE_SOURCE_DIR}/geopsy-libs/SciFigs)

add_subdirectory(${CMAKE_SOURCE_DIR}/geopsy-libs/figue)

add_subdirectory(${CMAKE_SOURCE_DIR}/geopsy-libs/QGpCoreMath)

