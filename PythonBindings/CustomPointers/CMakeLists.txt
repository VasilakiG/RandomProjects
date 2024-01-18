add_library(CustomPointerLib STATIC CustomPointer.c)

target_include_directories(CustomPointerLib PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})