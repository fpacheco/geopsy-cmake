### RFPV ###
### Pass variables like this ... 
# cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DGEOPSY_APP_BUILD_PATH=/tmp/geopsy ..
###

cmake_minimum_required(VERSION 3.9)

project(@@P_NAME@@ VERSION 0.0.0 DESCRIPTION "@@P_NAME@@ description")

### Modules
list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake")
list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake/modules")
###

### Cxx options 
# With c++11
set(CMAKE_CXX_STANDARD 11)
# Warnings
if(MSVC)
  # Force to always compile with W4
  if(CMAKE_CXX_FLAGS MATCHES "/W[0-4]")
    string(REGEX REPLACE "/W[0-4]" "/W4" CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS}")
  else()
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /W4")
  endif()
elseif(CMAKE_COMPILER_IS_GNUCC OR CMAKE_COMPILER_IS_GNUCXX)
  # Update if necessary
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wno-long-long -Wdeprecated -pedantic")
endif()
###

# General build directory 
if(GEOPSY_APP_BUILD_PATH)
    # Global build
    set(THIS_BUILD_PATH ${GEOPSY_APP_BUILD_PATH})
else()
    set(THIS_BUILD_PATH ${CMAKE_BINARY_DIR})
endif()

# General bin directory 
if(GEOPSY_APP_BIN_PATH)
    # Global build
    set(THIS_BIN_PATH ${GEOPSY_APP_BIN_PATH})
else()
    set(THIS_BIN_PATH "${THIS_BUILD_PATH}/bin")
endif()

# General include directory 
if(GEOPSY_APP_INC_PATH)
    # Global build
    set(THIS_INC_PATH ${GEOPSY_APP_INC_PATH})
else()
    set(THIS_INC_PATH "${THIS_BUILD_PATH}/include")
endif()

# General library directory 
if(GEOPSY_APP_LIB_PATH)
    # Global build
    set(THIS_LIB_PATH ${GEOPSY_APP_LIB_PATH})
else()
    set(THIS_LIB_PATH "${THIS_BUILD_PATH}/lib")
endif()

#message(STATUS "THIS_BUILD_PATH: ${THIS_BUILD_PATH}")
#message(STATUS "THIS_BIN_PATH: ${THIS_BIN_PATH}")
#message(STATUS "THIS_INC_PATH: ${THIS_INC_PATH}")
#message(STATUS "THIS_LIB_PATH: ${THIS_LIB_PATH}")

### Add library directory to search path 
link_directories(${THIS_LIB_PATH})
###

### Add include directory to search path 
include_directories(${THIS_INC_PATH})
###

# RFPV: bin and lib should created automatically
# Create include if not exists 
if(NOT EXISTS ${THIS_INC_PATH})
    file(MAKE_DIRECTORY ${THIS_INC_PATH})
    #add_custom_command(
        #TARGET ${PROJECT_NAME}
        #POST_BUILD    
        #file(MAKE_DIRECTORY ${THIS_INC_PATH})
    #)
endif()

# Create include/${PROJECT_NAME} if not exists 
if(NOT EXISTS ${THIS_INC_PATH}/${PROJECT_NAME})
    file(MAKE_DIRECTORY ${THIS_INC_PATH}/${PROJECT_NAME})
    #add_custom_command(
        #TARGET ${PROJECT_NAME}
        #POST_BUILD    
        #file(MAKE_DIRECTORY ${THIS_INC_PATH}/${PROJECT_NAME})
    #)
endif()

### Find packages
set(THREADS_PREFER_PTHREAD_FLAG ON)
# Find libpthread
find_package(Threads REQUIRED)
# Find zlib
find_package(ZLIB REQUIRED)
# Find MPFR
find_package(MPFR REQUIRED)
# Find GMP
find_package(GMP REQUIRED)
# Find LAPACK
find_package(LAPACK REQUIRED)
# Find BLAS
find_package(BLAS REQUIRED)
###

### Qt5 support
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_INCLUDE_CURRENT_DIR ON)

# Find Qt5 and add components Widgets, Qml, Sql, Network
find_package(Qt5 COMPONENTS Core Gui Widgets Qml Network PrintSupport REQUIRED)
INCLUDE_DIRECTORIES(${Qt5Core_INCLUDE_DIRS})
#INCLUDE_DIRECTORIES(${Qt5Qml_INCLUDE_DIRS})
#INCLUDE_DIRECTORIES(${Qt5Network_INCLUDE_DIRS})

set(QT5_LIBRARIES Qt5::Core Qt5::Gui Qt5::Widgets Qt5::Qml Qt5::Network Qt5::PrintSupport)
#message(STATUS "QT5_LIBRARIES: ${QT5_LIBRARIES}")
#message(STATUS "Qt5Core_LIBRARIES: ${Qt5Core_LIBRARIES}")
#message(STATUS "Qt5Core_INCLUDE_DIRS: ${Qt5Core_INCLUDE_DIRS}")
#message(STATUS "Qt5Qml_INCLUDE_DIRS: ${Qt5Qml_INCLUDE_DIRS}")
###

set(TARGET ${CMAKE_PROJECT_NAME})

set(CPP_SRCS
@@CPP_SOURCES@@
)

# Headers got to include/*
set(HEA_INC

)

# Headers got to include/GpCoreTools/*
set(HEA_SRCS
@@HEA_SOURCES@@
)

# Headers got to include/*
set(UI_SRCS
@@UI_SOURCES@@
)

#
# Generate necessary headers from .ui files. (qmake lets `uic` do this job.)
# hint from [Cross-platform Qt5 project using cmake](http://stackoverflow.com/questions/21174586/cross-platform-qt5-project-using-cmake)
#
# QT5_WRAP_UI(UI_GENERATED_HEADERS ${UI_SRCS})

# Include header files for compilation
include_directories(src)

#get_property(dirs DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} PROPERTY INCLUDE_DIRECTORIES)
#foreach(dir ${dirs})
  #message(STATUS "dir='${dir}'")
#endforeach()

### Set BUILD PATHS
# Set library build path 
set (EXECUTABLE_OUTPUT_PATH ${THIS_BIN_PATH})
# Set library build path 
set (LIBRARY_OUTPUT_PATH ${THIS_LIB_PATH})
### 

# Add resources from file
qt5_add_resources(QRCS @@QRC_FILE@@)

# Create executable
add_executable(${PROJECT_NAME} ${CPP_SRCS} ${UI_HEADERS} ${QRCS})
target_link_libraries(${PROJECT_NAME} ${ZLIB_LIBRARIES} ${MPFR_LIBRARIES} ${GMP_LIBRARIES})
target_link_libraries(${PROJECT_NAME} ${BLAS_LIBRARIES} ${LAPACK_LIBRARIES}) 
target_link_libraries(${PROJECT_NAME} Threads::Threads)
target_link_libraries(${PROJECT_NAME} ${QT5_LIBRARIES})
# Geopsy libraries - Comment out
target_link_libraries(${PROJECT_NAME} QGpCoreTools)
target_link_libraries(${PROJECT_NAME} QGpGuiTools)
target_link_libraries(${PROJECT_NAME} QGpCoreMath)
target_link_libraries(${PROJECT_NAME} QGpGuiMath)
target_link_libraries(${PROJECT_NAME} QGpCoreWave)
target_link_libraries(${PROJECT_NAME} QGpGuiWave)
target_link_libraries(${PROJECT_NAME} SciFigs)
target_link_libraries(${PROJECT_NAME} DinverCore)
target_link_libraries(${PROJECT_NAME} DinverGui)
target_link_libraries(${PROJECT_NAME} DinverDCCore)
target_link_libraries(${PROJECT_NAME} DinverDCGui)

# Set VERSION
set_target_properties(${PROJECT_NAME} PROPERTIES VERSION ${PROJECT_VERSION})

# Set SOVERSION. Major version.
set_target_properties(${PROJECT_NAME} PROPERTIES SOVERSION 1)

### POST BUILD
# Include headers (include/*)
#foreach( file_i ${HEA_INC})
    #file(
        #COPY ${CMAKE_CURRENT_SOURCE_DIR}/${file_i}
        #DESTINATION ${THIS_INC_PATH}
    #)    
#endforeach( file_i )

## All other headers (include/${PROJECT_NAME}/*)
#foreach( file_i ${HEA_SRCS})
    #file(
        #COPY ${CMAKE_CURRENT_SOURCE_DIR}/${file_i} 
        #DESTINATION ${THIS_INC_PATH}/${PROJECT_NAME}
    #)
#endforeach( file_i )
###

### Install actions 
## TODO: review this
# Install library
install(TARGETS ${PROJECT_NAME} DESTINATION lib/${PROJECT_NAME})

# Install library headers
file(GLOB HEADERS include/*.h)
install(FILES ${HEADERS} DESTINATION include/${PROJECT_NAME})
