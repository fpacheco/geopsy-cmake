cmake_minimum_required(VERSION 2.6)

project(Geopsy_App)

### Modules
list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake")
list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake/modules")
###
 
set(CMAKE_BINARY_DIR ${CMAKE_SOURCE_DIR}/build)
 
set(EXECUTABLE_OUTPUT_PATH ${CMAKE_BINARY_DIR})
set(LIBRARY_OUTPUT_PATH ${CMAKE_BINARY_DIR})
 
set(PROJECT_INCLUDE_DIR ${PROJECT_SOURCE_DIR}/include)
 
include_directories("${PROJECT_INCLUDE_DIR}")
include_directories("${PROJECT_SOURCE_DIR}")

function(copy_and_rename opath ofname dpath dfname)
    message( STATUS "Copy and rename: ${opath}/${ofname} to ${dpath}/${dfname}")
    file(
        COPY ${opath}/${ofname}
        DESTINATION ${dpath}
    )
    file(RENAME ${dpath}/${ofname} ${dpath}/${dfname})    
endfunction()

## MODULAR 
# TRUE CMakeLists.txt for every director
# FALSE Monolitic 
set(CMAKE_MODULAR_BUILD TRUE)
# set(CMAKE_MODULAR_BUILD )

# cmake options
if (CMAKE_MODULAR_BUILD)
    # Copy and rename files
    copy_and_rename(
        ${CMAKE_CURRENT_SOURCE_DIR} CMakeLists_GpCoreTools.txt
        ${CMAKE_SOURCE_DIR}/geopsy-src/lib/GpCoreTools CMakeLists.txt
    )    
    copy_and_rename(
        ${CMAKE_CURRENT_SOURCE_DIR} CMakeLists_QGpCoreTools.txt
        ${CMAKE_SOURCE_DIR}/geopsy-src/lib/QGpCoreTools CMakeLists.txt
    )
    copy_and_rename(
        ${CMAKE_CURRENT_SOURCE_DIR} CMakeLists_QGpGuiTools.txt
        ${CMAKE_SOURCE_DIR}/geopsy-src/lib/QGpGuiTools CMakeLists.txt
    )
    copy_and_rename(
        ${CMAKE_CURRENT_SOURCE_DIR} CMakeLists_QGpCoreMath.txt
        ${CMAKE_SOURCE_DIR}/geopsy-src/lib/QGpCoreMath CMakeLists.txt
    )
    copy_and_rename(
        ${CMAKE_CURRENT_SOURCE_DIR} CMakeLists_QGpCoreWave.txt
        ${CMAKE_SOURCE_DIR}/geopsy-src/lib/QGpCoreWave CMakeLists.txt
    )
    copy_and_rename(
        ${CMAKE_CURRENT_SOURCE_DIR} CMakeLists_SciFigs.txt
        ${CMAKE_SOURCE_DIR}/geopsy-src/lib/SciFigs CMakeLists.txt
    )
    copy_and_rename(
        ${CMAKE_CURRENT_SOURCE_DIR} CMakeLists_QGpGuiMath.txt
        ${CMAKE_SOURCE_DIR}/geopsy-src/lib/QGpGuiMath CMakeLists.txt
    )
    copy_and_rename(
        ${CMAKE_CURRENT_SOURCE_DIR} CMakeLists_QGpGuiWave.txt
        ${CMAKE_SOURCE_DIR}/geopsy-src/lib/QGpGuiWave CMakeLists.txt
    )
    copy_and_rename(
        ${CMAKE_CURRENT_SOURCE_DIR} CMakeLists_QGpCompatibility.txt
        ${CMAKE_SOURCE_DIR}/geopsy-src/lib/QGpCompatibility CMakeLists.txt
    )
    copy_and_rename(
        ${CMAKE_CURRENT_SOURCE_DIR} CMakeLists_figue.txt
        ${CMAKE_SOURCE_DIR}/geopsy-src/figue CMakeLists.txt
    )
    copy_and_rename(
        ${CMAKE_CURRENT_SOURCE_DIR} CMakeLists_GeopsyCore.txt
        ${CMAKE_SOURCE_DIR}/geopsy-src/geopsy/GeopsyCore CMakeLists.txt
    )
    copy_and_rename(
        ${CMAKE_CURRENT_SOURCE_DIR} CMakeLists_GeopsyGui.txt
        ${CMAKE_SOURCE_DIR}/geopsy-src/geopsy/GeopsyGui CMakeLists.txt
    )
    copy_and_rename(
        ${CMAKE_CURRENT_SOURCE_DIR} CMakeLists_geopsyfigs.txt
        ${CMAKE_SOURCE_DIR}/geopsy-src/geopsy/geopsyfigs CMakeLists.txt
    )
    copy_and_rename(
        ${CMAKE_CURRENT_SOURCE_DIR} CMakeLists_GeopsySLink.txt
        ${CMAKE_SOURCE_DIR}/geopsy-src/geopsy/GeopsySLink CMakeLists.txt
    )
    copy_and_rename(
        ${CMAKE_CURRENT_SOURCE_DIR} CMakeLists_GeopsySLinkGui.txt
        ${CMAKE_SOURCE_DIR}/geopsy-src/geopsy/GeopsySLinkGui CMakeLists.txt
    )
        
    # Add subprojects
    add_subdirectory(${CMAKE_SOURCE_DIR}/geopsy-src/lib/GpCoreTools)
    add_subdirectory(${CMAKE_SOURCE_DIR}/geopsy-src/lib/QGpCoreTools)
    add_subdirectory(${CMAKE_SOURCE_DIR}/geopsy-src/lib/QGpGuiTools)
    add_subdirectory(${CMAKE_SOURCE_DIR}/geopsy-src/lib/QGpCoreMath)
    add_subdirectory(${CMAKE_SOURCE_DIR}/geopsy-src/lib/QGpCoreWave)
    add_subdirectory(${CMAKE_SOURCE_DIR}/geopsy-src/lib/SciFigs)
    add_subdirectory(${CMAKE_SOURCE_DIR}/geopsy-src/lib/QGpGuiMath)
    add_subdirectory(${CMAKE_SOURCE_DIR}/geopsy-src/lib/QGpGuiWave)
    add_subdirectory(${CMAKE_SOURCE_DIR}/geopsy-src/lib/QGpCompatibility)
    add_subdirectory(${CMAKE_SOURCE_DIR}/geopsy-src/figue)
    # add_subdirectory(${CMAKE_SOURCE_DIR}/geopsy-src/geopsy/GeopsyCore)
    # add_subdirectory(${CMAKE_SOURCE_DIR}/geopsy-src/geopsy/GeopsyGui)
    # add_subdirectory(${CMAKE_SOURCE_DIR}/geopsy-src/geopsy/geopsfigs)    
    # add_subdirectory(${CMAKE_SOURCE_DIR}/geopsy-src/geopsy/GeopsySLink)
    # add_subdirectory(${CMAKE_SOURCE_DIR}/geopsy-src/geopsy/GeopsySLinkGui)

    # add_subdirectory(${CMAKE_SOURCE_DIR}/geopsy-src/dinver/DinverCore)
    # add_subdirectory(${CMAKE_SOURCE_DIR}/geopsy-src/dinver/DinverGui)
    # add_subdirectory(${CMAKE_SOURCE_DIR}/geopsy-src/dinver/DinverDCCore)
    # add_subdirectory(${CMAKE_SOURCE_DIR}/geopsy-src/dinver/DinverDCGui)
    # add_subdirectory(${CMAKE_SOURCE_DIR}/geopsy-src/dinver/dinver)
    # add_subdirectory(${CMAKE_SOURCE_DIR}/geopsy-src/dinver/dinverdc)
    # add_subdirectory(${CMAKE_SOURCE_DIR}/geopsy-src/dinver/dinverext)
    # add_subdirectory(${CMAKE_SOURCE_DIR}/geopsy-src/dinver/dinvermatlab)

    # add_subdirectory(${CMAKE_SOURCE_DIR}/geopsy-src/geopsy/QGpCoreStat)
    # add_subdirectory(${CMAKE_SOURCE_DIR}/geopsy-src/geopsy/ArrayCore)
    # add_subdirectory(${CMAKE_SOURCE_DIR}/geopsy-src/geopsy/ArrayGui)
    # add_subdirectory(${CMAKE_SOURCE_DIR}/geopsy-src/geopsy/MonoStation)
    # add_subdirectory(${CMAKE_SOURCE_DIR}/geopsy-src/geopsy/geopsy-fk)
    # add_subdirectory(${CMAKE_SOURCE_DIR}/geopsy-src/geopsy/geopsy)

    ###
else()
    set(CUR_PROJ_REL_SRC )
    # Se compila todo de una sola vez
    include(CMakeLists_GpCoreTools.txt)
    include(CMakeLists_QGpCoreTools.txt)
    include(CMakeLists_QGpGuiTools.txt)
    include(CMakeLists_QGpCoreMath.txt)
    include(CMakeLists_QGpCoreWave.txt)
    include(CMakeLists_SciFigs.txt)
    include(CMakeLists_QGpGuiMath.txt)
    include(CMakeLists_QGpGuiWave.txt)
    include(CMakeLists_QGpCompatibility.txt)
    include(CMakeLists_figue.txt)

    include(CMakeLists_GeopsyCore.txt)
    include(CMakeLists_GeopsyGui.txt)
    include(CMakeLists_geopsyfigs.txt)
    include(CMakeLists_GeopsySLink.txt)
    include(CMakeLists_GeopsySLinkGui.txt)

    include(CMakeLists_DinverCore.txt)
    include(CMakeLists_DinverGui.txt)
    include(CMakeLists_DinverDCCore.txt)
    include(CMakeLists_DinverDCGui.txt)
    include(CMakeLists_dinver.txt)
    include(CMakeLists_dinverdc.txt)
    include(CMakeLists_dinverext.txt)
    include(CMakeLists_dinvermatlab.txt)

    include(CMakeLists_QGpCoreStat.txt)
    include(CMakeLists_ArrayCore.txt)
    include(CMakeLists_ArrayGui.txt)
    include(CMakeLists_MonoStation.txt)
    include(CMakeLists_geopsy-fk.txt)
    include(CMakeLists_geopsy.txt)
    #include(CMakeLists_vslarray.txt)
endif()






